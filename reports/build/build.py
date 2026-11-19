"""Monta o livro: capa + sumário + capítulos (chapters/*.html) + créditos -> HTML -> PDF (Chromium)."""
import glob, html, json, os, re, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPORTS = os.path.dirname(HERE)
OUT_HTML = os.path.join(REPORTS, "_livro.html")
OUT_PDF = os.path.join(REPORTS, "Símbolos de proteção para a porta - guia ilustrado.pdf")

def slug(s):
    s = re.sub(r"<[^>]+>", "", s).lower()
    s = re.sub(r"[^a-z0-9à-ú]+", "-", s).strip("-")
    return s[:60]

ONLY = sys.argv[1] if len(sys.argv) > 1 else None  # prévia de um capítulo: python3 build.py 04_runas
if ONLY:
    OUT_HTML = os.path.join(REPORTS, f"_previa_{ONLY}.html")
    OUT_PDF = os.path.join(REPORTS, f"_previa_{ONLY}.pdf")
chapters, toc, n = [], [], 0
for path in sorted(glob.glob(os.path.join(HERE, "chapters", "*.html"))):
    if ONLY and ONLY not in os.path.basename(path):
        continue
    body = open(path, encoding="utf-8").read()
    n += 1
    def h1(m):
        title = m.group(1)
        cid = f"c{n}"
        toc.append(("c", cid, re.sub(r"<[^>]+>", "", title)))
        return f'<h1 id="{cid}"><span class="num">Capítulo {n}</span>{title}</h1>'
    body = re.sub(r"<h1[^>]*>(.*?)</h1>", h1, body, count=1, flags=re.S)
    k = [0]
    def h2(m):
        k[0] += 1
        sid = f"c{n}s{k[0]}"
        toc.append(("s", sid, re.sub(r"<[^>]+>", "", m.group(1))))
        return f'<h2 id="{sid}">{m.group(1)}</h2>'
    body = re.sub(r"<h2[^>]*>(.*?)</h2>", h2, body, flags=re.S)
    chapters.append(f'<section class="chapter">{body}</section>')

# créditos das imagens
credits = ""
mpath = os.path.join(REPORTS, "assets", "manifest.json")
if os.path.exists(mpath):
    used = "".join(chapters)
    rows = []
    for it in json.load(open(mpath, encoding="utf-8")):
        if f'assets/{it["file"]}' in used:
            rows.append("<tr><td>{}</td><td>{}</td><td>{}</td><td><a style=\"word-break:normal;white-space:nowrap\" href=\"{}\">Commons</a></td></tr>".format(
                html.escape(it.get("caption_pt", it["file"])[:110]), html.escape(("autor desconhecido" if str(it.get("author", "")).lower().startswith("unknown") or not it.get("author") else re.sub(r"<[^>]+>", "", str(it.get("author", ""))))[:70]),
                html.escape(str(it.get("license", ""))), html.escape(it.get("source_url", ""))))
    if rows:
        n += 1
        toc.append(("c", "creditos", "Créditos das imagens"))
        credits = ('<section class="chapter"><h1 id="creditos"><span class="num">Anexo</span>Créditos das imagens</h1>'
                   '<p>Todas as fotografias vêm do Wikimedia Commons, sob licença livre ou em domínio público. Os diagramas foram desenhados para este estudo.</p>'
                   '<table><thead><tr><th>Imagem</th><th>Autor</th><th>Licença</th><th>Fonte</th></tr></thead><tbody>' + "".join(rows) + "</tbody></table></section>")

toc_html = '<section class="toc"><h1>Sumário</h1><ol>' + "".join(
    f'<li class="{c}"><a href="#{i}">{t}</a></li>' for c, i, t in toc) + "</ol></section>"
cover = open(os.path.join(HERE, "cover.html"), encoding="utf-8").read()
css = open(os.path.join(HERE, "style.css"), encoding="utf-8").read()
doc = f'<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><title>Símbolos de proteção para a porta</title><style>{css}</style></head><body>{cover}{toc_html}{"".join(chapters)}{credits}</body></html>'
open(OUT_HTML, "w", encoding="utf-8").write(doc)

missing = [m for m in re.findall(r'src="(assets/[^"]+)"', doc) if not os.path.exists(os.path.join(REPORTS, m))]
if missing:
    print("IMAGENS AUSENTES:", sorted(set(missing)))
subprocess.run(["node", os.path.join(HERE, "render.js"), OUT_HTML, OUT_PDF], check=True)
print("PDF:", OUT_PDF)
