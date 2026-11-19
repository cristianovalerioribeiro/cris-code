"""Versão 2: busca por HTML (sem API), metadados em lote (API, 50 títulos por chamada), download de upload.wikimedia.org."""
import hashlib, html, json, os, re, subprocess, sys, time, urllib.parse
from PIL import Image
HERE = os.path.dirname(os.path.abspath(__file__)); ASSETS = os.path.join(HERE, "..", "assets")
UA = "DoorSymbolsBook/1.0 (educational research)"
OK = re.compile(r"^(public domain|pd|cc0|cc[ -]by([ -]sa)?([ -]\d\.\d)?( \w+)?)", re.I)
TOPICS = json.load(open(os.path.join(HERE, "image_topics.json"), encoding="utf-8"))
mpath = os.path.join(ASSETS, "manifest.json")
manifest = {m["file"]: m for m in (json.load(open(mpath, encoding="utf-8")) if os.path.exists(mpath) else [])}
cpath = os.path.join(HERE, "candidates.json")
cands = json.load(open(cpath)) if os.path.exists(cpath) else {}

def curl(url, out=None):
    cmd = ["curl", "-sS", "-L", "-m", "90", "-A", UA, "-w", "%{http_code}", url] + (["-o", out] if out else [])
    r = subprocess.run(cmd, capture_output=True).stdout
    return (r[-3:].decode(), r[:-3]) if not out else (r.decode()[-3:], b"")

only = sys.argv[1:]
todo = [k for k in TOPICS if (k in only) or (not only and k + ".jpg" not in manifest)]
# 1) busca HTML
for k in todo:
    if k in cands and not only: continue
    titles = []
    for q in TOPICS[k]["q"]:
        for attempt in range(6):
            code, body = curl("https://commons.wikimedia.org/w/index.php?fulltext=1&ns6=1&limit=12&search=" + urllib.parse.quote(q + " filetype:bitmap"))
            if code == "200": break
            time.sleep(10)
        for t in re.findall(r'title="(File:[^"]+)"', body.decode("utf-8", "ignore")):
            t = html.unescape(t)
            if "page does not exist" not in t and t not in titles and re.search(r"\.(jpe?g|png)$", t, re.I): titles.append(t)
        time.sleep(2.5)
        if len(titles) >= 5: break
    cands[k] = titles[:8]
    print("busca", k, len(titles), flush=True)
    json.dump(cands, open(cpath, "w"), ensure_ascii=False)
# 2) metadados em lote
info = {}
alltitles = sorted({t for k in todo for t in cands.get(k, [])})
strip = lambda s: re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", s or "")).strip()
for i in range(0, len(alltitles), 40):
    batch = alltitles[i:i + 40]
    url = "https://commons.wikimedia.org/w/api.php?action=query&format=json&prop=imageinfo&iiprop=url|extmetadata|size|mime&titles=" + urllib.parse.quote("|".join(batch))
    for attempt in range(40):
        code, body = curl(url)
        if code == "200":
            for p in json.loads(body).get("query", {}).get("pages", {}).values():
                ii = (p.get("imageinfo") or [None])[0]
                if ii: info[p["title"]] = ii
            break
        time.sleep(11)
    print("meta lote", i, code, len(info), flush=True); time.sleep(3)
# 3) download
for k in todo:
    pick = TOPICS[k].get("pick", 0); n = 0; got = False
    for t in cands.get(k, []):
        ii = info.get(t.replace("_", " ")) or info.get(t)
        if not ii: continue
        md = ii.get("extmetadata", {}); lic = md.get("LicenseShortName", {}).get("value", "")
        if not OK.match(lic) or ii.get("width", 0) < 500 or ii.get("mime") not in ("image/jpeg", "image/png"): continue
        n += 1
        if n <= pick: continue
        url = ii["url"].split("?")[0]
        if ii["width"] > 1280:
            m = re.match(r"(https://upload\.wikimedia\.org/wikipedia/commons)/(./../)(.+)$", url)
            url = f"{m.group(1)}/thumb/{m.group(2)}{m.group(3)}/1280px-{m.group(3)}"
        dest = os.path.join(ASSETS, k + ".jpg")
        curl(url, dest)
        try:
            im = Image.open(dest); im.load(); im = im.convert("RGB")
        except Exception:
            time.sleep(3); continue
        if im.width > 1280: im = im.resize((1280, int(im.height * 1280 / im.width)))
        im.save(dest, "JPEG", quality=80, optimize=True)
        manifest[k + ".jpg"] = dict(file=k + ".jpg", topic=TOPICS[k]["topic"], caption_pt=TOPICS[k]["topic"], commons_title=t,
            commons_desc=strip(md.get("ImageDescription", {}).get("value", ""))[:300], author=strip(md.get("Artist", {}).get("value", ""))[:120],
            license=lic, license_url=md.get("LicenseUrl", {}).get("value", ""), source_url=ii.get("descriptionurl", ""), width=im.width, height=im.height)
        got = True; break
    print("OK   " if got else "FALHA", k, "|", manifest.get(k + ".jpg", {}).get("commons_title", "") if got else "", flush=True)
    json.dump(list(manifest.values()), open(mpath, "w", encoding="utf-8"), ensure_ascii=False, indent=1); time.sleep(1.5)
