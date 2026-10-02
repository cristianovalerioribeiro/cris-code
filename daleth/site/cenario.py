"""Cenário do hero da home: uma implantação em isométrica.

Três camadas, que se aproximam em velocidades diferentes conforme a página desce
(a variável --p é escrita pelo site.js; sem JS, o desenho fica parado):
  fundo  quadras e ruas
  meio   massas edificadas do entorno
  frente o lote em estudo, tracejado, com três volumetrias alternativas

Por que uma implantação: o Manual (p39) pede diagramas que expliquem e veta
imagens de luxo. O terreno é o objeto de trabalho; as três volumetrias sobre o
mesmo lote são o MODELAR desenhado.
"""
import math

ESCALA = 26
ORIGEM = (640, 250)
COS = math.cos(math.radians(30))


def iso(x, y, z=0):
    ox, oy = ORIGEM
    return (ox + (x - y) * COS * ESCALA, oy + (x + y) * 0.5 * ESCALA - z * ESCALA)


def pts(*coords):
    return " ".join(f"{a:.1f},{b:.1f}" for a, b in (iso(*c) for c in coords))


def losango(x, y, w, d, z=0):
    return pts((x, y, z), (x + w, y, z), (x + w, y + d, z), (x, y + d, z))


def caixa(x, y, w, d, h, cor_topo, cor_esq, cor_dir, traco="rgba(255,255,255,.10)", extra=""):
    # faces visíveis: frente-esquerda (y+d), frente-direita (x+w) e topo
    esq = pts((x, y + d, 0), (x + w, y + d, 0), (x + w, y + d, h), (x, y + d, h))
    dir_ = pts((x + w, y, 0), (x + w, y + d, 0), (x + w, y + d, h), (x + w, y, h))
    topo = losango(x, y, w, d, h)
    a = f'stroke="{traco}" stroke-width="1" {extra}'
    return (f'<polygon points="{esq}" fill="{cor_esq}" {a}/>'
            f'<polygon points="{dir_}" fill="{cor_dir}" {a}/>'
            f'<polygon points="{topo}" fill="{cor_topo}" {a}/>')


def aramado(x, y, w, d, h, cor, tracejado="6 5", opacidade=1):
    """Volume só em arestas: uma alternativa ainda não escolhida."""
    p = lambda *c: iso(*c)
    arestas = [
        ((x, y + d, 0), (x + w, y + d, 0)), ((x + w, y, 0), (x + w, y + d, 0)),
        ((x, y + d, 0), (x, y + d, h)), ((x + w, y + d, 0), (x + w, y + d, h)), ((x + w, y, 0), (x + w, y, h)),
        ((x, y, h), (x + w, y, h)), ((x + w, y, h), (x + w, y + d, h)),
        ((x + w, y + d, h), (x, y + d, h)), ((x, y + d, h), (x, y, h)),
    ]
    linhas = "".join(
        f'<line x1="{p(*a)[0]:.1f}" y1="{p(*a)[1]:.1f}" x2="{p(*b)[0]:.1f}" y2="{p(*b)[1]:.1f}"/>'
        for a, b in arestas)
    return (f'<g fill="none" stroke="{cor}" stroke-width="1.4" stroke-dasharray="{tracejado}" '
            f'opacity="{opacidade}" stroke-linecap="round">{linhas}</g>')


def svg():
    fundo, meio = [], []
    # malha de quadras: 4 x 4, cada uma 6 x 6, ruas de 1.6
    passo = 7.6
    for i in range(-1, 4):
        for j in range(-1, 4):
            fundo.append(f'<polygon points="{losango(i * passo, j * passo, 6, 6)}" '
                         'fill="rgba(255,255,255,.025)" stroke="rgba(255,255,255,.16)" stroke-width="1"/>')
    # eixo de rua com marcação central
    for k in range(-1, 4):
        a, b = iso(k * passo - 0.8, -8), iso(k * passo - 0.8, 30)
        fundo.append(f'<line x1="{a[0]:.1f}" y1="{a[1]:.1f}" x2="{b[0]:.1f}" y2="{b[1]:.1f}" '
                     'stroke="rgba(255,255,255,.07)" stroke-dasharray="3 9"/>')

    topo, esq, dir_ = "#1D4F74", "#123D5C", "#0D3350"
    # massas do entorno: (quadra i, j, dx, dy, w, d, h)
    massas = [
        (0, 0, .6, .6, 2.4, 4.6, 4.2), (0, 0, 3.4, .8, 2.0, 2.2, 2.2),
        (1, 0, .8, .8, 4.4, 2.0, 6.5), (1, 0, .8, 3.4, 2.2, 2.0, 2.8),
        (2, 0, 1.0, 1.0, 3.6, 3.6, 3.4),
        (0, 1, .8, .8, 2.0, 2.0, 3.0), (0, 1, 3.2, 3.0, 2.2, 2.4, 5.0),
        (2, 1, .6, .6, 2.0, 4.6, 8.4), (2, 1, 3.0, 2.6, 2.4, 2.6, 3.2),
        (0, 2, 1.0, .8, 4.0, 2.2, 2.4), (0, 2, 1.0, 3.6, 2.0, 2.0, 4.0),
        (1, 2, 3.4, .6, 2.0, 2.0, 2.0),
        (3, 0, .8, .8, 2.0, 2.0, 3.6), (3, 1, .8, .8, 4.0, 2.2, 2.6),
        (-1, 1, 3.0, .8, 2.4, 4.0, 3.0), (1, -1, .8, 3.0, 4.0, 2.4, 3.8),
        (2, 2, .8, .8, 4.4, 4.4, 1.6),
    ]
    massas.sort(key=lambda m: (m[0] * passo + m[2]) + (m[1] * passo + m[3]))
    for i, j, dx, dy, w, d, h in massas:
        meio.append(caixa(i * passo + dx, j * passo + dy, w, d, h, topo, esq, dir_))

    # o lote em estudo: quadra (1,1), à frente
    lx, ly = passo + .5, passo + .5
    lw, ld = 5.0, 5.0
    ouro, ouro_claro = "#B58A44", "#D2B07A"
    frente = [
        f'<polygon points="{losango(lx, ly, lw, ld)}" fill="rgba(181,138,68,.10)" stroke="{ouro}" '
        'stroke-width="2" stroke-dasharray="9 6"/>',
        # cotas do lote
        _cota(lx, ly + ld + .9, lx + lw, ly + ld + .9, ouro_claro),
        _cota(lx + lw + .9, ly, lx + lw + .9, ly + ld, ouro_claro),
        # três alternativas sobre o mesmo lote
        aramado(lx + .4, ly + .4, 4.2, 1.8, 7.5, ouro_claro, "5 6", .55),   # torre esbelta
        aramado(lx + .4, ly + .4, 4.2, 4.2, 3.0, ouro_claro, "5 6", .55),   # lâmina baixa
        caixa(lx + .6, ly + 2.6, 2.0, 2.0, 5.2, "rgba(181,138,68,.55)", "rgba(181,138,68,.30)",
              "rgba(181,138,68,.20)", traco=ouro),
    ]
    marco = iso(lx + lw / 2, ly + ld / 2, 0)
    frente.append(f'<circle cx="{marco[0]:.1f}" cy="{marco[1]:.1f}" r="3.5" fill="{ouro}"/>')

    return (
        '<svg viewBox="0 0 1200 900" xmlns="http://www.w3.org/2000/svg" aria-hidden="true" focusable="false">'
        f'<g class="camada-fundo">{"".join(fundo)}</g>'
        f'<g class="camada-meio">{"".join(meio)}</g>'
        f'<g class="camada-frente">{"".join(frente)}</g>'
        '</svg>')


def _cota(x1, y1, x2, y2, cor):
    a, b = iso(x1, y1), iso(x2, y2)
    return (f'<g stroke="{cor}" stroke-width="1" opacity=".7">'
            f'<line x1="{a[0]:.1f}" y1="{a[1]:.1f}" x2="{b[0]:.1f}" y2="{b[1]:.1f}"/>'
            f'<circle cx="{a[0]:.1f}" cy="{a[1]:.1f}" r="2" fill="{cor}"/>'
            f'<circle cx="{b[0]:.1f}" cy="{b[1]:.1f}" r="2" fill="{cor}"/></g>')
