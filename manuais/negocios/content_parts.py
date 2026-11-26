# -*- coding: utf-8 -*-
from bookkit import *
import content_rotas

def part_decisao():
    H = []
    H.append(h1("dec", "A decisão do dono", "Parte II · Decisão", brk=False))
    H.append(p("Toda Parte deste manual termina aqui: o diagnóstico da empresa, a avaliação de um sócio, a leitura de uma proposta ou de um terreno viram, no fim, uma pergunta de sim ou não, um momento e uma data. Os gráficos de decisão difundidos têm quatro respostas (sim, não, talvez, refazer a pergunta); este manual usa a quinta, “não me cabe responder”, como saída ética para perguntas sobre terceiros, dinheiro alheio ou futuro. A base de regras vem de José Medeiros: controle de sensibilidade antes de perguntar, duas ou três formulações que precisam convergir, percentagem, calendário e lista de causas de erro. Os Servranx acrescentam o gráfico de escolha entre 2, 4 ou 10 soluções, com o aviso de que “as cotovias não caem assadas no prato”."))
    H.append(box("variacao", "O pêndulo indica tendência; a decisão é da pessoa", "Nenhuma resposta desta Parte decide por alguém. O que o gráfico devolve é uma indicação para a conversa com sócios, contador e advogado. Vetos repetidos pelas escolas e adotados aqui: nunca usar o pêndulo para decisões legais ou financeiras drásticas sem os números na mesa, nem para responder sobre a vida de quem não pediu."))
    H.append(h2("dec-regras", "Regras do operador"))
    H.append(ul([
        "<b>Controle de sensibilidade antes de perguntar</b> (Medeiros): três perguntas de resposta conhecida; se acertar menos de duas, não decidir nada importante naquele dia. Em números: autoauditoria do G2 abaixo de 30.",
        "<b>Uma pergunta, uma vez, por sessão.</b> Não repetir em loop até obter a resposta desejada; a repetição é a causa de erro mais citada.",
        "<b>Só decisões importantes.</b> O pêndulo não é consultado para trivialidades; o hábito corrói a sensibilidade e a credibilidade com a equipe.",
        "<b>Duas ou três formulações convergentes.</b> A mesma questão dita de dois ou três modos (“é favorável aceitar?”, “é melhor recusar?”, “aceitar traz mais bem do que recusar?”). Só vale se convergirem; divergiram, a resposta é “refazer a pergunta” e a questão fica para outro dia.",
        "<b>Aqui e agora.</b> As respostas valem para o momento da pergunta; uma decisão para daqui a meses é remedida perto da data.",
        "<b>Controle cego quando a carga emocional é alta.</b> Opções escritas em cartões iguais, virados e embaralhados; o pêndulo escolhe o cartão; só depois se vira.",
        "<b>Critérios e pesos antes das opções.</b> Quando a decisão é de critérios (G106, G107, G112, G116, G120), o leque de critérios é lido antes de se olhar para qualquer opção.",
        "<b>Registro e revisão.</b> Pergunta exata, resposta, grau, confiança e decisão no caderno; em 90 dias, o que aconteceu. É o único termômetro honesto.",
        "<b>Causas de erro.</b> Quando uma resposta não faz sentido, antes de repetir: lista G88 (" + pergunta("Qual a causa do erro?") + ").",
    ]))
    H.append(h2("dec-roteiro", "Roteiro"))
    H.append(steps([
        "Pergunta escrita no caderno, com sujeito, verbo e tempo (“aceitar a proposta X neste mês é favorável para a empresa Y?”). Trio de permissão para " + pergunta("esta decisão de [nome] sobre [assunto]") + "; autoauditoria no G2.",
        "G84: " + pergunta("[pergunta]") + ". Sim ou não vão ao passo 4. “Ainda não” abre o G85. “Refazer a pergunta” pede nova redação e uma única nova tentativa; se repetir, o G111 diz o que trava. “Não me cabe responder” encerra o assunto nesta sessão, registrado.",
        "Momento, no G85: " + pergunta("Quando é o momento para [ação]?") + ". Se a resposta for “depois de resolver outra coisa”, " + pergunta("O quê?") + " abre o G111 (trava), o G24 (área da vida), o G94 (bloqueio) ou o G113 (negociação). Dia, semana, mês ou hora no G87, só quando a data importa.",
        "Grau: " + pergunta("Quanto esta decisão é favorável para [nome ou empresa], de 0 a 100?") + " no G2. Abaixo de 40 é desfavorável; de 40 a 69 é incerta e pede informação fora do pêndulo; acima de 70, favorável.",
        "Confirmação por formulação diferente (regra das duas ou três). Divergência: registrar e devolver como “sem resposta hoje”.",
        "Devolutiva: o valor e a tendência, nunca a ordem; os critérios de peso; a quem confirmar. “O pêndulo indica tendência favorável; a decisão é sua.” Registro na ficha; revisão em 90 dias.",
    ]))
    H.append(chart_group(["G84", "G85"]))
    H.append(h2("dec-alternativas", "Alternativas: A, B, C, D"))
    H.append(p("Não há gráfico padrão para comparar opções; o procedimento é o das escolas espanholas e inglesas: as opções escritas antes, uma pergunta de sim ou não para cada uma, depois o percentual de cada uma no mesmo biômetro, depois registro e revisão. O G86 serve de leque quando a pessoa prefere ver as opções lado a lado; para listas maiores, os leques em branco G109 e G110 (" + go("neg-plano", "Parte III") + ")."))
    H.append(steps([
        "Escrever as opções (até quatro) no caderno; a mesma letra no G86.",
        pergunta("A opção A é favorável para [nome ou empresa] hoje?") + " para cada opção, sim ou não.",
        "Para as favoráveis: " + pergunta("Qual o grau de favorabilidade da opção A, de 0 a 100?") + " no G2. Diferença menor que 10 pontos entre duas opções é empate: a decisão volta para a pessoa com os critérios dela.",
        "G86: " + pergunta("Qual opção o pêndulo indica?") + " só como confirmação; “nenhuma delas” e “outra, ainda não vista” são respostas válidas e frequentes.",
        "Cenários: escrever até quatro (otimista, base, pessimista, ruptura) e perguntar " + pergunta("Para qual cenário a empresa deve se preparar primeiro?") + ". É conversa, não previsão.",
    ]))
    H.append(h2("dec-calendario", "Calendário: dia, mês, semana e hora"))
    H.append(p("O G87 é o relógio radiestésico de datas: anel externo com os dias do mês, depois os meses, os dias da semana e as horas. Lê-se um anel por vez, como escala. Medeiros acrescenta duas chaves tradicionais, dadas aqui como convenção e não como regra: no quarto crescente da Lua, ações para aumentar; no minguante, para reduzir; e os dias da semana regidos por planetas, de domingo a sábado: Sol, Lua, Marte (ação), Mercúrio (gestão), Júpiter (concretização), Vênus, Saturno (administração). “Melhor data” para lançamento ou assinatura por pêndulo não tem método publicado; o que se mede é o momento da empresa, não a sorte do dia. Os Servranx pendulavam “os melhores dias para anúncios e promoções”: entra aqui como confirmação, nunca como calendário comercial."))
    H.append(steps([
        pergunta("Em que mês é o momento para [ação]?") + " (anel dos meses) → " + pergunta("Em que dia?") + " (anel dos dias) → " + pergunta("Em que dia da semana?") + " só como confirmação → " + pergunta("Em que hora?") + " quando fizer diferença.",
        "Datas no futuro distante são remedidas quando se aproximam.",
    ]))
    H.append(chart_group(["G86", "G87"]))
    H.append(chart("G88"))
    H.append(h2("dec-trava", "O que trava a decisão"))
    H.append(p("Quando o G84 responde “refazer” duas vezes, quando a pessoa adia uma decisão já medida ou quando diz “não sei por quê”, a trava tem nome. O G111 separa falta de dado, medo, valores, pressão, lealdade, apego e cansaço, porque cada um se trata de um jeito: dado se busca, medo se nomeia, valor se respeita, pressão se devolve a quem pressiona, cansaço se adia com data. Insegurança e incerteza, as palavras mais ouvidas de um empresário indeciso, quase sempre caem nos setores 1 a 4."))
    H.append(steps([
        pergunta("O que trava esta decisão hoje?") + " no G111; " + pergunta("Há uma segunda trava?") + ".",
        "Falta de informação: listar o dado, quem traz e quando; só então voltar ao G84. Medos: G127 pelo lado da pessoa; separar risco real (G107 critério 4) de medo; pré-mortem.",
        "Conflito de valores: a decisão não é de pêndulo, e já está tomada. Pressão de terceiro: nomear quem; a decisão só vale quando for da pessoa.",
        "Lealdade e apego: G62 (ganho em manter) e G59 (lealdades e votos); G115 para o que o modelo antigo ainda entrega.",
        "Cansaço e “não é a hora”: adiar com data no G85; registrar; voltar na data.",
    ]))
    H.append(chart("G111"))
    H.append(end())
    return H

def part_negocio():
    H = []
    H.append(h1("neg", "A empresa como um todo", "Parte III · A empresa", brk=False))
    H.append(p("O empresário que chega dizendo “alguma coisa não vai bem” precisa primeiro de um retrato, não de uma decisão. Esta Parte faz o retrato: a energia do conjunto no G3, as onze áreas do negócio no G92, o bloco frágil do modelo de negócio no G114, a fase no G115, e os leques em branco para prioridades e para o plano de doze meses. O retrato repetido a cada trimestre é o painel do dono: uma série de onze percentuais que ele compara com o que os números dizem."))
    H.append(box("variacao", "O que o pêndulo mede e o que não mede numa empresa", "<b>Mede</b>: a energia do conjunto; o peso de cada área; a fragilidade de cada bloco do modelo; a fase; a sintonia da sociedade; a afinidade do produto, do nome e do ponto com o público; o clima da equipe como conjunto; a própria decisão. <b>Não mede</b>: faturamento, resultado, valor de mercado, a honestidade ou a competência de qualquer pessoa, o que o concorrente vai fazer. Os Servranx admitem a empresa como sujeito de medição; o testemunho é a razão social, o endereço e o nome de quem decide."))
    H.append(h2("neg-360", "Diagnóstico 360: a sessão de retrato"))
    H.append(steps([
        "Testemunho da empresa a lápis; trio de permissão; autoauditoria no G2.",
        "Energia geral no G3: " + pergunta("Qual a vitalidade da empresa [nome], em unidades Bovis?") + ". Abaixo de 6.500, o espaço vem primeiro (" + go("esp", "Parte IX") + ").",
        "G92: percentual de cada uma das onze áreas no G2, na ordem do leque; depois " + pergunta("Qual área pede atenção primeiro?") + " e " + pergunta("Há uma segunda?") + ".",
        "Para as duas áreas indicadas, um gráfico de aprofundamento: clima da equipe no G91; finanças no G94 na pessoa do responsável; sócios no G106; produto, nome e clientes no G2 com perguntas de afinidade; ponto e espaço na Parte IX; liderança como pessoa, só com pedido (" + go("pes", "Parte XI") + ").",
        "Devolutiva: três prioridades em ordem, cada uma com uma ação prática pequena e o profissional que confirma. Registro dos onze percentuais na ficha de diagnóstico.",
        "Repetir a cada trimestre; a série é o painel. Uma área que cai dois trimestres seguidos pede sessão própria.",
    ]))
    H.append(chart("G92"))
    H.append(h2("neg-modelo", "Modelo de negócio: o bloco frágil"))
    H.append(p("Os nove blocos do quadro de modelo de negócio (clientes, proposta de valor, canais, relacionamento, receitas, recursos, atividades, parcerias, custos) são construção de gestão, não da tradição radiestésica; entram aqui como lista pendulável de prioridade, declarados como tal. O pêndulo não desenha o modelo: ordena a conversa sobre ele."))
    H.append(steps([
        pergunta("Qual bloco do modelo de negócio está mais frágil hoje?") + " no G114; percentual de solidez de cada bloco no G2.",
        "O bloco mais frágil devolve a um setor do G92 ou a um critério do G107; o segundo mais frágil vira a próxima conversa.",
        "Abaixo de 50 em “segmentos de clientes” ou “proposta de valor”: entrevistar dez clientes antes de qualquer projeto novo.",
    ]))
    H.append(h2("neg-fase", "Fase do negócio"))
    H.append(p("A mesma decisão muda de sentido conforme a fase: contratar na validação é prematuro, contratar no crescimento é tardio. O G115 pergunta em que fase a empresa está de fato, não na que o dono gostaria; “apego ao modelo antigo” do G111 e “reinvenção” do G115 costumam aparecer juntos."))
    H.append(chart_group(["G114", "G115"]))
    H.append(h2("neg-plano", "Planejamento anual, prioridades e cenários"))
    H.append(steps([
        "Roda da Vida do dono e G24 (" + go("pes-roda", "Parte XI") + "): o lado pessoal entra como critério 9 de todo projeto.",
        "Diagnóstico 360 (acima): os onze percentuais e as duas áreas que pedem atenção.",
        "Projetos candidatos, numerados, no G107 com pesos e pré-mortem (" + go("proj", "Parte VI") + ").",
        "Prioridades: até oito no G109, " + pergunta("Qual prioridade vem primeiro?") + " e percentual de cada uma.",
        "Doze meses no G110: " + pergunta("Em que mês cabe [ação]?") + " e " + pergunta("Qual mês pede mais cuidado?") + ". Datas distantes são remedidas quando se aproximam.",
        "Cenários no G86 (" + go("dec-alternativas", "Parte II") + "). Revisão trimestral com o diagnóstico 360.",
    ]))
    H.append(chart_group(["G109", "G110"]))
    H.append(end())
    return H

def part_socios():
    H = []
    H.append(h1("soc", "Sócios, parceiros e investidores", "Parte IV · Sociedade", brk=False))
    H.append(p("A sociedade é medida como relação: do lado de quem pede, nunca como juízo sobre o outro. Primeiro a sintonia e os níveis (G89), o que a relação pede (G90) e o tipo de tensão (G91); depois a compatibilidade para um objetivo escrito (G118) e os doze critérios de sociedade (G106). O gráfico de pesquisa de compatibilidade de referência traz um campo “Objetivo” entre os dois testemunhos: a mesma dupla pode ser compatível para um projeto e não para outro, e essa é a informação mais útil que esta Parte devolve. Os Servranx mediam a harmonia “entre uma pessoa e o objetivo de uma ação, ou entre duas pessoas” (Psicoindutor); aqui só se mede, nunca se emite sem consentimento dos dois."))
    H.append(box("variacao", "A regra do terceiro na sociedade", "O candidato a sócio entra só como parte da relação de sociedade com quem pede. Pergunta aceitável: “qual o percentual de confiança nesta sociedade hoje?”. Pergunta inaceitável: “ele é honesto?”, “ele está escondendo algo?”. Honestidade, competência e vida privada são entrevista, referência, contrato e período de teste. O nome completo e a data de nascimento do outro não entram no testemunho sem consentimento dele."))
    H.append(h2("soc-roteiro", "Roteiro: a sociedade como relação"))
    H.append(steps([
        "Nomear a relação no caderno (“a sociedade com A no projeto X”); trio de permissão para " + pergunta("a relação de [nome] com [sócio ou candidato]") + ".",
        "Sintonia geral: " + pergunta("Qual o percentual de sintonia entre [nome] e [sócio] hoje, de 0 a 100?") + " no G2. Não há limiar publicado; registre e compare entre sessões. Abaixo de 50 abre o G106 critério a critério.",
        "Níveis no G89, um por vez: emocional, mental e comunicação, energético, valores, confiança, apoio; percentual de cada um no G2. O nível mais baixo é o tema da conversa.",
        "Compatibilidade para o objetivo no G118: objetivo escrito antes (“sociedade na clínica”, “parceria no lançamento”), " + pergunta("Qual a compatibilidade entre [T1] e [T2] para [objetivo], hoje?") + ". Se o valor muda muito entre dois objetivos, dizer para qual sim e para qual não. Compatibilidade de Medeiros no G4 dividido por dez como segunda leitura.",
        "Padrão repetido: " + pergunta("Há um padrão que se repete nas sociedades de [nome]?") + ". Se sim, G10 (crença) e as três últimas parcerias no caderno.",
        "O que a relação pede, no G90: " + pergunta("O que esta relação pede de [nome] agora?") + ". É a devolutiva e a pauta da próxima reunião de sócios.",
        "Tensão no G91 quando há conflito: " + pergunta("Qual o tipo de tensão entre [nome] e [sócio]?") + " e " + pergunta("Qual o papel de [nome] nessa tensão?") + ".",
    ]))
    H.append(chart_group(["G89", "G90"]))
    H.append(chart_group(["G91", "G118"]))
    H.append(h2("soc-criterios", "Os doze critérios de sociedade"))
    H.append(p("Cada critério do G106 recebe um percentual no G2 para cada candidato numerado; depois o pêndulo diz quais dois ou três critérios pesam mais nesta sociedade. A matriz é lida pelos pesos, não pela soma. Todo critério abaixo de 50 vira cláusula do contrato ou conversa explícita antes dele; “regras de saída” mede baixo em quase toda sociedade nova, e é o contrato que resolve, não o pêndulo. Para investidor e conselheiro, pesam mais capacidade financeira, apetite a risco e regras de saída, e “complementaridade” lê-se como “o que traz além do dinheiro”. Para cliente e fornecedor, o mesmo leque é lido como afinidade comercial (" + go("prop", "Parte V") + ")."))
    H.append(chart("G106"))
    H.append(h2("soc-ciclo", "O ciclo da sociedade"))
    H.append(table(["Momento", "O que se mede", "O que fica com o advogado e os sócios"], [
        ["Antes de entrar", "G118 para o objetivo; G106 completo com pesos; G84 com duas formulações; G85 momento", "contrato social, acordo de sócios, aportes, papéis"],
        ["Ao formalizar", "cada critério abaixo de 50 do G106 é relido como cláusula a escrever", "redação e registro"],
        ["Em operação", "sintonia geral no G2 a cada trimestre; G90 como pauta da reunião de sócios", "governança, reuniões, atas"],
        ["Na crise", "G91 tipo de tensão; G90 o que a relação pede; G106 critério a critério; G62 ganho em manter; G84 só depois, com prazo", "mediação, revisão do acordo"],
        ["Na saída ou sucessão", "G84 com formulações convergentes; G85; G115 fase; G59 e G62 para lealdades", "dissolução, compra de quotas, acordo de família"],
    ], cls="small"))
    H.append(h2("soc-casos", "Casos resolvidos"))
    B = []
    B.append(h3("Caso 1 · Escolher entre dois candidatos a sócio"))
    B.append(p("A dona de uma clínica precisa de um sócio investidor e tem dois candidatos. No caderno: 1 = A, 2 = B. G118 para o objetivo “sociedade na clínica”: A 58, B 74. G106 para cada um no G2 (A: valores 80, visão 60, complementaridade 85, confiança 55, comunicação 70, comprometimento 50, capacidade financeira 90, risco 40, rede 75, saída 30, sintonia geral 62. B: valores 70, visão 85, complementaridade 45, confiança 75, comunicação 80, comprometimento 85, capacidade financeira 60, risco 65, rede 50, saída 35, sintonia geral 71). Critérios que mais pesam, pelo pêndulo: confiança, visão e comprometimento. Leitura: A traz dinheiro e complementa, mas confiança e comprometimento estão baixos, e são critérios de peso; B tem visão e comprometimento altos e aporta menos. G84 para cada um, com duas formulações: A, “ainda não”; B, “sim” com grau 68. Momento de B no G85: em semanas. Devolutiva: tendência favorável a B, com a ressalva de capital; A pode entrar como investidor sem gestão se a confiança subir depois de referências e de um período de teste. Regras de saída medem 30 e 35 nos dois: o contrato resolve; o pêndulo só avisou que isso ainda não foi conversado."))
    B.append(h3("Caso 2 · Sócio atual: a afinidade caiu"))
    B.append(p("Dois sócios de uma loja, dez anos juntos, brigam por tudo. O que procura o atendimento quer saber se desfaz a sociedade. Primeiro a relação: sintonia geral no G2 (hoje 35; há dois anos, pela memória dele, era alta); tensão no G91 (“hierarquia” e “dinheiro”); o que a relação pede no G90 (“limites” e “projeto comum”). G118 para dois objetivos: “manter a loja como está”, 32; “abrir a segunda unidade juntos”, 61. Depois o G106 critério a critério: valores 75, visão 30, complementaridade 80, confiança 60, comunicação 25, comprometimento desigual (50 e 85), apetite a risco oposto (30 e 80), saída 20, sintonia geral 38. Leitura: não é falta de valores nem de confiança; é visão divergente, comunicação quebrada, dedicação desigual e risco oposto, sem regra de saída; e a dupla serve a um projeto novo mais do que à loja atual. G84 para “desfazer a sociedade agora”: “ainda não”. G85: “depois de resolver outra coisa”, e o quê: comunicação e regras. Devolutiva: três conversas mediadas sobre visão, dedicação e regra de saída, com prazo de 60 dias e remedida da sintonia; se não passar de 50, a pergunta de sair volta ao G84. O outro sócio só é pendulado se pedir."))
    B.append(h3("Caso 3 · Investidor para um projeto"))
    B.append(p("Um empreendedor recebeu proposta de um investidor para 30 % da empresa. Objetivo escrito: “sociedade com investidor para o crescimento de 2027”. G118: 66. G106 com os pesos de investidor: capacidade financeira 90, apetite a risco 40 (o dele é 75: diferença grande), regras de saída 30, visão 55, valores 70, sintonia geral 58. Leitura: compatível em parte; a diferença de apetite a risco e a saída não combinada são os pontos, e os dois são matéria de acordo de sócios, não de pêndulo. G84 para “aceitar a proposta como está”: “não”; para “aceitar com regras de decisão de investimento e cláusula de saída”: “sim”, grau 72. G85: em semanas, depois da redação do acordo. Devolutiva: tendência favorável com condições; o percentual de participação e a avaliação da empresa ficam com o contador e o advogado."))
    H.append(cols3("".join(B)))
    H.append(end())
    return H

def part_propostas():
    H = []
    H.append(h1("prop", "Propostas, contratos, clientes e fornecedores", "Parte V · Propostas", brk=False))
    H.append(p("Uma proposta é lida como objeto: o resumo numerado no caderno é o testemunho. O G112 aponta o ponto que pede atenção primeiro e mede o conforto de quem decide com cada ponto; o G113 diz onde a negociação travou; o G106 lido como afinidade comercial mede a relação com o cliente ou o fornecedor; o G84 e o G85 fecham. José Medeiros é o único autor da tradição que trata contrato como objeto (“a oportunidade ou vantagem de assinar um contrato ou as cláusulas que dele devem constar”); os Servranx ensinam a medir a própria abordagem numa negociação (“como devo agir com X para obter Y?”: melhor contato, melhor momento, como me comportar), nunca a outra parte."))
    H.append(box("alerta", "O que não se pendula numa proposta", "O valor da multa, o preço final, a situação financeira da outra empresa como se fosse auditoria, a honestidade de quem assina. O G112 não lê a cláusula: diz onde o advogado e o contador devem olhar. A reputação da outra parte é referência e consulta pública, nunca pêndulo sobre a pessoa."))
    H.append(h2("prop-roteiro", "Roteiro"))
    H.append(steps([
        "Resumo da proposta em uma linha, numerado, no caderno; se houver mais de uma, todas numeradas (G109). Trio de permissão para " + pergunta("a decisão de [nome ou empresa] sobre a proposta [n]") + "; autoauditoria.",
        "Afinidade comercial no G106 lido para a outra parte: valores, visão (o que cada parte espera), complementaridade, confiança, comunicação, comprometimento, capacidade financeira (pagar e entregar), risco, regras de saída (contrato), sintonia geral. Abaixo de 50 em confiança ou em capacidade financeira: garantias e referências antes de fechar.",
        "Pontos de atenção no G112: " + pergunta("Qual ponto desta proposta pede atenção primeiro?") + "; conforto por ponto no G2; " + pergunta("Há um segundo ponto?") + ". Os pontos abaixo de 50 vão ao advogado e ao contador com nome.",
        "Se a negociação está parada: G113, " + pergunta("O que trava esta negociação hoje?") + ". Fator nosso devolve ao G112 e ao G111; fator da outra parte se pergunta a eles, não ao pêndulo.",
        "Decisão no G84 com duas formulações; momento de assinar no G85; G87 só se a data importar.",
        "Devolutiva e registro: “tendência favorável a fechar, com atenção a [pontos]; confirme com [advogado, contador]”. Revisão em 90 dias: o que o contrato de fato trouxe.",
    ]))
    H.append(h2("prop-pontos", "Os doze pontos de atenção"))
    H.append(p("Preço e pagamento, prazo, escopo, garantias, saída, exclusividade, responsabilidades, reputação, valores, informação que falta, momento e outro. “Saída e rescisão” mede baixo em quase toda proposta nova, como “regras de saída” na sociedade: é o contrato que resolve. Preço entre várias opções vai ao G109 com os valores escritos (" + go("proj-preco", "Parte VI") + "), lido como tendência e confirmado pelo contador."))
    H.append(chart("G112"))
    H.append(h2("prop-trava", "Onde trava a negociação"))
    H.append(p("Uma proposta que “não anda” trava em um de oito lugares, e só três deles são nossos. O G113 separa fator nosso, fator da outra parte, contexto, terceiro, ambiente, pessoa que drena, ganho em não fechar e falta de informação. Quando aponta a outra parte ou o contexto, a resposta é perguntar a eles ou olhar os dados, e o pêndulo só diz quando voltar (G85). As três perguntas dos Servranx sobre a abordagem (melhor contato, melhor momento, como me comportar) são lidas no G109 com as opções escritas: telefonar, visitar, escrever; esta semana, no mês que vem; direto, com intermediário."))
    H.append(chart("G113"))
    H.append(h2("prop-casos", "Casos resolvidos"))
    B = []
    B.append(h3("Caso 4 · Proposta grande de um cliente novo"))
    B.append(p("Uma prestadora de serviços recebe a maior proposta da sua história, de um cliente que não conhece. G106 como afinidade comercial: valores 70, visão 60, complementaridade 80, confiança 45, comunicação 65, comprometimento 70, capacidade financeira 50, risco 70, saída 30, sintonia geral 61. G112: ponto que pede atenção primeiro, “exclusividade e dependência” (conforto 30); segundo, “saída e rescisão” (25); “preço e pagamento” 70. Leitura: a proposta é boa de preço e perigosa de dependência; a confiança e a capacidade de pagar estão incertas. G84 para “aceitar como está”: “não”; para “aceitar com prazo de doze meses, sem exclusividade e com garantia de pagamento”: “sim”, grau 70. G85: em semanas. Devolutiva: tendência favorável com três condições, todas para o advogado redigir e o contador confirmar."))
    B.append(h3("Caso 5 · A negociação que não anda"))
    B.append(p("Uma empresa negocia há quatro meses a venda de um equipamento e o comprador não responde. G113: “fator da outra parte” (decisor ausente). Leitura: não há o que mudar na proposta; o pêndulo só avisa que a trava não é nossa. G85 para “retomar o contato”: em semanas; abordagem no G109 com três opções escritas (telefonar ao decisor, visitar, propor prazo final): o leque indica “visitar”, percentual 72. Devolutiva: parar de reescrever a proposta; marcar a visita; se em 30 dias nada mudar, arquivar com data de retorno. A segunda leitura do G113, meses depois, apontou “ganho em não fechar”: o dono temia a entrega. Esse ganho foi ao G62 e, só depois, a venda ao G84."))
    B.append(h3("Caso 6 · Trocar de fornecedor"))
    B.append(p("Uma loja quer trocar o fornecedor principal por um mais barato. Dois fornecedores numerados (1 = atual, 2 = novo). G106 como afinidade comercial para os dois: o atual mede confiança 85 e capacidade de entregar 80, preço baixo (critério acrescentado no setor 12: 40); o novo mede confiança 50, entrega 55, preço 85. Pesos: entrega e confiança. G112 para a proposta do novo: “garantias e penalidades” pede atenção primeiro (30). G84 para “trocar agora”: “ainda não”; G85: “depois de resolver outra coisa”, e o quê: um pedido de teste. Devolutiva: pedido pequeno de teste com o novo, por três meses, mantendo o atual; remedir confiança e entrega no fim; só então a troca volta ao G84."))
    H.append(cols3("".join(B)))
    H.append(end())
    return H

def part_projetos():
    H = []
    H.append(h1("proj", "Projetos, produtos, preços e oportunidades", "Parte VI · Projetos", brk=False))
    H.append(p("Um projeto, um produto novo, uma oportunidade: cada um escrito e numerado no caderno recebe um percentual por critério no G107, e a soma não decide sozinha. O pêndulo diz quais dois ou três critérios pesam mais nesta decisão; uma opção forte nos critérios de peso vence uma opção forte na média. O pré-mortem entra antes da decisão, como passo opcional de higiene; o preço entre opções, a exposição na loja, o meio de publicidade e o dia da promoção, usos comerciais que os Servranx já descreviam, entram no G109 com as opções escritas, como tendência a confirmar com os números."))
    H.append(h2("proj-roteiro", "Roteiro"))
    H.append(steps([
        "Projetos numerados no caderno, com uma linha cada (“1 = delivery; 2 = segunda unidade; 3 = curso”). Trio de permissão; autoauditoria.",
        "Pesos: " + pergunta("Qual critério pesa mais nesta decisão?") + " no G107; marcar os dois ou três que mais pesam antes de medir qualquer projeto.",
        "Para cada projeto, percentual de cada critério no G2; registrar na matriz da ficha. Risco acima de 70 em qualquer projeto: plano de saída antes de entrar.",
        "Pré-mortem (abaixo) para os dois projetos mais fortes.",
        "Favorabilidade geral (critério 11) de cada um; diferença menor que 10 entre dois é empate e devolve a decisão à pessoa. Comparação em G86 ou G109 só como confirmação.",
        "G84 para o projeto indicado, com duas formulações; G85 para o momento; G87 se a data importar. Devolutiva: “tendência favorável a [projeto] por [critérios]; os pontos fracos são [critérios]; confirme com [contador, equipe, clientes]”. Revisão em 90 dias e remedida em seis meses.",
    ]))
    H.append(chart("G107"))
    H.append(h2("proj-premortem", "Pré-mortem: antes de decidir, imaginar que deu errado"))
    H.append(p("Técnica de Gary Klein: antes de aprovar, a equipe imagina que o projeto fracassou daqui a doze meses e escreve as causas. Reduz a confiança excessiva mais do que listar prós e contras. Com o pêndulo: " + pergunta("Se este projeto falhar em doze meses, qual será a causa principal?") + " lida sobre os doze critérios do G107; depois " + pergunta("E a segunda?") + ". As causas apontadas viram as duas primeiras tarefas do plano, ou o motivo de não fazer. Não é previsão: é uma pergunta que a equipe tem vergonha de fazer e o leque faz por ela."))
    H.append(h2("proj-preco", "Preço, exposição, publicidade e datas: as opções no leque em branco"))
    H.append(p("Os Servranx escreviam que o pêndulo “indica com precisão o preço que fará vender, porque o número agradará à clientela”, escolhe os melhores lugares da loja para expor os artigos, o meio de publicidade e os melhores dias para anúncios e promoções. Este manual aceita os quatro usos com uma condição: sempre entre opções escritas, numeradas e já aprovadas pelo contador ou por quem faz marketing. O pêndulo ordena opções viáveis; não inventa o preço."))
    H.append(steps([
        "Preço: três a cinco valores viáveis, numerados, no G109; " + pergunta("Qual preço agrada mais à clientela de [produto]?") + "; percentual de cada um no G2; o contador confirma a margem.",
        "Exposição: pontos da loja numerados na planta (G109); " + pergunta("Qual lugar vende mais [artigo]?") + "; cruzar com o baguá do imóvel (G70).",
        "Publicidade: meios numerados (G109); percentual de afinidade de cada um com o público desejado.",
        "Datas de promoção ou lançamento: G87 só como confirmação de datas já possíveis no calendário comercial.",
    ]))
    H.append(h3("Caso 7 · Escolher entre três projetos"))
    H.append(p("Um restaurante pode abrir delivery (1), uma segunda unidade (2) ou um curso de culinária (3), e não tem recursos para os três. Pesos pelo pêndulo: viabilidade, retorno e capacidade da equipe. Delivery: viabilidade 85, momento 80, retorno 60, risco 30, propósito 50, demanda 90, equipe 70, recursos 80, vida pessoal 70, aprendizado 40, favorabilidade geral 74. Segunda unidade: viabilidade 45, momento 35, retorno 80, risco 85, propósito 70, demanda 60, equipe 40, recursos 30, vida pessoal 30, aprendizado 60, geral 42. Curso: viabilidade 70, momento 55, retorno 40, risco 20, propósito 90, demanda 50, equipe 60, recursos 75, vida pessoal 65, aprendizado 85, geral 63. Pré-mortem do delivery: causa principal “capacidade da equipe”; do curso: “demanda dos clientes”. Leitura: a segunda unidade tem o maior retorno e o maior risco, com recursos e equipe baixos: “ainda não” no G84 e, no G85, “depois de resolver outra coisa” (equipe). Delivery e curso são favoráveis; delivery ganha nos critérios de peso. Devolutiva: começar pelo delivery com uma contratação de função prevista, preparar o curso como segundo passo depois de validar a demanda, e condicionar a segunda unidade a equipe e caixa, remedindo em seis meses."))
    H.append(end())
    return H

def part_pessoas():
    H = []
    H.append(h1("eq", "Pessoas, equipe e liderança", "Parte VII · Pessoas", brk=False))
    H.append(p("Esta é a Parte com mais vetos e menos gráficos, de propósito. A equipe entra como conjunto (clima no G92, tipo de tensão no G91); uma vaga entra como função e momento; uma pessoa só entra com pedido dela. O lado humano que este manual mede com liberdade é o de quem decide: o que pesa no trabalho (G95), o talento mais ativo (G101) e a matriz de foco (G123), para o empreendedor e para o profissional liberal que trabalha sozinho."))
    H.append(box("alerta", "Contratar, promover, desligar", "O que se pendula é a função (“esta vaga é necessária?”, “qual função: vendedor ou assistente?”) e o momento (“é hora de contratar?”). Candidatos nunca são pendulados: a seleção é entrevista, referências e período de teste. Se o pêndulo escolher um candidato entre vários, isso não entra no manual: é o caso em que ele substituiria o RH e discriminaria sem critério verificável. Depois da contratação, com o consentimento da pessoa, mede-se a relação de trabalho (G91) e o clima (G92), nunca a pessoa."))
    H.append(h2("eq-equipe", "A equipe como conjunto"))
    H.append(steps([
        "Clima no G92 setor 3, percentual no G2; " + pergunta("Qual o clima da equipe de [empresa] como conjunto, de 0 a 100?") + ".",
        "Tipo de tensão no G91, para a equipe inteira ou para um vínculo nomeado pelo papel (“a relação da dona com a gerência”): " + pergunta("Qual o tipo de tensão?") + " e " + pergunta("Qual o papel de [nome] nessa tensão?") + ".",
        "Vaga: opções numeradas (“1 = vendedor; 2 = assistente; 3 = não contratar agora”) no G107 adaptado (viabilidade, momento, retorno, risco, capacidade da equipe, recursos, impacto na vida do dono); G84 para cada uma; G85.",
        "Clima do posto de trabalho e da sala de reunião pela " + go("esp", "Parte IX") + ": o espaço é a causa mais fácil de corrigir.",
        "Devolutiva à equipe, quando o dono quiser compartilhar: o tipo de tensão e o que o conjunto pede, nunca nomes. Uma reunião de clima com o G91 na mesa, com todos sabendo, é uso legítimo; sem que saibam, não é.",
    ]))
    H.append(h2("eq-profissional", "O profissional e o empreendedor: o que pesa no trabalho"))
    H.append(p("Para quem trabalha sozinho ou lidera, o G95 responde o que pesa hoje: sobrecarga, falta de propósito, vínculos, remuneração, insegurança ou a vontade de mudar. Mudança de carreira ou de negócio vai à Parte II; sobrecarga com carga acima de 10 vai ao atendimento pessoal."))
    H.append(chart("G95"))
    H.append(h2("eq-talentos", "Talentos e o que fica com o dono"))
    H.append(p("Os psicométricos clássicos rotulam “qualidades morais” e “inteligência” e são a raiz da seleção de pessoal por pêndulo. Este manual reaproveita só a estrutura, para a própria pessoa e com consentimento: talento mais ativo (G101) e, a partir dele, a matriz de foco (G123) para o empreendedor que precisa decidir o que delega e o que mantém."))
    H.append(steps([
        pergunta("Qual o talento mais ativo de [nome] hoje?") + " no G101, e " + pergunta("Qual talento está pedindo expressão?") + ".",
        "As atividades da semana, numeradas, na matriz de foco (G123): o que fica com o dono é o que usa o talento mais ativo.",
        "O que o dono faz melhor fica com ele; o resto vira função a contratar (" + go("eq-equipe", "acima") + "). Bloqueio da expressão do talento: G10 (crença) ou G62 (ganho).",
    ]))
    H.append(chart("G101"))
    H.append(end())
    return H

def part_bloqueios():
    H = []
    H.append(h1("blo", "Interferências e bloqueios", "Parte VIII · Interferências", brk=False))
    H.append(p("“Tem algo me travando?” é a segunda pergunta mais ouvida de um empresário, depois de “faço ou não faço?”. Esta Parte responde em ordem: onde está (G119: em quem decide, numa relação, na equipe, no espaço, na memória, num contrato energético, no coletivo, ou em lugar nenhum), de onde veio (G28), que ganho sustenta (G62), que voto ou lealdade prende (G59), que sabotador e que crença estão por trás (G127, G10), e como proteger sem agir contra ninguém (G67). O bloqueio de prosperidade propriamente dito está na " + go("fin", "Parte X") + ". A tradição toda fala de inveja e “olho gordo”; este manual os trata como energia de fora, sem nome, respondida com limites e proteção, e adota o veto dos Servranx: nunca “devolver”."))
    H.append(h2("blo-triagem", "Triagem: onde está a interferência"))
    H.append(steps([
        pergunta("Onde está a interferência que pesa no negócio hoje?") + " no G119; " + pergunta("Há uma segunda?") + ".",
        "Em quem decide: bloqueios no G94 (" + go("fin", "Parte X") + "), sabotador no G127, crença no G10, ganho no G62; origem no G28.",
        "Numa relação ou na equipe: G91 e G89, sem nomear a pessoa na devolutiva. No espaço: G69 cômodo a cômodo, G66, G3 (" + go("esp", "Parte IX") + ").",
        "Memória do local ou do negócio: G82 (negócio anterior, ex-ocupante); caiação e consagração (G71); a história documentada do imóvel ou da empresa.",
        "Contrato energético: G59. Coletivo: G67 limites e proteção, nunca emissor contra alguém. Não é energético: contador, consultor e dados; G111 se a decisão travar mesmo assim.",
        "Carga da interferência no G2: até 10, residual; acima de 30, tratar antes de decidir qualquer coisa.",
    ]))
    H.append(chart_group(["G119", "G28"]))
    H.append(h2("blo-dono", "O que trava em quem decide: ganho, emoção e crença"))
    H.append(p("O ganho secundário não é culpa: é o motivo pelo qual a mudança não se sustenta, e em negócios costuma ser evitar uma conversa difícil, manter uma identidade (“o fundador”) ou uma lealdade (ao pai, ao sócio antigo). O G62 entra antes de toda decisão importante. O sabotador (G127, Parte XII) e a família de crença (G10) são nomeados, não tratados: este manual registra, dá um passo pequeno e, se o padrão voltar em três sessões, encaminha ao atendimento pessoal pelo Manual de Radiestesia Terapêutica, onde a emoção presa é liberada."))
    H.append(chart_group(["G62", "G10"]))
    H.append(h2("blo-contratos", "Votos, promessas, pactos e contratos energéticos"))
    H.append(p("Voto de pobreza, voto de não ter sucesso, promessa a pai ou mãe de nunca vender a empresa, lealdade a um sócio morto, contrato de sofrimento: a lista do G59 é a mesma do manual terapêutico, lida aqui para a prosperidade e para a sucessão. A ação é dita em voz alta, em primeira pessoa, com a data de hoje; depois se retesta e se vai ao G62."))
    H.append(chart("G59"))
    H.append(h2("blo-protecao", "Limites e proteção, sem agir contra ninguém"))
    H.append(p("Inveja, ciúme, concorrente que “olha”, cliente que drena: a resposta deste manual é a do Psicoprotetor dos Servranx, com o seu veto literal: “nunca tente devolver ao remetente: lei do contragolpe”. O G67 escolhe o selamento do espaço e a proteção da pessoa; o G119 e o G28 dizem se a energia é de fora; a devolutiva nunca nomeia ninguém. Proteção é hábito de fechamento, não arma."))
    H.append(chart("G67"))
    H.append(end())
    return H

def part_espacos():
    H = []
    H.append(h1("esp", "Espaço, ponto comercial, terreno e empreendimento imobiliário", "Parte IX · Espaços e imóveis", brk=False))
    H.append(p("O lugar é o objeto em que a radiestesia tem mais tradição e mais oferta de mercado: geobiólogos europeus vendem perícia de terreno antes da construção, com planta anotada, datada e assinada; o acervo brasileiro traz o método da planta quadriculada com régua de Bovis e o histórico do terreno. Esta Parte percorre os três objetos: o imóvel da empresa (cômodo a cômodo, de quem é a energia, fontes, baguá, limpeza), o ponto comercial a escolher (G120) e o terreno e o empreendimento imobiliário (G116 e G117), do primeiro lote ao pós-ocupação. O que a radiestesia entrega é complemento declarado: sondagem geotécnica, laudo ambiental, medição de radônio e de campos por instrumento e análise jurídica da matrícula ficam com quem os assina."))
    H.append(box("alerta", "O que o laudo radiestésico não é", "Não é laudo geotécnico, ambiental, estrutural, de potabilidade nem jurídico. Redes Hartmann e Curry não são detectáveis por instrumento, e a literatura controlada não as confirma; radônio e campos eletromagnéticos são reais e mensuráveis, e são medidos por aparelho, não por pêndulo. Todo laudo deste manual leva no cabeçalho: “análise radiestésica complementar; não substitui sondagem geotécnica, laudo ambiental, medição de radônio e de campos eletromagnéticos por instrumento, nem a análise jurídica da matrícula”."))
    H.append(h2("esp-ponto", "Ponto comercial: escolher e avaliar"))
    H.append(steps([
        "Pontos candidatos numerados no caderno (G109), com endereço e foto da fachada como testemunho.",
        "Energia de cada um no G3: " + pergunta("Qual a vitalidade do ponto [n], em unidades Bovis?") + ". Abaixo de 6.500, não alugar sem harmonizar antes; abaixo de 4.500, não.",
        "Critérios no G120 com pesos: " + pergunta("Qual critério pesa mais nesta escolha?") + "; percentual de cada critério por ponto no G2. Fluxo, visibilidade e concorrência são contados e mapeados: o dado vale mais que o pêndulo, que só confirma.",
        "Memória do ponto no G82 (negócio anterior) e fontes no G66; afinidade com o público no G109 com os públicos numerados.",
        "G84 para o ponto indicado, com duas formulações; G85; o contrato de locação no G112 e com o advogado.",
        "Antes de abrir: harmonização completa (abaixo), caiação se houver memória, consagração do imóvel; remedir G3 depois.",
    ]))
    H.append(chart("G120"))
    H.append(h2("esp-medir", "O imóvel da empresa, cômodo a cômodo"))
    H.append(steps([
        "Planta ou croqui do imóvel orientado com a bússola; endereço escrito em cima. Onde quem decide de fato trabalha, no G83.",
        "Cômodo a cômodo no G69: giro no alvo, percentual na régua. Ordem: posto de quem decide e caixa primeiro; depois entrada e recepção, que recebem o cliente; por fim estoque e copa.",
        "Nos cômodos abaixo de 70: de quem é a energia no G82 (dono, sócio ou funcionário como papéis, cliente, negócio anterior, vizinho, o lugar); a fonte no G66.",
        "Quando a queixa é de vida do negócio (vendas, sócios, clientes) e não de sintoma: baguá da planta no G70, a partir da porta de entrada.",
        "Limpar e harmonizar (abaixo); proteger (G67); remedir G3 e G69 em 7 dias.",
    ]))
    H.append(chart_group(["G69", "G83"]))
    H.append(chart_group(["G82", "G70"]))
    H.append(h2("esp-planta", "Planta quadriculada: terreno e imóvel com régua de Bovis"))
    H.append(p("Método do acervo de referência, aqui transcrito como está: anda-se primeiro no terreno com a régua de Bovis; se houver água subterrânea, a régua acusa queda de energia. Consegue-se a planta do local com o norte magnético marcado; potencializa-se a planta como testemunho por vinte minutos; traça-se um quadriculado com quadrados de 2,5 cm; em cada cruzamento mede-se a energia com o biômetro de Bovis (G3); traçam-se as curvas de isofrequência; sobre a planta anotam-se a malha de Hartmann, a rede Curry e os veios, varrendo em linhas paralelas norte-sul e leste-oeste e depois em diagonais, marcando cada reação e ligando as marcas. Com os geobiólogos europeus este manual adota três regras: em terreno nu a rede Hartmann é pouco confiável, porque se desloca com massas metálicas, e se confirma depois de construído; a perícia leva três a quatro horas por até 400 m²; a entrega é a planta anotada, datada e assinada, mais relatório."))
    H.append(steps([
        "Bovis geral do terreno ou do imóvel no G3. Abaixo de 4.500: zona a evitar; abaixo de 6.500: harmonizar ou implantar fora da zona baixa.",
        "Quadrícula e Bovis por cruzamento; curvas de isofrequência; as zonas abaixo de 6.500 marcadas em cor.",
        "Fontes na lista G66 por zona: água, falha, rede, radônio (medir por aparelho), memória, objetos.",
        "Implantação: dormitórios, salas de decisão, postos de trabalho e caixa fora dos nós e dos veios; a sala de decisão na zona de maior valor; vibração do local no G4 dividido por dois como segunda leitura.",
        "Correção só onde não se pode mover: isolantes, geopuntura, dispositivos; remedir em 7 dias.",
        "Laudo com o cabeçalho fixo e a lista do que fica com engenharia, laudo ambiental, medição por instrumento e jurídico (" + go("esp-laudo", "abaixo") + ").",
    ]))
    H.append(chart("G66"))
    H.append(h2("esp-limpar", "Limpar, harmonizar e proteger o espaço"))
    H.append(p("A ordem vai do mais físico ao mais sutil: janelas, limpeza e descarte, sal, defumação, caiação para memória de parede, mudar móveis e cores; depois comandos e gráficos com o endereço da empresa em cima; depois proteção (G67). Emissores de prosperidade com testemunho da empresa estão na " + go("fin-emissores", "Parte X") + ". Orientação eletromagnética (quadro de luz longe do posto, Wi-Fi desligado à noite, medição de radônio e de campos) é a primeira a dar, porque tem evidência independente."))
    H.append(chart("G71"))
    H.append(h2("esp-terreno", "Terreno para empreender"))
    H.append(p("O investidor chega com dois ou três lotes. Cada um recebe um número (G109), uma medida de energia (G3) e doze critérios (G116) com pesos, como no G107. Viabilidade legal, geotécnica, ambiental e financeira ficam fora de propósito: são da engenharia, do advogado e do consultor, e o critério “risco” do leque não as substitui. O histórico do terreno (aterro, hospital, cemitério, incêndio, tragédia), que as formações brasileiras ensinam a evitar, é documentado antes da compra e tratado com limpeza e consagração se a compra for adiante."))
    H.append(steps([
        "Lotes numerados; testemunho de cada um (matrícula ou planta com norte, endereço). Trio de permissão para " + pergunta("a decisão de [empreendedor] sobre o terreno [n] para [empreendimento]") + "; autoauditoria.",
        "G3 de cada lote; abaixo de 6.500, pesa contra; abaixo de 4.500, não.",
        "Pesos no G116: " + pergunta("Qual critério pesa mais nesta escolha?") + "; percentual de cada critério por lote no G2; matriz na ficha.",
        "No lote mais forte: planta quadriculada (acima), histórico documentado, afinidade com o público e com o empreendedor.",
        "G84 para comprar, com formulações convergentes; G85; G87 só se a data importar. Sócios e investidores do empreendimento pela " + go("soc", "Parte IV") + ".",
        "Laudo complementar entregue antes da assinatura, nunca no lugar da sondagem.",
    ]))
    H.append(chart("G116"))
    H.append(h2("esp-empreendimento", "O empreendimento fase a fase"))
    H.append(table(["Fase", "O que o pêndulo faz", "Gráficos", "O que fica com outros profissionais"], [
        ["1 Prospecção de terrenos", "lotes numerados; energia de cada um; afinidade com público e empreendedor; o que o terreno carrega", "G109, G3, G2, G66, G82", "corretor, análise de mercado, zoneamento"],
        ["2 Avaliação do lote", "planta quadriculada; água, falhas e redes; zonas para implantar; doze critérios", "G3, G66, G116, G70", "sondagem, laudo ambiental, radônio e campos por instrumento, jurídico"],
        ["3 Aquisição e sócios", "decisão de comprar; momento; investidores e parceiros", "G84, G85, G87, G106, G118", "contrato, financiamento, estrutura societária"],
        ["4 Projeto e implantação", "torres, acessos, dormitórios e postos fora dos nós; baguá do projeto; afinidade de cada tipologia com o público", "G70, G109, G2", "arquitetura, engenharia, aprovação"],
        ["5 Obra", "empreiteiros e fornecedores como relação comercial; contratos; clima da equipe de obra como conjunto; peso da fase", "G106, G112, G91, G117", "gestão de obra, segurança, qualidade"],
        ["6 Lançamento e vendas", "momento do lançamento; onde está o peso quando as vendas não andam; afinidade do produto com o público; estande e decorado harmonizados", "G85, G87, G117, G2, G71", "preço, marketing, corretagem"],
        ["7 Entrega e pós-ocupação", "limpeza e harmonização das áreas comuns; memória da obra; indicação de unidade para um cliente só com pedido dele", "G71, G66, G109", "assistência técnica, condomínio"],
    ], cls="small"))
    H.append(p("O G117 é o G92 do empreendimento: a cada marco, " + pergunta("Onde está o peso do empreendimento hoje?") + " e o percentual de cada área no G2. Vendas que não andam costumam apontar “projeto” (a tipologia não conversa com o público) ou “comunicação”; o pêndulo ordena a investigação, e o dado de mercado confirma."))
    H.append(chart("G117"))
    H.append(h2("esp-laudo", "O laudo complementar"))
    H.append(table(["Seção do laudo", "Conteúdo"], [
        ["Cabeçalho fixo", "“Análise radiestésica complementar. Não substitui sondagem geotécnica, laudo ambiental, medição de radônio e de campos eletromagnéticos por instrumento, nem a análise jurídica da matrícula.”"],
        ["Identificação", "endereço ou matrícula, planta com norte, data, condições (tempo seco), quem mediu"],
        ["Medidas", "Bovis geral (G3); Bovis por quadrícula com curvas de isofrequência; vibração do local (G4 ÷ 2)"],
        ["Zonas", "água, falhas, redes e nós desenhados na planta, com a ressalva de que a rede Hartmann em terreno nu se confirma depois de construído"],
        ["Fontes e memória", "itens do G66; histórico documentado do terreno ou do imóvel"],
        ["Critérios", "G116 ou G120 com pesos e percentuais, em matriz"],
        ["Recomendações", "implantação fora das zonas baixas; correções só onde não se pode mover; limpeza e consagração se houver memória"],
        ["O que fica com outros", "lista nominal: sondagem, laudo ambiental de passivos, radônio e campos por instrumento, estrutura, potabilidade, jurídico"],
        ["Assinatura e remedida", "planta anotada, datada e assinada; remedida prevista em 7 dias após correções e após a obra"],
    ], cls="small"))
    H.append(end())
    return H

def part_financas():
    H = []
    H.append(h1("fin", "Finanças e prosperidade da empresa", "Parte X · Finanças", brk=False))
    H.append(p("Dinheiro chega ao atendimento de duas formas: a pessoa que sente bloqueio de prosperidade e a empresa cujo caixa não flui. A primeira usa as duas listas de bloqueios de referência (os 22 bloqueios da prosperidade e os 15 problemas do Mapa de Atendimento, cada um com uma linha de devolutiva) na pessoa de quem decide ou do responsável pelas finanças. A segunda usa as três perguntas de percentual do G92 (entrada, saída, bloqueio) e os emissores de prosperidade com testemunho da empresa, no uso de loja: testemunho a lápis, desimpregnado antes, renovado a cada 14 dias. Previsão de faturamento, bolsa e investimento financeiro não se pendulam."))
    H.append(h2("fin-bloqueio", "Bloqueio de prosperidade de quem decide"))
    H.append(steps([
        "Área no G24 (dinheiro ou trabalho) e grau no G2: " + pergunta("Qual o grau de equilíbrio da área financeira de [nome], de 0 a 100?") + ".",
        "Finanças da empresa no G92 setor 8, em três perguntas de percentual: " + pergunta("Qual o percentual de saúde da entrada de dinheiro? Da saída? Há bloqueio?") + ".",
        "Bloqueio na lista G94, por bissecção, na pessoa do responsável: " + pergunta("O bloqueio principal está na primeira lista?") + ", depois linha a linha; " + pergunta("Há um segundo bloqueio?") + ".",
        "Cada item aponta onde tratar: crença (G10), emoção (G127), interferência (G119, G28), linhagem e sucessão (G59), ambiente (Parte IX), relação (G91), hábito (G24). Confirmar no G62 se há ganho em manter.",
        "Devolutiva com a linha do Mapa de Atendimento correspondente (não merecimento, procrastinação, não soltar, absorve conselhos invejosos), dita como tendência, com uma orientação prática pequena: preço, proposta, cobrança, agenda.",
        "Depois: emissor de prosperidade escolhido abaixo, com testemunho da pessoa ou da empresa, renovado a cada 14 dias; remedir o G92 setor 8 no trimestre.",
    ]))
    H.append(chart("G94"))
    H.append(h2("fin-emissores", "Emissores de prosperidade com testemunho da empresa"))
    H.append(p("Os gráficos abaixo são os de referência do mercado luso-brasileiro (não estão nos Servranx). Regra única: testemunho da própria empresa ou de quem pediu, a lápis, desimpregnado antes; nunca o nome de um cliente, de um concorrente ou de um fornecedor; tempo medido no G2 em minutos ou dias; renovação a cada 14 dias; o gráfico é retirado quando o objetivo é atingido. Onde colocar, segundo a tradição: na gaveta do caixa, junto da agenda de clientes, no computador onde se fecham negócios. Nenhum deles substitui preço certo, cobrança e venda."))
    H.append(table(["Gráfico de referência", "Para quê", "Regra e tempo"], [
        ["Prosperador", "prosperidade geral; “atraindo clientes, liberando dinheiro parado”", "testemunho dentro, gráfico ao norte, pelo menos 30 minutos; renovar a cada 14 dias"],
        ["Saúde Financeira", "harmonizar a área financeira depois que a parte prática já está quase adequada", "precedido de pesquisa radiestésica; testemunho da empresa sobre o gráfico, ou sobre a mesa de trabalho"],
        ["Quadrata", "objetivos materiais; novas oportunidades e clientes", "testemunho da pessoa ou da empresa"],
        ["Turbilhão com Júpiter", "expansão, fechamento de contratos, aumento de vendas", "ativar na quinta-feira, ao norte, por 24 horas"],
        ["Desembaraçador em sentido horário", "atrair e potencializar pedidos", "giro horário"],
        ["Desembaraçador em sentido anti-horário", "abrir caminhos; afastar falta de sorte e crenças limitantes sobre dinheiro", "giro anti-horário; nunca com testemunho de terceiro"],
        ["Harmonia", "relação com clientes e entre a equipe, como conjunto", "testemunho da empresa; até 21 dias; remedir a sintonia"],
        ["SCAP, Nove Círculos", "proteção do imóvel e do caixa", "SCAP não emite: energizar depois; rever a cada 1 a 3 meses"],
    ], cls="small"))
    H.append(end())
    return H

def part_pessoa():
    H = []
    H.append(h1("pes", "O empreendedor como pessoa", "Parte XI · A pessoa", brk=False))
    H.append(p("Quem decide é a única pessoa que este manual pendula como pessoa, e só com pedido dela. Mede-se pouco e com propósito: o custo do negócio na vida (G24 cruzado com a Roda da Vida), o que pesa no trabalho (G95, Parte VII), o bloqueio de prosperidade (G94, Parte X), o ganho, a emoção e a crença (Parte VIII). Chakras, limpeza energética, causas e harmonização ficam com o Manual de Radiestesia Terapêutica: aqui se registra e se encaminha."))
    H.append(h2("pes-roda", "Roda da Vida e áreas da vida"))
    H.append(p("A pessoa preenche a Roda da Vida (0 a 10 por área, na ficha) antes de qualquer medida; o operador mede o G24 depois, sem ver a roda; a conversa é sobre as diferenças. A área que a pessoa pontuou alto e o pêndulo mediu baixo (ou o inverso) é o tema; o pêndulo não decreta. Em negócios, a pergunta mais útil é a terceira: " + pergunta("Quanto este projeto vai custar à área [n]?") + ", que vira o critério 9 do G107."))
    H.append(chart("G24"))
    H.append(h2("pes-remissao", "Quando a pessoa precisa de mais do que este manual"))
    H.append(table(["Sinal", "Para onde"], [
        ["Carga de interferência ou de emoção acima de 10 que volta em três sessões", "atendimento pessoal pelo Manual de Radiestesia Terapêutica: triagem, chakras, causas, harmonização"],
        ["Insônia, pânico, exaustão, sofrimento", "médico e psicólogo; o pêndulo registra e encaminha"],
        ["Voto, pacto ou lealdade que não se desfaz com a ação do G59", "manual terapêutico, Nível 4 e limpeza de pessoa"],
        ["Ambiente da casa pesando no trabalho", "Parte IX deste manual aplicada à casa, ou a Parte de espaços do manual terapêutico"],
    ], cls="small"))
    H.append(end())
    return H

def part_coaching():
    H = []
    H.append(h1("coach", "Coaching empresarial com pêndulo: rodas, foco, metas e desbloqueio", "Parte XII · Coaching", brk=False))
    H.append(p("O coach empresarial trabalha com rodas de 0 a 10, matriz de prioridades, valores, metas bem formuladas, sabotadores e planos de ação. Esta Parte põe o pêndulo dentro dessas ferramentas: a pessoa dá a nota dela, o pêndulo mede o campo, e a diferença entre as duas é o que se conversa. Três leituras por item, sempre nesta ordem: a nota da pessoa, a medida, a diferença. O pêndulo não substitui a pergunta do coach; obriga a pessoa a escrever antes e devolve o que ela sente e ainda não disse. Fecha com o protocolo de desbloqueio para o que está agarrado: nomear, localizar o nó, medir a carga, escolher a ação, dar o passo pequeno, datar, remedir."))
    H.append(box("variacao", "A regra das três leituras", "<b>Nota da pessoa</b>: ela preenche a roda ou dá a nota antes, sem o operador olhar. <b>Medida</b>: o pêndulo lê a mesma área na roda pendulável ou na régua. <b>Diferença</b>: três pontos ou mais entre as duas é o tema da sessão; o pêndulo não decreta quem está certo. Nas rodas, a área que “se subir, puxa as outras” é o foco do trimestre; no máximo três itens ficam em foco ao mesmo tempo."))
    H.append(h2("coach-rodas", "Rodas de 1 a 10: a vida de quem decide, o negócio e o projeto"))
    H.append(steps([
        "A pessoa preenche a Roda da Vida na ficha (0 a 10 por área) e, se for o caso, a roda do negócio ou do projeto, sem o operador olhar.",
        "Testemunho e permissão; autoauditoria no G2. Pêndulo no centro da roda pendulável: uma área por vez, " + pergunta("Qual a nota da área [n] de [nome] hoje, de 1 a 10?") + ", deslizando do centro para a borda; o anel em que a oscilação vira giro é a nota. Quem preferir usa a régua G124.",
        "Comparar as duas rodas: as diferenças de 3 ou mais são o tema. " + pergunta("Qual área, se subir, puxa as outras?") + " define o foco do trimestre.",
        "Roda do negócio (G122) com o testemunho da empresa; roda do projeto com o projeto numerado: " + pergunta("Para o projeto [n], qual área está mais fraca?") + " vira critério no G107 e meta no G126.",
        "Cruzar com o G92: a roda diz desempenho (nota), o G92 diz peso energético. Área com nota alta e peso alto é a que mais cansa; área com nota baixa e peso baixo é a que ninguém está olhando.",
        "Devolutiva: uma área de foco, uma meta pequena por área crítica, revisão da roda a cada trimestre; a série de rodas é o histórico do coaching.",
    ]))
    H.append(chart("G121"))
    H.append(chart("G122"))
    H.append(chart("G124"))
    H.append(h2("coach-foco", "Foco e prioridade: em que pôr energia"))
    H.append(p("“No que devo focar mais?” é a pergunta de toda sessão de coaching, e o pêndulo responde em dois passos: a nota de energia e impacto de cada item (G124) e o momento (G85), cruzados na matriz de foco (G123). Entram na lista atividades, projetos, áreas da roda, clientes, qualquer coisa escrita e numerada. Saem quatro listas: foco agora (no máximo três), planejar e datar, delegar ou simplificar, soltar. Soltar é o quadrante que mais libera energia e o que a pessoa mais resiste a preencher."))
    H.append(steps([
        "Itens escritos e numerados no caderno (até oito no G109, até doze no G110).",
        "Para cada item: " + pergunta("Qual a energia e o impacto de [item] para [nome ou empresa], de 0 a 10?") + " no G124, e " + pergunta("É agora?") + " no G85.",
        "Quadrante no G123, com o pêndulo no centro confirmando: " + pergunta("Em que quadrante cai [item] hoje?") + ".",
        pergunta("Qual item, se feito agora, puxa os outros?") + ": é o primeiro da semana. " + pergunta("O que sair da lista libera mais energia?") + ": é o que se solta com data de revisão.",
        "Mais de três itens em “foco agora”: ordem pelo G109 (" + pergunta("Qual vem primeiro?") + "). Delegar é função a contratar ou tarefa a encolher, nunca pessoa por pêndulo.",
        "Registro na ficha de foco; revisão em 30 dias: o que de fato foi feito e o que voltou para a lista.",
    ]))
    H.append(chart("G123"))
    H.append(h2("coach-metas", "Valores e metas: do desejo à decisão"))
    H.append(p("Uma meta contra o valor dominante da pessoa não se sustenta, por mais favorável que meça no G84. Por isso os valores (G125) vêm antes da meta, e a meta passa por duas listas (G126): o que falta na formulação e o que a segura depois de escrita. O roteiro segue a sequência clássica do coaching, meta, realidade, opções e vontade, com um gráfico em cada passo."))
    H.append(steps([
        "Valores: " + pergunta("Qual valor mais guia [nome] hoje?") + " no G125, e o segundo e o terceiro. Escrever os três no caderno; toda meta e sociedade é checada contra eles.",
        "Meta escrita em uma frase, no positivo, com prazo. " + pergunta("O que falta nesta meta?") + " na primeira lista do G126, por bissecção; reescrever até a lista não acusar nada.",
        "Realidade: a nota de hoje na roda (G121 ou G122) e a taxa de base (quantas metas desse tipo deram certo antes).",
        "Opções: até quatro caminhos no G86, ou oito no G109; percentual de cada um no G2; pré-mortem do mais forte (" + go("proj-premortem", "Parte VI") + ").",
        "Vontade: " + pergunta("Qual o comprometimento de [nome] com esta meta, de 0 a 10?") + " no G124. Abaixo de 7, " + pergunta("O que segura esta meta?") + " na segunda lista do G126: medo, ganho, crença, meta alheia, recurso, habilidade, apoio.",
        "Primeiro passo pequeno, data no G85 e G87, quem precisa saber. Revisão em 30 e 90 dias; a meta que não andou volta ao G126 e ao protocolo de desbloqueio.",
    ]))
    H.append(chart("G125"))
    H.append(chart("G126"))
    H.append(h2("coach-sabotadores", "Sabotadores e padrões"))
    H.append(p("O coaching de inteligência positiva nomeia dez padrões automáticos que assumem o comando sob pressão: o Juiz, presente em todos, e nove cúmplices (controlador, perfeccionista, agradador, hiper-realizador, vítima, evitador, inquieto, hiper-vigilante, hiper-racional). Este manual os usa como leque, só na própria pessoa e com consentimento, para dar nome ao padrão na hora em que a trava aparece; o tratamento é a conversa, a crença (G10) e o ganho (G62). Nunca se rotula um sócio, um funcionário ou um cliente com este gráfico."))
    H.append(chart("G127"))
    H.append(h2("coach-desbloqueio", "Protocolo de desbloqueio: o que está agarrado"))
    H.append(p("Projeto parado, venda que não fecha, cobrança que não sai, decisão adiada há meses, conflito que se repete, vaga aberta, lançamento que não acontece, dívida, licença presa, hábito que a pessoa faz e desfaz. O protocolo tem oito passos e não pula nenhum: o nome do que está agarrado e a carga; onde está o nó; o ganho em manter; a crença, a emoção ou o sabotador por trás; a ação que desagarra; o passo pequeno; a data; a remedida. A tradição radiestésica entra em dois pontos, a limpeza e a proteção quando o nó é do espaço ou energético, e a medida da carga antes e depois; o resto é conversa e ação."))
    H.append(steps([
        "<b>Nomear.</b> " + pergunta("O que está agarrado em [empresa ou nome] hoje?") + " no G128; " + pergunta("Qual a carga disso, de 0 a 100?") + " no G2. Acima de 30, nada se decide antes de desagarrar. " + pergunta("Há uma segunda coisa agarrada?") + ".",
        "<b>Localizar o nó.</b> " + pergunta("Onde está o nó?") + " no G119 (em mim, numa relação, na equipe, no espaço, na memória, num contrato energético, no coletivo, em nenhum lugar: nos números). Negociação travada: G113; decisão adiada: G111.",
        "<b>O ganho em manter.</b> " + pergunta("Há um ganho em manter isto agarrado?") + " no G62. Quase sempre há, e quase sempre é evitar uma conversa.",
        "<b>O que está por trás.</b> Crença no G10, emoção no G127, sabotador no G127, voto ou lealdade no G59. Nomear, não tratar: um passo pequeno nesta semana; se voltar em três sessões, atendimento pessoal.",
        "<b>A ação que desagarra.</b> " + pergunta("Qual ação desagarra [item] primeiro?") + " no G129: conversar, decidir, delegar, soltar, pedir ajuda, reduzir, datar, mudar o lugar, limpar e proteger, aprender, descansar. Se for limpar e proteger: G71 e G67 pela Parte IX.",
        "<b>O passo pequeno.</b> " + pergunta("Qual o primeiro passo pequeno dessa ação?") + ": algo que cabe em uma hora e nesta semana. A pessoa diz; o pêndulo confirma; escreve-se no caderno.",
        "<b>A data.</b> G85 para o momento, G87 se o dia importar; quem precisa saber.",
        "<b>Remedir.</b> Carga no G2 em 7 dias e em 30; abaixo de 10, desagarrado; se não caiu, a ação foi a errada: voltar ao G129 com a primeira ação riscada.",
    ]))
    H.append(chart("G128"))
    H.append(chart("G129"))
    H.append(h3("Formas de agir, por tipo de trava"))
    H.append(table(["O que está agarrado", "Onde costuma estar o nó", "Ações que mais desagarram", "O que fica com outros"], [
        ["Projeto parado, lançamento", "capacidade, escopo, momento", "reduzir o escopo; delegar função; datar e comunicar; decidir", "gestão de projeto"],
        ["Venda que não fecha, cliente, fornecedor", "outra parte, abordagem, informação", "conversar (contato, momento, comportamento no G113); pedir referência; soltar", "comercial"],
        ["Cobrança, dívida, caixa", "medo, merecimento, ganho", "conversar (cobrar); decidir; pedir ajuda ao contador; reduzir", "contador, advogado"],
        ["Decisão adiada", "falta de dado, medo, valores, lealdade", "decidir (G84); conversar; datar", "quem tem o dado"],
        ["Conflito com sócio ou equipe", "comunicação, papéis, limites", "conversar; pedir mediação; limites (G67)", "mediador, acordo de sócios"],
        ["Contratação ou vaga", "função mal definida, momento", "delegar ou contratar função; reduzir; datar", "RH, entrevista, referências"],
        ["Processo, licença, burocracia", "terceiro, prazo", "datar e comunicar; pedir ajuda; descansar e voltar", "despachante, advogado"],
        ["Hábito ou rotina", "sabotador, ganho, energia", "descansar; aprender; passo pequeno; soltar", "coach, terapeuta"],
        ["Espaço ou memória do local", "ambiente", "mudar o lugar; limpar e proteger", "Parte IX"],
    ], cls="small"))
    H.append(h2("coach-casos", "Casos resolvidos"))
    B = []
    B.append(h3("Caso 8 · A venda que não fecha há três meses"))
    B.append(p("Uma consultoria tem uma proposta parada há três meses com um cliente grande. G128: “venda que não fecha”; carga no G2: 45. G119: “em mim”. G113: “ganho em não fechar”. G62: “evitar responsabilidade” (a entrega assusta). G127: “evitador” e “perfeccionista”. G129: “reduzir o escopo” primeiro, “conversar” segundo. Passo pequeno: reescrever a proposta em uma fase menor e ligar para o cliente na quinta (G87). Carga em 7 dias: 15; a venda fechou na fase pequena em três semanas. A devolutiva não falou em “energia da venda”: falou do medo da entrega, que a pessoa já sabia."))
    B.append(h3("Caso 9 · O projeto que todo trimestre volta para a lista"))
    B.append(p("O dono de uma indústria tem um projeto de novo produto que entra e sai do plano há dois anos. Roda do negócio (G122): inovação 3, processos 4, resultado 7. Matriz de foco para seis itens: o produto novo caiu em “planejar e datar” com energia 8; dois itens de rotina caíram em “soltar”. G128: “projeto parado”; carga 60. G119: “na equipe”; G91: “sobrecarga”. G126 para a meta do produto: faltava “primeiro passo definido” e segurava “falta recurso: equipe”. G129: “delegar ou contratar função”. Decisão da função (não da pessoa) no G107 adaptado e no G84: “sim”, grau 74; momento: em semanas. O projeto ganhou um responsável e uma data; os dois itens soltos liberaram as horas. Remedida em 30 dias: carga 20; roda: inovação 5."))
    B.append(h3("Caso 10 · A sucessão que ninguém decide"))
    B.append(p("Pai e filha numa empresa familiar: a passagem de comando está “agarrada” há anos. Quem pede é a filha. G128: “decisão adiada”; carga 70. G119: “contrato energético”; G59: “promessa a pai ou mãe” (não mudar o que o pai construiu). G62: “lealdade à família”. G125: valor dominante dela, “realização”; o que ela acha que a empresa pede, “segurança”. G111: “lealdade a alguém” e “medo do julgamento”. G129: “conversar: dizer o não dito”. Passo pequeno: uma conversa só sobre o que ela quer manter da obra do pai, antes de qualquer conversa sobre mudar. Data no G85: em dias. O pai só seria pendulado se pedisse; não pediu, e não precisou: a carga caiu a 25 em 30 dias depois de duas conversas, e a decisão de sucessão foi ao G84 com os dois na sala, pela Parte IV."))
    H.append(cols3("".join(B)))
    H.append(h3("Sessão de coaching com pêndulo, em 60 minutos"))
    H.append(table(["Minutos", "Passo", "Gráficos"], [
        ["0 a 5", "abertura: permissão, autoauditoria, a pergunta da sessão escrita", "G1, G2"],
        ["5 a 15", "a roda que a pessoa trouxe preenchida; a medida; as diferenças", "G121 ou G122, G124"],
        ["15 a 25", "foco: itens numerados, energia, momento, quadrantes", "G124, G85, G123"],
        ["25 a 40", "a meta do foco: valores, o que falta, comprometimento; ou o desbloqueio do que está agarrado", "G125, G126, G128, G119, G62, G129"],
        ["40 a 50", "decisão e data do primeiro passo", "G84, G85, G87"],
        ["50 a 60", "devolutiva como tendência; registro na ficha; o que a pessoa leva escrito; data da próxima roda", "diário de decisões"],
    ], cls="small"))
    H.append(end())
    return H

def part_estrategia():
    H = []
    H.append(h1("estr", "Estratégia, carteira, negociação e relações-chave", "Parte XIII · Estratégia", brk=False))
    H.append(p("Esta Parte põe o pêndulo dentro das ferramentas de planejamento empresarial e de negociação: a carteira de projetos (o que gera caixa rápido, o que gera prosperidade duradoura, onde dedicar o tempo), o funil de vendas, a análise SWOT, a preparação de uma apresentação (o que ela pede para ser entendida), o mapa de expectativas de quem vai decidir, o mapa de atores de um grupo, a relação com investidores e a roda do líder. Abre com um seletor: diante de um projeto ou de uma sessão, o pêndulo diz qual ferramenta usar primeiro. Em tudo, a regra é a mesma do manual inteiro: mede-se o nosso lado, a nossa apresentação, a nossa estratégia de relação; não se lê a pessoa do outro e não se emite sobre ela."))
    H.append(box("variacao", "O que se mede e o que não se mede nesta Parte", "<b>Mede</b>: a carteira e o tempo; em que etapa o funil trava; onde está a chave da estratégia; o que a nossa apresentação pede; o que a outra parte precisa ouvir para dizer sim e para continuar; o poder e o interesse de cada ator no projeto, como estratégia de relação; as competências do líder. <b>Não mede</b>: o caráter, a intenção ou a vida de quem está do outro lado; o que ele vai decidir; o que o mercado vai fazer. Com o cliente de coaching, e só com o consentimento dele, a própria pessoa pode ser lida (canal preferido, roda do líder)."))
    H.append(h2("estr-seletor", "Qual ferramenta este projeto pede"))
    H.append(steps([
        "Projeto, situação ou pergunta da sessão escrita em uma linha; testemunho; autoauditoria.",
        pergunta("Qual ferramenta este projeto pede primeiro?") + " no G134; " + pergunta("Qual a segunda?") + ". Duas por sessão bastam.",
        "Abrir o roteiro da ferramenta nesta Parte ou na " + go("coach", "Parte XII") + "; registrar qual foi usada e o que saiu dela.",
    ]))
    H.append(chart("G134"))
    H.append(table(["Situação que o empresário traz", "Ferramenta", "Gráficos"], [
        ["“Tenho vários projetos e não sei onde pôr o tempo”", "carteira caixa × prosperidade; matriz de foco", "G130, G124, G85, G2; G123"],
        ["“Preciso de dinheiro rápido”", "funil de vendas; carteira (fôlegos); preço entre opções", "G133, G130, G109"],
        ["“Quero construir algo que dure”", "carteira (sementes); roda do negócio; SWOT", "G130, G122, G135"],
        ["“Vou apresentar para alguém ou para um grupo”", "abordagem; expectativas; mapa de atores", "G131, G132, G136"],
        ["“Preciso convencer um investidor, um cliente, um sócio”", "expectativas; compatibilidade para o objetivo; sociedade; proposta", "G132, G118, G106, G112"],
        ["“A venda não fecha, a proposta não anda”", "funil; onde trava; desbloqueio", "G133, G113, G128, G129"],
        ["“Não sei o que a empresa tem de forte e de fraco”", "SWOT; roda do negócio; modelo de negócio", "G135, G122, G114"],
        ["“Preciso crescer como líder”", "roda do líder; talento; sabotador", "G137, G101, G127"],
        ["“Tenho uma dívida e preciso de prazo”", "abrir caminhos: o que se faz; expectativa do credor; proposta de prazo", "G132, G109, G84, G85, G67"],
    ], cls="small"))
    H.append(h2("estr-carteira", "Carteira de projetos: caixa rápido, prosperidade e tempo"))
    H.append(p("“O que vai gerar dinheiro mais rápido? O que vai gerar mais prosperidade? Em que dedicar o tempo?” são três perguntas, e a carteira responde às três de uma vez. Cada projeto numerado recebe o momento do primeiro real (G85: agora, dias e semanas são rápido; meses e anos são lento) e uma nota de prosperidade duradoura (G124), e cai num dos quatro quadrantes do G130: motor, semente, fôlego ou dreno. Depois o pêndulo distribui o tempo: o percentual de cada projeto no mês, no G2, com a soma perto de 100. Uma carteira saudável tem um motor ou uma semente com horas protegidas e um ou dois fôlegos que pagam as contas; os drenos saem."))
    H.append(steps([
        "Projetos, produtos ou frentes numerados no caderno (até oito no G109, até doze no G110). Trio de permissão; autoauditoria: dinheiro é o tema que mais contamina.",
        "Para cada projeto: " + pergunta("Quando chega o primeiro real do projeto [n]?") + " no G85 e " + pergunta("Quanto o projeto [n] constrói de prosperidade duradoura, de 0 a 10?") + " no G124.",
        "Quadrante no G130 com o pêndulo no centro: " + pergunta("Em que quadrante cai o projeto [n] hoje?") + ". Registrar na ficha de carteira.",
        pergunta("Qual projeto, se andar, puxa os outros?") + " e, para o caixa, " + pergunta("Qual cliente, produto ou canal traz mais dinheiro com menos esforço?") + " nos itens numerados do G109: é a leitura de Pareto, confirmada com os números.",
        "Tempo: " + pergunta("Qual percentual do tempo de [nome] deve ir para o projeto [n] neste mês?") + " no G2, projeto por projeto. Soma acima de 110: o dreno sai e o fôlego encolhe; a matriz de foco (G123) distribui a semana.",
        "Devolutiva: a carteira em uma página (motor, sementes, fôlegos, o que sai), as horas protegidas e a data de revisão em 90 dias; números com o contador antes de qualquer corte.",
    ]))
    H.append(chart("G130"))
    H.append(h2("estr-swot", "SWOT com pêndulo: onde está a chave"))
    H.append(p("A pessoa escreve até três forças, três fraquezas, três oportunidades e três ameaças, numeradas de 1 a 12. O leque G135 diz onde está a chave da estratégia hoje (uma força a usar mais, uma fraqueza a corrigir, uma oportunidade a pegar agora, uma ameaça a proteger) e também o que ignorar: a força que drena, a fraqueza que não vale corrigir, a oportunidade que fica para depois, a ameaça que é medo e não risco. O item exato sai do G110 com a lista numerada, e o peso no G2."))
    H.append(chart("G135"))
    H.append(h2("estr-funil", "Funil de vendas: onde trava e o que traz caixa mais rápido"))
    H.append(steps([
        "Testemunho da empresa ou do projeto; " + pergunta("Em que etapa do funil [empresa] trava hoje?") + " no G133; " + pergunta("Qual etapa, se melhorar, traz caixa mais rápido?") + ".",
        "Percentual de saúde de cada etapa no G2, da prospecção ao pós-venda: a série é o painel comercial.",
        "A etapa indicada abre a ferramenta: prospecção e qualificação, o cliente certo (G114, G132); apresentação, o que ela pede (G131); proposta e negociação, G112 e G113; fechamento, pedir o sim com prazo (G85); entrega, processo e equipe (G91); pós-venda, cadência de contato (G87).",
        "O caixa mais rápido costuma estar na última etapa: quem já comprou. Antes de prospectar, " + pergunta("Qual cliente atual compraria de novo esta semana?") + " nos clientes numerados do G109.",
    ]))
    H.append(chart("G133"))
    H.append(h2("estr-abordagem", "Antes de negociar: o que a apresentação pede e o que a outra parte precisa ouvir"))
    H.append(box("alerta", "A pessoa do outro lado não é pendulada", "Perfil, caráter, intenção, canal preferido ou ponto fraco de um cliente, investidor ou sócio não se leem sem consentimento: é terceiro, e é o uso que mais expõe quem opera. O que se lê é o nosso lado: o que a nossa apresentação pede para ser entendida (G131), o que a relação pede de nós para a outra parte dizer sim e continuar (G132), e como abordar (contato, momento, comportamento, as três perguntas dos Servranx). Os canais visual, auditivo e cinestésico entram como propriedades da apresentação, não como rótulo da pessoa. Em coaching, com o consentimento do cliente, o canal preferido dele pode ser lido no mesmo G131."))
    H.append(steps([
        "Testemunho: a nossa proposta em uma linha e o nome de quem vai apresentar; quem vai ouvir entra só pelo papel (“o investidor do projeto X”, “o comitê da prefeitura”).",
        pergunta("O que a apresentação de [proposta] para [quem] pede primeiro?") + " no G131, e o segundo elemento. Mostrar pede protótipo, fotos e visita; contar pede reunião sem slide e história; experimentar pede teste e amostra; números pedem planilha de uma página e o contador na sala.",
        pergunta("O que [quem] mais precisa ouvir para dizer sim?") + ", " + pergunta("O que precisa receber para continuar?") + " e " + pergunta("O que, se faltar, o faria sair?") + " no G132. As três respostas viram a ordem da apresentação e o que vai por escrito.",
        "Abordagem, nas opções numeradas do G109: " + pergunta("Qual a melhor maneira de contato?") + " (telefonar, visitar, escrever, por indicação), " + pergunta("Qual o melhor momento?") + " (G85, G87) e " + pergunta("Como me comportar?") + " (direto, ouvir primeiro, com intermediário).",
        "Se a negociação já travou: G113. Se há um grupo: mapa de atores (abaixo).",
        "Depois da reunião: registrar o que de fato pesou e comparar com a leitura. É a calibração desta Parte: em dez apresentações, a taxa de acerto do G131 e do G132 diz quanto peso lhes dar.",
    ]))
    H.append(chart_group(["G131", "G132"]))
    H.append(h2("estr-atores", "Grupos, sócios e investidores: mapa de atores, conquistar e manter"))
    H.append(p("Quando quem decide é um grupo (conselho, família empresária, comitê, condomínio, banco), cada ator é numerado e cai no mapa de poder por interesse (G136): envolver de perto, manter satisfeito, manter informado, acompanhar de longe. O mapa é a nossa estratégia de relação, nunca é mostrado a quem está nele, e o pêndulo mede poder e interesse como nota, não como juízo. Com investidores, a mesma lógica se estende no tempo: conquistar é responder à expectativa (G132) com uma apresentação que ela pede (G131); manter é previsibilidade, e não rédea: cadência de contato combinada (G87), relatório com o que ele precisa ouvir, sintonia da sociedade remedida a cada trimestre (G2, G106) e a pergunta que ninguém faz, “o que o faria sair?”, feita antes de ele sair."))
    H.append(steps([
        "Atores numerados no caderno pelo papel. Para cada um: " + pergunta("Qual o poder de [ator] de decidir ou travar [projeto], de 0 a 10?") + " e " + pergunta("Qual o interesse de [ator] em [projeto], de 0 a 10?") + " no G124; quadrante no G136.",
        pergunta("Qual ator, se mudar de lado, muda o projeto?") + ": é a primeira conversa. Mais de três em “envolver de perto”: ordem no G109.",
        "Investidor, antes: expectativa (G132), compatibilidade para o objetivo “captação para X” (G118), critérios de investidor no G106 com os pesos de capacidade financeira, apetite a risco e regras de saída.",
        "Investidor, durante: abordagem (G131), termos no G112, o número com o contador e o advogado. Nunca prometer retorno por pêndulo.",
        "Investidor, depois: cadência de contato no G87 (mensal costuma medir melhor do que trimestral no primeiro ano); relatório com o que ele precisa ouvir (G132); sintonia trimestral; “o que o faria sair?” a cada seis meses. Se a sintonia cair abaixo de 50, Parte IV, caso 2.",
    ]))
    H.append(chart("G136"))
    H.append(h2("estr-caminhos", "Abrir caminhos, convencer e prosperar: o que se faz e o que não se faz"))
    H.append(box("alerta", "O que não entra", "Gráficos emissores para convencer, amarrar, fazer alguém esquecer, ignorar ou mudar de ideia não entram neste manual, mesmo que a tradição os venda: são emissão sobre terceiro sem consentimento, vetada pelo Código de Ética da ABRAD e pela regra do terceiro, e os próprios Servranx avisam da lei do contragolpe. Também não entra “ficar invisível” para um credor: um credor que esquece não cancela a dívida, e o que resolve dívida é proposta previsível e prazo combinado, que esta Parte ensina a preparar."))
    H.append(p("O que entra, e funciona pelas regras deste manual, é agir sobre o nosso lado em cinco frentes: tirar os nossos entraves (G113 onde trava, G111 o que trava, G128 e G129 o que está agarrado); preparar a apresentação e a expectativa (G131, G132); emissores de prosperidade com testemunho da própria empresa ou da própria proposta, nunca de quem está do outro lado: Desembaraçador em sentido anti-horário para “abrir caminhos”, Prosperador para a empresa, Turbilhão com Júpiter para contratos e vendas, com o tempo, a renovação a cada 14 dias e as regras da " + go("fin-emissores", "Parte X") + "; proteção e discrição para si (G67: Escudo, proteção pessoal, não anunciar o que ainda não fechou, foco); e o espaço da reunião harmonizado pela " + go("esp", "Parte IX") + ". Quando se pergunta “há algum entrave?”, a resposta vem do G113, do G119 e do G128, e a ação do G129; não existe gráfico que convença por nós."))
    H.append(h3("Dívida e prazo: negociar, não desaparecer"))
    H.append(steps([
        pergunta("Qual a carga desta dívida em [nome] hoje, de 0 a 100?") + " no G2; acima de 30, a ansiedade decide por ela, e a proteção pessoal (G67) entra antes da conversa, para a pessoa, não para sumir.",
        "O que está agarrado (G128: dívida ou caixa) e o ganho em adiar (G62): quase sempre, evitar a conversa com o credor.",
        "A expectativa do credor no G132: o que ele precisa ouvir para aceitar prazo (previsibilidade, parte agora, garantia, data) e o que o faria recusar.",
        "Opções de proposta numeradas no G109, todas viáveis pelo contador: valor de entrada, número de parcelas, data; " + pergunta("Qual proposta o credor tende a aceitar?") + " e percentual de cada uma no G2.",
        "Abordagem (G131: números e garantias costumam pesar mais), momento no G85, data no G87; G84 para a proposta escolhida, com duas formulações.",
        "Registro; carga remedida em 7 dias depois da conversa. A dívida não some; a carga sim.",
    ]))
    H.append(h2("estr-lider", "Roda do líder"))
    H.append(p("Doze competências de quem conduz um negócio (visão, decidir, delegar, comunicar, vender e negociar, finanças, pessoas, planejar, foco, resiliência, aprender, executar), de 1 a 10, com a regra das três leituras da " + go("coach-rodas", "Parte XII") + ": a nota da pessoa, a medida, a diferença. A competência que, se subir, puxa as outras é o foco do desenvolvimento; a que a empresa cobra e o líder não tem costuma ser função a contratar ou sócio complementar, não meta pessoal."))
    H.append(chart("G137"))
    H.append(h2("estr-casos", "Casos resolvidos"))
    B = []
    B.append(h3("Caso 11 · Quatro projetos e uma agenda"))
    B.append(p("Uma arquiteta empreendedora tem quatro frentes: consultoria por hora (1), um curso gravado (2), uma incorporação pequena com um sócio (3) e um produto de decoração (4). Primeiro real no G85: 1 agora; 2 em meses; 3 em anos; 4 em semanas. Prosperidade duradoura no G124: 1 nota 4; 2 nota 8; 3 nota 9; 4 nota 3. Quadrantes no G130: consultoria, fôlego; curso, semente; incorporação, semente; produto, dreno (rápido mas pouco, e a nota de 3 veio com carga de cansaço). Tempo no G2: 45, 25, 25, 15; soma 110. Devolutiva: o produto sai da lista com revisão em seis meses; a consultoria encolhe para 40 % e paga as duas sementes; o curso ganha manhãs fixas de terça e quinta; a incorporação, uma tarde por semana e a Parte IX. O que puxa os outros: o curso, porque alimenta a consultoria e a venda do produto. Revisão em 90 dias."))
    B.append(h3("Caso 12 · O investidor que some depois de assinar"))
    B.append(p("Uma empresa de tecnologia captou com um investidor que, seis meses depois, não responde às mensagens. G132 lido antes da captação tinha apontado “controle e participação” e “reconhecimento”; o contrato deu participação e nada de reconhecimento. Mapa de atores (G136): o investidor em “envolver de perto”, com poder 8 e interesse que caiu de 9 para 4. “O que o faria sair?”: “ser surpreendido”. Devolutiva: relatório mensal de uma página com o que ele precisa ouvir, menção pública ao investidor no lançamento seguinte, cadência de contato no G87 (quinzenal por três meses), e a pergunta de saída feita na primeira reunião. Sintonia remedida no trimestre: de 38 para 66."))
    B.append(h3("Caso 13 · Dívida com fornecedor e o prazo que faltava"))
    B.append(p("Um restaurante deve a um fornecedor e evita o telefone há dois meses. Carga no G2: 70. G62: evitar a conversa. G132 para o credor: “previsibilidade” e “parte agora”. Propostas numeradas com o contador: (1) 20 % agora e seis parcelas, (2) 10 % agora e dez parcelas, (3) só parcelas. G109: a 1, percentual 76. G131: números e garantias. Momento no G85: agora; data no G87: a quinta. G84 para a proposta 1: sim, grau 72. Proteção pessoal no G67 antes da ligação. O fornecedor aceitou com uma mudança de data. Carga em 7 dias: 20. Nenhum gráfico foi montado sobre o fornecedor."))
    H.append(cols3("".join(B)))
    H.append(end())
    return H

def part_registro():
    H = []
    H.append(h1("reg", "Registro, revisão e calibração", "Parte XIV · Registro", brk=False))
    H.append(p("Nada neste manual vale sem o registro. A ficha de decisão empresarial, o diagnóstico 360, a matriz opções × critérios e o diário de decisões estão no arquivo de fichas à parte, para imprimir quantas vezes for preciso. O manual é fixo; a sessão fica no papel."))
    H.append(h2("reg-diario", "O diário de decisões"))
    H.append(ul([
        "<b>Por decisão</b>: data; pergunta exata; opções numeradas; critérios e pesos; percentuais; resposta do G84; grau; momento; confiança do operador em percentual; decisão de fato tomada (que pode ser outra); a quem foi encaminhado.",
        "<b>Em 90 dias</b>: o que aconteceu; a decisão foi boa pelo que se sabia na hora? O resultado foi bom? As duas perguntas são separadas: decisão boa com resultado ruim existe, e o inverso também.",
        "<b>Taxa de acerto</b> por tipo de pergunta (sim ou não, momento, critério, lugar), ao longo de dezenas de decisões. Só então se decide quanto peso dar ao ritual.",
    ]))
    H.append(h2("reg-revisao", "Revisão: trimestre, 90 dias, 7 dias"))
    H.append(table(["Prazo", "O que se remede", "Onde"], [
        ["7 dias", "Bovis e cômodos depois de uma harmonização de espaço", "G3, G69"],
        ["14 dias", "renovação dos emissores com testemunho da empresa", "Parte X"],
        ["30 dias", "“não é o momento”: perguntar de novo; carga residual", "G85, G2"],
        ["90 dias", "toda decisão medida: o que aconteceu; o contrato assinado; a sociedade formada", "diário de decisões"],
        ["Trimestre", "diagnóstico 360: onze áreas; sintonia da sociedade; o G117 do empreendimento a cada marco", "G92, G2, G117"],
        ["Seis meses", "projetos adiados com condição (“depois de resolver outra coisa”)", "G107, G85"],
    ], cls="small"))
    H.append(h2("reg-fichas", "As fichas do arquivo à parte"))
    H.append(ul([
        "<b>Ficha de decisão empresarial</b>: matriz opções × critérios (G106, G107, G112, G116, G120 ou critérios próprios), pesos, G84 com duas formulações, grau, momento, pontos a confirmar com profissional, revisão em 90 dias.",
        "<b>Diagnóstico 360</b>: Bovis geral e os onze percentuais do G92 por trimestre, as duas áreas que pedem atenção e as três prioridades.",
        "<b>Sociedade</b>: G118 por objetivo, G106 por candidato, cláusulas sugeridas para o advogado.",
        "<b>Laudo complementar de terreno ou ponto</b>: cabeçalho fixo, planta anotada, Bovis por quadrícula, G116 ou G120, lista do que fica com outros profissionais.",
        "<b>Roda da Vida</b> de quem decide, preenchida antes do G24.",
        "<b>Diário de decisões</b>: uma linha por decisão, com a coluna dos 90 dias.",
    ]))
    H.append(end())
    return H

def build():
    H = []
    for f in (part_decisao, part_negocio, part_socios, part_propostas, part_projetos, part_pessoas, part_bloqueios, part_espacos, part_financas, part_pessoa, part_coaching, part_estrategia, part_registro):
        H.extend(f())
    H.append(content_rotas.teorias_cap())
    return "".join(H)
