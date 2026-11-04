// Exercise Twe's actual page extractor against the audited HTML snapshots.
// Requires the local Twe-ios source, Swift and Turnstile-Slip dependencies.
import fs from 'node:fs/promises';
import path from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';
import { execFileSync } from 'node:child_process';

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const serviceRoot = process.env.TURNSTILE_SLIP_ROOT || path.resolve(root, '../../Turnstile-Slip');
const iosRoot = process.env.TWE_IOS_ROOT || path.resolve(root, '../Twe-ios');
const { launch } = await import(pathToFileURL(path.join(serviceRoot, 'node_modules/cloakbrowser/dist/puppeteer.js')));
const loader = await fs.readFile(path.join(iosRoot, 'Twe/Browse/Comments/CommentsLoader.swift'), 'utf8');
const literal = loader.split('private static let generic = ')[1]?.split('\n    """')[0];
if (!literal) throw new Error('Cannot find CommentsScript.generic in Twe-ios');
const directory = await fs.mkdtemp('/tmp/twe-native-extractor-');
const swiftFile = path.join(directory, 'extractor.swift');
await fs.writeFile(swiftFile, 'let generic = ' + literal + '\n    """\nprint(generic)\n');
const source = execFileSync('swift', [swiftFile], { encoding: 'utf8' });
const statuses = JSON.parse(await fs.readFile(path.join(root, 'tools/blocked-english-status.json'), 'utf8'));
const latest = text => new Map(text.trim().split('\n').filter(Boolean).map(line => { const row = JSON.parse(line); return [row.pkg, row]; }));
const audit = latest(await fs.readFile(path.join(root, 'tools/blocked-english.jsonl'), 'utf8'));
const rendered = latest(await fs.readFile(path.join(root, 'tools/blocked-rendered.jsonl'), 'utf8'));
const results = [];
const browser = await launch({ headless: true });
try {
  const page = await browser.newPage();
  await page.setRequestInterception(true);
  page.on('request', request => request.abort());
  for (const [pkg, status] of Object.entries(statuses)) {
    if (status.status !== 'working' || !status.rule) continue;
    const rule = JSON.parse(await fs.readFile(path.join(root, 'rules', status.rule + '.json'), 'utf8')).rules[0];
    if (rule.type !== 'page') continue;
    const snapshots = [rendered.get(pkg), ...(audit.get(pkg)?.pages || [])].filter(Boolean);
    const snapshot = snapshots.find(p => p.url === status.url && p.cache);
    if (!snapshot) throw new Error(`No snapshot for ${status.name}`);
    const html = (await fs.readFile(snapshot.cache, 'utf8')).replace(/<script\b[^>]*>[\s\S]*?<\/script>/gi, '');
    const base = status.url.replace(/&/g, '&amp;').replace(/"/g, '&quot;');
    await page.setContent(`<base href="${base}">` + html, { waitUntil: 'domcontentloaded' });
    const raw = await page.evaluate(source.replace('__TWE_SPEC__', JSON.stringify(rule.page)));
    const result = typeof raw === 'string' ? JSON.parse(raw) : raw;
    if (!result.comments.length) throw new Error(`${status.name}: native extractor returned no comments`);
    const evidence = { name: status.name, rule: status.rule, comments: result.comments.length,
      withImages: result.comments.filter(c => c.images?.length).length,
      maxDepth: Math.max(...result.comments.map(c => c.depth)), more: result.more };
    if (status.name === 'Hiperdex' && !evidence.withImages) throw new Error('Image-only Hiperdex comment was lost');
    if (status.name === 'Comix' && (!evidence.withImages || !evidence.maxDepth)) throw new Error('Comix images or reply nesting were lost');
    results.push(evidence);
    console.log(JSON.stringify(evidence));
  }
  await fs.writeFile(path.join(root, 'tools/blocked-native-verification.json'), JSON.stringify(results, null, 2) + '\n');
} finally {
  await browser.close();
  await fs.rm(directory, { recursive: true, force: true });
}
