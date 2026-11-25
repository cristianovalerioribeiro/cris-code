#!/usr/bin/env python3
"""Decode a Drive download result (JSON with "content" base64, or raw base64) to a file.
usage: python3 -I tools_download.py <input_file> <output_path>
"""
import sys, json, base64, re, os
src, dst = sys.argv[1], sys.argv[2]
raw = open(src, 'rb').read()
txt = raw.decode('utf-8', errors='ignore').strip()
b64 = None
if txt.startswith('{'):
    try:
        obj = json.loads(txt)
        b64 = obj.get('content')
    except Exception:
        m = re.search(r'"content"\s*:\s*"([^"]+)"', txt)
        if m:
            b64 = m.group(1)
if b64 is None:
    b64 = txt
b64 = re.sub(r'\s+', '', b64)
b64 += '=' * (-len(b64) % 4)
data = base64.b64decode(b64)
os.makedirs(os.path.dirname(dst), exist_ok=True)
open(dst, 'wb').write(data)
print(dst, len(data), 'bytes')
