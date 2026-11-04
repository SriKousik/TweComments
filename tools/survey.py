"""Survey keiyoushi extensions' sites for their comment systems.

For each extension: load its home page, find one title page, and look for known comment
systems (wpDiscuz, Disqus, Facebook, WordPress, others) and the site template.
Writes one JSON line per extension. Two requests per site, 16 sites at a time.
"""
import concurrent.futures as cf
import json
import re
import sys
import urllib.parse
import urllib.request

UA = "Mozilla/5.0 (iPhone; CPU iPhone OS 18_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0 Mobile/15E148 Safari/604.1"
INDEX, OUT = sys.argv[1], sys.argv[2]

TITLE_PATTERNS = [r"/manga/[^/?#]+/?$", r"/series/[^/?#]+/?$", r"/comics?/[^/?#]+/?$", r"/title/[^/?#]+", r"/webtoons?/[^/?#]+/?$",
                  r"/manhwa/[^/?#]+/?$", r"/manhua/[^/?#]+/?$", r"/read/[^/?#]+/?$", r"/book/[^/?#]+/?$", r"/obra/[^/?#]+/?$",
                  r"/serie/[^/?#]+/?$", r"/truyen[^/]*/[^/?#]+/?$", r"/[^/?#]+-\d+/?$", r"/g/\d+/?$"]
SKIP = re.compile(r"/(genre|genres|tag|tags|category|categories|author|artist|page|search|login|register|list|latest|popular|all|az-list|\?|#)", re.I)

THEMES = [
    ("Madara", r"wp-manga|madara"), ("MangaThemesia", r"ts_reader|bixbox|themesia|mangareader-theme"), ("HeanCMS", r"heancms|hean-cms"),
    ("Keyoapp", r"keyoapp"), ("ZeistManga", r"zeistmanga|zeist"), ("MangaBox", r"mangabox|manganato|mangakakalot"),
    ("Liliana", r"liliana"), ("MMRCMS", r"my-manga-reader|mmrcms"), ("WPComics", r"wpcomics|halim"), ("FMReader", r"fmreader"),
    ("Iken", r"iken"), ("Blogger", r"blogger\.com|blogspot"), ("Next.js", r"__NEXT_DATA__|/_next/"), ("Astro", r"astro-island"),
]
SYSTEMS = [
    ("wpDiscuz", r"wpdiscuz|wpdcom"), ("Disqus", r"disqus\.com/embed\.js|disqus_thread|disqus_shortname|\.disqus\.com"),
    ("Facebook", r"fb-comments|facebook\.com/plugins/comments"), ("Commento", r"commento"), ("Remark42", r"remark42"),
    ("Cusdis", r"cusdis"), ("Giscus", r"giscus"), ("Utterances", r"utteranc\.es"), ("Hyvor", r"hyvor"), ("GraphComment", r"graphcomment"),
    ("Valine", r"valine|waline"), ("Twikoo", r"twikoo"),
    ("WordPress", r'<ol class="comment-list|class="commentlist|id="respond"[^>]*class="comment-respond|li class="comment'),
]


def fetch(url):
    request = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "text/html,*/*;q=0.8", "Accept-Language": "en"})
    with urllib.request.urlopen(request, timeout=15) as response:
        body = response.read(1_500_000).decode("utf-8", "replace")
        return response.status, response.geturl(), body


def blocked(status, body):
    return status in (403, 503) or "Just a moment" in body or "cf-chl" in body or "challenge-platform" in body


def find_title(base, html):
    host = urllib.parse.urlparse(base).netloc
    links = re.findall(r'href=["\']([^"\'#]+)["\']', html)
    seen = []
    for link in links:
        absolute = urllib.parse.urljoin(base, link)
        parsed = urllib.parse.urlparse(absolute)
        if parsed.netloc != host or SKIP.search(parsed.path) or len(parsed.path) < 4:
            continue
        if any(re.search(p, parsed.path, re.I) for p in TITLE_PATTERNS) and absolute not in seen:
            seen.append(absolute)
    # Prefer links that look like titles, not chapters.
    seen.sort(key=lambda u: ("chapter" in u.lower() or "/ch-" in u.lower(), len(u)))
    return seen[0] if seen else None


def survey(extension):
    source = (extension.get("sources") or [{}])[0]
    home = source.get("homeUrl") or ""
    row = {"pkg": extension["packageName"], "name": extension["name"], "lang": extension["packageName"].split(".")[-2],
           "nsfw": extension.get("contentWarning") == "CONTENT_WARNING_NSFW", "home": home,
           "sources": [s["id"] for s in extension.get("sources", [])][:3]}
    if not home.startswith("http"):
        row["result"] = "no-site"
        return row
    try:
        status, final, html = fetch(home)
    except Exception as error:
        row["result"], row["error"] = "unreachable", str(error)[:120]
        return row
    if blocked(status, html):
        row["result"] = "blocked"
        return row
    row["theme"] = next((name for name, pattern in THEMES if re.search(pattern, html, re.I)), None)
    title = find_title(final, html)
    row["title"] = title
    page = html
    if title:
        try:
            status, _, page = fetch(title)
            if blocked(status, page):
                row["result"] = "blocked-title"
                return row
        except Exception as error:
            row["titleError"] = str(error)[:120]
            page = html
    found = [name for name, pattern in SYSTEMS if re.search(pattern, page, re.I)]
    row["systems"] = found
    endpoints = sorted(set(re.findall(r'["\'`](/[a-z0-9/_-]*(?:comment|cmt|discuss)[a-z0-9/_\-?=&.{}$]*)["\'`]', page, re.I)))[:5]
    if endpoints:
        row["endpoints"] = endpoints
    row["commentWords"] = len(re.findall(r"comment", page, re.I))
    row["result"] = "ok"
    return row


def main():
    extensions = json.load(open(INDEX))["extensionList"]["extensions"]
    done = set()
    try:
        for line in open(OUT):
            done.add(json.loads(line)["pkg"])
    except FileNotFoundError:
        pass
    todo = [e for e in extensions if e["packageName"] not in done]
    print(f"{len(todo)} to survey ({len(done)} done)", flush=True)
    with open(OUT, "a") as out, cf.ThreadPoolExecutor(16) as pool:
        for index, row in enumerate(pool.map(survey, todo)):
            out.write(json.dumps(row) + "\n")
            out.flush()
            if index % 50 == 0:
                print(index, row["name"], row.get("result"), row.get("systems"), flush=True)


if __name__ == "__main__":
    main()
