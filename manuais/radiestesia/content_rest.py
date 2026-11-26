# -*- coding: utf-8 -*-
from bookkit import *
from bookkit import ROUTES, short_title
from chakra_data import CHAKRAS
import content_limpeza, content_aplicacoes

EMO60 = [
    ("Coração ou intestino delgado", "abandono · traição · desamparo · perda · amor não recebido", "esforço não reconhecido · desgosto · insegurança · alegria excessiva · vulnerabilidade"),
    ("Baço ou estômago", "ansiedade · desespero · repulsa · nervosismo · preocupação", "fracasso · impotência · desesperança · falta de controle · baixa autoestima"),
    ("Pulmão ou cólon", "choro · desânimo · rejeição · tristeza · pesar", "confusão · atitude defensiva · luto · autoagressão · teimosia"),
    ("Fígado ou vesícula", "raiva · amargura · culpa · ódio · ressentimento", "depressão · frustração · indecisão · pânico · sentir-se usado"),
    ("Rins ou bexiga", "culpar · pavor · medo · horror · irritação", "conflito · insegurança criativa · terror · falta de apoio · vacilação"),
    ("Glândulas e órgãos sexuais", "humilhação · ciúme · anseio · luxúria · sobrecarga", "orgulho · vergonha · choque · indignidade · sentir-se sem valor"),
]
PSICO = ["Agressividade", "Angústia", "Apatia", "Ansiedade", "Baixa autoestima", "Autoobsessão", "Autopiedade", "Cansaço mental", "Ceticismo", "Ciúmes", "Criticismo", "Culpas", "Decepções", "Depressão", "Desapontamento", "Descrença", "Dominação", "Egoísmo", "Extroversão", "Fixação", "Frustração", "Histeria", "Hostilidades", "Infelicidade", "Insegurança", "Intolerância", "Introversão", "Inveja", "Irritabilidade, mau humor", "Medos", "Melancolia, nostalgia", "Ódio", "Orgulho, preconceitos", "Passividade", "Preguiça física", "Preguiça mental", "Preocupação", "Presunção", "Rancor", "Solidão", "Tendência a suicídio", "Traição", "Timidez", "Tristeza", "Traumas", "TDAH", "TOC", "Burnout", "Síndrome do pânico", "Vítima de abuso ou assédio sexual", "Vítima de violência doméstica ou urbana", "Conflito de gênero ou sexualidade", "Conflito com família ou filhos", "Conflito de relacionamento", "Maternidade ou paternidade", "Mudança de cidade", "Mudança de emprego", "Desemprego", "Dívidas elevadas", "Doença terminal na família", "Luto"]
ORGAOS = ["Baço", "Bexiga", "Cérebro", "Cólon", "Coração", "Costelas", "Dentes", "Duodeno", "Coluna vertebral", "Esôfago", "Faringe", "Fígado", "Glândulas mamárias", "Glândulas salivares", "Intestino delgado", "Intestino grosso", "Laringe", "Língua", "Meninges", "Nariz", "Olhos", "Ouvidos", "Ovários", "Pâncreas", "Paratireoide", "Pele", "Trompas", "Útero", "Vértebras", "Vesícula biliar", "Próstata", "Testículos", "Pulmões", "Rins", "Tireoide", "Memória"]
HORMONIOS = [("Hipotálamo", "PIF, CRH, TRH, GnRH, GHRH, ocitocina, vasopressina (ADH)"), ("Hipófise", "ACTH, GH, FSH, LH, TSH, prolactina"), ("Pineal", "melatonina"), ("Tireoide", "calcitonina, tiroxina (T4), tri-iodotironina (T3)"), ("Paratireoide", "paratormônio"), ("Suprarrenais", "aldosterona, cortisol; adrenalina, noradrenalina"), ("Pâncreas", "insulina, glucagon"), ("Testículos", "testosterona"), ("Ovários", "estrógeno, progesterona")]
HAY = [("Coração, problemas", "problemas emocionais sérios longamente suportados; falta de prazer; rejeição da vida"), ("Estômago", "medo do novo; incapacidade de assimilar"), ("Úlcera", "medo; convicção de não ser bom o bastante"), ("Garganta", "raiva engolida; criatividade sufocada"), ("Costas, superior", "falta de apoio emocional; reter o amor"), ("Costas, média", "culpa; preso ao passado"), ("Costas, inferior", "medo ligado a dinheiro; falta de apoio"), ("Dor de cabeça", "autocrítica; medo"), ("Enxaqueca", "aversão a ser pressionado; resistir ao fluxo"), ("Fígado", "depósito de raiva; queixas crônicas"), ("Rins", "crítica; decepção; fracasso; vergonha"), ("Pulmões", "medo de absorver a vida; tristeza"), ("Asma", "amor sufocante; choro reprimido"), ("Tireoide", "humilhação; vontade de desistir; hiper: raiva por ser deixado de lado"), ("Pressão alta", "problema emocional antigo não resolvido"), ("Pressão baixa", "falta de amor na infância; derrotismo"), ("Pele", "ansiedade; medo; mágoas antigas"), ("Alergias", "negar o próprio poder; a quem é alérgico?"), ("Artrite", "crítica; ressentimento; sentir-se não amado"), ("Prisão de ventre", "recusa em liberar velhas ideias"), ("Insônia", "medo; desconfiança no processo da vida; culpa"), ("Fadiga", "resistência; tédio; falta de amor pelo que se faz"), ("Obesidade", "necessidade de proteção; medo; raiva encoberta"), ("Depressão", "raiva sem direito de ser sentida; desesperança")]

def grid(items, cols, id_, title):
    rows = []
    for i in range(0, len(items), cols):
        chunk = items[i:i+cols]
        rows.append([f"<b>{i+j+1}</b> {e(x)}" for j, x in enumerate(chunk)] + [""] * (cols - len(chunk)))
    tbl = "<table class='grid big'><tbody>" + "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows) + "</tbody></table>"
    return f'<figure class="chart full" id="fig-{id_}"><div class="chart-head"><span class="chart-id">{e(id_)}</span><span class="chart-title">{e(title)}</span></div>{tbl}<div class="chart-note">Leitura por bissecção: “está na metade de cima?”, “na coluna da esquerda?”, depois linha, depois célula. Nunca varrer.</div></figure>'

def build():
    H = []
    # ================= PARTE V =================
    H.append(h1("n4", "Nível 4 · Sub-biômetros gerais", "Parte V · Listas completas", brk=False))
    H.append(p("Os capítulos por chakra trazem listas curtas. Quando o pêndulo responde “Outro”, quando nada da lista curta testa sim, ou quando a categoria é energética, ambiental, transgeracional ou espiritual, a sessão vem para cá. As listas desta parte são, na maior parte, as da prancha “Avaliação Radiestesia” das formações brasileiras (agentes nocivos, causas físicas, psicológicas e espirituais, fases da vida, pessoas, sistemas, órgãos, glândulas), reorganizadas por biômetro."))
    H.append(p("Quando a sessão não parte de um chakra (queixa de vida, autoatendimento rápido), o biômetro de causas " + go("fig-G8", "G8") + " é usado diretamente; os destinos são os da " + go("n4-arvores", "árvore de desdobramento") + "."))
    H.append(h2("n4-cadeia", "Cadeia de decodificação (origem, época, contexto)"))
    H.append(p("É a estrutura do Emotion Code (“precisamos decodificar mais?”) generalizada para qualquer causa. Depois do item, sempre estes passos, nesta ordem."))
    H.append(chart_group(["G19", "G35"]))
    H.append(chart_group(["G20b", "G21"]))
    H.append(chart("G36"))


    H.append(h2("n4-arvores", "Árvores de desdobramento: da categoria ao item e ao que o sustenta"))
    H.append(p("Cada setor do biômetro de causas abre em três ou quatro níveis. A tabela mostra o caminho completo de cada categoria; os capítulos por chakra entram no nível 2 já com listas curtas, e vêm para cá quando precisam da lista completa. Em todas as categorias, depois do item, duas perguntas fecham o desdobramento: " + pergunta("O que sustenta esta causa?") + " (G58) e " + pergunta("Há um ganho em manter o problema?") + " (G62). Sem esses dois, a causa liberada tende a voltar."))
    H.append(p("Perguntas-ponte, usadas em qualquer categoria quando a resposta do nível 2 for “Outro” ou quando nada testar sim: " + pergunta("A causa está em outra categoria?") + " (volta ao G8), " + pergunta("A causa está em outro chakra?") + " (volta ao G5) e " + pergunta("A causa não pode ser nomeada hoje?") + " (registrar e harmonização geral)."))
    H.append(chart_group(["G58", "G62"]))
    H.append(chart("G61"))

    H.append(h2("n4-emocoes", "Emoções: gráfico de 60 (G9)"))
    H.append(p("Quando a lista curta do chakra não resolve, o G9 traz as sessenta emoções do Emotion Code."))
    H.append(chart("G9"))
    H.append(p("Se nenhuma emoção testar sim: considerar herdada e ir uma única vez ao " + go("n4-linhagem", "sub-biômetro de linhagem") + ". Depois de cada liberação: " + pergunta("Há outra emoção presa ligada a este chakra?") + " e, quando não, " + pergunta("Há um muro no coração?") + "."))

    H.append(h2("n4-crencas", "Crenças, feridas e repertório psicológico"))
    H.append(p("Sequência: família de crença (G10), ferida de infância (G11), frase exata (G55) e, se for preciso saber o nível, o barômetro (G56). A ferida diz com quem e em que idade a crença se instalou."))
    H.append(table(["Ferida", "Máscara", "Com quem", "Idade (a conferir)", "Maior medo", "Traço na sessão"], [
        ["Rejeição", "fugitivo", "progenitor do mesmo sexo", "concepção a 1 ano", "pânico", "solitário, sente-se sem valor, foge"],
        ["Abandono", "dependente", "progenitor do sexo oposto", "1 a 3 anos", "solidão", "vínculos excessivos, medo de ficar só"],
        ["Humilhação", "masoquista", "quem cuida, em geral a mãe", "1 a 3 anos", "liberdade", "nega as próprias necessidades, vergonha"],
        ["Traição", "controlador", "progenitor do sexo oposto", "2 a 4 anos", "separação", "mostra domínio, supervisiona tudo"],
        ["Injustiça", "rígido", "progenitor do mesmo sexo", "4 a 6 anos", "frieza", "perfeccionista, “não tenho problemas”"],
    ]))
    H.append(chart_group(["G10", "G11"]))

    H.append(chart("G55"))

    H.append(chart("G56"))
    H.append(chart("G33"))

    H.append(h2("n4-corpo", "Corpo: sistemas, órgãos, glândulas, tipo de desarmonia"))
    H.append(p('<span class="sym">⚠</span> Tudo aqui é hipótese energética. Sinal de alarme ou sintoma persistente: ' + go("encaminhar", "encaminhar") + " antes de continuar."))
    H.append(steps([
        "Estado geral, só quando a queixa é de doença instalada: G30. " + pergunta("Qual o estado energético de saúde de [nome]?"),
        "Sistema: G12. " + pergunta("Em qual sistema está a causa física?"),
        "Órgão: G13 (silhueta) ou G38 (lista). Bovis do órgão no G3; abaixo de 6.500 confirma.",
        "Glândula, se o sistema for endócrino ou a queixa hormonal: G39; hormônio em carência ou excesso na tabela abaixo, como no roteiro de glândulas das formações.",
        "Tipo e sub-tipo de desarmonia na lista G57, por bissecção nos grupos; causa física de referência no G32 quando o grupo for nutrição e hábitos.",
        "Conflito biológico (opcional): G27; devolve à emoção ou crença.",
        "Ponte de Louise Hay quando há sintoma conhecido; depois " + pergunta("Podemos harmonizar esta causa agora?") + ".",
    ]))
    H.append(chart_group(["G30", "G12"]))
    H.append(chart("G13", beside=list_block("G38", cols=3, narrow=True), frac=0.24))
    H.append(chart_group(["G39", "G32"]))
    H.append(table(["Glândula", "Hormônios (roteiro de glândulas)"], [[a, b] for a, b in HORMONIOS]))

    H.append(chart("G57"))
    H.append(chart("G27", legend=[("“Bocado” (endoderma)", "não conseguir pegar, engolir, digerir ou eliminar algo; susto de morte"), ("Ataque ou ninho (mesoderma antigo)", "ataque à integridade, sujidade; preocupação com o ninho"), ("Desvalorização (mesoderma novo)", "“não sou capaz”, “não valho”; ossos, músculos, tendões"), ("Separação, território, identidade (ectoderma)", "contato perdido, perda ou raiva de território, frustração")]))
    H.append(table(["Problema (Louise Hay)", "Causa provável"], [[a, b] for a, b in HAY]))

    H.append(h2("n4-interf", "Interferências energéticas"))
    H.append(p("Interferência confirmada no G8 (setor 4) ou no pré-ciclo. Sequência: item (G15), carga (G2), origem (G28), onde está (G60), o que a sustenta (G58, G59) e a remoção na Parte VII."))
    H.append(steps([
        "Item no G15 (" + go("fig-G15", "gráfico") + "): " + pergunta("Qual interferência está sobre o chakra [nome]?") + " e " + pergunta("Há outra?") + ".",
        "Carga: " + pergunta("Qual a carga desta interferência sobre o chakra, de 0 a 100?") + " na régua G2 (no pré-ciclo, “sobre [nome]”). A escala de −100 a +100 de Raymon Grace fica só para o comando de neutralização.",
        "Origem no G28 (" + go("fig-G28", "gráfico") + "): própria, externa (pessoa, lugar, objeto) ou herdada.",
        "Onde está alojada: G60. " + pergunta("Em qual corpo sutil está alojada esta interferência?") + " e, se for um chakra, qual (G5). A localização define por onde a limpeza começa (" + go("limp", "limpeza de pessoa") + ").",
        "O que a sustenta: G58 (" + go("fig-G58", "gráfico") + "). " + pergunta("O que sustenta esta interferência?") + " Se for voto, pacto ou contrato, nomear no G59 e escolher a ação da lista CQM antes de remover.",
        "Detalhe espiritual, se o item for obsessor, entidade, ataque ou vampirismo: G34; se for implante, cordão ou ser: G50 e G51.",
        pergunta("Esta interferência pode ser removida ou neutralizada agora?") + " Se não: " + pergunta("Precisa de proteção antes?") + " Técnicas 1, 3 e 4 da " + go("n5-tecnicas", "Parte VI") + "; remedir a carga (meta: até 10).",
    ]))
    H.append(chart_group(["G34", "G60"]))

    H.append(chart("G59"))

    H.append(h2("n4-ambiente", "Ambiente"))
    H.append(p("Sequência: fonte (G16), cômodo e posição (G25), remediação (G71). As dimensões das redes variam entre fontes (Hartmann a cada 2,5 m ou 3 a 4 m; Curry em diagonal com faixas de 40 a 50 cm; Benker a cada 10 m); o pior caso é um cruzamento sob a cama ou o posto de trabalho."))
    H.append(steps([
        "Fonte no G16; cômodo e posição no G25 sobre a planta do imóvel, com o pêndulo marcando o ponto.",
        "Remediação na lista G71, na ordem: mudar a cama ou a mesa de lugar; neutralizar por comando ou gráfico (SCAP e Desimpregnador); dispositivo; medir radônio e reduzir exposição eletromagnética no quarto, que têm evidência independente.",
        "Verificação: concordância entre dois operadores ou repetição às cegas com a planta virada; até lá, registrar “a confirmar”.",
        "A remediação vira orientação de fechamento; o chakra é remedido na sessão seguinte.",
    ]))

    H.append(h2("n4-linhagem", "Linhagem (transgeracional e ancestral)"))
    B = []
    B.append(p("Um anel por vez, de fora para dentro, no G17; depois a emoção herdada no G9 e a liberação em toda a linhagem."))
    B.append(steps([
        pergunta("A causa foi herdada da linhagem materna, paterna ou de ambas?") + " (anel interno).",
        pergunta("De quantas gerações atrás?") + " pais, avós, bisavós, quatro ou mais.",
        pergunta("Por qual mecanismo?") + " e " + pergunta("Qual o tema?") + ".",
        "Emoção herdada: voltar ao G9 ou ao gráfico de emoções do chakra, uma única vez; a liberação é feita “em toda a linhagem” (no Emotion Code, 10 passadas em vez de 3).",
        "Se nada testar sim: registrar “sem item” e voltar ao biômetro de causas do chakra, próximo setor.",
    ]))
    H.append(chart("G17", beside="".join(B)))

    H.append(h2("n4-mannah", "Influências e seres (biômetros de referência)"))
    H.append(p("Dois leques da Mesa de Autodiagnóstico de referência, usados quando o G15 responde entidade, implante, cordão ou ser: influência de energia (G50) e seres negativos (G51). A escala de Hawkins (G54) mede o estado emocional no início e no fim da sessão."))
    H.append(chart_group(["G50", "G51"]))
    B = []
    B.append(h2("n4-espiritual", "Espiritual e existencial"))
    B.append(p("Tema no G18 e, se a resposta for obsessão, ataque ou proteção, o G34. " + pergunta("A causa está nesta vida?") + " O conteúdo de vidas passadas e karma entra só se operador e pessoa compartilham essa crença, e fica registrado como tal."))
    H.append(chart("G54", beside="".join(B)))
    H.append(chart("G18"))
    H.append(end())

    # ================= PARTE VI =================
    H.append(h1("n5", "Nível 5 · Harmonização", "Parte VI · Técnicas", brk=False))
    H.append(p("O pêndulo escolhe a técnica (G22), depois a dose (G23), e a sessão só avança quando a aplicação testa como concluída. A regra de ouro das mesas e dos gráficos: o pêndulo escolhe a ferramenta e a ordem, não o operador."))
    H.append(h2("n5-proc", "Procedimento"))
    H.append(steps([
        "Trio de permissão para " + pergunta("harmonizar [causa] no chakra [nome] de [nome completo]") + ".",
        "Testemunho no G22: " + pergunta("Qual técnica harmoniza esta causa neste chakra agora?"),
        "Eficácia no G2: " + pergunta("Qual o percentual de eficácia desta técnica para esta causa, de 0 a 100?") + " Abaixo de 70, próxima técnica; se nenhuma chegar a 70, a de maior percentual, registrando. Este teste é prática de consultório, convenção deste manual.",
        "Dose no G23: " + pergunta("Por quantos minutos?") + " (ou horas, dias, semanas), " + pergunta("Quantas aplicações?") + ", " + pergunta("Com que intervalo?") + ". Convenções do relógio radiestésico: linha 0 a 100 é percentual; 0 a 60 segundos, doses ou minutos; 0 a 24 horas; 0 a 12 meses; 0 a 10 dias.",
        "Aplicar até o sinal de término: o pêndulo deixa de girar e passa a oscilar, ou o tempo testado expira.",
        pergunta("A aplicação está concluída?") + " Não: " + pergunta("Precisa de mais tempo?") + " (uma nova dose) ou " + pergunta("Outra técnica em sequência?") + "; dois “não” levam à reavaliação com o que houver.",
    ]))
    H.append(chart_group(["G22", "G23"]))

    H.append(h2("n5-tecnicas", "Fichas das doze técnicas"))
    TEC = [
        ("Comando de neutralização (Raymon Grace)", "energética, emocional, ambiental; pré-ciclo", ["Medir o nível de −100 a +100 no G4.", "Pêndulo em giro anti-horário com o comando em voz alta: “Neutralize e embaralhe a frequência de [causa] em [nome], agora.” Deixar girar até parar.", "Pêndulo em giro horário: “Preencha [nome] com [qualidade: paz, vitalidade, proteção] a 100%.” Até parar.", "Remedir no G4. Comando alternativo das mesas radiônicas: “Harmoniza, equilibra, alinha” três vezes sobre o chakra."], "até o pêndulo parar; mover o corpo depois (caminhar, alongar) para integrar", "imediata, no G4; chakra no G2"),
        ("Liberação pelo Vaso Governador (Emotion Code)", "emoção presa, herdada, muro do coração", ["Com a emoção, origem e época identificadas, declarar: “Libero [emoção] de [época/origem] de [nome], agora.”", "Passar ímã ou a mão do ponto entre as sobrancelhas, por cima da cabeça, até a nuca: 3 passadas; 10 se herdada (libera em toda a linhagem).", "Retestar: " + pergunta("[Emoção] foi liberada?") + " Se não, repetir uma vez.", "Depois: " + pergunta("Há outra emoção presa que podemos liberar agora?")], "3 ou 10 passadas; sessão termina quando o subconsciente responde que não é hora de liberar mais", "carga da emoção (meta até 10); chakra no G2"),
        ("Pêndulo Hebraico", "interferências, chakras, cordões, miasmas, selamento", ["Limpar o pêndulo (água, sal ou luz) e abrir o espaço com proteção.", "Etiqueta de limpeza; irradiar sobre o chakra (pessoa deitada ou testemunho) até o pêndulo parar.", "Etiqueta específica escolhida na lista fechada do operador (Ahava, Shalom, Refuah, Tlishut, Lajatz, Mem Hei Shin…); irradiar até parar.", "Releitura do giro sobre o chakra; selamento com etiqueta de fechamento (Tav por 33 segundos no Método Tikun; Keter, Luz, Amor em outras escolas); limpar o pêndulo."], "até parar por etiqueta; conjuntos variam de 5 a mais de 400 etiquetas conforme a escola", "giro sobre o chakra; chakra no G2"),
        ("Gráfico radiônico de tratamento", "qualquer categoria; padrão das escolas brasileiras", ["Testemunho a lápis em papel branco novo, com o objetivo escrito.", "Desimpregnador 30 minutos; Decágono duplo 30 minutos (potencializar).", "Gráfico escolhido na " + go("n5-graficos", "mesa seletora") + " com o pêndulo; orientar ao norte quando o gráfico pede; remédio radiônico (cor, pedra, floral) sobre o testemunho se indicado.", "Tempo no relógio G23; decreto de ativação com giro horário; verificar conexão (sim ou não).", "Confirmar término antes de retirar: " + pergunta("O gráfico já atuou 100%?") + " Regra das pranchas montadas: deixar 72 horas, remedir; se não chegou à meta, refazer, no máximo três ciclos; depois, esperar 30 dias."], "Desimpregnador 30 min; gráficos de dias (ex.: Harmonia 16 dias, Alta Vitalidade 10 dias em laudo real); 72 h para pranchas", "chakra no G2 após retirar; remedida de 7 dias"),
        ("Cromoterapia", "chakra hipo, hiper ou bloqueado", ["Hipoativo: cor própria do chakra. Hiperativo: cor complementar. Bloqueado: complementar em movimento circular.", "Com pêndulo de cor ou luz: 20 segundos por chakra (uso corrente); lâmpada: 3 minutos, 3 vezes ao dia; cores quentes 3 a 10 minutos e frias 10 a 30 minutos nas apostilas de cromoterapia.", "Água solarizada: 1 a 2 horas de sol entre 8h e 11h, preparada no dia.", "Testar a cor com o pêndulo quando houver dúvida entre a própria e a complementar."], "20 s por chakra; lâmpada 3 min × 3; água 1 a 2 h", "chakra no G2; giro"),
        ("Cristal", "chakra hipo, proteção, aterramento", ["Escolher na tabela de consulta rápida ou perguntar pedra a pedra: " + pergunta("Este cristal harmoniza este chakra desta pessoa?"), "Limpar (água corrente 30 s a 1 min; selenita, turmalina bruta e pirita não vão à água; sal grosso 24 h), energizar (sol da manhã até 9h; ametista e quartzo rosa na lua), programar (declarar a intenção testada, visualizar realizada).", "Aplicar sobre o chakra pelo tempo testado no G23, ou carregar; limpar a cada uso.", "Comando das mesas radiônicas: “Eu sou ativar a energia deste cristal no chakra [nome], harmonizando e realinhando” quatro vezes."], "tempo testado; limpar a cada uso", "chakra no G2"),
        ("Floral de Bach", "emocional, mental", ["Pêndulo sobre o gráfico das 38 essências em 7 grupos (medo; incerteza; desinteresse pelo presente; solidão; hipersensibilidade; desânimo e desespero; preocupação excessiva com os outros).", "Selecionar até 6 essências; Rescue (Rock Rose, Impatiens, Cherry Plum, Star of Bethlehem, Clematis) em emergência.", "Dose de referência: 4 gotas, 4 vezes ao dia (dose comercial do Rescue, por analogia); dias no G23.", "O Bach Centre pede que seus praticantes registrados evitem técnicas de seleção que confundam o cliente; informar que a seleção foi radiestésica."], "4 gotas × 4 ao dia; dias testados", "chakra no G2 na remedida de 7 dias"),
        ("Afirmação ou novo padrão", "crença, padrão mental", ["Escrever três frases na primeira pessoa, positivas, no presente.", "Testar cada uma: " + pergunta("Quanto esta frase está alinhada para [nome], de 0 a 100?") + " Ficar com a mais alta desde que chegue a 80; abaixo, reescrever.", "Repetir em voz alta, de manhã e à noite, por 21 a 30 dias (Hay sugere um mês); anotar na ficha de remedida.", "Opcional: Ho’oponopono sobre a memória (“Sinto muito, me perdoe, eu te amo, sou grato”) e EFT com a frase de preparação."], "21 a 30 dias", "frase retestada e chakra no G2 em 7 dias"),
        ("Som e frequência", "chakra, espiritual", ["Frequência do chakra: 396, 417, 528, 639, 741, 852, 963 Hz (origem numerológica, uso corrente); ou mantra bija LAM, VAM, RAM, YAM, HAM, OM.", "Minutos testados no G23; ouvir ou entoar com atenção no chakra.", "Fechamento das mesas radiônicas: “Harmoniza, equilibra, alinha” três vezes com o mantra do chakra."], "minutos testados", "chakra no G2"),
        ("Aromaterapia", "emocional, sacral, cardíaco", ["Óleo por chakra da tabela de consulta rápida; as tabelas divergem, o pêndulo escolhe entre dois.", "Inalação ou diluído; gotas e dias no G23."], "gotas e dias testados", "chakra no G2 em 7 dias"),
        ("Reiki ou imposição de mãos", "física, cardíaco, aura", ["Símbolo testado: Cho Ku Rei (físico, proteção), Sei He Ki (emocional), Hon Sha Ze Sho Nen (à distância).", "Minutos testados no G23; sobre o chakra ou o testemunho."], "minutos testados", "chakra no G2; aura 1C"),
        ("Prática corporal", "básico, plexo, integração; sempre como orientação diária", ["Da tabela de Judith por chakra: aterramento e exercício (1), movimento e prazer saudável (2), exercício vigoroso ou relaxamento (3), respiração e braços (4), cantar e entoar (5), visualização (6), meditação (7).", "Diária, por 7 dias, até a remedida; anotar cumprimento na ficha."], "diária por 7 dias", "chakra no G2 em 7 dias"),
    ]
    TEC_CHART = {3: "G44", 5: "G42", 6: "G46", 7: "G45", 9: "G43", 10: "G47"}
    H.append(span(table(["Nº", "Técnica", "Quando o pêndulo costuma escolher", "Dose de referência", "O que remedir", "Biômetro"],
        [[str(i), e(nome), quando, dose, remed, (go("fig-" + TEC_CHART[i], TEC_CHART[i]) if i in TEC_CHART else "G22, G23")] for i, (nome, quando, como, dose, remed) in enumerate(TEC, 1)], cls="small")))
    for i, (nome, quando, como, dose, remed) in enumerate(TEC, 1):
        H.append(f'<div class="tec" id="n5-tec-{i}"><h3>Técnica {i} · {e(nome)}</h3>')
        H.append(steps(como))
        H.append("</div>")
    H.append(h2("n5-biometros", "Biômetros das técnicas"))
    H.append(p("Seis biômetros de apoio às técnicas: o pêndulo escolhe o item; nas listas, a linha; nos leques, o setor."))
    H.append(chart_group(["G42", "G43"]))
    H.append(chart("G44"))
    H.append(chart("G45"))
    H.append(list_pair("G46", "G47"))

    H.append(h2("n5-geral", "Harmonização geral (pré-ciclo e fechamento)"))
    H.append(steps([
        "Testemunho no centro; trio de permissão para " + pergunta("limpar e proteger o campo de [nome]") + ".",
        "Escolha no G22 restrita às técnicas 1, 3, 4 e 11, que não exigem causa; dose no G23.",
        "Aplicar até o sinal de término. No pré-ciclo, remedir 1A (vitalidade) e 1C (proteção): seguir ao Nível 2 quando a vitalidade passa de 4.500 e a proteção de 40, ou após duas tentativas, registrando o que ficou.",
        "No fechamento, a técnica padrão é a de proteção e selamento (comando, gráfico de proteção da mesa seletora, ou etiqueta de fechamento), sem remedida adicional. Depois, limpeza do operador e do instrumento com Desimpregnador e SCAP, como no Manual Técnico de Sintonização e Limpeza do Operador.",
    ]))
    H.append(h2("n5-graficos", "Seletor de gráficos radiônicos "))
    H.append(p("Dois biômetros para escolher o gráfico radiônico: a categoria pelos grupos da lista pendulável G41 e depois o gráfico, linha a linha (ou direto na lista, por bissecção). O tempo vem do G23. Gráficos de detecção (psicométrico de La Foye) nunca são usados para emitir."))
    H.append(chart("G41"))
    H.append(h3("Recursos por chakra", id_="n5-tabela") + p("Cor, cristais, óleos, frequência, etiqueta e floral de cada chakra estão no Passo 4 do capítulo do chakra (" + go("ch1-harm", "chakra 1") + " a " + go("ch7-harm", "chakra 7") + ")."))
    H.append(h2("n5-sub", "Sub-protocolos por objetivo (modelos de referência)"))
    H.append(ul([
        "<b>Kit Saúde (técnica Aselma)</b>: testemunho a lápis com frase afirmativa; sequência Desimpregnador, Luxor, Harmonizador, Turbilhão de Vênus, Labirinto d’Amiens, Antidor, Vesica Piscis, Cho Ku Rei, Turbilhão de Marte, Trígono; no dia seguinte perguntar se concluiu; se não, tempo no relógio.",
        "<b>Modelo liberar, regenerar, harmonizar</b> (protocolo Sinusite de referência): três fases com dias testados (3 a 5 dias de liberação, 7 a 21 de regeneração) e reavaliação ao fim de cada fase.",
        "<b>Vidas passadas, quando a crença permite</b>: quantas vidas, século, memória a liberar, país, relação das pessoas, gráfico de tratamento, tempo; ativar diariamente com “Ajusta, harmoniza e equilibra” três vezes.",
        "<b>Prancha Saúde e Proteção</b> (Diana Raquel): 15 passos, 72 horas montada, remedir, no máximo três ciclos, intervalo de 30 dias.",
    ]))
    H.append(end())

    # ================= PARTE VII =================
    H.extend(content_limpeza.part_limpeza())
    H.extend(content_limpeza.part_espacos())
    H.append(h1("reav", "Reavaliação, fechamento e remedida", "Parte IX · Reavaliação", brk=False))
    H.append(p("A reavaliação do chakra está no passo 5 de cada capítulo de chakra. Esta parte reúne o que vem depois: a decisão de continuar, o fechamento, a remedida de sete dias e os sinais que encaminham."))
    H.append(h2("reav-outro", "Decisão: outro chakra e há tempo?"))
    H.append(table(["Situação", "Caminho"], [
        ["Há outro chakra fora da faixa e a sessão tem menos de 90 minutos e menos de 3 chakras tratados", "Perguntar " + pergunta("Qual chakra deve ser tratado agora?") + " no G5 e <b>▶</b> o capítulo dele (" + go("n2-decisao", "tabela de capítulos") + ")"],
        ["Há outro chakra fora da faixa, mas o limite foi atingido, ou " + pergunta("Há mais alguma coisa a tratar hoje em [nome]?") + " deu não", "registrar pendência; <b>▶</b> " + go("fechamento", "Fechamento")],
        ["Fadiga, pêndulo parado em três perguntas, respostas incoerentes", "<b>▶</b> " + go("fechamento", "Fechamento") + " mesmo com pendência"],
        ["Nenhum chakra fora da faixa", "<b>▶</b> " + go("fechamento", "Fechamento")],
    ]))
    H.append(h2("fechamento", "Fechamento, em seis passos"))
    H.append(steps([
        "Remedir toda a triagem (1A a 1E) e registrar ao lado dos valores iniciais. " + '<span class="sym">✎</span>',
        "Conferência etapa a etapa, em voz baixa, como na verificação ritual apométrica: permissões pedidas, chakras medidos, causas tratadas, aplicações concluídas, nada aberto. Se algo ficou incompleto, voltar a ele antes de fechar.",
        "Harmonização geral de proteção e selamento, sempre (" + go("n5-geral", "procedimento") + ").",
        "Desconexão: declarar encerrada a sessão, retirar o testemunho, limpar pêndulo e gráficos; limpeza do operador (Desimpregnador, SCAP, água corrente), como no Manual Técnico de Sintonização e Limpeza do Operador.",
        "Orientações à pessoa: água, mover o corpo para integrar, a prática diária escolhida, a remediação de ambiente se houver, e a data da remedida.",
        "Registro completo e pergunta de retorno: " + pergunta("Em quantos dias remedir?") + " (padrão 7; mesas falam de 1 a 3 semanas para efeito pleno; apometria, 21 a 30 dias). Autoauditoria final. " + '<span class="sym">✎</span>',
    ]))
    H.append(h2("remedida7", "Remedida de sete dias"))
    H.append(p("Repetir 1A, 1C e o chakra tratado, na mesma convenção. Se o chakra voltou a sair da faixa, a causa tratada era secundária ou há uma causa de manutenção (ambiente, relação, hábito): " + pergunta("O que está realimentando este desequilíbrio?") + " no biômetro de causas do chakra, começando pelos setores 5 e 6. Três remedidas seguidas na faixa encerram o caso para aquele chakra."))
    H.append(h2("encaminhar", "Quando encaminhar, sem esperar a remedida"))
    H.append(p('<span class="sym">⚠</span> Esta lista é regra de boa prática, não veio de fonte radiestésica: dor no peito ou falta de ar; sangramento; febre alta persistente; perda de peso sem explicação; sintoma neurológico súbito; ideação suicida ou sofrimento psíquico intenso; qualquer sintoma físico com mais de duas semanas sem avaliação médica. O encaminhamento é registrado e a radiestesia segue como complemento, nunca como motivo para alterar tratamento prescrito. No Brasil, apresentar leitura radiestésica como diagnóstico foi tratado como exercício irregular da medicina; por isso a ficha usa sempre “hipótese energética”.'))
    H.append(end())

    # ================= PARTE VIII =================
    H.append(h1("auto", "Autoatendimento", "Parte X · Medir a si mesmo", brk=False))
    H.append(p("Medir a si mesmo é o caso mais exposto ao efeito ideomotor: o operador conhece a queixa, tem hipóteses e deseja o resultado. As adaptações reduzem o viés sem mudar nenhum nível. A regra geral é separar, no tempo e no papel, o que você pensa do que o pêndulo responde."))
    H.append(table(["Ponto do protocolo", "Adaptação", "Por quê"], [
        ["Testemunho", "nome completo e data escritos, ou foto; perguntas na terceira pessoa", "afasta a pergunta do “eu” que já tem opinião"],
        ["Antes de pegar o pêndulo", "escrever queixa, chakra suspeito e causa suspeita; dobrar; comparar só no fechamento", "mostra quando o pêndulo só confirmou a expectativa"],
        ["Ordem dos chakras", "sortear com sete cartões", "quebra a antecipação"],
        ["Régua e escala", "ler com os olhos fechados até o movimento mudar; abrir os olhos só para ler", "reduz a influência do número esperado"],
        ["Biômetro de causas e sub-biômetros", "cartões idênticos por setor, embaralhados e virados; “qual cartão?”; virar depois", "único modo de cegar a escolha"],
        ["Resultado conveniente", "quando sair exatamente o esperado, remedir em outro horário antes de tratar", "coincidência com a expectativa pede confirmação"],
        ["Autoauditoria", "início, meio e fim; acima de 30, parar", "freio principal em si mesmo"],
        ["Causas mentais", "responder por escrito às feridas e famílias; depois medir; registrar discrepâncias", "dupla via, como no método Tempo Divino"],
        ["Teste cego mensal", "dez envelopes com sim ou não preparados por outra pessoa; contar contra 50%", "único controle que mede alguma coisa"],
    ]))
    H.append(p("Harmonização em si mesmo: todas as doze técnicas funcionam. As passadas do Emotion Code são feitas com a própria mão, da testa por cima da cabeça até a nuca; o comando é dito em voz alta com o pêndulo sobre o testemunho; o Pêndulo Hebraico é feito deitado, com o braço apoiado."))
    H.append(p("Quando não se medir: doente, exausto, com sono ou emocionalmente abalado; depois de duas falhas de calibração no mesmo dia; nas 24 horas seguintes a uma sessão completa. O Manual Técnico de Sintonização e Limpeza do Operador diz o mesmo: não operar deprimido, doente ou estressado."))
    H.append(table(["Frequência", "Duração", "O que fazer"], [
        ["Diária", "5 min", "prática do Nível 5 e remedida rápida do chakra em tratamento, numa linha"],
        ["Semanal", "30 min", "calibração, 1A (duas primeiras linhas), 1C, sete chakras em percentual e giro; se algo sair da faixa, ciclo completo para um chakra"],
        ["Mensal", "90 min", "sessão completa com até três chakras; teste cego de dez envelopes"],
        ["Trimestral", "20 min", "reler as fichas: chakra que mais saiu, categoria mais frequente, técnica com melhor ganho médio; se o mesmo chakra sai toda semana com a mesma categoria, a causa de manutenção está fora da sessão (setor 5 ou 6)"],
    ]))
    H.append(end())

    # ================= PARTE IX =================
    H.append(h1("fichas", "Registro no caderno", "Parte XI · Registro", brk=False))
    H.append(p("Tudo o que a sessão produz vai para o caderno ou para as Fichas de Registro do arquivo à parte (atendimento, remedida, laudo, limpeza, ambiente, Roda da Vida, diário de decisões, matriz empresarial, planta na grade), impressas quantas vezes for preciso. Na ficha de atendimento ficam: identificação e queixa, triagem (Bovis, campos, aura, polaridade, área), chakras com percentual, giro e forma, causa principal e cadeia, técnica e dose, remedida, autoauditoria e pendências. O laudo para a pessoa é o resumo em linguagem simples: o que foi medido, o que mudou, o que fazer até o retorno; nunca diagnóstico."))
    H.append(end())

    H.extend(content_aplicacoes.parts())

    # ================= APÊNDICES =================
    import content_rotas; H.append(content_rotas.teorias_cap())

    return "".join(H)
