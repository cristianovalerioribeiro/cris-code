"""Cenário do hero da home: prancha a traço de um empreendimento sobre o lote.

Desenho de linha, como numa prancha de projeto (Brand 45, seção 5):
  fundo  malha de quadras em fio fino
  meio   poucos volumes do entorno, só em aresta, sem preenchimento
  frente o lote demarcado com cotas; o volume escolhido em linha cheia, montado com os
         módulos do símbolo D (hastes crescentes); duas volumetrias alternativas em
         tracejado dourado: o MODELAR desenhado.
As camadas se deslocam no máximo 16px com a rolagem (--p, escrita pelo site.js).
"""
import math

ESCALA = 30
ORIGEM = (320, 236)
COS = math.cos(math.radians(30))
GELO = "#B9C8D4"
OURO = "#B58A44"
OURO_CLARO = "#D4B37C"


def iso(x, y, z=0):
    ox, oy = ORIGEM
    return (ox + (x - y) * COS * ESCALA, oy + (x + y) * 0.5 * ESCALA - z * ESCALA)


def _p(c):
    a, b = iso(*c)
    return f"{a:.1f},{b:.1f}"


def poligono(cs, **attrs):
    extra = " ".join(f'{k.rstrip("_").replace("_", "-")}="{v}"' for k, v in attrs.items())
    return f'<polygon points="{" ".join(_p(c) for c in cs)}" {extra}/>'


def linha(a, b, **attrs):
    (x1, y1), (x2, y2) = iso(*a), iso(*b)
    extra = " ".join(f'{k.rstrip("_").replace("_", "-")}="{v}"' for k, v in attrs.items())
    return f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" {extra}/>'


def losango(x, y, w, d, z=0):
    return [(x, y, z), (x + w, y, z), (x + w, y + d, z), (x, y + d, z)]


def volume(x, y, w, d, h, traco, largura=1, tracejado=None, preenche="none", opacidade=1):
    """Caixa só em arestas visíveis (frente-esquerda, frente-direita e topo)."""
    frente = [(x, y + d, 0), (x + w, y + d, 0), (x + w, y + d, h), (x, y + d, h)]
    lado = [(x + w, y, 0), (x + w, y + d, 0), (x + w, y + d, h), (x + w, y, h)]
    topo = losango(x, y, w, d, h)
    a = dict(fill=preenche, stroke=traco, stroke_width=largura, stroke_linejoin="round")
    if tracejado:
        a["stroke_dasharray"] = tracejado
    return (f'<g opacity="{opacidade}">' + poligono(frente, **a) + poligono(lado, **a)
            + poligono(topo, **a) + "</g>")


def svg():
    fundo, meio, frente = [], [], []
    # malha de quadras (3 x 3), ruas de 1.4
    passo = 7.4
    for i in range(-1, 3):
        for j in range(-1, 3):
            fundo.append(poligono(losango(i * passo, j * passo, 6, 6), fill="none",
                                  stroke=GELO, stroke_width=0.8, opacity=0.28))
    # entorno: poucos volumes, só aresta
    for i, j, dx, dy, w, d, h in [(-1, 0, .8, .8, 4.2, 2.2, 3.2), (0, -1, 1, 1, 2.4, 4, 5.4),
                                  (1, -1, .8, .8, 4.4, 2, 2.6), (-1, 1, 3.2, .8, 2, 4.2, 2.2),
                                  (1, 1, 3.4, .8, 2, 2, 6.2), (0, 1, .8, 3.4, 4.4, 2, 1.8)]:
        meio.append(volume(i * passo + dx, j * passo + dy, w, d, h, GELO, 1, opacidade=0.42))

    # o lote em estudo, na quadra (0,0)
    lx, ly, lw, ld = .4, .4, 5.2, 5.2
    frente.append(poligono(losango(lx, ly, lw, ld), fill="rgba(181,138,68,.08)", stroke=OURO,
                           stroke_width=1.6, stroke_dasharray="7 5", class_="tracejado-decisao"))
    # cotas do lote
    for a, b in [((lx, ly + ld + .8), (lx + lw, ly + ld + .8)), ((lx + lw + .8, ly), (lx + lw + .8, ly + ld))]:
        frente.append(linha((*a, 0), (*b, 0), stroke=GELO, stroke_width=0.8, opacity=0.8))
        for c in (a, b):
            cx, cy = iso(*c, 0)
            frente.append(f'<line x1="{cx-4:.1f}" y1="{cy+4:.1f}" x2="{cx+4:.1f}" y2="{cy-4:.1f}" stroke="{GELO}" stroke-width="1"/>')
    # alternativas modeladas: tracejado dourado
    frente.append(volume(lx + .5, ly + .5, 4.2, 1.6, 8.2, OURO_CLARO, 1.2, "5 5", opacidade=0.75))
    frente.append(volume(lx + .5, ly + .5, 4.2, 4.2, 2.4, OURO_CLARO, 1.2, "5 5", opacidade=0.75))
    # a escolhida: módulos do símbolo D, hastes crescentes, em linha cheia
    for k, h in enumerate((2.6, 3.8, 5.0, 6.2)):
        frente.append(volume(lx + .6 + k * 1.05, ly + 2.8, .9, 1.9, h, "#FFFFFF", 1.3,
                             preenche="rgba(8,37,56,.85)"))
    # marco: o triângulo de decisão
    mx, my = iso(lx + lw / 2, ly + ld + 1.6, 0)
    frente.append(f'<path d="M{mx:.1f} {my-7:.1f} L{mx+7:.1f} {my+5:.1f} L{mx-7:.1f} {my+5:.1f} Z" fill="{OURO}"/>')

    return ('<svg viewBox="0 0 640 620" xmlns="http://www.w3.org/2000/svg" aria-hidden="true" focusable="false">'
            f'<g class="camada-fundo">{"".join(fundo)}</g>'
            f'<g class="camada-meio">{"".join(meio)}</g>'
            f'<g class="camada-frente">{"".join(frente)}</g></svg>')
