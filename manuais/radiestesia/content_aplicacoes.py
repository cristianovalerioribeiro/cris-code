# -*- coding: utf-8 -*-
from bookkit import *

def part_decisao():
    H = []
    H.append(h1("dec", "Perguntas da vida prática: decisões, momento, alternativas e calendário", "Parte XII · Vida prática", brk=False))
    H.append(p("Esta parte responde ao pedido mais comum fora da saúde: “devo ou não devo?”, “agora ou depois?”, “qual das opções?”, “em que dia?”. Os gráficos de decisão difundidos têm quatro respostas (sim, não, talvez, refazer a pergunta); este manual acrescenta uma quinta, “não me cabe responder”, como saída ética para perguntas sobre terceiros, saúde, dinheiro de outros ou futuro. A base de regras vem de José Medeiros (O Livro do Pêndulo), que organiza um kit de decisão inteiro: controle de sensibilidade antes de perguntar, duas ou três formulações que precisam convergir, percentagem, calendário e lista de causas de erro."))
    H.append(box("variacao", "O pêndulo indica tendência; a decisão é da pessoa", "Nenhuma resposta desta parte decide por alguém. O que o gráfico devolve é uma indicação para a conversa. Vetos repetidos pelas escolas: nunca usar o pêndulo para interromper um tratamento, para decisões legais ou financeiras drásticas, nem para responder sobre a vida de quem não pediu."))
    H.append(h2("dec-regras", "Regras do operador"))
    H.append(ul([
        "<b>Controle de sensibilidade antes de perguntar</b> (Medeiros): três perguntas de resposta conhecida; se acertar menos de metade, não perguntar nada importante naquele dia. Em números: autoauditoria do G2 acima de 70.",
        "<b>Uma pergunta, uma vez, por sessão.</b> Não repetir em loop até obter a resposta desejada; a repetição é a causa de erro mais citada.",
        "<b>Só decisões importantes.</b> O pêndulo não é consultado para trivialidades; o hábito corrói a sensibilidade.",
        "<b>Duas ou três formulações convergentes.</b> A mesma questão dita de dois ou três modos diferentes (“é favorável aceitar?”, “é melhor recusar?”, “aceitar traz mais bem do que recusar?”). Só vale se as respostas convergirem; se divergirem, a resposta é “refazer a pergunta” e a questão fica para outro dia.",
        "<b>Aqui e agora.</b> As respostas valem para o momento da pergunta (Mutarelli); uma decisão para daqui a meses é remedida perto da data.",
        "<b>Controle cego quando a carga emocional é alta.</b> Opções escritas em cartões iguais, virados e embaralhados; o pêndulo escolhe o cartão; só depois se vira. No treino, dez cartões “sim” e dez “não” para medir a própria taxa de acerto.",
        "<b>Registro e revisão.</b> Pergunta exata, resposta e data no caderno; semanas depois, o que de fato aconteceu. O diário de acertos é o único termômetro honesto da própria sensibilidade.",
        "<b>Causas de erro.</b> Quando uma resposta não faz sentido, antes de repetir: lista G88 (" + pergunta("Qual a causa do erro?") + ").",
    ]))
    H.append(h2("dec-roteiro", "Roteiro"))
    H.append(steps([
        "Pergunta escrita no caderno, com sujeito, verbo e tempo (“aceitar a proposta X neste mês é favorável para mim?”). Trio de permissão para " + pergunta("esta decisão de [nome]") + ".",
        "G84: " + pergunta("[pergunta]") + ". Sim ou não vão ao passo 4. “Ainda não” abre o G85. “Refazer a pergunta” pede nova redação e uma única nova tentativa. “Não me cabe responder” encerra o assunto nesta sessão, registrado.",
        "Momento, no G85: " + pergunta("Quando é o momento para [ação]?") + ". Se a resposta for “depois de resolver outra coisa”, " + pergunta("O quê?") + " abre o G8 (categoria de causa) ou o G24 (área da vida). Dia, semana, mês ou hora no G87, só quando a data importa.",
        "Grau: " + pergunta("Quanto esta decisão é favorável para [nome], de 0 a 100?") + " no G2. Abaixo de 40 é desfavorável; de 40 a 69 é incerta e pede mais informação fora do pêndulo; acima de 70, favorável. Iniciantes esperam valores acima de 60 só em decisões simples.",
        "Confirmação por formulação diferente (regra das duas ou três). Divergência: registrar e devolver como “sem resposta hoje”.",
        "Devolutiva: o valor e a tendência, nunca a ordem. “O pêndulo indica tendência favorável; a decisão é sua.”",
    ]))
    H.append(chart_group(["G84", "G85"]))
    H.append(h2("dec-alternativas", "Alternativas: A, B, C"))
    H.append(p("Não há gráfico padrão para comparar opções; o procedimento é o das escolas espanholas e inglesas: as opções escritas antes, uma pergunta de sim ou não para cada uma, depois o percentual de cada uma no mesmo biômetro, depois registro e revisão. O G86 serve de leque quando a pessoa prefere ver as opções lado a lado."))
    H.append(steps([
        "Escrever as opções (até quatro) no caderno; a mesma letra no G86.",
        pergunta("A opção A é favorável para [nome] hoje?") + " para cada opção, sim ou não.",
        "Para as favoráveis: " + pergunta("Qual o grau de favorabilidade da opção A, de 0 a 100?") + " no G2. Diferença menor que 10 pontos entre duas opções é empate: a decisão volta para a pessoa com os critérios dela.",
        "G86: " + pergunta("Qual opção o pêndulo indica?") + " só como confirmação; “nenhuma delas” e “outra, ainda não vista” são respostas válidas e frequentes.",
        "Com carga emocional alta: cartões virados.",
    ]))
    H.append(h2("dec-calendario", "Calendário: dia, mês, semana e hora"))
    H.append(p("O G87 é o relógio radiestésico de datas: anel externo com os dias do mês, depois os meses, os dias da semana e as horas. Lê-se um anel por vez, como escala. Medeiros acrescenta duas chaves tradicionais, dadas aqui como convenção e não como regra: no quarto crescente da Lua, ações para aumentar; no minguante, para reduzir; e os dias da semana regidos por planetas, de domingo a sábado: Sol (meditação e proteção), Lua (imaginação e criatividade), Marte (ação), Mercúrio (gestão), Júpiter (concretização), Vênus (emoção), Saturno (administração e conhecimento). “Melhor data” para eventos por pêndulo não tem método publicado; o que se mede é o momento da pessoa, não a sorte do dia."))
    H.append(steps([
        pergunta("Em que mês é o momento para [ação]?") + " (anel dos meses) → " + pergunta("Em que dia?") + " (anel dos dias) → " + pergunta("Em que dia da semana?") + " só como confirmação → " + pergunta("Em que hora?") + " quando fizer diferença.",
        "Datas no futuro distante são remedidas quando se aproximam.",
    ]))
    H.append(chart_group(["G86", "G87"]))
    H.append(chart("G88"))
    H.append(end())
    return H

def part_relacoes():
    H = []
    H.append(h1("rel", "Relações entre pessoas", "Parte XIII · Relações", brk=False))
    H.append(p("Três camadas que as escolas misturam e que este manual separa: medir (biômetro de sintonia e de níveis da relação), emitir (gráficos de harmonização, como Harmonia, Harmonia Familiar, Desembaraçador de Relacionamento e Turbilhão com Vênus) e orientar (a conversa sobre o que a relação pede). Só a primeira cabe num atendimento sem conflito ético; a segunda exige consentimento dos dois; a terceira é aconselhamento, e o terapeuta diz “não sou terapeuta de casal”."))
    H.append(box("variacao", "A regra do terceiro", "A outra pessoa entra só como parte da relação de quem está sendo atendido. Pergunta aceitável: “qual o percentual de sintonia entre A e B hoje?”. Pergunta inaceitável: “B está mentindo?”, “B ama outra pessoa?”. Para pendular a outra pessoa como pessoa (chakras, causas, limpeza), é preciso a autorização explícita dela; “acho que ela deixaria” não é autorização. Gráficos emissores para “trazer de volta”, “amarrar” ou “reaproximar” sem consentimento das duas partes não entram neste manual."))
    H.append(h2("rel-roteiro", "Roteiro"))
    H.append(steps([
        "Nomear a relação: quem é B (G36 para o vínculo; nome completo no caderno, nunca no gráfico sem consentimento) e trio de permissão para " + pergunta("a relação de [nome] com [vínculo]") + ".",
        "Sintonia geral: " + pergunta("Qual o percentual de sintonia entre [nome] e [vínculo] hoje, de 0 a 100?") + " no G2. Não há limiar publicado; registre e compare entre sessões.",
        "Níveis no G89, um por vez: físico e atração, emocional, mental e comunicação, energético, espiritual e valores, confiança, apoio e amizade; percentual de cada um no G2. O nível mais baixo é o tema da conversa.",
        "Padrão repetido: " + pergunta("Há um padrão que se repete nas relações de [nome]?") + " Se sim, G61 (evento) e G10 (crença), e o capítulo do chakra cardíaco ou sacral conforme o G5.",
        "Cordão: " + pergunta("Há cordão desequilibrado nesta relação?") + " e " + pergunta("De quem para quem?") + " → " + go("limp-cordoes", "corte de cordões") + ", só com o consentimento da pessoa atendida e sem mexer na outra.",
        "O que a relação pede, no G90: " + pergunta("O que esta relação pede de [nome] agora?") + ". É a resposta que vai para a devolutiva, sempre do lado de quem está na sala.",
        "Gráfico emissor (Harmonia, Harmonia Familiar, Desembaraçador de Relacionamento, Turbilhão com Vênus) só com consentimento dos dois: testemunhos a lápis, desimpregnados antes, tempo no G23, no máximo 21 dias; remedir a sintonia depois.",
        "Compatibilidade energética na escala de −10 a +10 de Medeiros, lida no G4 dividido por dez: " + pergunta("Qual a compatibilidade energética entre [nome] e [vínculo, lugar, objeto ou projeto] hoje?") + ". Serve para escolher parceiros de trabalho, casas e objetos; não para julgar pessoas.",
    ]))
    H.append(p("Mesas de relacionamento de referência reúnem sete gráficos em torno do Desembaraçador de Relacionamento: Nome Místico de Jesus, Hrim, Nove Círculos, Equilíbrio, Harmonia e Pentagrama Esotérico; a Mesa do Amor Próprio troca três deles por Turbilhão com Mercúrio, Autoestima e Turbilhão com Vênus. O gráfico Harmonia Familiar leva a sequência 8545146 em seis anéis, com a pessoa no centro e os familiares nas pétalas. Nenhuma dessas mesas traz tempo ou decreto próprio: usam-se o tempo do G23 e o fechamento “Harmoniza, equilibra, alinha”, e sempre com o consentimento de quem entra na mesa."))
    H.append(chart_group(["G89", "G90"]))
    H.append(h2("rel-familia", "Família, amizade e equipe"))
    H.append(p("Para grupos (família, amigos, equipe), a pessoa atendida fica no centro e cada vínculo é uma pétala, como no gráfico Harmonia Familiar: por pétala, o percentual de harmonia com o centro (G2) e o tipo de tensão (G91). É um mapa de medição, não um emissor; o que diz sobre terceiros fica no caderno e não vira rótulo."))
    H.append(steps([
        "Vínculos no G36, um por vez: " + pergunta("Há tensão entre [nome] e [vínculo]?") + " e, se sim, o percentual de harmonia no G2.",
        "Tipo de tensão no G91: " + pergunta("Qual o tipo de tensão entre [nome] e [vínculo]?") + " e " + pergunta("Qual o papel de [nome] nessa tensão?") + " (o que depende dela: G90).",
        "Em equipes de trabalho, acrescentar o clima do ambiente (" + go("esp", "Parte VIII") + ", cômodo do posto de trabalho) e a " + go("pros", "Parte XIV") + " para o lado da empresa.",
        "Devolutiva: nomear o vínculo e a tensão, nunca a pessoa (“a relação com a chefia pesa em hierarquia e feedback”).",
    ]))
    H.append(chart("G91"))
    H.append(end())
    return H

def part_prosperidade():
    H = []
    H.append(h1("pros", "Prosperidade, trabalho e empresa", "Parte XIV · Prosperidade e empresa", brk=False))
    H.append(p("Dinheiro e trabalho chegam ao atendimento de três formas: a pessoa que sente bloqueio de prosperidade, a pessoa que sofre no trabalho, e o empresário que quer medir o negócio. As duas primeiras usam listas de bloqueios de referência (o leque de 22 bloqueios da prosperidade e os 15 problemas do Mapa de Atendimento Terapêutico, cada um com uma linha de devolutiva) e devolvem ao protocolo dos chakras, em geral básico (segurança material) e plexo solar (poder pessoal). A terceira usa cinco objetos de medição e um biômetro próprio. Os gráficos de prosperidade (Prosperador, Saúde Financeira, Quadrata, Turbilhão com Júpiter) seguem o uso de loja: testemunho da pessoa ou da empresa a lápis, desimpregnado antes, renovado a cada 14 dias."))
    H.append(box("variacao", "O que não se faz", "Avaliar candidatos, funcionários ou sócios por foto ou pêndulo não entra neste manual, mesmo que cursos ensinem: é discriminação sem critério verificável, mede um terceiro sem consentimento e expõe o terapeuta. O Código de Ética empresarial da ABRAD pede registro do histórico de cada cliente, confidencialidade, não interferir no trabalho de outro profissional e não anunciar soluções fáceis. Frase de devolução para empresário: “indico áreas para olhar; não substituo contador, advogado, consultor nem RH”."))
    H.append(h2("pros-pessoa", "Bloqueio de prosperidade da pessoa"))
    H.append(steps([
        "Área no G24 (dinheiro ou trabalho) e grau no G2: " + pergunta("Qual o grau de equilíbrio da área financeira de [nome], de 0 a 100?") + ".",
        "Bloqueio na lista G94, por bissecção: " + pergunta("O bloqueio principal está na primeira lista?") + ", depois linha a linha. " + pergunta("Há um segundo bloqueio?") + ".",
        "Causa por trás do bloqueio: a maioria dos itens devolve ao G8 (crença limitante e autossabotagem ao setor 2; padrões ancestrais e dívidas kármicas ao 6; obsessores, magia e dispositivo ao 4; ambientes tóxicos ao 5; pessoas tóxicas à " + go("rel", "Parte XIII") + "). Confirmar o chakra no G5; na prática, básico ou plexo solar.",
        "Tratar pelo capítulo do chakra; depois, gráfico de prosperidade escolhido no G41 (categoria Materialização), com tempo no G23 e renovação a cada 14 dias.",
        "Devolutiva com a linha do Mapa de Atendimento correspondente (não merecimento, procrastinação, não soltar…), dita como tendência, com uma orientação prática pequena.",
    ]))
    H.append(chart("G94"))
    H.append(table(["Gráfico de prosperidade (kit de referência)", "Para quê", "Regra e tempo"], [
        ["Prosperador", "prosperidade geral", "testemunho dentro, gráfico ao norte, pelo menos 30 minutos; renovar a cada 14 dias"],
        ["Turbilhão com Júpiter", "atrair prosperidade e abundância", "ativar na quinta-feira, ao norte, por 24 horas"],
        ["Desembaraçador em sentido horário", "atrair e potencializar pedidos", "giro horário"],
        ["Desembaraçador em sentido anti-horário", "abrir caminhos; afastar falta de sorte, pessoas que drenam as finanças, crenças limitantes sobre dinheiro", "giro anti-horário"],
        ["Cartões de intenção (atrair e obter; abrir caminhos e afastar)", "o mesmo, com testemunho e pedra", "nome completo, data de nascimento e intenção no testemunho; pedra vermelha, preta ou transparente; ativação de 10 a 15 minutos; montado até 72 horas"],
        ["Inspiração e criatividade para prosperar", "ideias, insights e intuições", "testemunho no Prosperador com pedra azul ou violeta; até 72 horas"],
        ["Mesa da Prosperidade (sete gráficos)", "Desembaraçador ao centro; Nome Místico de Jesus, Diafragma, Alta Vitalidade 9797979, Pirâmide de Integração, Turbilhão, Pentagrama Esotérico", "sem tempo próprio: G23 e fechamento “Harmoniza, equilibra, alinha”"],
    ]))
    H.append(h2("pros-trabalho", "Trabalho e carreira"))
    H.append(p("O que pesa no trabalho, no G95. Decisão de mudar de emprego ou de carreira: " + go("dec", "Parte XII") + "; vocação e talentos: " + go("areas-auto", "autoconhecimento") + "."))
    H.append(steps([
        pergunta("O que mais pesa no trabalho de [nome] hoje?") + " no G95; percentual no G2; " + pergunta("Há um segundo peso?") + ".",
        "Chefia ou colegas: G91 (tensão) pelo lado da pessoa. Stress e desequilíbrio: chakra plexo solar e cardíaco no G5; limpeza de pessoa se a carga passar de 10.",
        "Mudança desejada: G84 e G85, com a regra das formulações convergentes.",
    ]))
    H.append(chart("G95"))
    H.append(h2("pros-empresa", "Empresa e negócio: decidir como dono"))
    H.append(p("Esta seção é para quem responde pela empresa e precisa decidir: com quem se associar, em qual projeto pôr o dinheiro, se contrata, se expande, se fecha. O pêndulo entra como mais uma fonte de informação na mesa do dono, ao lado do contador, do advogado, das referências e do próprio faro. Ele mede a sociedade, o projeto, a relação e a decisão; não mede o caráter de ninguém. O que vem do gráfico é tendência a confirmar com a conversa e com os números; a decisão continua sendo da pessoa."))
    H.append(box("variacao", "O que o pêndulo mede e o que não mede numa empresa", "<b>Mede</b>: a sintonia da sociedade entre você e um candidato, critério a critério; a favorabilidade de cada projeto; o momento; o peso de cada área do negócio; o clima da equipe como conjunto; a afinidade com um cliente ou fornecedor; a sua própria decisão. <b>Não mede</b>: a honestidade, a competência ou a vida privada de um candidato a sócio, funcionário ou cliente; isso é entrevista, referência, contrato e período de teste. Funcionários e candidatos não são pendulados como pessoas: pendula-se a função (“esta vaga é necessária?”), o momento (“é hora de contratar?”) e, com o consentimento deles, a relação de trabalho. O Código de Ética empresarial da ABRAD pede registro de cada cliente, confidencialidade, não interferir no trabalho de outro profissional e não anunciar soluções fáceis. Frase para o empresário: “indico áreas para olhar; não substituo contador, advogado, consultor nem RH”."))
    H.append(h3("Roteiro geral de uma decisão empresarial"))
    H.append(steps([
        "Escrever no caderno a decisão em uma frase, com as opções numeradas (“1 = sócio A; 2 = sócio B”, “1 = projeto X; 2 = projeto Y; 3 = não fazer nenhum”). Toda lista entra numerada, para usar os leques em branco.",
        "Testemunho: razão social e endereço escritos a lápis, mais o nome completo de quem decide. Trio de permissão para " + pergunta("a decisão de [nome] sobre [assunto] na empresa [nome]") + ". Autoauditoria no G2: acima de 30 de influência do desejo, parar; decisões de dinheiro são as que mais contaminam o operador.",
        "Situação no G108: " + pergunta("Qual é a situação a decidir?") + " e abrir o caso correspondente abaixo.",
        "Critérios: usar o leque de critérios do caso (G106 ou G107) ou escrever os seus no G110. Para cada opção, percentual de cada critério no G2; registrar na matriz da ficha de decisão empresarial.",
        "Peso dos critérios: " + pergunta("Qual critério pesa mais nesta decisão?") + " no mesmo leque; marcar os dois ou três que mais pesam. A matriz é lida com esses pesos, não pela soma simples.",
        "Decisão por opção: G84 para cada opção (" + pergunta("Entrar na sociedade com [A] é favorável para [nome] e para a empresa hoje?") + "), com duas formulações diferentes que precisam convergir; grau no G2; momento no G85.",
        "Comparação: G86 ou G109 só como confirmação; diferença menor que 10 pontos entre duas opções é empate e devolve a decisão à pessoa pelos critérios dela.",
        "Devolutiva e registro: “o pêndulo indica tendência favorável a [opção] por [critérios]; os pontos fracos são [critérios]; confirme com [contador, advogado, referências]”. Revisão em 90 dias: o que aconteceu, para calibrar a própria leitura.",
    ]))
    H.append(chart_group(["G108", "G106"]))
    H.append(chart_group(["G107", "G92"]))
    B = []
    B.append(h3("Caso 1 · Escolher entre dois candidatos a sócio"))
    B.append(p("A dona de uma clínica precisa de um sócio investidor e tem dois candidatos. No caderno: 1 = A, 2 = B. Para cada um, os doze critérios do G106 medidos no G2 (A: valores 80, visão 60, complementaridade 85, confiança 55, comunicação 70, comprometimento 50, capacidade financeira 90, risco 40, rede 75, saída 30, sintonia geral 62. B: valores 70, visão 85, complementaridade 45, confiança 75, comunicação 80, comprometimento 85, capacidade financeira 60, risco 65, rede 50, saída 35, sintonia geral 71). Critérios que mais pesam, pelo pêndulo: confiança, visão e comprometimento. Leitura: A traz dinheiro e complementa, mas a confiança está em 55 e o comprometimento em 50, e esses são critérios de peso; B tem visão e comprometimento altos, mas aporta menos. G84 para cada um, com duas formulações: A, “ainda não”; B, “sim” com grau 68. Momento de B no G85: em semanas. Devolutiva: tendência favorável a B, com a ressalva de capital; A pode entrar como investidor sem gestão, se a confiança subir depois de referências e de um período de teste. Regras de saída medem 30 e 35 nos dois: é o contrato que resolve, e o pêndulo só avisou que isso ainda não foi conversado."))
    B.append(h3("Caso 2 · Escolher entre três projetos"))
    B.append(p("Um restaurante pode abrir delivery (1), uma segunda unidade (2) ou um curso de culinária (3), e não tem recursos para os três. G107 para cada um, critérios no G2; pesos pelo pêndulo: viabilidade, retorno e capacidade da equipe. Delivery: viabilidade 85, momento 80, retorno 60, risco 30, propósito 50, demanda 90, equipe 70, recursos 80, vida pessoal 70, aprendizado 40, favorabilidade geral 74. Segunda unidade: viabilidade 45, momento 35, retorno 80, risco 85, propósito 70, demanda 60, equipe 40, recursos 30, vida pessoal 30, aprendizado 60, geral 42. Curso: viabilidade 70, momento 55, retorno 40, risco 20, propósito 90, demanda 50, equipe 60, recursos 75, vida pessoal 65, aprendizado 85, geral 63. Leitura: a segunda unidade tem o maior retorno e o maior risco, com recursos e equipe baixos: “ainda não” no G84 e, no G85, “depois de resolver outra coisa” (equipe). Delivery e curso são favoráveis; delivery ganha nos critérios de peso. Devolutiva: começar pelo delivery, preparar o curso como segundo passo (alto propósito e aprendizado), e condicionar a segunda unidade a equipe e caixa, remedindo em seis meses."))
    B.append(h3("Caso 3 · Sócio atual: a afinidade caiu"))
    B.append(p("Dois sócios de uma loja, dez anos juntos, brigam por tudo. O dono que procura o atendimento quer saber se desfaz a sociedade. Primeiro, a sociedade como relação (" + go("rel", "Parte XIII") + "): sintonia geral no G2 (hoje 35; há dois anos, pela memória dele, era alta); tensão no G91 (“hierarquia” e “dinheiro”); o que a relação pede no G90 (“limites” e “projeto comum”). Depois, o G106 critério a critério: valores 75, visão 30, complementaridade 80, confiança 60, comunicação 25, comprometimento 50 e 85 (desigual), capacidade financeira 60, risco diferente (30 e 80), saída 20, sintonia geral 38. Leitura: não é falta de valores nem de confiança; é visão divergente, comunicação quebrada, dedicação desigual e apetite a risco oposto, sem regra de saída. G84 para “desfazer a sociedade agora”: “ainda não”. G85: “depois de resolver outra coisa”, e o quê: comunicação e regras. Devolutiva: antes de decidir sair, três conversas mediadas sobre visão, dedicação e regra de saída, com prazo (G23: 60 dias) e remedida da sintonia; se a sintonia não passar de 50, a pergunta de sair volta ao G84. O outro sócio só é pendulado se pedir."))
    B.append(h3("Caso 4 · Contratar ou não; qual função"))
    B.append(p("A empresa cresceu e o dono não sabe se contrata um vendedor ou um assistente administrativo, ou se não contrata. Opções numeradas: 1 = vendedor, 2 = assistente, 3 = não contratar agora. O que se pendula é a função e o momento, nunca candidatos. G107 adaptado (viabilidade, momento, retorno, risco, capacidade da equipe, recursos, impacto na vida do dono) para as opções 1 e 2; G84 para cada uma das três; G85. Resultado típico: assistente favorável (o dono está afogado em tarefas que não vendem), vendedor “ainda não” (não há processo de venda para entregar a ele). Devolutiva: contratar o assistente; a seleção é por entrevista e referências; com o consentimento da pessoa contratada, mede-se depois a relação de trabalho (G91) e o clima (G92). Se o pêndulo escolher um candidato entre vários, isso não entra no manual: é o caso em que o pêndulo substituiria RH e discriminaria sem critério verificável."))
    B.append(h3("Caso 5 · Expandir, abrir filial, mudar de ponto"))
    B.append(p("Decisão em duas camadas. A decisão de expandir é um projeto: G107, G84, G85, com atenção aos critérios de recursos, equipe e vida pessoal. O ponto é um lugar: com os pontos candidatos numerados (G109), a energia de cada um no G3 (abaixo de 6.500, não) e no G2, as fontes que pesam (G66) e o baguá do ponto (G70), e depois a " + go("esp", "Parte VIII") + " inteira no ponto escolhido antes da assinatura. A afinidade do ponto com os clientes desejados: " + pergunta("Qual o percentual de afinidade entre o ponto [n] e os clientes que a empresa quer?") + ". O contrato de aluguel e a análise de mercado continuam sendo do advogado e do consultor."))
    B.append(h3("Caso 6 · Cliente, fornecedor ou proposta"))
    B.append(p("Para uma proposta grande, um cliente novo ou a troca de fornecedor, o G106 é lido como afinidade comercial: valores e ética, visão (o que cada parte espera), complementaridade, confiança, comunicação, comprometimento, capacidade financeira (pagar e entregar), risco, regras de saída (contrato), sintonia geral. Abaixo de 50 em confiança ou em capacidade financeira: pedir garantias ou referências antes de fechar. G84 para a proposta, com duas formulações; G85 para o momento de assinar; G87 só se a data importar. Nunca se pendula a situação financeira da outra empresa como se fosse auditoria: mede-se a relação comercial do lado de quem decide."))
    B.append(h3("Caso 7 · Conflito entre sócios ou na equipe"))
    B.append(p("Quando a queixa é conflito, a sequência é a da " + go("rel", "Parte XIII") + " aplicada à empresa: tensão no G91 (hierarquia, comunicação, dinheiro, valores, sobrecarga, competição), o papel de quem consulta no G90, a sintonia da sociedade no G106, e só depois uma decisão no G84. O pêndulo não decide quem tem razão; ele aponta o tipo de tensão e o que cabe a quem está na sala. Mediação e acordo escrito são a orientação de fechamento."))
    B.append(h3("Regras de leitura comuns aos casos"))
    B.append(ul([
        "<b>Critérios com peso.</b> Dois ou três critérios pesam mais em cada decisão; o pêndulo diz quais. Uma opção forte nos critérios de peso vence uma opção forte na média.",
        "<b>Empate</b> (diferença menor que 10 entre opções) devolve a decisão à pessoa; o pêndulo cumpriu o papel ao mostrar que as opções se equivalem.",
        "<b>Listas próprias</b> vão nos leques G109 e G110, sempre numeradas e datadas no caderno, porque o mesmo leque serve a muitas listas.",
        "<b>Revisão em 90 dias.</b> O diário de decisões (ficha) é o único modo de saber se a leitura empresarial do operador é confiável.",
    ]))
    H.append(cols3("".join(B)))
    H.append(chart_group(["G109", "G110"]))
    H.append(end())
    return H

def part_alimentos():
    H = []
    H.append(h1("ali", "Alimentos, remédios e doses", "Parte XV · Alimentos e doses", brk=False))
    H.append(p("Três roteiros de referência convergem: Lucyana Mutarelli (dose no relógio: gotas ou goles, quantidade, vezes por dia, dias), Sávio Mendonça (teste do prato pela cor pessoal) e José Medeiros (a pergunta certa é “devemos comer”, não “podemos”, com as tabelas de alimentos, vitaminas e plantas). O que o pêndulo responde aqui é compatibilidade energética naquele instante; a resposta vale para o dia, não para a vida. O código de ética da ABRAD veta prescrever e interferir em tratamento: por isso o último passo de todo roteiro desta parte é “confirmar com o profissional habilitado”, e nenhuma dose de medicamento prescrito é alterada por pêndulo."))
    H.append(h2("ali-roteiro", "Roteiro para alimento ou suplemento"))
    H.append(steps([
        "Trio de permissão para " + pergunta("a alimentação de [nome]") + ". Alimento na mesa, ou nome escrito, ou lista G97.",
        pergunta("[Nome] deve comer [alimento] hoje?") + " (não “pode”). Sobre o alimento real: pêndulo sobre o prato; giro horário é compatível, anti-horário não (Mutarelli). Pelo teste da cor pessoal (Sávio): a cor da pessoa medida no G42 e o alimento confrontado com ela, em três movimentos.",
        "Grau: " + pergunta("Qual o grau de compatibilidade de [alimento] com [nome] hoje, de 0 a 100?") + " no G2. Abaixo de 40, evitar hoje; de 40 a 69, pouco; acima de 70, livre.",
        "Carência: " + pergunta("[Nome] está em carência de alguma vitamina?") + " na lista G98; " + pergunta("De qual grupo de alimentos?") + " no G97; " + pergunta("Uma planta de tonificação, eliminação ou manutenção?") + " no G97.",
        "Quantidade e horário, quando fizer sentido: G96 (forma, vezes por dia, horário, duração) e quantidade no G20b ou no relógio G23.",
        "Devolutiva: lista curta de alimentos favoráveis e desfavoráveis para a semana, dita como tendência, e a frase obrigatória: “confirme com nutricionista ou médico, principalmente se houver doença, gravidez ou medicação”.",
    ]))
    H.append(h2("ali-dose", "Dose de floral, chá ou suplemento sem prescrição"))
    B = []
    B.append(p("Roteiro de Mutarelli, usado só para o que não é medicamento prescrito (florais, chás, suplementos de venda livre que a pessoa já decidiu tomar): " + pergunta("São gotas ou goles?") + " → " + pergunta("Qual a dosagem?") + " (G20b, confirmada com " + pergunta("São [N] gotas?") + ") → " + pergunta("Quantas vezes por dia?") + " (confirmar) → " + pergunta("Por quantos dias?") + " (confirmar). Padrão dos florais de Bach quando o pêndulo não define: quatro gotas, quatro vezes ao dia. Para medicamento prescrito, a única pergunta admitida é " + pergunta("Este tratamento está em sintonia com [nome] hoje?") + ", e a resposta vai para a conversa com o médico, nunca para a mudança da dose."))
    H.append(chart("G96", beside="".join(B)))
    H.append(list_pair("G97", "G98"))
    H.append(h2("ali-ervas", "Ervas e alimentos por chakra"))
    H.append(p("A lista G104 cruza o capítulo do chakra com a cozinha: para cada chakra, uma erva-símbolo e as ervas e alimentos associados pelas apostilas de ervas e chakras. Uso citado pelas fontes: chá, folhas em pratos, óleo para cozinhar ou algumas gotas sobre a pele, aroma na casa; a lavanda serve a todos os chakras. Nenhuma fonte dá posologia numérica de ervas: o que se mede é compatibilidade (" + pergunta("Esta erva é compatível com [nome] hoje?") + ") e forma de uso no G96, e a quantidade fica em “uma xícara de chá” ou “algumas gotas”. Ervas interagem com medicamentos: gravidez, doença e medicação em uso pedem confirmação profissional antes de qualquer uso regular."))
    H.append(chart("G104"))
    H.append(end())
    return H

def part_areas():
    H = []
    H.append(h1("areas", "Áreas da vida e pequenas aplicações", "Parte XVI · Áreas da vida", brk=False))
    H.append(p("O G24 é o retrato de oito áreas da vida. A novidade de método é o cruzamento: a pessoa preenche a Roda da Vida (0 a 10 por área, no arquivo de fichas) antes de qualquer medida; o terapeuta mede depois; e a conversa é sobre as diferenças. Uma planche de pêndulo, como lembra uma escola francesa, é “ferramenta de diálogo interior, não instrumento de medida objetiva”; o cruzamento com a autoavaliação é o antídoto contra o viés do operador."))
    H.append(h2("areas-roteiro", "Roteiro das áreas da vida"))
    H.append(p("Roda da Vida preenchida pela pessoa (ficha), sem o terapeuta olhar; depois G24 e G2 como em " + go("n1e", "1E") + ". A área que a pessoa pontuou alto e o pêndulo mediu baixo (ou o inverso) é o tema da conversa; o pêndulo não decreta. Uma área por sessão: saúde e emocional abrem o protocolo dos chakras; relações, a " + go("rel", "Parte XIII") + "; trabalho e dinheiro, a " + go("pros", "Parte XIV") + "; casa, a " + go("esp", "Parte VIII") + "."))
    H.append(h2("areas-agua", "Água"))
    H.append(p("Copo d'água no centro de um gráfico energizador por cerca de 12 minutos (tempo confirmado no G23); vitalidade da água no G3, com 6.500 como mínimo para consumo humano; qualidade pela roseta de Mager no G99 (" + pergunta("Qual a qualidade desta água?") + "). Os gráficos saturam com o uso: desimpregnar entre usos. Água solarizada por cor (G42): uma a duas horas de sol, entre 8 e 11 horas da manhã, em vidro da cor escolhida. Nada disto substitui análise de potabilidade."))
    H.append(h2("areas-cores", "Cores, roupas e tecidos"))
    H.append(p("Cromo-radiestesia da palma da mão: pêndulo sobre a palma, gráfico de cores G42 ao lado, " + pergunta("Qual cor [nome] precisa hoje?") + " e " + pergunta("Qual cor está em excesso?") + " (percentual de cada uma no G2, como no roteiro do curso CEAP). Roupa por intenção no G100, conforme as apostilas de cromoterapia; Sávio Mendonça usa um tecido da cor indicada (seda, algodão ou lã) sobre o corpo pelo tempo medido. Base de evidência fraca e uso inofensivo: entra como orientação de fechamento, nunca como tratamento."))
    H.append(chart_group(["G99", "G100"]))
    H.append(h2("areas-auto", "Autoconhecimento: talentos, áreas a desenvolver, atividades"))
    H.append(p("Os psicométricos clássicos (Bélizal, La Foye) rotulam “qualidades morais” e “inteligência” e as lojas avisam para nunca usá-los como emissores. Este manual reaproveita só a estrutura, para a própria pessoa e com consentimento, sem rótulo: talento (G101), área a desenvolver (G24) e atividades (G103). Nunca em terceiros, nunca para selecionar ninguém."))
    H.append(steps([
        pergunta("Qual o talento mais ativo de [nome] hoje?") + " no G101, e " + pergunta("Qual talento está pedindo expressão?") + ".",
        pergunta("Qual área [nome] mais precisa desenvolver neste ano?") + " no G24; grau no G2.",
        pergunta("Qual atividade está em sintonia com o momento de [nome]?") + " no G103, por bissecção; com três candidatas, percentual de cada uma.",
        "Bloqueio da expressão do talento: G10 (crença) ou G62 (ganho secundário). Próximo passo pequeno, combinado na devolutiva.",
    ]))
    H.append(chart("G101", beside=list_block("G103", cols=3, narrow=True)))
    H.append(end())
    return H

def anexo_anamnese():
    H = []
    H.append(h1("ap-anamnese", "Apêndice D · Anamnese verbal e técnicas de entrevista", "Apêndices", brk=False))
    H.append(p("Dois instrumentos de referência para a conversa que abre e fecha a sessão (" + go("p1-conversa", "Conversar e avisar") + "): a anamnese verbal em 25 perguntas do Caderno de Análises de Radiestesia e as técnicas de entrevista da apostila Abordagem Ética e Anamnese Terapêutica. A anamnese é falada, não lida à pessoa como questionário; as respostas vão para o caderno."))
    H.append(h2("ap-anamnese-25", "Anamnese verbal em 25 perguntas"))
    H.append(table(["Nº", "Pergunta", "Para que serve na sessão"], [
        ["1", "Sua pressão arterial é baixa, alta ou não sabe?", "sinal de alarme e cuidado com técnicas de ativação"],
        ["2", "Tem alguma doença? Qual?", "encaminhamento e limite da hipótese energética"],
        ["3", "Toma alguma medicação? Qual?", "nunca alterar; ponte para o médico"],
        ["4", "Tem problemas cardíacos?", "sinal de alarme"],
        ["5", "Está em período de menopausa?", "chakra sacral e glândulas"],
        ["6", "É alérgico a alguma medicação ou alimento?", "Parte XV e G57"],
        ["7", "Tem insônia?", "ambiente do quarto, Parte VIII"],
        ["8", "Irrita-se facilmente?", "plexo solar; G9"],
        ["9", "Desânimo?", "vitalidade; básico"],
        ["10", "Preguiça?", "vitalidade; hábitos"],
        ["11", "Muitas preocupações?", "mental; G10"],
        ["12", "Algum medo ou trauma?", "G61; cadeia de decodificação"],
        ["13", "Necessidades fisiológicas normais?", "físico; G12"],
        ["14", "Consumiu carne ou bebida alcoólica nas últimas 48 horas?", "convenção de algumas escolas para medir; registrar"],
        ["15", "Casada, solteira, relaciona-se com alguém?", "Parte XIII"],
        ["16", "Filhos?", "família; G82"],
        ["17", "Considera-se feliz no relacionamento?", "Parte XIII"],
        ["18", "Vida sexual ativa?", "sacral"],
        ["19", "Como é o relacionamento familiar (pais e irmãos)?", "G91; transgeracional"],
        ["20", "Espiritualidade?", "G18"],
        ["21", "Experiência paranormal?", "G34; limite da radiestesia"],
        ["22", "Profissão?", "Parte XIV"],
        ["23", "Trabalha? É realizado profissionalmente?", "G95"],
        ["24", "Como é o relacionamento no trabalho?", "G91"],
        ["25", "Financeiro?", "G94"],
    ]))
    H.append(h2("ap-anamnese-tec", "Técnicas de entrevista"))
    H.append(table(["Técnica", "O que é", "Como fica numa sessão de radiestesia"], [
        ["Escuta em três níveis", "o que é dito; o que é sentido por trás do dito; o que o próprio terapeuta sente enquanto escuta", "antes de pegar o pêndulo, dois minutos só de escuta; o terceiro nível é a autoauditoria"],
        ["Empatia", "perceber e compreender o sentimento do outro sem se perder nele, diferente de simpatia", "repetir o sentimento com as palavras da pessoa antes de medir"],
        ["Congruência", "intervenções coerentes com o que o terapeuta de fato pensa e sente", "não dizer “está tudo bem” quando o biômetro diz outra coisa; dizer o número"],
        ["Questão aberta", "pergunta que não se responde com sim ou não, focada nas expressões “lugar comum” da pessoa", "“o que é, para você, ‘estar cansada’?” antes de medir vitalidade"],
        ["Reformulação dos conteúdos", "devolver o que foi entendido, para verificar e refocalizar", "“então o que mais pesa é a casa, não o trabalho; é isso?” antes de escolher a parte do manual"],
        ["Reflexo dos sentimentos", "nomear a emoção que a pessoa expressa; há mais de 200 palavras para sentimentos", "liga-se ao G9: a palavra que a pessoa reconhece é a que se mede"],
        ["Esclarecimento", "tornar mais claro um aspecto evocado, aumentando a capacidade de análise da pessoa", "na devolutiva, uma pergunta por vez sobre cada medida"],
        ["Silêncio", "momentos silenciosos favorecem o processo, exceto nos primeiros minutos", "depois de dizer um número, esperar; não preencher o silêncio com interpretação"],
    ]))
    H.append(h2("ap-anamnese-sessao", "Passo a passo de sessão com mesa ou mapa de apoio (referência)"))
    H.append(p("Sete passos de um manual brasileiro de mapa de atendimento, úteis como esqueleto de qualquer sessão com gráficos: (1) fechar com a pessoa o objetivo da sessão e preparar o espaço; (2) escrever o testemunho (nome completo, data de nascimento, endereço onde está e a intenção em uma frase; só nome e data não bastam, porque outras pessoas têm os mesmos dados) e colocá-lo no decágono; (3) oração ou intenção de abertura, na tradição do operador; (4) medir a frequência inicial na escala de Hawkins (G54) e anotar; (5) fazer as verificações, perguntando ferramenta a ferramenta no relógio ou saindo do decágono com o pêndulo (“qual a próxima ferramenta?”), até o giro anti-horário encerrar; (6) medir a frequência final e devolver as duas à pessoa; (7) corte da conexão em voz alta: “agradeço as informações; corto agora a energia de conexão do atendimento; eu fico com a minha energia e [nome] fica com a sua; gratidão; atendimento encerrado”. O mesmo manual veta falsificar ou omitir informações do atendimento e recomenda não fotografar nem enviar a mesa."))
    H.append(p("Setting das apostilas: consultório, nunca um templo; sem símbolos religiosos impostos; a pessoa sabe que a avaliação é energética; o que não se revela é rótulo (“não podemos é dizer-lhe que ele é neurótico”). O termo de consentimento fica com a ficha."))
    H.append(end())
    return H

def parts():
    return part_decisao() + part_relacoes() + part_prosperidade() + part_alimentos() + part_areas()
