"""Modelo de caixa ilustrativo, gêmeo do assets/js/ferramentas.js.

Monta o quadro de alternativas da home ({{QUADRO}}): o mesmo empreendimento de
exemplo em quatro estruturas de capital, com a exposição máxima de cada uma.
Os números saem daqui, na hora do build, para não existir número escrito à mão.
"""
MESES, OBRA, CUSTO, DESPESAS, REPASSE = 30, 24, 0.55, 0.12, 3

ARRANJOS = [
    ("proprio", "Capital próprio", "Terreno em dinheiro, sem vender na planta nem tomar crédito",
     dict(vgv=20, terreno=15, permuta=0, planta=0, credito=0)),
    ("planta", "Vendas na planta", "40% do VGV vendido e recebido durante a obra",
     dict(vgv=20, terreno=15, permuta=0, planta=40, credito=0)),
    ("permuta", "Permuta do terreno", "70% do terreno pago em unidades, e não em dinheiro",
     dict(vgv=20, terreno=15, permuta=70, planta=0, credito=0)),
    ("combinada", "Estrutura combinada", "Permuta, vendas na planta e crédito de obra juntos",
     dict(vgv=20, terreno=15, permuta=70, planta=35, credito=55)),
]


def calcular(vgv, terreno, permuta, planta, credito):
    vgv *= 1e6
    custo_obra, despesas = vgv * CUSTO, vgv * DESPESAS
    t = vgv * terreno / 100
    t_dinheiro = t * (1 - permuta / 100)
    vgv_disp = vgv - t * permuta / 100
    cred = custo_obra * credito / 100
    pl = vgv_disp * planta / 100
    entrega = vgv_disp - pl
    saldo, pior, mes = 0.0, 0.0, -1
    for m in range(MESES + 1):
        f = 0.0
        if m == 0:
            f -= t_dinheiro
        if 1 <= m <= OBRA:
            f += (cred + pl - custo_obra - despesas) / OBRA
        if m == OBRA + REPASSE:
            f += entrega - cred
        saldo += f
        if saldo < pior - 1:
            pior, mes = saldo, m
    return {"exposicao": -pior, "mes": mes, "resultado": saldo}


def moeda(v):
    mi = v / 1e6
    return "R$ " + (f"{mi:.1f}" if abs(mi) >= 10 else f"{mi:.2f}").replace(".", ",") + " mi"


def quadro():
    linhas = []
    resultados = [(a, calcular(**a[3])) for a in ARRANJOS]
    maior = max(r["exposicao"] for _, r in resultados)
    for (chave, nome, desc, _), r in resultados:
        largura = r["exposicao"] / maior * 100
        destaque = " destaque" if chave == "combinada" else ""
        linhas.append(f"""<div class="alternativa{destaque}">
  <p class="alt-nome">{nome}<small>{desc}</small></p>
  <div class="alt-barra" role="img" aria-label="{nome}: exposição máxima de {moeda(r['exposicao'])}, no mês {r['mes']}"><i style="width:{largura:.1f}%"></i></div>
  <p class="alt-numero">{moeda(r['exposicao'])}<small>pico no mês {r['mes']}</small></p>
</div>""")
    menor = min(r["exposicao"] for _, r in resultados)
    resultado = moeda(resultados[0][1]["resultado"])
    return f"""<div class="quadro surge">
  <div class="quadro-topo">
    <h3>Um empreendimento de exemplo, quatro estruturas de capital</h3>
    <p class="apoio">VGV de R$ 20 mi · terreno de 15% · obra de 24 meses · capital próprio exigido no pior mês</p>
  </div>
  {"".join(linhas)}
  <div class="quadro-pe"><p>O resultado ao fim do ciclo é o mesmo nos quatro ({resultado}), porque esta conta não cobra o custo de cada instrumento. O que muda é o capital que precisa estar disponível no caminho: de {moeda(maior)} para {moeda(menor)}. Números de exemplo, e não leitura de um projeto real.</p></div>
</div>"""


if __name__ == "__main__":
    for a in ARRANJOS:
        print(a[1], calcular(**a[3]))
