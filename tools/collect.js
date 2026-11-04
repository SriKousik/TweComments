// Twe comment-rule collector.
//
// Paste into the browser console (F12 → Console) on a title page or a chapter page, AFTER the
// page has loaded, you've passed any Cloudflare check yourself, and you've scrolled down to the
// comments (press "Load more" / "View replies" once if there are any). It prints a JSON report
// and copies it to the clipboard when the browser allows. Send that report to write a rule.
//
// It reads only what's on the page: no cookie values, passwords, tokens or form contents.
(async () => {
  const text = el => (el && (el.innerText || el.textContent) || '').trim();
  const cls = el => (typeof el.className === 'string' ? el.className : el.getAttribute?.('class') || '').trim();
  const trim = (html, n = 1500) => html.replace(/<svg[\s\S]*?<\/svg>/g, '<svg/>').replace(/\s+/g, ' ').slice(0, n);
  const sel = el => {
    if (!el || el === document.body) return 'body';
    if (el.id && !/\d{3,}/.test(el.id)) return `#${el.id}`;
    // Classes shared by every comment: not per-user, per-depth or per-state ones.
    const stable = cls(el).split(/\s+/).filter(c => c && !/\d|author-|^(even|odd|alt|byuser|bypostauthor)$|thread-|depth|level|active|open|show|hidden|selected|user-/.test(c));
    const named = stable.filter(c => /comment|discuss|reply|post|message/i.test(c));
    const classes = (named.length ? named : stable).slice(0, 3);
    return el.tagName.toLowerCase() + classes.map(c => `.${CSS.escape(c)}`).join('');
  };

  // Known comment systems and site templates.
  const html = document.documentElement.outerHTML;
  const systems = [
    ['wpDiscuz', /wpdiscuz|wpdcom/i], ['Disqus', /disqus\.com\/embed\.js|disqus_thread|disqus_shortname/i],
    ['Facebook', /fb-comments|facebook\.com\/plugins\/comments/i], ['Discourse', /data-discourse-url|DiscourseEmbed/i],
    ['zmio', /zmio\.org\/post/i], ['QQ Comment Service', /id="comment-wrapper"\s+data-model=/i], ['Koe comments', /<koe-comments/i],
    ['Manga Comments Pro', /mcp-list|mcp-thread/i], ['Manga Comments System', /class="mcs-comment"/i],
    ['Livewire discussion', /data-testid="comment-discussion"/i], ['Blogger', /content=['"]blogger['"]/i],
    ['Commento', /commento/i], ['Remark42', /remark42/i], ['Cusdis', /cusdis/i], ['Giscus', /giscus/i], ['Utterances', /utteranc\.es/i],
    ['Hyvor', /hyvor/i], ['GraphComment', /graphcomment/i], ['Valine/Waline', /valine|waline/i], ['Twikoo', /twikoo/i],
    ['WordPress', /<ol class="comment-list|class="commentlist|class="comment-respond/i],
  ].filter(([, rx]) => rx.test(html)).map(([name]) => name);
  const theme = [['Madara', /wp-manga|madara/i], ['MangaThemesia', /ts_reader|bixbox|themesia/i], ['HeanCMS', /heancms/i],
    ['Keyoapp', /keyoapp/i], ['ZeistManga', /zeistmanga/i], ['Next.js', /__NEXT_DATA__|\/_next\//], ['Nuxt', /__NUXT__|\/_nuxt\//],
    ['Astro', /astro-island/], ['Livewire', /wire:id=/], ['htmx', /hx-get=|hx-post=/]].filter(([, rx]) => rx.test(html)).map(([n]) => n);

  // Comment sections: named or headed "comments" / "discussion".
  const nameRx = /(comment|discuss|reply|replies|review)/i;
  const containers = new Set();
  document.querySelectorAll('[id], [class]').forEach(el => { if (nameRx.test(`${el.id} ${cls(el)}`) && text(el).length > 20) containers.add(el); });
  document.querySelectorAll('h1,h2,h3,h4,h5,h6,[role=heading]').forEach(h => {
    if (/^\s*(user\s+)?(comments?|discussions?|replies)\b/i.test(text(h)) && text(h).length < 40) containers.add(h.parentElement);
  });

  // In each, the biggest group of look-alike elements: likely the comments.
  const groups = [];
  containers.forEach(container => {
    const bySig = new Map();
    container.querySelectorAll('li, article, div, section').forEach(el => {
      const t = text(el);
      if (t.length < 8 || t.length > 6000 || !el.children.length) return;
      const s = sel(el);
      if (!bySig.has(s)) bySig.set(s, []);
      bySig.get(s).push(el);
    });
    bySig.forEach((els, s) => {
      if (els.length < 2 || groups.some(g => g.selector === s)) return;
      // Whole comments hold more text than their parts (header, footer): favour them.
      const avg = els.reduce((n, e) => n + Math.min(text(e).length, 400), 0) / els.length;
      groups.push({ selector: s, count: els.length, score: els.length * (nameRx.test(s) ? 2 : 1) * avg });
    });
  });
  groups.sort((a, b) => b.score - a.score);
  const best = groups[0];
  const samples = best ? [...document.querySelectorAll(best.selector)].slice(0, 2).map(el => trim(el.outerHTML)) : [];

  // Requests the page made for comments (addresses only).
  const requests = [...new Set(performance.getEntriesByType('resource').map(e => e.name)
    .filter(u => /comment|discuss|disqus|reply|replies|thread|cmt|zmio|graphql|\/api\//i.test(u) && !/\.(css|png|jpe?g|webp|gif|svg|woff2?)(\?|$)/i.test(u)))].slice(0, 25);

  // Comment forms: where they send, and field names (never values).
  const forms = [...document.querySelectorAll('form')].filter(f => nameRx.test(`${f.id} ${cls(f)} ${f.action}`) || f.querySelector('textarea'))
    .slice(0, 4).map(f => ({ selector: sel(f), action: f.getAttribute('action'), method: f.getAttribute('method'),
      fields: [...f.querySelectorAll('input[name], textarea[name], select[name]')].map(i => `${i.name}${i.type === 'hidden' ? ' (hidden)' : ''}`) }));

  // IDs the comments are tied to (data-* attributes near the comments; script config names).
  const ids = {};
  containers.forEach(el => { for (const a of el.attributes || []) if (/^data-/.test(a.name) && a.value.length < 80) ids[`${sel(el)} ${a.name}`] = a.value; });
  const configNames = [...new Set((html.match(/\b(?:var|let|const)\s+([A-Za-z_$][\w$]*(?:comment|Comment|disqus|nonce|post_?id|manga_?id|chapter_?id)[\w$]*)/g) || []).map(s => s.split(/\s+/)[1]))].slice(0, 15);
  const globals = Object.keys(window).filter(k => /comment|disqus|discuz|nonce|ajax/i.test(k)).slice(0, 15);

  const report = {
    page: location.href, title: document.title, kind: /chapter|episode|\/read\/|\/ch-?\d/i.test(location.pathname) ? 'chapter' : 'title',
    systems, theme, signedIn: /log ?out|sign ?out/i.test(document.body.innerText),
    commentCountText: (document.body.innerText.match(/\b\d[\d,.]*\s+(comments?|replies)\b/i) || [null])[0],
    commentGroups: groups.slice(0, 5).map(({ selector, count }) => ({ selector, count })), samples,
    iframes: [...document.querySelectorAll('iframe')].map(f => f.src).filter(s => s && nameRx.test(s) || /disqus|zmio|discourse|giscus|utteranc/i.test(s)).slice(0, 5),
    requests, forms, ids, configNames, globals,
    csrfMeta: [...document.querySelectorAll('meta[name*=csrf i], meta[name*=token i]')].map(m => m.getAttribute('name')),
    cookieNames: document.cookie.split('; ').map(c => c.split('=')[0]).filter(Boolean),
  };
  const json = JSON.stringify(report, null, 2);
  console.log(json);
  try { copy(json); console.log('Report copied to the clipboard.'); } catch { try { await navigator.clipboard.writeText(json); console.log('Report copied to the clipboard.'); } catch { console.log('Copy the report above.'); } }
  return report;
})();
