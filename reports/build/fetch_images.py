"""Baixa imagens de licença livre do Wikimedia Commons. Uso: python3 fetch_images.py [chave ...]"""
import json, os, re, subprocess, sys, time, urllib.parse
from PIL import Image

ASSETS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "assets")
UA = "DoorSymbolsBook/1.0 (educational research)"
OK = re.compile(r"^(public domain|pd|cc0|cc[ -]by([ -]sa)?([ -]\d\.\d)?( \w+)?)", re.I)
TOPICS = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "image_topics.json"), encoding="utf-8"))

def curl(url, out=None):
    cmd = ["curl", "-sS", "-L", "-m", "60", "-A", UA, url]
    if out: cmd += ["-o", out]
    return subprocess.run(cmd, capture_output=True).stdout

def search(q, n=8):
    url = ("https://commons.wikimedia.org/w/api.php?action=query&format=json&generator=search&gsrnamespace=6&gsrlimit=%d"
           "&prop=imageinfo&iiprop=url|extmetadata|size|mime&gsrsearch=%s" % (n, urllib.parse.quote(q)))
    pages = {}
    for attempt in range(14):
        raw = curl(url)
        try:
            pages = json.loads(raw).get("query", {}).get("pages", {}); break
        except Exception:
            time.sleep(11)
    time.sleep(4)
    res = []
    for p in sorted(pages.values(), key=lambda p: p.get("index", 99)):
        ii = (p.get("imageinfo") or [{}])[0]; md = ii.get("extmetadata", {})
        lic = md.get("LicenseShortName", {}).get("value", "")
        if ii.get("mime") not in ("image/jpeg", "image/png") or not OK.match(lic) or ii.get("width", 0) < 500: continue
        strip = lambda s: re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", s or "")).strip()
        res.append(dict(title=p["title"], url=ii["url"], w=ii["width"], h=ii["height"], license=lic,
                        license_url=md.get("LicenseUrl", {}).get("value", ""), author=strip(md.get("Artist", {}).get("value", ""))[:120],
                        desc=strip(md.get("ImageDescription", {}).get("value", ""))[:300], source_url=ii.get("descriptionurl", "")))
    return res

def download(c, dest):
    url = c["url"].split("?")[0]
    if c["w"] > 1280:
        m = re.match(r"(https://upload\.wikimedia\.org/wikipedia/commons)/(./../)(.+)$", url)
        url = f"{m.group(1)}/thumb/{m.group(2)}{m.group(3)}/1280px-{m.group(3)}"
    curl(url, dest)
    try:
        im = Image.open(dest); im.load()
    except Exception:
        if os.path.exists(dest): os.remove(dest)
        return False
    im = im.convert("RGB")
    if im.width > 1280: im = im.resize((1280, int(im.height * 1280 / im.width)))
    im.save(dest, "JPEG", quality=80, optimize=True)
    c["width"], c["height"] = im.size
    return True

mpath = os.path.join(ASSETS, "manifest.json")
manifest = {m["file"]: m for m in (json.load(open(mpath, encoding="utf-8")) if os.path.exists(mpath) else [])}
keys = sys.argv[1:] or list(TOPICS)
for key in keys:
    spec = TOPICS[key]; fname = key + ".jpg"
    if fname in manifest and not sys.argv[1:]: continue
    got = False
    for q in spec["q"]:
        cands = search(q)
        pick = spec.get("pick", 0)
        for c in cands[pick:] :
            if download(c, os.path.join(ASSETS, fname)):
                manifest[fname] = dict(file=fname, topic=spec["topic"], caption_pt=spec["topic"], commons_title=c["title"], commons_desc=c["desc"],
                                       author=c["author"], license=c["license"], license_url=c["license_url"], source_url=c["source_url"],
                                       width=c["width"], height=c["height"])
                got = True; break
            time.sleep(3)
        if got: break
    print(("OK   " if got else "FALHA"), key, "|", manifest.get(fname, {}).get("commons_title", ""), flush=True)
    json.dump(list(manifest.values()), open(mpath, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    time.sleep(2)
