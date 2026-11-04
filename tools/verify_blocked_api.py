import json,pathlib,re
# Requires the local response/HTML caches from the English audit (not committed).
R=pathlib.Path(__file__).resolve().parents[1];P=pathlib.Path('/tmp/twe-blocked-english')
def value(obj,path):
 for k in path.split('.'):
  if not k:continue
  obj=obj.get(k) if isinstance(obj,dict) else obj[int(k)] if isinstance(obj,list) else None
 return obj
fixtures=[('atsu','bca5837c559dbc30460695d07af6d768c2674e608a81f67af23f6022e002288f.response.json',7),('flamecomics','2bb99cf4c9dc70512b7b3c14d17cfe2b1e1120b1bf400120165f530d8524ab23.response.json',11),('diva-valir','diva-discussion.json',2),('diva-valir','valir-discussion.json',1),('diva-valir','diva-chapter-comments.json',13),('diva-valir','valir-chapter-comments.json',14),('lolobun','lolobun-comments.json',2),('jnovel-forum','jnovel-forum.json',20),('jnovel-forum','jnovel-page2.json',20),('webtoonlib','webtoonlib-api-0.json',50),('webtoonlib','webtoon-chapter.json',4),('toonkotsu','toon-final-0.json',1),('toonkotsu','toon-api-1.json',1),('toonkotsu','toon-final-1.json',1)]
results=[]
for rule,file,minimum in fixtures:
 api=json.loads((R/f'rules/{rule}.json').read_text())['rules'][0]['api'];d=json.loads((P/file).read_text());rows=value(d,api['list']);assert len(rows)>=minimum,(rule,file,len(rows))
 flattened=[]
 def walk(items):
  for item in items:
   assert value(item,api['id']) is not None,(rule,'id')
   assert value(item,api['author']),(rule,'author')
   assert value(item,api['text']),(rule,'text')
   flattened.append(item)
   if api.get('children') and value(item,api['children']):walk(value(item,api['children']))
 walk(rows);results.append({'rule':rule,'sample':file,'roots':len(rows),'includingReplies':len(flattened),'authorAndText':True})
# Actual saved title/chapter HTML must resolve IDs, not merely fit a hand-written fixture.
for rule,file,target,expected in [('toonkotsu','toonkotsu-title.html',None,'38090'),('toonkotsu','toonkotsu-service.html',None,'38090'),('webtoonlib','fb816988557c5e3b07e0b586a771e3b598f6c066a3d63deda5d830ce67a613f8.rendered.html','entry','cmim8tn7v03d7e12665ce9f58'),('webtoonlib','webtoonlib-chapter.html','chapter','cmin6ptvql5i860y4bmb')]:
 r=json.loads((R/f'rules/{rule}.json').read_text())['rules'][0];v=(r[target] if target else r)['vars'];var=v.get('targetId',v.get('seriesId'));m=re.search(var['regex'],(P/file).read_text());assert m and m.group(1)==expected,(rule,file)
(R/'tools/blocked-api-verification.json').write_text(json.dumps(results,indent=2)+'\n');print('Verified',len(fixtures),'real API fixtures and title/chapter ID extraction')
