"""Inspect extra title/chapter samples after blocked_english.py; uses its local cache."""
import sys,json,pathlib,concurrent.futures,re
import blocked_english as audit
rows={json.loads(l)['pkg']:json.loads(l) for l in audit.OUT.read_text().splitlines()}
statuses=json.loads((audit.ROOT/'tools/blocked-english-status.json').read_text())
def deep(r):
 pages=r.get('pages',[])
 for p in pages+[r.get('homeEvidence',{})]:
  cache=p.get('cache') or (r.get('cache') if p is r.get('homeEvidence') else None)
  if cache and pathlib.Path(cache).exists():
   _,new=audit.inspect(p.get('url',r.get('final',r['home'])),pathlib.Path(cache).read_text());p.update(new)
 systems={s for p in pages for s in p.get('systems',[])}
 if systems:r['systems']=sorted(systems)
 if r['pkg'] in statuses:return r
 if r['status'] in ('blocked','error','unreachable'):return r
 candidates=list(r.get('candidates',[]))[2:5]
 # Include a real chapter when title pages have only an empty form or no discussion.
 for p in pages[:2]:
  if p.get('cache'):
   soup,_=audit.inspect(p['url'],pathlib.Path(p['cache']).read_text())
   for a in soup.select('a[href]'):
    if re.search(r'chapter[-/]|/read/|chaptered.php|/reader/',a['href'],re.I):
     from urllib.parse import urljoin
     target=urljoin(p['url'],a['href'])
     if target.startswith(('https://','http://')):candidates.append(target);break
 checked={p['url'] for p in pages}
 for target in list(dict.fromkeys(candidates))[:4]:
  if target in checked:continue
  try:
   code,url,body,denied,cookie,cache=audit.fetch(target)
   if code<400 and not denied:
    _,e=audit.inspect(url,body);e['cache']=cache;pages.append(e)
    systems.update(e['systems'])
    if any(e.get('counts',{}).values()):break
  except Exception:pass
 r['pages']=pages;r['systems']=sorted(systems)
 if systems:r['status']='comments-found'
 r['deepened']=True
 return r
print('Deepening',len(rows),'sites',flush=True)
with concurrent.futures.ThreadPoolExecutor(12) as ex,audit.OUT.open('a') as out:
 for r in ex.map(deep,rows.values()):
  out.write(json.dumps(r,ensure_ascii=False)+'\n');out.flush()
  if r.get('systems'):print(r['name'],r['systems'],flush=True)
