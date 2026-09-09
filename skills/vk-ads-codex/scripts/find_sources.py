"""Search the local official-source index; does not access accounts or network."""
import argparse,json
from pathlib import Path
p=argparse.ArgumentParser(description=__doc__);p.add_argument('query');p.add_argument('--limit',type=int,default=20);a=p.parse_args()
items=json.loads((Path(__file__).resolve().parents[1]/'references/sources.json').read_text(encoding='utf-8'))['sources']
q=a.query.casefold();found=[x for x in items if q in (x['title']+' '+x['url']).casefold()]
print(json.dumps({'matched':len(found),'items':found[:max(0,a.limit)]},ensure_ascii=False,indent=2))
