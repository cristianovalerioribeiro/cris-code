# -*- coding: utf-8 -*-
"""Pós-processamento do .docx: ids únicos nos marcadores (o docx-js repetiu o id 1) e hifenização automática nas configurações."""
import sys, re, zipfile, shutil, os, subprocess, tempfile
src = sys.argv[1]; tmp = tempfile.mkdtemp()
with zipfile.ZipFile(src) as z: z.extractall(tmp)
p = os.path.join(tmp, "word", "document.xml"); x = open(p, encoding="utf-8").read()
n = [0]
def renum(m):
    n[0] += 1; return m.group(1) + str(n[0]) + m.group(3)
x = re.sub(r'(<w:bookmarkStart[^>]*w:id=")(\d+)("[^>]*/>)', renum, x)
k = [0]
def renum_end(m):
    k[0] += 1; return f'<w:bookmarkEnd w:id="{k[0]}"/>'
x = re.sub(r'<w:bookmarkEnd w:id="\d+"/>', renum_end, x)
assert n[0] == k[0], (n[0], k[0])
open(p, "w", encoding="utf-8").write(x)
ps = os.path.join(tmp, "word", "settings.xml"); st = open(ps, encoding="utf-8").read()
if "autoHyphenation" not in st:
    hy = '<w:autoHyphenation/><w:hyphenationZone w:val="283"/>'
    if "<w:defaultTabStop" in st: st = re.sub(r"(<w:defaultTabStop[^>]*/>)", r"\1" + hy, st, count=1)
    elif "<w:evenAndOddHeaders" in st: st = st.replace("<w:evenAndOddHeaders", hy + "<w:evenAndOddHeaders", 1)
    else: st = st.replace("</w:settings>", hy + "</w:settings>")
    open(ps, "w", encoding="utf-8").write(st)
out = src + ".tmp"
if os.path.exists(out): os.remove(out)
subprocess.run(["zip", "-XrD", "-q", os.path.abspath(out), "."], cwd=tmp, check=True)
shutil.move(out, src); shutil.rmtree(tmp); print("marcadores renumerados:", n[0], "| hifenização ok")
