# -*- coding: utf-8 -*-
from bookkit import *

def build():
    NGER = len(MANIFEST) - 21
    H = []
    # ---------------- CAPA ----------------
    H.append('<section class="cover"><img class="cover-bg" src="figs/capa_land.svg" alt=""/>'
             '<div class="cover-text"><div class="cover-kicker">Apostila de atendimento e autoatendimento</div>'
             '<h1 class="cover-title">Manual de<br/>Radiestesia<br/>Terapêutica</h1>'
             '<div class="cover-sub">Protocolo ramificado: triagem, chakras, causas e sub-causas, harmonização, limpeza de pessoas e de espaços, relações, decisões, prosperidade e reavaliação</div>'
             '<div class="cover-meta">Edição 16 · novembro de 2026 · ' + str(NGER) + ' biômetros gerais e 21 biômetros por chakra, coloridos, prontos para pendular</div></div>'
             '<div class="cover-foot"><span>Prática complementar de bem-estar. Não substitui avaliação médica ou psicológica e não altera tratamento prescrito.</span></div></section>')

    # ---------------- COMO USAR ----------------
    H.append(h1("como-usar", "Como usar este manual"))
    H.append(p("Este manual é um caminho com bifurcações. Cada etapa termina numa tabela de resultados, e cada resultado diz para onde ir, com o número da página. Você não lê o livro de ponta a ponta durante a sessão: abre no ponto em que está, mede, consulta o resultado e pula para a página indicada."))
    H.append(box("variacao", "Impresso uma vez, usado em todas as consultas", "O manual é fixo: nele não há campos para preencher, e nenhuma instrução pede para marcar o papel. Cada pergunta é dita em voz alta ou pensada; cada valor lido vai para o caderno de registro ou para as fichas do arquivo à parte, que se imprimem quantas vezes for preciso. O símbolo ✎ ao longo dos passos marca o momento de anotar no caderno. Os gráficos podem ser plastificados; para usá-los sobre a mesa, basta abrir o manual na página."))
    H.append(h3("Três ajudas para não se perder"))
    H.append(ul([
        "<b>Trilha no início de cada capítulo</b>: os gráficos daquele capítulo na ordem de uso, cada um com a página.",
        "<b>Rota em cada gráfico</b>: a linha “Etapa · Vem de” diz em que ponto da sessão ele entra e de onde se chega a ele; a coluna “O que fazer · vá para” traz, resultado por resultado, o próximo gráfico com a página (▶).",
        "<b>Mapa do método</b> (" + go("mapa", "a seguir") + "): o fluxo mestre, os cartões de bifurcação (“se der isto, vá para”) e a trilha de cada caminho. O " + go("glossario", "Glossário") + " define os termos usados.",
    ]))
    H.append(h3("Símbolos"))
    H.append(table(["Símbolo", "Significa"], [
        ['<span class="sym">▶</span> vá para (p. N)', "pule para a página indicada e continue de lá"],
        ['<span class="sym">✎</span> registre', "anote no caderno de registro (ou na ficha do arquivo à parte) antes de interpretar"],
        ['<span class="sym">⚠</span> encaminhe', "sinal de alarme: orientação médica ou psicológica antes de continuar"],
        ['<span class="sym">?</span> pergunta', "a frase exata a dizer em voz alta ou pensar antes de pegar o pêndulo; troque [nome] e [chakra] pelos da sessão"],
        ['<span class="sym">G</span> gráfico', "o biômetro a usar; os gráficos estão impressos à parte (quatro por folha) e aparecem aqui em tamanho reduzido, com a interpretação e a rota"],
    ]))
    H.append(h3("Regras que valem o tempo todo"))
    H.append(ul([
        "A pergunta é escrita antes de pegar o pêndulo e lida como está.",
        "Toda resposta só vale depois das permissões (posso, devo, estou pronto) e de uma verificação.",
        "Nunca pular a triagem nem a reavaliação. Sem medida inicial não há como saber se houve mudança.",
        "O pêndulo escolhe o setor e a técnica; o que o manual chama de “hipótese” é só o primeiro setor a confirmar.",
        "Nada aqui substitui médico ou psicólogo. Sintoma persistente, dor aguda, sinais de alarme e sofrimento intenso são encaminhados, e nenhum tratamento prescrito é interrompido por resultado de pêndulo.",
        "Só se mede alguém com consentimento; o resultado é apresentado como leitura energética, nunca como diagnóstico.",
    ]))
    H.append(box("nota", "Cortes que não estão em gráfico algum", "Ganho mínimo após uma harmonização: <b>15 pontos</b>. Setor de causa entra na fila com <b>30 %</b> ou mais de contribuição; campo com <b>30 %</b> ou mais é relevante. Tolerância entre duas varreduras: <b>5 pontos</b> (250 no Bovis). Limite da sessão: <b>3 chakras ou 90 minutos</b>. Os demais cortes (faixas do chakra, Bovis, aura, polaridade, eficácia, afirmação, remedida) estão nas linhas de resultado dos próprios gráficos."))
    H.append(box("variacao", "Três modos de uso", "<b>Presencial</b>: pêndulo sobre o corpo ou sobre os gráficos, pessoa ao lado. <b>À distância</b>: testemunho (nome e data de nascimento escritos, foto) no centro dos gráficos. <b>Autoatendimento</b>: testemunho próprio, perguntas na terceira pessoa e as adaptações da " + go("auto", "Parte X") + ". Onde um passo muda conforme o modo, há uma caixa como esta."))
    H.append(end())

    # ---------------- MAPA ----------------
    H.append(h1("mapa", "Mapa do método", brk=False))
    H.append(p("O fluxo abaixo é o esqueleto de toda sessão. Três decisões (limpar antes?, algum chakra abaixo de 70?, chakra em 70 ou mais na remedida?) e o retorno “há tempo para outro chakra?” são as únicas bifurcações do caminho principal; todas as outras ramificações estão nos cartões a seguir e dentro de cada gráfico."))
    import content_rotas
    H.append(content_rotas.mapa_topo([
        ["Abertura", go("p1-abertura", "Abertura passo a passo"), "G1"],
        ["Nível 1 · Triagem", go("n1", "Triagem geral"), "G2, G3, G4, G5, G6, G24"],
        ["Pré-ciclo", go("pre-ciclo", "Pré-ciclo de limpeza e proteção"), "G15, G28, G16, G25, G22, G23"],
        ["Nível 2 · Chakras", go("n2", "Leitura dos sete chakras"), "G2, G4, G5, G6, G7, G29"],
        ["Nível 3 e 4 · por chakra", go("ch-roteiro", "Roteiro comum e capítulos por chakra"), "G8, C1 a C7, G10, G11"],
        ["Nível 4 · listas completas", go("n4", "Sub-biômetros gerais"), "G9 a G21, G25, G27, G28, G55 a G62"],
        ["Nível 5 · Harmonização", go("n5", "Harmonização"), "G22, G23"],
        ["Limpeza de pessoas", go("limp", "Limpeza energética de pessoas"), "G63 a G68, G58, G59, G60"],
        ["Espaços e localização", go("esp", "Limpeza e localização em espaços"), "G66, G69 a G75, G82, G83, G25"],
        ["Perguntas da vida prática", go("dec", "Decisões, momento, alternativas, calendário"), "G84 a G88"],
        ["Relações entre pessoas", go("rel", "Relações"), "G89 a G91, G36"],
        ["Prosperidade, trabalho e empresa", go("pros", "Prosperidade e empresa"), "G92, G94, G95, G106 a G110"],
        ["Alimentos, remédios e doses", go("ali", "Alimentos e doses"), "G96 a G98, G104, G23"],
        ["Áreas da vida e pequenas aplicações", go("areas", "Áreas da vida"), "G24, G99 a G101, G103"],
        ["Reavaliação e fechamento", go("reav", "Reavaliação"), "os mesmos de antes"],
    ]))
    H.append(content_rotas.mapa_rotas())
    H.append(end())

    # ---------------- PARTE I ----------------
    H.append(h1("p1-material", "Material e convenções", "Parte I · Preparação", brk=False))
    H.append(h2("p1-material-lista", "O que ter à mão"))
    H.append(ul([
        "Pêndulo de uso exclusivo para medição (o de tratamento pode ser outro).",
        "Os gráficos impressos à parte (quatro por folha A4), numerados e guardados na ordem do índice; o manual mostra cada um em tamanho reduzido, com interpretação e rota.",
        "Caderno de registro (ou as fichas do arquivo à parte, impressas quantas vezes for preciso), lápis, papel branco novo para testemunhos. Neste manual não se escreve: ele é a caixa de ferramentas; o registro de cada atendimento vai para o caderno (" + go("fichas", "Parte XI") + ").",
        "Testemunho: nome completo e data de nascimento escritos a lápis, ou foto recente. Para lugar, a planta ou foto.",
        "Para autoatendimento: os cartões de setores (um cartão por setor de G8, G10, G11, G15, G22 e das linhas de G9), para sortear a ordem e reduzir a influência do desejo.",
        "Relógio ou cronômetro, água, e um lugar sem observadores.",
    ]))
    H.append(h2("p1-convencao", "Convenção de respostas"))
    H.append(p("A convenção é declarada uma vez, em voz alta, no início da sessão, e não muda no meio dela. Este manual adota a convenção da coluna “adotada”; se a sua for outra, anote-a na primeira página do caderno de registro e use o gráfico G1 para programar e conferir."))
    H.append(p("A quarta resposta é obrigatória. Sem ela, toda dúvida é forçada para sim ou não. Há três sentidos de “pêndulo parado” neste manual: resposta neutra (só depois de pergunta binária), “sem resposta” numa régua ou leque, e sinal de fadiga quando acontece em três perguntas seguidas, que encerra a sessão."))
    H.append(chart("G1", legend=[("Não posso ou não devo responder", "encerrar o assunto desta sessão; registrar"), ("Não", "seguir a tabela do passo em que está"), ("Neutro, nenhuma das anteriores", "reescrever a pergunta; se repetir, registrar “sem resposta”"), ("Sim", "seguir a tabela do passo em que está"), ("Pronto para a pergunta", "fazer a pergunta")]))
    H.append(end())

    H.append(h1("p1-abertura", "Abertura passo a passo", "Parte I · Preparação", brk=False))
    H.append(p("A abertura leva de cinco a dez minutos e não pode ser encurtada: é nela que a sessão ganha ou perde confiabilidade."))
    H.append(steps([
        "<b>Centrar.</b> Sentar, pés no chão, três respirações lentas. Estado “calmo, indiferente e passivo”, sem ideia preconcebida (Mermet). Sem observadores.",
        "<b>Queixa em uma frase.</b> " + '<span class="sym">✎</span> Escrever a queixa como a pessoa a disse. Em autoatendimento, escrever também o chakra e a causa que você suspeita, dobrar e guardar; só comparar no fechamento.',
        "<b>Testemunho.</b> Nome completo e data de nascimento a lápis em papel branco novo, ou foto. Colocar no centro do gráfico ou no canto esquerdo da régua; é o mesmo do início ao fim.",
        "<b>Calibração, três perguntas na mesma ordem.</b> " + pergunta("Hoje é [dia da semana correto]?") + " deve dar sim. " + pergunta("Meu nome é [nome errado]?") + " deve dar não. " + pergunta("A cor desta mesa é um número?") + " deve dar neutro. Uma falha: repetir uma vez. Duas falhas: encerrar e tentar em outro horário.",
        "<b>Autoauditoria.</b> " + pergunta("Qual o percentual de influência dos meus sentimentos ou do meu livre-arbítrio nas respostas desta sessão, de 0 a 100?") + " Ler no G2. " + '<span class="sym">✎</span> Registrar. Acima de 30, parar e recomeçar mais tarde.',
        "<b>Trio de permissão.</b> " + pergunta("Posso medir [nome completo] nesta sessão?") + " " + pergunta("Devo medir [nome completo] nesta sessão?") + " " + pergunta("Estou pronto para medir [nome completo] nesta sessão?") + " Um não encerra o assunto sem insistência (“tactful avoidance”, Woods). O trio se repete ao mudar de assunto: ao entrar nos chakras, ao abrir cada biômetro de causa e antes de cada harmonização.",
        "<b>Consentimento.</b> Com terceiros, consentimento verbal antes de pegar o pêndulo; para quem não pode responder por si, o de um responsável. " + '<span class="sym">✎</span> Marcar na ficha.',
    ]))
    H.append(box("variacao", "Variações", "<b>Presencial</b>: a pessoa deitada ou sentada ao lado; a calibração é feita antes de ela se deitar. <b>À distância</b>: tudo igual, com o testemunho; a pessoa não precisa estar presente, mas precisa ter consentido. <b>Autoatendimento</b>: perguntas na terceira pessoa (“Posso medir [seu nome]…”); sortear a ordem dos chakras antes de começar."))
    H.append(p("Abertura concluída: " + go("n1", "Nível 1, Triagem geral") + "."))
    H.append(end())

    H.append(h1("p1-conversa", "Conversar e avisar: a comunicação com a pessoa", "Parte I · Preparação", brk=False))
    H.append(p("Toda sessão começa e termina com conversa. A pessoa sabe o que vai ser medido e por quê, autoriza, e recebe o resultado como medida radiestésica, em linguagem simples. Os códigos das associações (ABRAD no Brasil, sociedades britânica e americana, cartas francesas e belgas) convergem em seis pontos: pedir consentimento explícito; explicar que a avaliação é energética, não diagnóstico; não prometer resultado; encaminhar a quem de direito; sigilo; não interferir em tratamento ou avaliação de outro profissional. As frases abaixo são a versão adotada por este manual."))
    H.append(h2("p1-conversa-abertura", "Antes de pegar o pêndulo"))
    H.append(box("variacao", "Fala de abertura (recomendação da casa)", "“O que eu faço é uma avaliação energética com pêndulo e gráficos. Não é diagnóstico e não substitui médico, psicólogo ou advogado. Vou medir tendências e indicar áreas; a decisão sobre o que fazer é sua. Se outra pessoa aparecer na leitura, ela entra só como parte da sua relação e com a sua autorização; eu não pendulo a vida dela. Tudo o que for lido fica em sigilo. Posso começar?”"))
    H.append(ul([
        "<b>O que vai ser medido.</b> Dizer a sequência da sessão em uma frase: linha de base, chakras, causa, harmonização, remedida. Se a pessoa pede só “uma limpeza” ou só “a casa”, dizer qual parte do manual será usada.",
        "<b>Consentimento.</b> Verbal, antes de pegar o pêndulo; para quem não responde por si, o do responsável. Para pendular um terceiro (parceiro, pai, filho, chefe), autorização explícita desse terceiro; sem ela, mede-se a relação do lado da pessoa (“o que esta relação pede de você”), o cômodo como lugar, nunca a outra pessoa. “Acho que ela deixaria” não é autorização.",
        "<b>Expectativa.</b> Nenhum resultado é prometido. A pessoa ouve que a resposta do pêndulo é hipótese a confirmar na remedida e, quando for o caso, com o profissional adequado.",
        "<b>Sinais de alarme.</b> Dor persistente, sintoma agudo, ideação suicida, doença grave sem acompanhamento: a conversa vira encaminhamento antes de qualquer medida (" + go("encaminhar", "quando encaminhar") + ").",
    ]))
    H.append(h2("p1-conversa-durante", "Durante a sessão"))
    H.append(ul([
        "Dizer em voz alta cada pergunta antes de medir; a pessoa acompanha e pode corrigir o nome, a data, o contexto.",
        "Ler o valor e dizê-lo sem adjetivo: “o cardíaco mediu 45; a faixa de equilíbrio começa em 70”. A interpretação vem só depois da sessão inteira.",
        "Quando a leitura aponta terceiros (G36, G82), nomear o vínculo, não a pessoa: “a relação com o pai pesa no setor transgeracional”, e não “seu pai é o problema”.",
        "Quando a pessoa discorda de uma leitura, registrar as duas versões e seguir; o pêndulo não decreta.",
    ]))
    H.append(h2("p1-conversa-devolutiva", "Devolutiva no fechamento"))
    H.append(table(["Dizer", "Não dizer"], [
        ["“O que medi foi…; o que fizemos foi…; o que mudou foi…” com os números de antes e depois", "“você tem [doença]”, “isso é [diagnóstico]”"],
        ["“A hipótese energética é…; vamos confirmar na remedida em 7 dias”", "“isso vai acontecer”, “garanto que vai dar certo”"],
        ["“Isto pede um profissional: procure…”", "“pare o remédio”, “não precisa de médico”, “faça a cirurgia em tal dia”"],
        ["“A relação com [vínculo] apareceu na leitura; o que você reconhece disso?”", "“seu marido está te traindo”, “sua mãe fez um trabalho”"],
        ["“Sugiro mais N sessões porque ficaram as pendências X e Y”", "“você precisa de mais sessões” sem dizer por quê"],
        ["“Isso fica entre nós; o registro é meu caderno”", "comentar o caso com terceiros; criticar outro terapeuta ou tratamento"],
    ]))
    H.append(p("O registro no caderno guarda o que o gráfico não guarda: data e hora, a pergunta exatamente como foi dita, o gráfico usado, a leitura inicial e final, o que foi dito à pessoa, o encaminhamento e o consentimento (com o nome do terceiro incluído, se houver). Os modelos de ficha brasileiros têm quase tudo isso, menos a pergunta exata e o consentimento para terceiro; os dois foram acrescentados às fichas deste manual."))
    H.append(end())

    H.append(h1("p1-leitura", "Como formular perguntas e ler os gráficos", "Parte I · Preparação", brk=False))
    H.append(h2("p1-perguntas", "Perguntas"))
    H.append(ul([
        "Binária: só admite sim ou não. Uma ideia por pergunta; assuntos amplos viram cadeias de perguntas curtas.",
        "Escrita antes, lida como está. Sem ambiguidade de tempo (“agora”, “hoje”), de sujeito (nome completo) e de escala (“de 0 a 100”).",
        "Sem carga emocional nem desejo de resultado. Concentrar-se na pergunta, não na resposta.",
        "A primeira resposta vale. Não se repete até sair o que se quer; repetir só após pausa, com a pergunta reescrita.",
        "Não perguntar o que já se sabe como “teste”: a resposta é sempre a esperada e não mede nada.",
    ]))
    H.append(h2("p1-leitura-graficos", "Leitura por tipo de gráfico"))
    H.append(table(["Gráfico", "Como ler", "Regra de descarte"], [
        ["Leque (setores)", "Pêndulo oscilando no ápice enquanto se lê a pergunta; a resposta é o setor em que a oscilação migra e se estabiliza. Mais de uma resposta possível: obter a primeira e perguntar “Há outro?” até sair não.", "Sem estabilizar em 20 segundos, registrar “sem resposta”. Nunca escolher o setor mais próximo."],
        ["Escala semicircular (G2, G3, G4)", "Partir do ponto neutro e deslocar o pêndulo ao longo da escala até o movimento mudar de oscilação para giro horário; esse é o valor. Repetir no sentido oposto.", "Aceitar só se as duas varreduras coincidirem em até 5 pontos (ou 250 no Bovis). Senão, registrar as duas e repetir após pausa."],
        ["Régua linear (G20b)", "Igual à escala, começando no meio; o valor é lido no ponto em que o movimento muda.", "Igual à escala."],
        ["Tabela ou grade (G9, G33, G38)", "Nunca varrer. Navegar por bissecção com sim ou não: coluna, metade das linhas, linha, célula, item.", "Dois itens da mesma célula com sim: “qual é o principal?”. Nenhum: voltar um nível."],
        ["Anéis (G17, G23)", "Um anel por vez, do externo ao interno, lido como leque.", "Igual ao leque."],
        ["Silhueta (G6, G13, G29)", "Percorrer devagar; a resposta é o ponto em que o pêndulo passa a girar; confirmar com pergunta sim ou não.", "Sem giro em toda a silhueta, registrar “sem resposta” e usar a lista escrita."],
    ]))
    H.append(h2("p1-controles", "Controles de confiabilidade"))
    H.append(p("A literatura científica atribui o movimento do pêndulo ao efeito ideomotor, e os testes controlados não mostraram acerto acima do acaso quando o operador não tinha acesso à resposta. Os próprios radiestesistas apontam “ideias preconcebidas e pensamento desejoso” como a principal causa de falha. Por isso toda resposta é tratada como hipótese, e os controles abaixo são parte do método, não enfeite."))
    H.append(table(["Controle", "Como", "Quando"], [
        ["Calibração", "as três perguntas da abertura", "toda sessão"],
        ["Varredura dupla", "ler a escala nos dois sentidos; aceitar só se coincidir", "toda medida numérica"],
        ["Remedida após pausa", "repetir a medida-chave (chakra prioritário) após 5 minutos", "toda sessão (Nível 2, passo 7)"],
        ["Registro", "pergunta, resposta e horário antes de interpretar", "toda pergunta"],
        ["Teste cego com terceiro", "envelopes opacos com “sim” ou “não”, ou três copos com um objeto sob um; medir sem ver; contar acertos contra o acaso", "semanal no treino, mensal depois"],
        ["Cego de testemunho", "terceiro coloca o testemunho de uma de duas pessoas em envelope; medir o chakra prioritário e conferir", "mensal, se atende terceiros"],
        ["Autoauditoria", "percentual de influência dos meus sentimentos", "início, meio e fim"],
    ]))
    H.append(h2("p1-parar", "Quando parar"))
    H.append(p("Mermet lista seis causas de erro: o pêndulo, o organismo do operador, o estado mental, o campo dos corpos próximos, a interpretação e os assistentes presentes. Encerrar ao notar fadiga, pêndulo que para em três perguntas seguidas (“fading”) ou respostas incoerentes; retomar em outro dia, nunca forçar."))
    H.append(end())


    # ---------------- PARTE II: NÍVEL 1 ----------------
    H.append(h1("n1", "Nível 1 · Triagem geral", "Parte II · Triagem", brk=False))
    H.append(p("A triagem produz a linha de base da sessão em cinco biômetros e decide se a sessão começa por limpeza ou vai direto aos chakras. Faça os cinco na ordem; todos são remedidos no fechamento, e a diferença entre antes e depois é o resultado registrado da sessão."))
    H.append(h2("n1a", "1A · Vitalidade (escala Bovis, G3)"))
    H.append(p("Sete medidas, sempre na mesma ordem, na régua de 0 a 10.000 com referência 6.500. Os números de Bovis são unidade convencional e só valem dentro da mesma régua: a leitura principal é comparar a pessoa com ela mesma, sessão a sessão. O único valor absoluto usado como gatilho é 4.500."))
    H.append(steps([
        pergunta("Qual a vitalidade geral de [nome completo] agora, em unidades Bovis?") + " Varredura dupla a partir de 6.500. " + '<span class="sym">✎</span>',
        "Repetir para: corpo físico, corpo etérico (vital), corpo emocional, corpo mental, corpo espiritual.",
        pergunta("Qual a vitalidade do ambiente onde [nome] dorme?") + " e " + pergunta("…onde trabalha?"),
    ]))
    H.append(h2("n1b", "1B · Campos (G2 e G5)"))
    H.append(p("Para cada um dos quatro campos, duas perguntas."))
    H.append(steps([
        pergunta("Qual o percentual de desequilíbrio do campo mental de [nome], de 0 a 100?") + " no G2. Repetir para emocional, espiritual e físico. " + '<span class="sym">✎</span>',
        "Para cada campo com 30% ou mais: " + pergunta("Esse desequilíbrio afeta qual chakra?") + " no G5; depois do primeiro, " + pergunta("Há outro?") + " até sair não.",
    ]))
    H.append(chart_group(["G3", "G2"]))
    B = []
    B.append(h2("n1c", "1C · Campo áurico (G2 e G6)"))
    B.append(steps([
        pergunta("Qual a proteção da aura de [nome], de 0 a 100?") + " no G2.",
        pergunta("Qual o tamanho da aura de [nome] em relação ao normal dela, de 0 a 100?") + " (50 é o normal da pessoa).",
        pergunta("Há rompimento ou vazamento na aura de [nome]?") + " Se sim, " + pergunta("Em qual região?") + " na silhueta G6; confirmar com sim ou não.",
    ]))
    B.append(table(["Resultado", "Caminho"], [
        ["Proteção abaixo de 40, ou rompimento presente", "marcar “pré-ciclo”"],
        ["Tamanho fora de 40 a 60", "só registro; comparar sessão a sessão"],
        ["Tudo na faixa", "seguir para 1D"],
    ]))
    H.append(chart("G5", beside="".join(B)))
    H.append(h2("n1d", "1D · Polaridade e interferência (G4)"))
    H.append(steps([
        pergunta("Qual o equilíbrio yin e yang de [nome] agora, de −100 (yin) a +100 (yang)?") + " no G4. Faixa −20 a +20.",
        pergunta("Há interferência energética ativa que impede uma leitura confiável de [nome] agora?") + " sim ou não.",
    ]))
    H.append(h2("n1e", "1E · Áreas da vida (G24)"))
    H.append(p("Oito áreas no leque G24. Não é diagnóstico, é correlação: a área que pede atenção é confrontada com o chakra e a categoria de causa encontrados depois, e a sessão só fecha quando essa correlação faz sentido para a pessoa. Na triagem bastam duas perguntas; a leitura completa, com a Roda da Vida que a própria pessoa preenche, está na " + go("areas", "Parte XVI") + "."))
    H.append(p(pergunta("Qual área da vida de [nome] pede atenção primeiro hoje?") + " no G24; depois " + pergunta("Qual o grau de equilíbrio dessa área, de 0 a 100?") + " no G2. Repetir para uma segunda área, se houver."))
    H.append(chart_group(["G4", "G24"]))
    H.append(h2("n1-decisao", "Decisão ao fim da triagem"))
    H.append(p("Com os cinco resultados em mãos: " + goD(4, "cartão D4 · Fim da triagem") + "."))
    H.append(end())

    # ---------------- PRÉ-CICLO ----------------
    H.append(h1("pre-ciclo", "Pré-ciclo de limpeza e proteção", "Parte II · Triagem", brk=False))
    H.append(p("O pré-ciclo existe para que a leitura dos chakras não seja feita sobre um campo sem vitalidade, desprotegido ou com interferência ativa. É curto: harmonização geral, remedida, e volta ao caminho."))
    H.append(p("Os três pré-ciclos abaixo são a versão curta. Quando a carga passa de 30, quando há mais de dois itens a remover ou quando a pessoa pede uma limpeza, use a sessão completa da " + go("limp", "Parte VII, limpeza de pessoas") + "; para o pré-ciclo de ambiente, a " + go("esp", "Parte VIII, espaços") + " traz o roteiro inteiro do imóvel."))
    H.append(h2("pre-ciclo-geral", "Pré-ciclo por vitalidade ou aura"))
    H.append(steps([
        "Trio de permissão para " + pergunta("limpar e proteger o campo de [nome]") + ".",
        "Harmonização geral: " + go("n5-geral", "procedimento da harmonização geral") + " (técnicas 1, 3, 4 ou 11 no G22; dose no G23).",
        "Remedir 1A (vitalidade geral), 1C (proteção) e 1D (interferência). " + '<span class="sym">✎</span>',
        "Vitalidade acima de 4.500 e proteção acima de 40: <b>▶</b> " + go("n2", "Nível 2") + ". Senão, repetir uma vez; depois de duas tentativas, seguir ao Nível 2 registrando o que ficou.",
    ]))
    H.append(h2("pre-ciclo-interf", "Pré-ciclo por interferência ativa"))
    H.append(steps([
        "Abrir o G15 com a pergunta " + pergunta("Qual interferência está ativa sobre [nome] agora?") + " e, se houver mais de uma, " + pergunta("Há outra?") + ".",
        "Carga: " + pergunta("Qual a carga desta interferência sobre [nome], de 0 a 100?") + " no G2 (no pré-ciclo a carga é “sobre [nome]”, não sobre um chakra).",
        "Origem no G28: " + pergunta("Esta interferência é própria, externa ou herdada?") + "; se externa, de pessoa, lugar ou objeto.",
        pergunta("Esta interferência pode ser removida ou neutralizada agora?") + " Se não: " + pergunta("Precisa de proteção antes?") + " e aplicar a técnica 1 ou 3 do Nível 5.",
        "Limpar pela técnica 1 (comando), 3 (Pêndulo Hebraico) ou 4 (gráfico Desimpregnador): " + go("n5-geral", "harmonização geral") + ".",
        "Remedir a carga (meta: até 10) e 1A, 1C, 1D. <b>▶</b> " + go("n2", "Nível 2") + ".",
    ]))
    H.append(chart_group(["G15", "G28"]))
    H.append(h2("pre-ciclo-ambiente", "Pré-ciclo de ambiente"))
    H.append(steps([
        "Fonte no G16: " + pergunta("Qual a fonte principal que pesa sobre o ambiente onde [nome] dorme (ou trabalha)?") + " Depois " + pergunta("Há outra?") + ".",
        "Cômodo e posição no G25; sobre a planta do imóvel, o pêndulo marca o ponto.",
        "Remediação na lista G71, na ordem que as fontes sugerem: mudar a cama ou a mesa de lugar; neutralizar por comando ou gráfico; dispositivo; e, com evidência independente, medir radônio e reduzir exposição eletromagnética no quarto.",
        "A remediação vira orientação de fechamento. " + '<span class="sym">✎</span>' + " Geopatia é registrada como “a confirmar” até concordância de dois operadores ou repetição às cegas com a planta virada.",
        "Harmonização geral e <b>▶</b> " + go("n2", "Nível 2") + " na mesma sessão.",
    ]))
    H.append(chart_group(["G16", "G25"]))
    H.append(end())

    # ---------------- PARTE III: NÍVEL 2 ----------------
    H.append(h1("n2", "Nível 2 · Leitura dos sete chakras", "Parte III · Chakras", brk=False))
    H.append(p("Cada chakra é medido no mesmo biômetro com quatro parâmetros: percentual de funcionamento (G2), sentido do giro, amplitude (G4) e forma do movimento (G7). A faixa de equilíbrio adotada é de 70 a 100%; é convenção deste manual, não dado de literatura, e por isso fica fixa."))
    H.append(box("variacao", "Três modos de medir", "<b>Sobre o corpo</b> (Brennan): pessoa deitada, pêndulo a 2 ou 3 cm da pele sobre cada chakra, mente quieta; lê-se sentido, diâmetro e forma; frente e, para 2 a 6, também as costas. <b>Sobre o gráfico com testemunho</b>: pergunta dita por chakra; é o modo padrão deste manual e o único possível à distância. <b>Híbrido</b>: silhueta G6 com réguas, para registrar os sete numa folha."))
    H.append(h2("n2-leitura", "Passo a passo"))
    B = []
    B.append(p("Antes: trio de permissão para " + pergunta("os chakras de [nome completo]") + ". Em autoatendimento, sortear a ordem dos sete."))
    B.append(steps([
        "<b>Percentual.</b> " + pergunta("Qual o percentual de funcionamento do chakra [nome do chakra] de [nome completo] agora, de 0 a 100?") + " no G2, varredura dupla. " + '<span class="sym">✎</span>' + " Repetir para os sete.",
        "<b>Giro.</b> " + pergunta("O chakra [nome] gira em sentido horário?") + " A resposta “não” significa chakra fechado ou invertido.",
        "<b>Amplitude.</b> " + pergunta("Qual a amplitude do chakra [nome] em relação ao normal desta pessoa, de −100 a +100?") + " no G4. Abaixo de −30: hipoativo; acima de +30: hiperativo. Sobre o corpo, é o diâmetro do giro comparado ao dos chakras já medidos.",
        "<b>Forma</b>, só para os fora da faixa ou com giro anti-horário: " + pergunta("Qual a forma do movimento do chakra [nome]?") + " no G7.",
        "<b>Posterior</b>, para os chakras 2 a 6 fora da faixa: " + pergunta("O aspecto posterior do chakra [nome] está dentro da faixa?") + " Posterior fora da faixa com frente na faixa entra no ciclo como chakra fora da faixa, com o setor 2 (vontade, controle) como hipótese a confirmar primeiro.",
        "<b>Prioridade.</b> Testemunho no G5: " + pergunta("Qual chakra deve ser tratado primeiro nesta sessão?") + " O prioritário nem sempre é o de menor percentual; a mesma pergunta define o próximo depois de cada chakra tratado.",
        "<b>Remedida após pausa.</b> Cinco minutos de pausa; remedir o percentual do prioritário. Diferença de até 5 pontos confirma; acima, registrar as duas, repetir uma vez e seguir com a última.",
        "<b>Meta.</b> " + pergunta("Qual o percentual ideal do chakra [nome] para hoje?") + " Sem resposta clara, a meta é 70. " + '<span class="sym">✎</span>',
    ]))
    H.append(chart("G7", beside="".join(B)))
    H.append(chart_group(["G6", "G6b", "G29"], mode="stacked", caps={"G6b": "Silhueta das costas: aspectos posteriores 2B a 6B (querer e agir)"}, extra={"G29": h3("Chakras secundários (G29)", id_="n2-secundarios") + p("Medidos só quando a queixa aponta para eles ou quando o principal ligado a eles está fora da faixa: mãos (cura e transmissão), pés (aterramento e descarga), joelhos (flexibilidade), timo (imunidade energética; ponte entre coração e garganta) e baço (vitalidade e sistema imune). O critério de faixa é o mesmo, e um secundário fora da faixa entra no ciclo junto com o principal ligado a ele: mãos e timo com o cardíaco (" + go("ch4", "capítulo 4") + "), pés e joelhos com o básico (" + go("ch1", "capítulo 1") + "), baço com o plexo solar (" + go("ch3", "capítulo 3") + ").")}))
    H.append(h2("n2-estados", "Estados e para onde ir"))
    H.append(p("Cada combinação produz um estado. O estado dá a hipótese a confirmar primeiro no Nível 3, onde a escolha final é sempre do pêndulo. Quando dois estados coexistem, vale a precedência: invertido, depois bloqueado, depois hiperativo, depois hipoativo, depois a forma. A direita e a esquerda são sempre as da pessoa medida."))
    H.append(table(["Estado", "Critério", "Significado (fonte)", "Hipótese a confirmar primeiro"], [
        ["Equilibrado", "70 a 100, horário, amplitude −30 a +30, círculo", "chakra psicodinamicamente aberto (Brennan)", "não entra no ciclo"],
        ["Hipoativo", "40 a 69, ou amplitude abaixo de −30", "deficiência: contração e evitação na área (Judith)", "setor 1, depois 3"],
        ["Bloqueado", "abaixo de 40, ou parado", "sem fluxo mensurável", "setor 4, depois 1"],
        ["Hiperativo", "amplitude acima de +30", "excesso: compensação e fixação (Judith)", "setor 2"],
        ["Invertido", "giro anti-horário", "fechado; crença negativa domina a área (Brennan)", "setor 2"],
        ["Caótico", "errático, mudança de eixo", "em transformação (Brennan)", "não tratar; remedir em 7 dias"],
    ]))
    H.append(h2("n2-decisao", "Decisão: algum chakra fora da faixa?"))
    H.append(p("Prioritário fora da faixa: " + goD(5, "cartão D5 · Algum chakra fora da faixa?") + "."))
    H.append(end())
    return "".join(H)
