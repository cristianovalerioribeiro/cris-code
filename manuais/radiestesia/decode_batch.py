#!/usr/bin/env python3
"""Decode every spooled Drive download result into OUT dir as <id>__<sanitized title>.<ext>.
usage: python3 -I decode_batch.py <tool_results_dir> <out_dir> [done_log]
"""
import sys, os, json, base64, re, glob
src_dir, out_dir = sys.argv[1], sys.argv[2]
log = sys.argv[3] if len(sys.argv) > 3 else os.path.join(out_dir, '..', 'livro', 'decoded.log')
os.makedirs(out_dir, exist_ok=True)
done = set()
if os.path.exists(log):
    done = set(l.split('\t')[0] for l in open(log, encoding='utf-8').read().splitlines() if l)
EXT = {'image/jpeg':'jpg','image/png':'png','image/tiff':'tif','image/webp':'webp','application/pdf':'pdf','image/gif':'gif','image/bmp':'bmp'}
def sanitize(t):
    t = re.sub(r'\.[A-Za-z0-9]{2,5}$', '', t)
    t = re.sub(r'[^\w\-\. ]+', '_', t, flags=re.UNICODE)
    t = re.sub(r'\s+', '_', t).strip('_')
    return t[:80] or 'arquivo'
n = 0
for p in sorted(glob.glob(os.path.join(src_dir, 'mcp-Google_Drive-download_file_content-*.txt'))):
    if p in done:
        continue
    try:
        txt = open(p, 'rb').read().decode('utf-8', errors='ignore')
        m_id = re.search(r'"id"\s*:\s*"([^"]+)"', txt)
        m_t = re.search(r'"title"\s*:\s*"((?:[^"\\]|\\.)*)"', txt)
        m_m = re.search(r'"mimeType"\s*:\s*"([^"]+)"', txt)
        m_c = re.search(r'"content"\s*:\s*"([^"]*)"', txt)
        if not (m_id and m_c):
            print('SKIP (no id/content):', p); continue
        fid = m_id.group(1); title = json.loads('"' + m_t.group(1) + '"') if m_t else fid
        mime = m_m.group(1) if m_m else ''
        ext = EXT.get(mime, (title.rsplit('.',1)[-1].lower() if '.' in title else 'bin'))
        b64 = re.sub(r'\s+', '', m_c.group(1)); b64 += '=' * (-len(b64) % 4)
        data = base64.b64decode(b64)
        out = os.path.join(out_dir, f'{fid}__{sanitize(title)}.{ext}')
        open(out, 'wb').write(data)
        with open(log, 'a', encoding='utf-8') as f:
            f.write(f'{p}\t{fid}\t{out}\t{len(data)}\n')
        print('OK', fid, os.path.basename(out), len(data)); n += 1
    except Exception as e:
        print('ERR', p, e)
print('decoded', n)
