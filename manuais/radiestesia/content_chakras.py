# -*- coding: utf-8 -*-
from bookkit import *
from chakra_data import CHAKRAS, ESTADO_HIPOTESE

SETOR_DEST = lambda k: [
    ("Emocional", "<b>▶</b> " + go(f"ch{k}-emocoes", "Emoções do chakra")),
    ("Mental e psicológica", "<b>▶</b> " + go(f"ch{k}-crencas", "Crenças e feridas do chakra")),
    ("Física e de saúde", "<b>▶</b> " + go(f"ch{k}-corpo", "Corpo do chakra")),
    ("Energética (interferência)", "<b>▶</b> " + go("n4-interf", "Sub-biômetro de interferências")),
    ("Ambiental", "<b>▶</b> " + go("n4-ambiente", "Sub-biômetro de ambiente")),
    ("Transgeracional e ancestral", "<b>▶</b> " + go("n4-linhagem", "Sub-biômetro de linhagem")),
    ("Espiritual e existencial", "<b>▶</b> " + go("n4-espiritual", "Sub-biômetro espiritual")),
    ("Outro", "nomear a categoria; <b>▶</b> " + go("n4", "sub-biômetros gerais")),
]

def roteiro_comum():
    """Abertura da Parte IV: o procedimento que vale para os sete capítulos, escrito uma única vez."""
    H = []
    H.append(h1("ch-roteiro", "Roteiro comum aos sete chakras", "Parte IV · Capítulos por chakra", brk=False))
    H.append(p("Cada capítulo de chakra traz só o que é próprio daquele chakra: ficha, sinais, hipóteses de causa, emoções, crenças, corpo e recursos de harmonização. O procedimento é o mesmo para os sete e está escrito aqui uma vez. O biômetro de causas (G8) também é um só: fica nesta abertura e serve a todos os capítulos."))
    H.append(chart("G8"))
    H.append(p("Hipótese a confirmar primeiro no G8, conforme o estado do Nível 2: " + "; ".join(f"<b>{st}</b>: {d}" for st, d in ESTADO_HIPOTESE.items() if st not in ("equilibrado",)) + ". Vale para os sete capítulos."))
    H.append(h2("ch-roteiro-2", "Passo 2 · Biômetro de causas (G8)"))
    H.append(p("Antes do G8, o sinal mais ativo da lista de sinais do chakra orienta a confirmação do setor: sinais de corpo apontam o setor 3; de emoção, o 1; de crença e atitude, o 2; chips, implantes, magias e ataques, o 4."))
    H.append(steps([
        "Trio de permissão para " + pergunta("as causas do desequilíbrio do chakra [nome do chakra] de [nome completo]") + ".",
        pergunta("Há uma causa principal deste desequilíbrio que podemos identificar e tratar nesta sessão?") + " Se não: " + pergunta("Há uma causa que podemos identificar, mas não tratar hoje?") + " Se ainda não, " + '<span class="sym">✎</span>' + " registrar e <b>▶</b> " + go("n5-geral", "harmonização geral") + ".",
        "Testemunho no centro do G8: " + pergunta("Em qual setor está a causa principal?") + " " + '<span class="sym">✎</span>',
        "Contribuição, para os sete setores: " + pergunta("Qual o percentual de contribuição deste setor para o desequilíbrio, de 0 a 100?") + " no G2. Não precisam somar 100. Todo setor com 30% ou mais entra na fila, em ordem decrescente.",
        pergunta("Há outra categoria que precisa ser tratada antes desta?") + " Se sim, qual, e reordenar. Isso evita tratar a emoção enquanto uma interferência a realimenta. Chakra bloqueado ou parado: testar os setores 4 (energética) e 5 (ambiental) antes dos outros.",
        "Confirmação fechada do setor com a pergunta da tabela abaixo. Se der não, repetir o passo 3 uma vez; se der não de novo, registrar “sem setor” e <b>▶</b> " + go("n5-geral", "harmonização geral") + ".",
        "Abrir o sub-biômetro do setor principal (tabela de hipóteses do capítulo), harmonizar e reavaliar. Só se o chakra continuar fora da faixa volta-se ao G8 para o próximo setor da fila; quando entra na faixa, os setores restantes viram pendência registrada.",
        "Em todos os setores, antes de harmonizar: " + pergunta("O que sustenta esta causa?") + " (G58) e " + pergunta("Há um ganho em manter o problema?") + " (G62). O desdobramento completo de cada setor está nas " + go("n4-arvores", "árvores de desdobramento") + ".",
    ]))
    H.append(h2("ch-roteiro-3a", "Passo 3a · Emoções"))
    H.append(steps([
        pergunta("A emoção presa ligada ao chakra [nome] está neste gráfico?") + " no biômetro de emoções do capítulo. Se não, <b>▶</b> " + go("n4-emocoes", "G9, gráfico de 60 emoções") + ".",
        "Bissecção: " + pergunta("Está na metade esquerda do gráfico?") + ", depois no quarto, depois " + pergunta("É [emoção]?") + " para cada setor restante.",
        "Cadeia de decodificação (" + go("n4-cadeia", "origem, época, contexto, saber mais") + "): " + pergunta("Esta emoção é própria?") + " (senão: absorvida, herdada, compartilhada, pré-natal, pré-concepção), " + pergunta("Ficou presa antes dos 21 anos?") + " e bissecção pelas fases (G35), " + pergunta("Envolve uma pessoa ou evento específico?") + " (G36, G61). " + pergunta("Precisamos saber mais?") + " no máximo duas vezes.",
        pergunta("Podemos liberar esta emoção agora?") + " Sim: passo 4. Não: " + pergunta("Falta outra causa antes?") + " (voltar ao G8, fila) ou " + pergunta("Não é o momento?") + " (registrar pendência e seguir).",
        "Se nada testar sim nem no G9: considerar emoção herdada e ir uma única vez ao " + go("n4-linhagem", "sub-biômetro de linhagem") + "; se de novo nada testar sim, registrar “sem item” e voltar ao G8.",
        "Depois de cada liberação: " + pergunta("Há outra emoção presa ligada a este chakra que podemos liberar agora?") + " Quando der não: " + pergunta("Há um muro no coração?") + " O muro se libera emoção por emoção pelo mesmo caminho.",
    ]))
    H.append(h2("ch-roteiro-3b", "Passo 3b · Crenças e feridas"))
    H.append(steps([
        "Família de crença no G10: " + pergunta("Em qual família está a crença que sustenta este desequilíbrio?") + " " + '<span class="sym">✎</span>',
        "Ferida no G11: " + pergunta("Qual ferida de infância instalou esta crença?") + " A ferida diz com quem e em que idade (tabela na " + go("n4-crencas", "Parte V") + ").",
        "Frase exata: as frases típicas do capítulo e a lista G55; a pessoa pode dizer a sua. " + pergunta("Esta frase descreve a crença instalada em [nome]?") + " A frase que testa sim vai para a harmonização como afirmação invertida.",
        "Cadeia de decodificação, depois " + pergunta("Podemos tratar esta crença agora?") + " Sim: passo 4. Não: G8 (fila) ou pendência.",
    ]))
    H.append(h2("ch-roteiro-3c", "Passo 3c · Corpo"))
    H.append(p("O resultado é sempre hipótese energética, nunca diagnóstico. " + '<span class="sym">⚠</span>' + " Sinal de alarme ou sintoma persistente: encaminhar antes de continuar (" + go("encaminhar", "lista de sinais") + ")."))
    H.append(steps([
        "Órgão ou região no biômetro de corpo do capítulo: " + pergunta("Em qual órgão ou região está a causa física ligada a este chakra?") + " Se “Outro”, <b>▶</b> " + go("n4-corpo", "G12, G13 e G38") + ".",
        "Vitalidade do órgão no G3: abaixo de 6.500 confirma o alvo.",
        "Tipo e sub-tipo de desarmonia na lista G57 (patógeno, toxina, nutrição e hábitos, estrutura, circuito), por bissecção nos grupos.",
        "Opcional: conflito biológico no G27; esse setor devolve ao passo 3a ou 3b, porque o conflito é emocional.",
        "Ponte de Louise Hay quando há sintoma conhecido (tabela do capítulo), depois " + pergunta("Podemos harmonizar esta causa agora?") + " Sim: passo 4.",
    ]))
    H.append(h2("ch-roteiro-4", "Passo 4 · Harmonização"))
    H.append(p("Trio de permissão para harmonizar; técnica no G22 com eficácia no G2 (mínimo 70); dose no G23; aplicar até o sinal de término. Procedimento completo e fichas das técnicas: " + go("n5-proc", "Nível 5, procedimento") + "."))
    H.append(h2("ch-roteiro-5", "Passo 5 · Reavaliação"))
    H.append(steps([
        "Remedir o chakra: percentual (G2), giro, forma (G7), varredura dupla. " + '<span class="sym">✎</span>',
        "Remedir a carga da causa tratada: " + pergunta("Qual a carga de [causa] sobre o chakra agora, de 0 a 100?") + " Causa liberada testa até 10.",
        "Remedir vitalidade geral (G3) e proteção da aura (G2) para registrar se mudaram.",
    ]))
    H.append(p("O que fazer com cada resultado da remedida: " + goD(14, "cartão D14 · Remedida") + "."))
    H.append(end())
    return "".join(H)

def chapter(k):
    c = CHAKRAS[k]
    nome = f"Chakra {k} · {c['nome']} ({c['sanscrito']})"
    H = []
    H.append(h1(f"ch{k}", nome, "Parte IV · Capítulos por chakra", brk=False))
    H.append(p(f"Chakra {c['nome']} prioritário fora da faixa. Procedimento: " + go("ch-roteiro", "roteiro comum") + "; aqui, só o que é próprio deste chakra."))
    ficha = table(["Campo", "Conteúdo"], [
        ["Localização", c["local"]], ["Cor e complementar", f"{c['cor']}; complementar {c['complementar']}"], ["Elemento e mantra", f"{c['elemento']}; {c['mantra']}"],
        ["Glândula adotada", c["glandula"]], ["Órgãos e sistemas", c["orgaos"]],
        ["Função frente (sentir)", c["frente"]], ["Função costas (querer, agir)", c["costas"]],
        ["Demônio, direito e estágio (Judith)", f"{c['demonio']}; {c['direito']}; {c['estagio']}"],
        ["Sinais de deficiência", c["deficiencia"]], ["Sinais de excesso", c["excesso"]],
    ])
    causas = table(["Setor", "Neste chakra"], [
        ["1 Emocional", c["causas_legenda"][0] + "; traumas: " + c["traumas"]],
        ["2 Mental e psicológica", c["causas_legenda"][1] + "; medos: " + c["medos"] + "; feridas: " + c["feridas"]],
        ["3 Física e de saúde", c["causas_legenda"][2] + "; disfunções (Myss): " + c["disfuncoes"]],
        ["4 Energética", c["causas_legenda"][3] + "; típica: " + c["interf_tipica"]],
        ["5 Ambiental", c["causas_legenda"][4]],
        ["6 Transgeracional", c["causas_legenda"][5]],
        ["7 Espiritual", c["causas_legenda"][6] + "; contexto: " + c["contexto"]],
        ["8 Outro", "o que não cabe nos sete"],
    ])
    H.append(span(f'<table class="two"><tr><td>{h2(f"ch{k}-ficha", "Passo 1 · Ficha do chakra", toc=False)}{ficha}</td><td class="gap"></td><td>{h2(f"ch{k}-causas", "Passo 2 · Causas neste chakra (G8)", toc=False)}{causas}</td></tr></table>'))
    H.append(h2(f"ch{k}-sinais", "Passo 1b · Sinais do chakra (lista pendulável)", toc=False))
    H.append(chart(f"C{k}-sinais"))
    # EMOÇÕES | CORPO lado a lado (55/45); sob emoções: 3b (crenças); sob corpo: Hay e recursos (passo 4).
    # Se o par saltou de página deixando 45 mm ou mais livres (passagem anterior), 3b e Hay sobem para o texto antes do par.
    B3b = ('<div class="keep">' + h3("Passo 3b · Crenças e feridas do chakra", id_=f"ch{k}-crencas")
           + p(f"Feridas prováveis: {c['feridas']}. Frases típicas e a afirmação que as inverte:")
           + table(["Frases típicas do chakra " + c["nome"], "Afirmação modelo (testar até 80 ou mais)"], [[f"“{fr}”", f"“{af}”"] for fr, af in zip(c["crencas"], c["afirmacoes"] + c["afirmacoes"])]) + '</div>')
    HAY = table(["Problema (Hay)", "Causa provável"], [[a, b] for a, b in c["hay"]])
    REC = ('<div class="keep">' + h3("Passo 4 · Recursos de harmonização do chakra", id_=f"ch{k}-harm")
          + table(["Recurso", f"Para o chakra {c['nome']}"], [
            ["Cromoterapia", f"hipoativo: {c['cor']}; hiperativo: {c['complementar']}; bloqueado: complementar em movimento circular; 20 s por chakra (uso corrente)"],
            ["Cristais", c["cristais"]], ["Óleos essenciais", c["oleos"]], ["Frequência", c["hz"]],
            ["Etiqueta do Pêndulo Hebraico", c["etiqueta"]], ["Florais de partida", c["floral"]],
            ["Afirmações modelo", "; ".join(f"“{a}”" for a in c["afirmacoes"])], ["Prática corporal", c["pratica"]],
            ["Interferência típica", c["interf_tipica"]], ["Contexto típico", c["contexto"]],
          ]) + '</div>'
          + p("Depois: " + go("ch-roteiro-5", "reavaliação") + " e " + go("reav-outro", "outro chakra e há tempo?") + "."))
    subiu = (FALLBACK.get(f"C{k}-emocoes") or 0) >= 45
    if subiu:
        H.append(B3b.replace('<div class="keep">', "<div>", 1))
        H.append(h3("Passo 3c · Corpo: ponte de Louise Hay (tabela)") + HAY)
    H.append(h2(f"ch{k}-emocoes", "Passos 3a a 4 · Emoções, crenças, corpo e recursos do chakra", toc=False))
    H.append(p(f"Emoções do gráfico de 60 que mais aparecem neste chakra: {c['emocoes_txt']}. O último setor devolve ao G9. À direita, o corpo do chakra; o resultado é hipótese energética, nunca diagnóstico."))
    H.append(chart_group([f"C{k}-emocoes", f"C{k}-corpo"], widths=[0.55, 0.45],
                         extra={f"C{k}-emocoes": "" if subiu else B3b, f"C{k}-corpo": REC if subiu else HAY + REC},
                         pre={f"C{k}-corpo": f'<div class="cellhead" id="ch{k}-corpo">Passo 3c · Corpo do chakra</div>', f"C{k}-emocoes": '<div class="cellhead">Passo 3a · Emoções prováveis</div>'}))
    H.append(end())
    return "".join(H)

def build():
    return roteiro_comum() + "".join(chapter(k) for k in range(1, 8))
