# -*- coding: utf-8 -*-
from bookkit import *

def part_limpeza():
    H = []
    H.append(h1("limp", "Limpeza energética de pessoas com o pêndulo", "Parte VII · Limpeza de pessoas", brk=False))
    H.append(p("Esta parte é a sessão de limpeza propriamente dita: o que o pré-ciclo pede quando a carga está acima de 10, o que o setor 4 do biômetro de causas pede quando a interferência está confirmada, e o que se faz quando a pessoa chega pedindo “uma limpeza”. As escolas convergem num esqueleto de cinco fases (preparar e proteger; medir; extrair com giro anti-horário; repor e selar com giro horário; verificar) e divergem nos detalhes. O roteiro abaixo fixa uma versão única, com o pêndulo decidindo o que remover, onde e com qual técnica. Tudo o que é medido aqui é medida radiestésica: registra-se como tal, sem substituir cuidado médico ou psicológico."))
    H.append(box("variacao", "Convenção de giro desta parte", "Antes de começar, declare a convenção em voz alta: <b>anti-horário = extraindo, limpando</b>; <b>horário = repondo, selando</b>; <b>parado = concluído naquele ponto</b>. Em várias escolas o anti-horário sobre um chakra significa só “chakra fechado”; aqui, durante a limpeza, ele é trabalho ativo, porque a intenção foi declarada. A leitura de estado do chakra continua sendo a do Nível 2."))

    H.append(h2("limp-quando", "Quando fazer e quando não fazer"))
    B = []
    B.append(table(["Situação", "O que fazer"], [
        ["Pré-ciclo marcado na triagem (vitalidade abaixo de 4.500, carga acima de 10, proteção abaixo de 40, rompimento presente)", "fazer a limpeza completa antes do Nível 2; depois remedir a triagem"],
        ["Setor 4 (energética) confirmado no biômetro de causas de um chakra", "entrar no passo 4 desta parte já com o item do G15; voltar ao capítulo do chakra para harmonizar"],
        ["Pessoa pede limpeza sem queixa definida", "sessão de limpeza inteira (passos 1 a 9), seguida de harmonização geral e fechamento"],
        ["Carga até 10 e aura protegida acima de 40", "não limpar: ir direto ao Nível 2; limpeza desnecessária gasta a sessão"],
        ["Pessoa em crise aguda, surto, ideação suicida, doença grave sem acompanhamento", "não é caso de limpeza: " + go("encaminhar", "encaminhar") + " e, se ela quiser, proteção e conforto apenas"],
        ["Trio de permissão com “não”", "não limpar hoje; perguntar " + pergunta("Posso fazer só a proteção?") + " e registrar"],
    ]))
    H.append(chart("G63", beside="".join(B)))

    H.append(h2("limp-seq", "Sequência em nove passos"))
    H.append(steps([
        "<b>Preparar e proteger o operador.</b> Pés no chão, respiração, intenção de neutralidade, pedido de que o trabalho seja para o bem de todos. Pêndulo e gráficos limpos (pano de feltro ou álcool nos gráficos; sal grosso só em pêndulos não metálicos). Escudo Protetor ou Antimagia com o seu próprio testemunho, pelo tempo que o pêndulo indicar no G23. Não limpar cansado, doente ou emocionalmente envolvido.",
        "<b>Permissão.</b> Trio Posso, Devo, Estou pronto para " + pergunta("a limpeza energética de [nome completo]") + ". Com a pessoa presente, pedir autorização verbal; à distância, autorização prévia registrada na ficha.",
        "<b>Medir o estado inicial</b> " + '<span class="sym">✎</span>' + ": vitalidade no G3 (" + pergunta("Qual a vitalidade geral de [nome] em unidades Bovis?") + "); carga total no G2 (" + pergunta("Qual a carga de interferências sobre [nome], de 0 a 100?") + "); estado da aura no G63, um anel por vez; percentual dos sete chakras na silhueta G6. Esses quatro valores são o “antes”.",
        "<b>O que remover.</b> Lista G64 por bissecção: " + pergunta("O que precisa ser removido está na coluna da esquerda?") + ", depois o grupo, depois linha a linha. " + pergunta("Há mais alguma coisa a remover?") + " até “não”; no máximo cinco itens por sessão, em ordem de prioridade (" + pergunta("Qual sai primeiro?") + "). Se o item for ser ou implante, nomear no G51 ou G50; se for cordão, ir ao " + go("limp-cordoes", "corte de cordões") + ".",
        "<b>Onde está.</b> Para cada item: corpo sutil no G60; chakra no G5; frente ou costas (" + pergunta("Está na frente?") + "); órgão ou região no G13 quando o corpo sutil for o físico ou o etérico. Marcar na silhueta. " + pergunta("Há outro ponto?") + ".",
        "<b>O que o sustenta.</b> G58: " + pergunta("O que sustenta este item?") + " Emoção, crença e trauma são liberados antes de remover (Nível 4); voto, pacto ou contrato é nomeado no G59 e desfeito em voz alta; vínculo com pessoa vai ao corte de cordões; “nada” autoriza a remoção direta. Depois: G62, " + pergunta("Há ganho em manter?") + ". Sem isso, o item tende a voltar em dias.",
        "<b>Remover.</b> Técnica no G65 (" + pergunta("Qual técnica remove este item?") + ") e, se for comando, o verbo no G68. Aplicar com o pêndulo em giro anti-horário sobre o ponto marcado (ou sobre o testemunho na silhueta), a 5 a 10 cm, até o pêndulo parar sozinho; se não parar em três minutos, perguntar " + pergunta("Falta liberar algo antes?") + " e voltar ao passo 6. Fórmula de comando: “Peço que [verbo] [item] em [local] de [nome], e que o espaço seja preenchido com luz; obrigado, está feito.” Seres e presenças são <b>encaminhados</b>, nunca “exorcizados”; se não saírem em duas tentativas, registrar e encaminhar a quem faz apometria ou trabalho espiritual.",
        "<b>Repor e selar.</b> Em cada ponto limpo, giro horário com visualização de luz até parar; depois o selamento do G67 (" + pergunta("Como selar este ponto?") + ") e a proteção geral da pessoa (" + pergunta("Qual proteção para [nome] hoje?") + "), pelo tempo do G23. Aura: " + pergunta("A aura está íntegra agora?") + " Se não, repetir o giro horário na camada do G63 com fuga ou furo, frente e costas.",
        "<b>Verificar</b> " + '<span class="sym">✎</span>' + ": remedir vitalidade, carga, aura e chakras. Critérios: carga até 10; proteção acima de 40; vitalidade subiu; " + pergunta("A limpeza está 100% concluída?") + ". Se algo ficou, " + pergunta("Pode ficar para a próxima sessão?") + " e registrar pendência. Reforço: 48 horas para as camadas 1 a 3, 7 dias para as camadas 4 a 7 (" + pergunta("Precisa de reforço?") + "). Orientações de saída na " + go("limp-pos", "pós-sessão") + ".",
    ]))
    H.append(chart("G64"))
    H.append(chart_group(["G65", "G68"]))
    H.append(chart("G67"))

    H.append(h2("limp-tabela", "O que remover e com o quê"))
    H.append(p("Correspondências de partida. O pêndulo confirma ou troca no G65; quando ele escolhe outra, vale a escolha dele."))
    H.append(table(["Item (G64)", "Selamento · tempo e reforço"], [[r[0], r[2] + "; " + r[3]] for r in [
        ["Encosto, obsessor, mago, consciência não atual", "encaminhamento com comando; Luxor; se persistir, apometria", "Nove Círculos ou Antimagia com testemunho", "até parar; reforço em 7 dias"],
        ["Chip, antena, implante, sonda, capacete", "comando (dissolver, transmutar) em giro anti-horário; Pêndulo Hebraico “quitar implante”; Desimpregnador", "selo por etiqueta (Keter, Arcanjo) ou giro horário com luz", "até parar; conferir em 48 h"],
        ["Miasma, larva, forma-pensamento, egrégora", "giro anti-horário; Triturador 21 dias; Desimpregnador", "giro horário com luz; Escudo Protetor", "15 a 30 min no gráfico; 21 dias no Triturador"],
        ["Energia absorvida de pessoa, lugar ou objeto", "giro anti-horário; comando “devolver à origem transmutada”", "giro horário; banho de ervas", "até parar"],
        ["Fuga ou furo na aura", "localizar a camada (G63) e varrer frente e costas", "giro horário na camada; etiqueta de selo", "reforço 48 h (camadas 1 a 3) ou 7 dias (4 a 7)"],
        ["Cordão, amarração", go("limp-cordoes", "corte de cordões") + "; SCAP", "selar cada corte com luz; energizar com outro gráfico", "até parar; conferir em 7 dias"],
        ["Voto, pacto, contrato, maldição", "nomear no G59; ação da lista CQM dita em voz alta; comando", "Antimagia; oração ou mantra", "conferir em 7 dias"],
        ["Mal de olho, inveja, magia, “trabalho”", "Antimagia; SCAP; Pêndulo Hebraico (Mal de ojo, Magia ritual)", "Nove Círculos; Escudo Protetor", "tempo pendulado; reforço em 7 dias"],
        ["Programa de medo ou controle, semente invasora", "comando (embaralhar e neutralizar) e substituir pela frequência desejada (preencher)", "selo; afirmação", "até parar"],
        ["Emoção, crença, trauma, memória celular", "Nível 4 (G9, G55, G61) antes; depois técnica 2 ou 8", "giro horário", "a do Nível 5"],
        ["Nada a remover: só energizar", "giro horário com luz nos chakras abaixo de 70", "proteção geral", "até parar"],
    ]]))

    H.append(h2("limp-cordoes", "Corte de cordões e vínculos"))
    H.append(p("Cordões são ligações energéticas entre a pessoa e alguém (ou algo) que drenam ou prendem. Regra ética repetida pelas escolas: corta-se só a conexão nociva; o que é amor e aprendizado permanece. O corte não é separação da pessoa, é devolução de energia a cada um."))
    H.append(steps([
        pergunta("Existe cordão nocivo ligado a [nome]?") + " e " + pergunta("Quantos?") + " (G20b como contador até 10).",
        "Com quem: G36 (pessoas) ou, se for alguém fora da lista, soletrar com a prancha de letras ou perguntar por iniciais. Vivo ou falecido.",
        "Em qual chakra (G5) e se entra pela frente ou pelas costas. Os mais citados são básico, sacral, plexo e cardíaco.",
        "Permissão: " + pergunta("Posso cortar este cordão hoje?") + " e " + pergunta("É para o bem maior dos dois?") + " Se não: " + pergunta("Precisa liberar uma emoção antes?") + " (G9) ou " + pergunta("Há um contrato por trás?") + " (G59).",
        "Cortar: testemunho no SCAP (cristal em cima, gráfico orientado ao norte) ou no gráfico Corte de Laços; comando em voz alta (“corto e dissolvo o cordão nocivo entre [nome] e [pessoa] no chakra [x]; devolvo a cada um a sua energia transmutada”); visualização de tesoura de luz, chakra a chakra, com o pêndulo em giro anti-horário até parar.",
        "Selar cada ponto cortado com luz (giro horário até parar) e energizar com outro gráfico (SCAP não emite energia positiva).",
        "Verificar: " + pergunta("O cordão foi dissolvido?") + " e " + pergunta("Há outro?") + ". Conferir em 7 dias; cordões de relações atuais tendem a se refazer e pedem a crença ou o ganho secundário (G62) tratados.",
    ]))

    H.append(h2("limp-auto", "Autolimpeza"))
    H.append(p("Sentado, pés no chão, pêndulo na mão dominante. Chakras acessíveis (coronário, frontal, laríngeo, cardíaco, plexo, sacral) diretamente, com a outra mão espalmada perto do ponto; básico, costas e aura pela própria foto ou nome sobre a silhueta G6 e sobre os gráficos. A sequência é a mesma; as perguntas, na terceira pessoa com o nome completo. Autoauditoria antes e depois: abaixo de 70, não fazer a autolimpeza nesse dia, só a proteção. Gráficos com testemunho próprio: Desimpregnador 15 a 30 minutos, Triturador 21 dias, SCAP com cristal."))

    H.append(h2("limp-pos", "Pós-sessão e cuidado do operador"))
    H.append(ul([
        "Pessoa: água, repouso de ao menos dez minutos, evitar discussões no dia; banho de ervas no dia seguinte como fechamento (o banho de sal grosso é recomendado por muitas escolas e proibido por uma; se usar, só do pescoço para baixo e sem sabonete depois). Retorno em 21 a 30 dias, ou remedida de 7 dias quando houve reforço marcado.",
        "Operador: pausa, pés no chão, lavar as mãos e o pêndulo em água corrente; testemunhos usados vão ao Desimpregnador ou são descartados; autoauditoria final registrada. Se caiu abaixo de 70 depois da sessão, proteção própria e nada mais naquele dia.",
        "Registro na " + go("fichas", "ficha de limpeza") + ": antes, itens, local, técnica, depois, pendências, reforço.",
    ]))
    H.append(end())
    return H

def part_espacos():
    H = []
    H.append(h1("esp", "Limpeza, harmonização e localização em espaços", "Parte VIII · Espaços e localização", brk=False))
    H.append(p("Três usos do pêndulo fora do corpo: diagnosticar e limpar um imóvel (casa, consultório, loja), mapear as fontes nocivas sobre a planta (geobiologia) e localizar algo sobre uma planta ou um mapa (cômodo, objeto). O roteiro brasileiro mais repetido é curto: analisar cômodo a cômodo com o pêndulo, medir o ambiente de péssima a excelente com o endereço escrito como testemunho, deixar o pêndulo escolher o gráfico e o tempo, e perguntar ao fim se está 100% concluído. Esta parte expande esse roteiro com as etapas que as escolas de geobiologia e de radiestesia de mapa acrescentam: preparação, fontes, limpeza, proteção e reavaliação."))

    H.append(h2("esp-prep", "Preparação: planta, testemunho e permissão"))
    H.append(ul([
        "<b>Planta baixa</b> em folha A4, a lápis ou tinta preta, sem detalhes, com o nome de cada cômodo e a posição da cama, da mesa de trabalho e da porta de entrada. Orientar a folha com a bússola (norte para cima) e anotar o norte na folha. Para localização em mapa, usar um mapa impresso da região na grade G72.",
        "<b>Testemunho</b>: o endereço completo escrito no retângulo do gráfico; se quiser, uma foto da entrada no centro; para apometria à distância, nomes dos moradores e endereço. A palavra escrita “carrega” em cerca de três dias; uma ficha em cartão dentro de um círculo acelera.",
        "<b>Permissão</b>: trio para " + pergunta("a análise e a limpeza do imóvel de [endereço]") + " e autorização de quem mora ou responde pelo lugar. Não se analisa a casa de terceiros sem pedido deles.",
        "<b>Operador</b>: os mesmos cuidados da " + go("limp-seq", "limpeza de pessoas") + " (centramento, pêndulo limpo, proteção própria). Sessão presencial: 1 a 4 horas conforme a área; sobre a planta, à distância, 45 a 90 minutos.",
    ]))

    H.append(h2("esp-medir", "Medir: casa inteira, cômodo a cômodo, áreas do baguá"))
    H.append(steps([
        "<b>Casa inteira</b> " + '<span class="sym">✎</span>' + ": " + pergunta("De péssima a excelente, como está a energia do imóvel de [endereço]?") + " no G2 (0 a 20 péssima, 20 a 40 ruim, 40 a 60 regular, 60 a 80 boa, 80 a 100 excelente) e " + pergunta("Qual a vitalidade do imóvel em unidades Bovis?") + " no G3. Faixas de referência (Medeiros, biômetro 5G, prancha de locais): 0 a 2.000, cruzamento de correntes negativas; 2.000 a 6.000, zona negativa, potencialmente nociva (o biômetro 5G chama de letal até 3.500 e patológica até 6.500); 6.500, neutra; 7.000 a 8.000, positiva, gera vitalidade; 9.000 a 10.000, muito ativa; 10.000 a 13.000, plano espiritual (lugares sagrados, portais naturais). As cinco zonas da prancha de locais de referência seguem a mesma ordem: perigosa, perturbada, neutra, saudável, espiritual. Mutarelli: 4.700 adoece os moradores; Rodrigues: uma pessoa sadia vibra entre 6.500 e 10.000 e perde energia para um local de 1.000 ou 2.000.",
        "<b>Cômodo a cômodo</b> na lista G69: pêndulo sobre o alvo de cada cômodo (ou sobre o cômodo na planta, ou andando pelo cômodo com a mão parada): giro horário é harmonia, anti-horário é desequilíbrio. Nos anti-horários, percentual na régua da linha; abaixo de 70 entra na limpeza. Dê atenção especial ao quarto (cama) e ao posto de trabalho: são os lugares de maior permanência.",
        "<b>Áreas de vida</b>, quando a queixa é de vida e não de sintoma (dinheiro, relação, trabalho): baguá sobre a planta a partir da porta de entrada, nove setores no G70; percentual de cada área no G2; tratar as de menor valor.",
        "<b>Pessoa e lugar</b>: se a sessão veio de um chakra com setor 5 (ambiental), medir também " + pergunta("Quanto este imóvel pesa sobre o chakra [nome] de [pessoa], de 0 a 100?") + " O valor volta para a ficha do chakra.",
    ]))
    H.append(chart_group(["G69", "G70"]))
    H.append(p("Elementos, cores, formas, plantas e pedras por área são os do baguá ilustrado de referência; servem como remediação da área de menor valor (introduzir a cor, a planta ou a pedra), confirmada no pêndulo."))

    H.append(h2("esp-espelho", "De quem é a energia do ambiente"))
    H.append(p("O ambiente registra energia e memória. O campo mental e o campo emocional de quem mora e de quem frequenta ficam impressos nas paredes, nos móveis e nos objetos (a “memória de parede” das escolas brasileiras), e o cômodo passa a espelhar essas pessoas. Por isso, antes de tratar um cômodo, duas leituras que mudam o direcionamento: onde a pessoa de fato dorme e passa o dia, e de quem é a energia que aquele cômodo espelha. Uma pessoa que dorme no quarto do filho, ou que está morando no quarto dos pais na casa deles, mede um ambiente que não é o retrato dela: é o retrato de outra pessoa, e o que ela sente ali é absorvido, não produzido."))
    H.append(steps([
        "Onde a pessoa está: G83, " + pergunta("Onde [nome] dorme hoje?") + " e " + pergunta("Onde [nome] passa a maior parte do dia?") + ". Se a resposta for um cômodo de outra pessoa (quarto dos filhos, quarto dos pais, casa de outra pessoa), é esse cômodo que entra na medição, não o quarto “dela” no papel.",
        "De quem é a energia: G82, " + pergunta("A energia deste cômodo espelha quem?") + " e, para cada nome que testar sim, o percentual no G2: " + pergunta("Quanto deste cômodo é energia de [pessoa], de 0 a 100?") + ". Dois ou três nomes podem somar mais de 100; interessa a ordem.",
        "Quanto espelha a própria pessoa: " + pergunta("Quanto este cômodo espelha o estado atual de [nome], de 0 a 100?") + " Acima de 70, o cômodo é um retrato dela: o que se mede no ambiente confirma o que se mediu nos chakras, e os dois se tratam juntos. Abaixo de 40, o ambiente não a espelha: o que pesa ali vem de outra pessoa ou do lugar, e a leitura dos chakras dela não deve ser explicada pelo cômodo.",
        "Direcionamento quando o cômodo espelha outra pessoa (pais, parceiro, filho): mede-se o cômodo, nunca a outra pessoa sem pedido dela. Orientar proteção pessoal (" + go("limp-seq", "Parte VII") + "), limpeza do cômodo com o consentimento de quem o imprime, e, quando possível, um espaço próprio (um canto, uma cama, uma gaveta que seja só da pessoa). O ganho secundário G62 ajuda a entender por que a pessoa permanece ali.",
        "Direcionamento quando espelha o lugar em si: fontes (passo seguinte) e geobiologia; a pessoa só volta a ser medida depois de o lugar ser tratado.",
        "Conversar e avisar " + '<span class="sym">✎</span>' + ": o que foi lido sobre o cômodo é dito à pessoa como medida radiestésica, sem rótulo sobre os familiares, e o encaminhamento é combinado com ela.",
    ]))
    H.append(chart_group(["G83", "G82"]))
    H.append(box("variacao", "Conversar e avisar, sempre", "Antes de medir, a pessoa sabe o que vai ser medido e por quê, e autoriza. Depois, recebe o resultado como medida radiestésica, em linguagem simples, sem diagnóstico e sem julgamento sobre terceiros. Cômodos de outras pessoas são medidos como lugar, não como pessoa; ninguém é medido sem pedir. O direcionamento (trocar de cômodo, proteger-se, limpar a casa) é proposto e combinado, não imposto."))

    H.append(h2("esp-fontes", "Fontes: o que pesa no lugar"))
    H.append(p("Para cada cômodo em desequilíbrio: " + pergunta("A fonte principal está em qual grupo?") + " no G16 (versão curta) ou na lista desdobrada G66 (geopatia, eletromagnética, memória e histórico, seres e formas, objetos), por bissecção. Depois " + pergunta("Há uma segunda fonte?") + " e a posição no G25 ou diretamente sobre a planta (o pêndulo gira sobre o ponto). Fontes de geopatia e eletromagnéticas pedem o " + go("esp-geo", "mapeamento") + "; memória, seres, formas e objetos pedem a " + go("esp-limpar", "limpeza") + "; objetos pedem ainda " + pergunta("Este objeto pode ser limpo?") + " ou " + pergunta("Deve sair da casa?") + "."))
    H.append(chart("G66"))
    H.append(p("A lista G66 incorpora as tabelas de José Medeiros (causas das energias nocivas, energias nocivas paranormais) e os objetos e terrenos do curso CEAP; a lista G71 incorpora os purificadores e as formas de neutralização do mesmo autor. Escala de vibração de locais, de −50 a +50, lida no G4 dividido por dois: abaixo de −40, perigo telúrico; −10 a +10, oscilante; acima de +40, portal cósmico-telúrico."))

    H.append(h2("esp-geo", "Mapear redes, veios e nós sobre a planta"))
    H.append(p("Espaçamentos citados pelas escolas: rede Hartmann a cada 2 m (leste-oeste) por 2,5 m (norte-sul), faixas de cerca de 21 cm, com variação pela latitude; rede Curry em diagonal, a cada 3,5 a 4 m para umas fontes e 6 a 8 m para outras; Benker a cada 10 m. O ponto crítico é o nó (cruzamento) e, pior, a sobreposição de Hartmann com Curry ou com veio d'água, sob a cama ou a cadeira de trabalho. A ciência não reconhece essas redes; o que tem evidência independente é reduzir campos eletromagnéticos e radônio no quarto. Registre como medida radiestésica e proponha remediações reversíveis primeiro."))
    H.append(steps([
        "Planta orientada; varrer com um lápis ou ponteiro em linhas paralelas norte-sul, a cada 2 ou 3 cm da folha, perguntando " + pergunta("Há linha Hartmann aqui?") + "; marcar onde o pêndulo gira; depois leste-oeste; ligar as marcas.",
        "Repetir em diagonais para a Curry (" + pergunta("Há linha Curry aqui?") + "). Marcar os nós e as sobreposições.",
        pergunta("Há veio d'água sob este imóvel?") + " Se sim, varrer e traçar; " + pergunta("É falha úmida?") + ". Direção de fluxo e profundidade são opcionais.",
        "Para cada nó: intensidade no G2 (" + pergunta("Qual a intensidade deste ponto, de 0 a 100?") + ") e " + pergunta("Este ponto afeta a cama ou o posto de trabalho?") + ".",
        "Método da planta quadriculada (António Rodrigues): planta com o norte marcado, potencializada 20 minutos no decágono; quadriculado de 2,5 cm (ou 2 × 2 cm); Bovis no G3 em cada cruzamento das linhas; ligar os valores iguais em curvas; os vales abaixo de 6.500 são as faixas e os nós. No local, as faixas Hartmann são marcadas com fita crepe no piso, a cada 2 m e 2,5 m.",
        "Confirmar, quando possível, no local com varetas em L (dual rod cruza sobre água e sobre a faixa) ou com segundo operador, às cegas (planta virada). Até lá, registrar “a confirmar”. Alerta das formações: o radiestesista quase sempre encontra um ponto sobre a cama; só o duplo cruzamento ou o valor baixo confirmado justifica mudar a cama.",
        "Decisão de cama: cabeceira e corpo fora de nós; cama de casal com os dois lados em célula neutra; deslocamento típico de 30 a 70 cm. Se não puder mover: isolante (cortiça, lã, sisal) sob a cama, gráfico (Diafragma I com quartzo rosa, ou SCAP) e remedida em 7 dias.",
    ]))

    H.append(h2("esp-limpar", "Limpar, harmonizar e proteger o imóvel"))
    H.append(steps([
        "<b>Ordem</b>: " + pergunta("Por qual cômodo começar?") + " (G69); dentro do cômodo, cantos e atrás das portas são os pontos mais citados.",
        "<b>Técnica</b> na lista G71 por grupo: " + pergunta("Qual técnica para este cômodo?") + " Gráficos: " + pergunta("Qual gráfico?") + " (G41, categoria Limpeza) com o endereço escrito em cima, posição no imóvel verificada com o pêndulo e tempo no G23. Comando: pêndulo em giro anti-horário sobre o cômodo na planta, “neutralizo e embaralho toda energia não benéfica deste cômodo; encaminho à luz o que não pertence a esta casa”, até parar; depois giro horário, “elevo a energia deste cômodo a, no mínimo, 70 e preencho com luz”, até parar. Físicos: copo de água com sal por 24 horas no centro, sal grosso nos cantos trocado a cada 7 dias (descartar no vaso, nunca na pia), defumação com janelas abertas, som por 3 minutos, pano com sal ou anil do fundo para a porta; para memória de parede antiga, caiação.",
        "<b>Seres, portais e formas</b>: encaminhamento com comando, Luxor ou Nove Círculos com o endereço; espelhos e portais fechados e selados (“fecho e selo este portal; nada entra, nada sai”); o que não sair em duas tentativas vai para apometria de ambiente (21 a 33 dias) ou para quem faz esse trabalho.",
        "<b>Objetos</b>: Desimpregnador com o objeto ou sua foto por 15 a 30 minutos; se " + pergunta("Deve sair da casa?") + " der sim, orientar o descarte ou a devolução.",
        "<b>Ordem das correções</b> (Rodrigues): monte a lista da técnica mais física para a mais sutil e aplique nessa ordem: ventilação, luz, limpeza, descarte e mudança de móveis primeiro; isolantes e cristais depois; gráficos e comandos por último. Não introduzir gráficos na casa sem análise prévia e não multiplicar proteções: ambientes ficam desequilibrados pelo excesso de dispositivos, e quase todos saturam (Keiti e SCAP não saturam; o Desimpregnador fica em área aberta, não dentro de casa; o Escudo Protetor não passa de 10 minutos com o testemunho, que valem um dia e meio).",
        "<b>Harmonizar</b>: depois de limpar, energizar (o SCAP e os gráficos de limpeza não emitem energia positiva): gráfico energizador da categoria Potencialização do G41, plantas, luz, cristais nos cantos, cores do G42 nas áreas de menor valor do baguá.",
        "<b>Proteger</b>: Nove Círculos, Luxor ou Escudo com o endereço, pelo tempo do G23; “fecho os escudos desta casa”; moradores com a proteção pessoal da " + go("limp-seq", "Parte VII") + " quando a carga deles estiver acima de 10.",
        "<b>Reavaliar</b> " + '<span class="sym">✎</span>' + ": remedir G2 (casa inteira), G3 e os cômodos tratados. Meta: casa acima de 6.500 e cômodos acima de 70; " + pergunta("A limpeza está 100% concluída?") + ". Gráficos ficam no imóvel até o pêndulo pedir a retirada; conferir a cada 30 dias e trocar só se danificados (as escolas sugerem revisão a cada 3 meses). Limpeza completa uma vez por mês ou após mudança, obra, briga ou doença.",
    ]))
    H.append(chart("G71"))

    H.append(h2("esp-loc", "Localizar sobre planta ou mapa"))
    H.append(p("Três técnicas das sociedades de radiestesia: a grade (linhas e colunas numeradas, célula a célula), a régua (deslizar uma régua da borda até o pêndulo responder, marcar a linha, repetir na borda perpendicular; o ponto é o cruzamento) e a bissecção (metades e quartos sucessivos, passando a mapas de escala maior). A triangulação toma a direção a partir de dois pontos diferentes; onde as linhas se cruzam está o alvo. Confirmação sempre por segundo método ou segunda sessão e, por fim, no local."))
    H.append(steps([
        "Testemunho do alvo (foto, nome, objeto semelhante) e permissão: " + pergunta("Posso procurar [alvo]?") + ", " + pergunta("[Alvo] ainda existe e pode ser encontrado?") + ".",
        pergunta("[Alvo] está dentro desta planta (ou deste mapa)?") + " Se não: direção no G73 e distância no G74 a partir do ponto de referência; trocar de mapa (bairro, cidade, região) e repetir.",
        "Grade G72: linha pelos alvos da esquerda, coluna pelos de cima; célula no cruzamento. Ou régua em X e Y. Ou bissecção (“está na metade de cima?”).",
        "Pêndulo lançado (António Rodrigues): planta orientada; fio de 12 a 15 cm; lançar o pêndulo a partir de um ponto da margem esquerda com a pergunta na mente; a oscilação se estabiliza num ângulo; marcar a linha; repetir de um ponto da margem direita; o cruzamento das duas linhas é o ponto. No mapa, limitar a região com papel branco e perguntar se o alvo está nela; se não, ampliar. Hierarquia de testemunhos: mecha de cabelo, foto, cartão, nome escrito (potencializado 72 horas no decágono).",
        "Gráfico Yogi (cartas Servranx), para pessoas e objetos: a foto do operador cobre a cabeça da figura e o testemunho do que se procura vai no plexo solar; segue rastros reais sem interferência de rotas antigas; o gráfico Amplificador também serve de antena para objetos perdidos, com comando e testemunho no centro e tempo no G23.",
        "Em outra sessão ou com outro operador, repetir às cegas; se as duas respostas coincidem, ir ao local. Se divergem, registrar as duas e não afirmar nada.",
        "Erros comuns: pergunta vaga, pressa ou ansiedade, terceiros opinando, mapa não orientado, não repetir em outra escala, tomar oscilação errática por resposta.",
    ]))
    H.append(chart_group(["G72", "G73"]))

    H.append(h2("esp-objetos", "Objetos perdidos"))
    H.append(p("Calibrar sim e não; " + pergunta("O objeto ainda existe e pode ser encontrado?") + "; " + pergunta("O objeto está dentro de casa?") + " (se não, situação no anel externo do G75: carro, trabalho, com alguém, na rua, descartado, roubado, em outra casa); " + pergunta("Neste andar?") + "; cômodo na planta ou no G69; depois os anéis “onde” e “altura” do G75 (a altura é sugestão prática, sem fonte); móvel ou gaveta por sim e não; buscar fisicamente e só repetir a consulta depois da busca. Pessoas desaparecidas: a radiestesia não substitui polícia nem busca organizada; se alguém pedir, registrar a resposta como hipótese e entregar às pessoas responsáveis, sem promessa de resultado e sem invadir a privacidade de quem não pediu."))
    H.append(chart_group(["G74", "G75"]))

    H.append(end())
    return H
