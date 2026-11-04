// Render unresolved English discussion widgets with the existing Turnstile-Slip
// browser dependency. No accounts, votes or comment submissions are used.
import fs from 'node:fs/promises';
import path from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';
import { createHash } from 'node:crypto';

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const serviceRoot = process.env.TURNSTILE_SLIP_ROOT || path.resolve(root, '../../Turnstile-Slip');
const { launch } = await import(pathToFileURL(path.join(serviceRoot, 'node_modules/cloakbrowser/dist/puppeteer.js')));
const cache = '/tmp/twe-blocked-english';
const output = path.join(root, 'tools/blocked-rendered.jsonl');
const ua = 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36';
const rows = new Map((await fs.readFile(path.join(root, 'tools/blocked-english.jsonl'), 'utf8')).trim().split('\n').map(line => { const row = JSON.parse(line); return [row.pkg, row]; }));
const statuses = JSON.parse(await fs.readFile(path.join(root, 'tools/blocked-english-status.json'), 'utf8'));
let done = new Set();
const retryErrors = process.argv.includes('--retry-errors');
const siteIndex = process.argv.indexOf('--site');
const selectedSite = siteIndex >= 0 ? process.argv[siteIndex + 1] : null;
const urlIndex = process.argv.indexOf('--url');
const requestedUrl = urlIndex >= 0 ? process.argv[urlIndex + 1] : null;
if (requestedUrl && !selectedSite) throw new Error('--url requires --site');
try {
  const latest = new Map((await fs.readFile(output, 'utf8')).trim().split('\n').filter(Boolean).map(line => { const row = JSON.parse(line); return [row.pkg, row]; }));
  done = new Set([...latest.values()].filter(row => !retryErrors || row.status !== 'error').map(row => row.pkg));
} catch {}
const todo = [...rows.values()].filter(row =>
  (selectedSite ? row.name === selectedSite : !done.has(row.pkg)) &&
  (selectedSite || !['working', 'unavailable'].includes(statuses[row.pkg]?.status)) &&
  !['blocked', 'error', 'unreachable'].includes(row.status));
await fs.mkdir(cache, { recursive: true });
const browser = await launch({ headless: true, args: [`--user-agent=${ua}`, '--fingerprint-platform=android', '--fingerprint-brand-version=120', '--fingerprint-brand=Chrome'] });
let serviceQueue = Promise.resolve();
const wait = ms => new Promise(resolve => setTimeout(resolve, ms));
const hash = value => createHash('sha256').update(value).digest('hex');

function publicUrl(raw) {
  const url = new URL(raw);
  url.hash = '';
  for (const key of [...url.searchParams.keys()]) if (/token|key|nonce|csrf|signature/i.test(key)) url.searchParams.delete(key);
  return url.href;
}

async function inspect(row) {
  const context = await browser.createBrowserContext();
  const page = await context.newPage();
  page.setDefaultNavigationTimeout(retryErrors ? 15000 : 35000);
  const requests = [];
  const scripts = [];
  if (process.argv.includes('--scripts')) page.on('response', response => {
    if (response.request().resourceType() !== 'script' || !response.url().startsWith('https://') || /\/cdn-cgi\//.test(response.url()) || new URL(response.url()).origin !== new URL(row.home).origin) return;
    pending.push((async () => { try {
      const file = path.join(cache, hash(response.url()) + '.client.js');
      await fs.writeFile(file, await response.text());
      scripts.push({ url: publicUrl(response.url()), cache: file });
    } catch {} })());
  });
  const pending = [];
  page.on('response', response => {
    const raw = response.url();
    const location = new URL(raw);
    const endpoint = location.hostname + location.pathname;
    if (/oauth|auth\/|login|accounts\.google|facebook\.com/i.test(endpoint)) return;
    if (!/comment|discuss|zmio|disqus|remark42/i.test(endpoint) || !['xhr', 'fetch', 'document'].includes(response.request().resourceType())) return;
    pending.push((async () => {
      const entry = { url: publicUrl(raw), status: response.status(), method: response.request().method() };
      if (response.ok() && (response.request().method() === 'GET' || location.pathname === '/api/embed/comments') && /json/.test(response.headers()['content-type'] || '')) {
        try {
          const data = await response.json();
          if (location.pathname === '/api/embed/comments') {
            const body = JSON.parse(response.request().postData() || '{}');
            entry.thread = Object.fromEntries(Object.entries(body).filter(([key]) => /^(host|path|domainId|pageId|sort)$/i.test(key)));
          }
          entry.keys = Array.isArray(data) ? ['<array>'] : Object.keys(data);
          entry.cache = path.join(cache, hash(raw) + '.response.json');
          await fs.writeFile(entry.cache, JSON.stringify(data));
        } catch {}
      }
      requests.push(entry);
    })());
  });
  const result = { pkg: row.pkg, name: row.name, home: row.home, checkedAt: new Date().toISOString(), requests };
  async function navigate(url) {
    try { await page.goto(url, { waitUntil: 'domcontentloaded' }); }
    catch (error) {
      if (!/Navigation timeout/i.test(error.message) || page.url() === 'about:blank') throw error;
      result.navigationWarning = error.message.slice(0, 180);
    }
  }
  try {
    const interesting = row.pages?.find(p => p.commentHints?.length && !p.url.includes('/wp-content/'));
    let target = requestedUrl || interesting?.url || row.pages?.find(p => p.cache)?.url || row.final || row.home;
    await navigate(target);
    await wait(1800);
    if (/Just a moment|Attention Required/i.test(await page.title())) {
      let session;
      const call = serviceQueue.then(async () => {
        const query = new URLSearchParams({ target, fast: 'true', ua });
        const serviceResponse = await fetch('http://127.0.0.1:3000/api?' + query, { signal: AbortSignal.timeout(85000) });
        if (serviceResponse.ok) session = await serviceResponse.json();
      });
      serviceQueue = call.catch(() => {});
      await call;
      if (session?.cookie) {
        const domain = new URL(page.url() === 'about:blank' ? target : page.url()).hostname;
        const cookies = session.cookie.split(';').map(pair => { const i = pair.indexOf('='); return { name: pair.slice(0, i).trim(), value: pair.slice(i + 1).trim(), domain, path: '/', secure: target.startsWith('https:') }; }).filter(c => c.name);
        await page.setCookie(...cookies);
        await navigate(target);
      }
      await wait(1800);
    }
    if (!requestedUrl && !row.pages?.length) {
      const link = await page.evaluate(() => [...document.querySelectorAll('a[href]')].map(a => a.href).find(url => {
        const parsed = new URL(url);
        return parsed.host === location.host && /\/(?:manga|series|comic|webtoon|title)\/[^/?#]+/.test(parsed.pathname) && !/genre|category|search/.test(parsed.pathname);
      }));
      if (link) { target = link; await navigate(target); await wait(1000); }
    }
    await page.waitForFunction(() => !!document.body, { timeout: 12000 });
    await page.evaluate(() => {
      const target = document.querySelector('#comments, #wpdcom, #disqus_thread, #cusdis_thread, [toonily-comments], #series-discussion, #comment_section, .comments-section, [id*=comment], [class*=comments]');
      if (target) target.scrollIntoView(); else if (document.body) window.scrollTo(0, document.body.scrollHeight);
    });
    for (const selector of ['.btn-load-comments', '.comment_loader_btn', '#disc-tab-comments', '.comments-btn', '[data-reader-comments-open]', '[role="tab"]', 'button', '#lcom']) {
      try {
        for (const element of await page.$$(selector)) {
          const text = await element.evaluate(el => (el.getAttribute('aria-label') || el.textContent).trim());
          const box = await element.boundingBox();
          if (box?.height && (/^(?:(?:show|load)\s+(?:more\s+)?)?(?:(?:series\s+)?comments|discussion)(?:[\s,]*\(?\d+\)?)?$/i.test(text) || /^\d+\s+comments$/i.test(text))) await element.click();
        }
      } catch {}
    }
    await wait(4500);
    result.url = page.url(); result.title = await page.title();
    result.cache = path.join(cache, hash(result.url) + '.rendered.html');
    await fs.writeFile(result.cache, await page.content());
    result.widgets = await page.evaluate(() => {
      const selectors = ['.wpd-comment', 'li.comment', '.comment-body', '.comment-item', '.cw-comment', '[id^="comment-"]:not(script)', '[id^="comment_"]', '#disqus_thread', '#cusdis_thread', '[toonily-comments]'];
      return Object.fromEntries(selectors.map(s => [s, document.querySelectorAll(s).length]).filter(([, count]) => count));
    });
    result.frames = page.frames().map(frame => frame.url()).filter(url => /disqus|comment|zmio|vuukle|remark/i.test(url)).map(publicUrl);
    result.status = /Just a moment|Attention Required/i.test(result.title) ? 'blocked' : 'rendered';
    await Promise.allSettled(pending);
    if (scripts.length) result.scripts = scripts;
  } catch (error) { result.status = 'error'; result.error = error.message.slice(0, 180); }
  finally { await context.close(); }
  // Public request locations and JSON shapes only. Cookies and response bodies are local.
  return result;
}

console.log(`Rendering ${todo.length} unresolved English sites`);
let next = 0;
try {
  await Promise.all(Array.from({ length: 3 }, async () => {
    while (next < todo.length) {
      const row = todo[next++];
      const result = await inspect(row);
      await fs.appendFile(output, JSON.stringify(result) + '\n');
      console.log(result.name, result.status, JSON.stringify(result.widgets || {}), `${result.requests.length} comment requests`);
    }
  }));
} finally { await browser.close(); }
