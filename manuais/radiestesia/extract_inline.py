# usage: python3 -I extract_inline.py <transcript.jsonl> <out_dir>
import sys, json, base64, os, re
src, out = sys.argv[1], sys.argv[2]
EXT = {'image/jpeg':'jpg','image/png':'png','image/tiff':'tif','image/webp':'webp','application/pdf':'pdf','image/gif':'gif','image/bmp':'bmp'}
def san(t):
    t = re.sub(r'\.[A-Za-z0-9]{2,4}$', '', t)
    return re.sub(r'[^\w\-]+', '_', t)[:80]
def texts(c):
    if isinstance(c, str): yield c
    elif isinstance(c, list):
        for it in c:
            if isinstance(it, dict):
                if it.get('type') == 'text' and isinstance(it.get('text'), str): yield it['text']
                elif it.get('type') == 'tool_result': yield from texts(it.get('content'))
done = 0
for line in open(src, encoding='utf-8', errors='ignore'):
    try: obj = json.loads(line)
    except Exception: continue
    msg = obj.get('message') if isinstance(obj, dict) else None
    cands = []
    if isinstance(msg, dict): cands.append(msg.get('content'))
    if 'toolUseResult' in obj: cands.append(obj['toolUseResult'])
    for c in cands:
        for t in texts(c):
            if '"content"' not in t or len(t) < 1000: continue
            try: d = json.loads(t)
            except Exception:
                m = re.search(r'"content"\s*:\s*"([A-Za-z0-9+/=]{500,})"', t)
                i = re.search(r'"id"\s*:\s*"([^"]+)"', t); mt = re.search(r'"mimeType"\s*:\s*"([^"]+)"', t); ti = re.search(r'"title"\s*:\s*"((?:[^"\\]|\\.)*)"', t)
                if not (m and i and mt and ti): continue
                d = {'content': m.group(1), 'id': i.group(1), 'mimeType': mt.group(1), 'title': ti.group(1)}
            if not (isinstance(d, dict) and isinstance(d.get('content'), str) and d.get('id')): continue
            ext = EXT.get(d.get('mimeType'), 'bin')
            p = os.path.join(out, f"{d['id']}__{san(d.get('title','sem_nome'))}.{ext}")
            if os.path.exists(p) and os.path.getsize(p) > 0: continue
            b = d['content']; b += '=' * (-len(b) % 4)
            try: raw = base64.b64decode(b)
            except Exception as e: print('ERR', d['id'], e); continue
            open(p, 'wb').write(raw); done += 1; print('OK', p, len(raw))
print('inline decoded', done)
