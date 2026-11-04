"""Recheck English entries in BLOCKED-SITES.md (requires beautifulsoup4).

Run from the repository root: python tools/blocked_english.py [--service]
The optional loopback Turnstile-Slip service is used only for blocked requests.
Evidence is resumable JSONL; cookies and raw pages stay outside the repository.
"""
import concurrent.futures
import hashlib
import json
import pathlib
import re
import sys
import threading
import urllib.error
import urllib.parse
import urllib.request
import base64
from datetime import datetime, timezone

from bs4 import BeautifulSoup

ROOT = pathlib.Path(__file__).resolve().parents[1]
CACHE = pathlib.Path('/tmp/twe-blocked-english')
CACHE.mkdir(exist_ok=True)
OUT = ROOT / 'tools/blocked-english.jsonl'
UA = 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36'
SERVICE = '--service' in sys.argv
SERVICE_LOCK = threading.Lock()
SYSTEMS = {
    'wpdiscuz': '#wpdcom, .wpd-thread-list, .wpd-comment',
    'wordpress': '.comment-list li.comment, ol.commentlist li.comment, #comments article.comment',
    'disqus': '#disqus_thread',
    'mcs': 'li.mcs-comment',
    'comment-body-articles': "article.comment-body[id^='div-comment-']",
    'livewire-discussion': "[data-testid='comment-discussion']",
    'manga-comments-pro': '#mcp-list, .mcp-thread',
    'facebook': '.fb-comments',
}
ITEMS = {
    'wpdiscuz': '.wpd-comment', 'wordpress': 'li.comment, article.comment',
    'mcs': 'li.mcs-comment', 'comment-body-articles': "article.comment-body[id^='div-comment-']",
    'livewire-discussion': "article[data-testid='comment-card']", 'manga-comments-pro': '.mcp-thread',
}
SKIP = re.compile(r'/(?:genres?|tags?|categor(?:y|ies)|authors?|artists?|page|search|login|register|privacy|terms|contact|dmca|wp-content|wp-includes)(?:/|$)', re.I)
TITLE = re.compile(r'/(?:manga|series|comics?|title|webtoons?|manhwa|manhua|read|book|serie|truyen[^/]*|g|gallery|view|reader)/[^/?#]+', re.I)


def fetch(url, cookie=''):
    headers = {'User-Agent': UA, 'Accept': 'text/html,application/json,*/*;q=0.8', 'Accept-Language': 'en'}
    if cookie:
        headers['Cookie'] = cookie
    try:
        with urllib.request.urlopen(urllib.request.Request(url, headers=headers), timeout=18) as response:
            status, final, raw = response.status, response.url, response.read(3_000_000)
    except urllib.error.HTTPError as error:
        status, final, raw = error.code, error.url, error.read(100_000)
    body = raw.decode('utf-8', 'replace')
    blocked = status in (403, 429, 503) or bool(re.search(r'<title>\s*(?:Just a moment|Attention Required)|cf-chl-', body, re.I))
    if blocked and SERVICE:
        with SERVICE_LOCK:
            query = urllib.parse.urlencode({'target': url, 'fast': 'true', 'ua': UA})
            with urllib.request.urlopen('http://127.0.0.1:3000/api?' + query, timeout=85) as response:
                session = json.load(response)
            cookie = session.get('cookie', '')
        if cookie:
            headers['Cookie'] = cookie
            with urllib.request.urlopen(urllib.request.Request(url, headers=headers), timeout=18) as response:
                status, final, body = response.status, response.url, response.read(3_000_000).decode('utf-8', 'replace')
            blocked = bool(re.search(r'<title>\s*(?:Just a moment|Attention Required)|cf-chl-', body, re.I))
    path = CACHE / (hashlib.sha256(url.encode()).hexdigest() + '.html')
    path.write_text(body)
    return status, final, body, blocked, cookie, str(path)


def candidates(base, soup):
    seen = {}
    host = urllib.parse.urlparse(base).netloc.removeprefix('www.')
    for a in soup.select('a[href]'):
        url = urllib.parse.urljoin(base, a['href']).split('#')[0]
        p = urllib.parse.urlparse(url)
        if p.scheme not in ('http', 'https') or p.netloc.removeprefix('www.') != host or SKIP.search(p.path):
            continue
        if p.path in ('', '/') or re.search(r'\.(?:css|js|png|jpe?g|webp|svg|pdf|zip)$', p.path):
            continue
        score = 10 if TITLE.search(p.path) else 0
        score += 5 if a.select_one('img') else 0
        score += 4 if re.search(r'title|manga|comic|series', ' '.join(a.get('class', [])), re.I) else 0
        score -= 3 if re.search(r'chapter|/ch[-/]', p.path, re.I) else 0
        if score > 0:
            seen[url] = max(score, seen.get(url, 0))
    return sorted(seen, key=lambda u: (-seen[u], len(u)))[:5]


def inspect(url, html):
    soup = BeautifulSoup(html, 'html.parser')
    systems = [k for k, selector in SYSTEMS.items() if soup.select_one(selector)]
    script_text = html
    for encoded in re.findall(r'data:text/javascript;base64,([A-Za-z0-9+/=]+)', html):
        try:
            script_text += '\n' + base64.b64decode(encoded).decode('utf-8', 'replace')
        except ValueError:
            pass
    for system, pattern in {
        'remark42': r'remark_config\s*=', 'zmio': r'zmio\.org/post\?',
        'cusdis': r'id=["\']cusdis_thread', 'vuukle': r'VUUKLE_CONFIG\s*=',
        'disqus': r'disqusShortname["\']?\s*:|\.disqus\.com/(?:count|embed)\.js',
        'blogger': r'<meta[^>]+content=["\']blogger["\']',
    }.items():
        if system not in systems and re.search(pattern, script_text, re.I):
            systems.append(system)
    counts = {k: len(soup.select(ITEMS[k])) for k in systems if k in ITEMS}
    # Names and URLs only: never store session cookies or inline script secrets.
    scripts = [urllib.parse.urljoin(url, s['src']) for s in soup.select('script[src]') if not s['src'].startswith('data:')]
    return soup, {'url': url, 'title': soup.title.get_text(' ', strip=True) if soup.title else '',
                  'systems': systems, 'counts': counts,
                  'commentScripts': [s for s in scripts if re.search(r'comment|disqus|discuss', s, re.I)],
                  'scriptUrls': scripts[-25:],
                  'commentHints': sorted(set(re.findall(r'(?:id|class)=["\']([^"\']*(?:comment|discuss)[^"\']*)', html, re.I)))[:20]}


def audit(row):
    result = {k: row[k] for k in ('pkg', 'name', 'home', 'sources')}
    result['checkedAt'] = datetime.now(timezone.utc).isoformat()
    result['service'] = SERVICE
    try:
        status, final, html, blocked, cookie, path = fetch(row['home'])
        result.update(http=status, final=final, cache=path)
        if blocked or status >= 400:
            result['status'] = 'blocked' if blocked else 'unreachable'
            return result
        soup, home = inspect(final, html)
        result['homeEvidence'] = home
        result['candidates'] = candidates(final, soup)
        pages = []
        for target in result['candidates'][:2]:
            try:
                code, url, body, denied, cookie, cache = fetch(target, cookie)
                if code >= 400 or denied:
                    pages.append({'url': target, 'http': code, 'blocked': denied})
                    continue
                _, evidence = inspect(url, body)
                evidence['cache'] = cache
                pages.append(evidence)
                if evidence['systems']:
                    break
            except Exception as error:
                pages.append({'url': target, 'error': str(error)[:180]})
        result['pages'] = pages
        evidence = pages + [home]
        result['systems'] = sorted(set(s for e in evidence for s in e.get('systems', [])))
        result['status'] = 'comments-found' if result['systems'] else 'inspect' if pages else 'no-title'
    except Exception as error:
        result.update(status='error', error=str(error)[:180])
    return result


def main():
    section = (ROOT / 'BLOCKED-SITES.md').read_text().split('### English (')[1].split('\n### ')[0]
    homes = set(re.findall(r'\| (https?://\S+) \|', section))
    rows = [r for r in json.loads((ROOT / 'checklist.json').read_text()) if r['lang'] == 'en' and r.get('home') in homes]
    previous = {}
    if OUT.exists():
        for line in OUT.read_text().splitlines():
            r = json.loads(line)
            previous[r['pkg']] = r
    todo = [r for r in rows if r['pkg'] not in previous or (SERVICE and previous[r['pkg']]['status'] in ('blocked', 'error') and not previous[r['pkg']].get('service'))]
    print(f'{len(todo)} sites to check; service={SERVICE}', flush=True)
    with OUT.open('a') as output, concurrent.futures.ThreadPoolExecutor(3 if SERVICE else 12) as pool:
        for r in pool.map(audit, todo):
            output.write(json.dumps(r, ensure_ascii=False) + '\n')
            output.flush()
            print(r['name'], r['status'], r.get('systems', []), flush=True)


if __name__ == '__main__':
    main()
