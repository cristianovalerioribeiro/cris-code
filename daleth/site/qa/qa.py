#!/usr/bin/env python3
"""QA do site DALETH: vocabulário proibido, links, transbordo, console e simulador.

Uso: python3 build.py --local && python3 qa/qa.py
Precisa do Playwright (pip install playwright) e de um Chromium.
"""
import functools, http.server, re, sys, threading, os
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
DIST = RAIZ / "dist"
sys.path.insert(0, str(RAIZ))
import modelo

# Regras inegociáveis (Briefing 30/09): termos que não podem aparecer no texto visível.
PROIBIDO = [
    r"parecer assinad", r"\blaudo\b", r"veredito", r"atestado", r"setup de estrutura",
    r"raio[- ]x", r"garant(e|imos) (a )?aprova", r"assumimos a execução(?! é)",
    r"projeto inteiro", r"solução completa", r"nunca do banco", r"percentual de êxito",
    r"êxito na contrata", r"mensalidade", r"abrimos portas", r"ficamos até funcionar",
    r"potencial não basta", r"começa antes da obra", r"r\$ ?324", r"\bcabal", r"esotér",
    r"\bGERIC\b", r"não administra, não gere",
]
LARGURAS = [360, 390, 768, 1024, 1280, 1440]
CHROME = os.environ.get("CHROME", "/opt/pw-browsers/chromium-1194/chrome-linux/chrome")

def texto_visivel(html):
    html = re.sub(r"<(script|style|svg)\b.*?</\1>", " ", html, flags=re.S)
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", html))

falhas = []
paginas = sorted(DIST.rglob("*.html"))

# 1. vocabulário
for p in paginas:
    t = texto_visivel(p.read_text(encoding="utf-8")).lower()
    for pad in PROIBIDO:
        for m in re.finditer(pad, t, re.I):
            # a frase de categoria aprovada usa "não assumimos a execução"
            trecho = t[max(0, m.start()-30):m.end()+30]
            if "não assumimos a execução" in trecho:
                continue
            falhas.append(f"vocabulário  {p.relative_to(DIST)}: '{m.group(0)}' em …{trecho}…")

# 2. links internos (modo --local: relativos)
for p in paginas:
    for alvo in re.findall(r'(?:href|src)="([^"#:]+)(?:#[^"]*)?"', p.read_text(encoding="utf-8")):
        if alvo.startswith(("http", "mailto", "tel", "//")) or not alvo:
            continue
        if not (p.parent / alvo).resolve().exists():
            falhas.append(f"link quebrado  {p.relative_to(DIST)} -> {alvo}")

# 3. navegador
class Quieto(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *a):
        pass
servidor = http.server.ThreadingHTTPServer(("127.0.0.1", 0), functools.partial(Quieto, directory=str(DIST)))
threading.Thread(target=servidor.serve_forever, daemon=True).start()
base = f"http://127.0.0.1:{servidor.server_port}/"

from playwright.sync_api import sync_playwright
with sync_playwright() as pw:
    nav = pw.chromium.launch(executable_path=CHROME)
    for largura in LARGURAS:
        pg = nav.new_page(viewport={"width": largura, "height": 900})
        erros = []
        pg.on("pageerror", lambda e: erros.append(str(e)))
        pg.on("console", lambda m: erros.append(m.text) if m.type == "error" else None)
        pg.on("response", lambda r: erros.append(f"{r.status} {r.url}") if r.status >= 400 else None)
        for p in paginas:
            rel = p.relative_to(DIST).as_posix()
            erros.clear()
            pg.goto(base + rel)
            larg = pg.evaluate("document.documentElement.scrollWidth")
            if larg > largura:
                quem = pg.evaluate(f"""[...document.querySelectorAll('body *')].filter(e=>{{const r=e.getBoundingClientRect();return r.right>{largura}+1 && getComputedStyle(e).position!=='fixed' && !e.closest('.cenario,.tabela-rolagem')}}).slice(0,3).map(e=>e.tagName+'.'+e.className)""")
                falhas.append(f"transbordo  {rel} @{largura}px: {larg}px {quem}")
            pequenos = pg.evaluate("""[...document.querySelectorAll('h1,h2,h3')].filter(h=>h.offsetParent&&!h.classList.contains('oculto')&&parseFloat(getComputedStyle(h).fontSize)<16).map(h=>h.textContent.trim().slice(0,30))""")
            if pequenos:
                falhas.append(f"título pequeno  {rel} @{largura}px: {pequenos}")
            for e in erros:
                if "404.html" in rel and "404" in e:
                    continue
                falhas.append(f"console  {rel} @{largura}px: {e}")
        pg.close()

    # 4. simulador confere com modelo.py, arranjo por arranjo
    pg = nav.new_page()
    pg.goto(base + "empreendimentos/simulador/index.html")
    for chave, nome, _, params in modelo.ARRANJOS:
        pg.click(f'[data-cenario="{chave}"]')
        tela = pg.text_content("#k-exposicao")
        esperado = modelo.moeda(modelo.calcular(**params)["exposicao"])
        if tela != esperado:
            falhas.append(f"simulador  {nome}: tela {tela} ≠ modelo {esperado}")
    # quadro da home usa os mesmos números
    pg.goto(base + "index.html")
    numeros = pg.eval_on_selector_all(".alt-numero", "els=>els.map(e=>e.firstChild.textContent.trim())")
    esperados = [modelo.moeda(modelo.calcular(**a[3])["exposicao"]) for a in modelo.ARRANJOS]
    if numeros != esperados:
        falhas.append(f"quadro da home {numeros} ≠ {esperados}")
    # menu mobile: abre, isola o resto, fecha com Esc
    m = nav.new_page(viewport={"width": 390, "height": 800})
    m.goto(base + "index.html")
    m.click(".menu-botao")
    if not m.is_visible("#menu") or not m.evaluate("document.querySelector('main').inert"):
        falhas.append("menu mobile não abre ou não isola o conteúdo")
    m.keyboard.press("Escape")
    if m.is_visible("#menu"):
        falhas.append("menu mobile não fecha com Esc")
    nav.close()
servidor.shutdown()

print(f"{len(paginas)} páginas × {len(LARGURAS)} larguras")
if falhas:
    print("\n".join(falhas)); sys.exit(1)
print("tudo certo")
