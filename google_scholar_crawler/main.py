from scholarly import scholarly, ProxyGenerator
import jsonpickle
import json
from datetime import datetime
import os
import sys

scholar_id = os.environ.get('GOOGLE_SCHOLAR_ID', '').strip() or 'k3BMw_QAAAAJ'

def fetch_author(id_str):
    try:
        print(f"[scholar] Searching author ID: {id_str} (direct)...", flush=True)
        author = scholarly.search_author_id(id_str)
        scholarly.fill(author, sections=['basics', 'indices', 'counts', 'publications'])
        return author
    except Exception as exc:
        print(f"[scholar] Direct fetch failed ({exc}), attempting with free proxies...", flush=True)
        try:
            pg = ProxyGenerator()
            if pg.FreeProxies():
                scholarly.use_proxy(pg)
                author = scholarly.search_author_id(id_str)
                scholarly.fill(author, sections=['basics', 'indices', 'counts', 'publications'])
                return author
        except Exception as proxy_exc:
            print(f"[scholar] Proxy fetch failed: {proxy_exc}", flush=True)
        raise exc

try:
    author = fetch_author(scholar_id)
except Exception as e:
    print(f"[scholar] Failed to retrieve author data: {e}", flush=True)
    sys.exit(1)

author['updated'] = str(datetime.now())
author['publications'] = {v['author_pub_id']: v for v in author.get('publications', [])}
print(f"[scholar] Successfully fetched {len(author['publications'])} publications, total citations: {author.get('citedby', 0)}")

os.makedirs('results', exist_ok=True)
with open('results/gs_data.json', 'w') as outfile:
    json.dump(author, outfile, ensure_ascii=False)

shieldio_data = {
  "schemaVersion": 1,
  "label": "citations",
  "message": f"{author.get('citedby', 0)}",
}
with open('results/gs_data_shieldsio.json', 'w') as outfile:
    json.dump(shieldio_data, outfile, ensure_ascii=False)
