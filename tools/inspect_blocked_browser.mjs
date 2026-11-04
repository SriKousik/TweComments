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
try { done = new Set((await fs.readFile(output, 'utf8')).trim().split('\n').filter(Boolean).map(line => JSON.parse(line).pkg)); } catch {}
const todo = [...rows.values()].filter(row => !done.has(row.pkg) && !['working', 'unavailable'].includes(statuses[row.pkg]?.status) && !['blocked', 'error', 'unreachable'].includes(row.status));
await fs.mkdir(cache, { recursive: true });
const browser = await launch({ headless: true, args: [`--user-agent=${ua}`, '--fingerprint-platform=android', '--fingerprint-brand-version=120', '--fingerprint-brand=Chrome'] });
let serviceQueue = Promise.resolve();
const wait = ms => new Promise(resolve => setTimeout(resolve, ms));
const hash = value => createHash('sha256').update(value).digest('hex');

function publicUrl(raw) {
  const url = new URL(raw);
  for (const key of [...url.searchParams.keys()]) if (/token|key|nonce|csrf|signature/i.test(key)) url.searchParams.delete(key);
  return url.href;
}

async function inspect(row) {
  const context = await browser.createBrowserContext();
  const page = await context.newPage();
  page.setDefaultNavigationTimeout(35000);
  const requests = [];
  const pending = [];
  page.on('response', response => {
    const raw = response.url();
    if (!/comment|discuss|zmio|disqus|remark42/i.test(raw) || !['xhr', 'fetch', 'document'].includes(response.request().resourceType())) return;
    pending.push((async () => {
      const entry = { url: publicUrl(raw), status: response.status(), method: response.request().method() };
      if (response.ok() && response.request().method() === 'GET' && /json/.test(response.headers()['content-type'] || '')) {
        try {
          const data = await response.json();
          entry.keys = Array.isArray(data) ? ['<array>'] : Object.keys(data);
          entry.cache = path.join(cache, hash(raw) + '.response.json');
          await fs.writeFile(entry.cache, JSON.stringify(data));
        } catch {}
      }
      requests.push(entry);
    })());
  });
  const result = { pkg: row.pkg, name: row.name, home: row.home, checkedAt: new Date().toISOString(), requests };
  try {
    const interesting = row.pages?.find(p => p.commentHints?.length && !p.url.includes('/wp-content/'));
    let target = interesting?.url || row.pages?.find(p => p.cache)?.url || row.final || row.home;
    await page.goto(target, { waitUntil: 'domcontentloaded' });
    await wait(1800);
    if (/Just a moment|Attention Required/i.test(await page.title())) {
      let session;
      const call = serviceQueue.then(async () => {
        const query = new URLSearchParams({ target, fast: 'true', ua });
        const response = await fetch('http://127.0.0.1:3000/api?' + query, { signal: AbortSignal.timeout(85000) });
        if (response.ok()) session = await response.json();
      });
      serviceQueue = call.catch(() => {});
      await call;
      if (session?.cookie) {
        const domain = new URL(target).hostname;
        const cookies = session.cookie.split(';').map(pair => { const i = pair.indexOf('='); return { name: pair.slice(0, i).trim(), value: pair.slice(i + 1).trim(), domain, path: '/', secure: target.startsWith('https:') }; }).filter(c => c.name);
        await context.setCookie(...cookies);
        await page.reload({ waitUntil: 'domcontentloaded' });
      }
      await wait(1800);
    }
    if (!row.pages?.length) {
      const link = await page.evaluate(() => [...document.querySelectorAll('a[href]')].map(a => a.href).find(url => {
        const parsed = new URL(url);
        return parsed.host === location.host && /\/(?:manga|series|comic|webtoon|title)\/[^/?#]+/.test(parsed.pathname) && !/genre|category|search/.test(parsed.pathname);
      }));
      if (link) { target = link; await page.goto(target, { waitUntil: 'domcontentloaded' }); await wait(1000); }
    }
    await page.evaluate(() => {
      const target = document.querySelector('#comments, #wpdcom, #disqus_thread, #cusdis_thread, [toonily-comments], #series-discussion, #comment_section, .comments-section, [id*=comment], [class*=comments]');
      if (target) target.scrollIntoView(); else window.scrollTo(0, document.body.scrollHeight);
    });
    for (const selector of ['.btn-load-comments', '.comment_loader_btn', '#disc-tab-comments', '.comments-btn', '[role="tab"]']) {
      try {
        await page.evaluate(selector => {
          for (const el of document.querySelectorAll(selector)) {
            if (el.getBoundingClientRect().height && /^(?:show |load )?(?:comments|discussion)(?:\s*\(?\d+\)?)?$/i.test(el.textContent.trim())) el.click();
          }
        }, selector);
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
