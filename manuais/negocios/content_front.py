# -*- coding: utf-8 -*-
from bookkit import *

def build():
    NG = len(MANIFEST); NNEW = len([c for c in MANIFEST if int(c[1:]) >= 111])
    H = []
    # ---------------- CAPA ----------------
    H.append('<section class="cover"><img class="cover-bg" src="figs/capa_land.svg" alt=""/>'
             '<div class="cover-text"><div class="cover-kicker">Apoio à decisão para quem responde por um negócio</div>'
             '<h1 class="cover-title">Manual de<br/>Radiestesia<br/>para Negócios</h1>'
             '<div class="cover-sub">Decisão do dono, a empresa como um todo, sócios e parceiros, propostas e contratos, projetos e preços, equipe, interferências e bloqueios, ponto comercial, terrenos e empreendimentos imobiliários, finanças, o empreendedor como pessoa, registro e calibração, coaching empresarial com rodas de 1 a 10, foco, metas e desbloqueio</div>'
             '<div class="cover-meta">Edição 1 · novembro de 2026 · ' + str(NG) + ' gráficos prontos para pendular, ' + str(NNEW) + ' deles próprios deste manual; os demais compartilhados com o Manual de Radiestesia Terapêutica, com a mesma numeração</div></div>'
             '<div class="cover-foot"><span>Apoio à decisão e diagnóstico qualitativo. Não substitui contador, advogado, engenheiro, consultor ou RH, não avalia pessoas e não promete resultado. “O pêndulo indica tendência; a decisão é sua.”</span></div></section>')

    # ---------------- COMO USAR ----------------
    H.append(h1("como-usar", "Como usar este manual"))
    H.append(p("Este manual é um caminho com bifurcações para quem responde por um negócio: dono, sócio, empreendedor, profissional liberal, incorporador, gestor. Cada etapa termina numa tabela de resultados, e cada resultado diz para onde ir, com a página. Não se lê de ponta a ponta durante uma sessão: abre-se no ponto em que a decisão está, mede-se, e o resultado manda adiante. Toda sessão começa pela abertura da Parte I e passa, cedo ou tarde, pela decisão da Parte II."))
    H.append(box("variacao", "O que o pêndulo faz na mesa de quem decide", "Ele não prevê nem decide. Ele obriga a uma disciplina que a maioria das decisões empresariais não tem: pergunta escrita antes, critérios e pesos declarados antes de olhar as opções, opções numeradas, registro e revisão. O movimento vem do próprio operador, por micro-movimentos involuntários; por isso a resposta reflete o que a pessoa já sabe e sente e ainda não formulou. É isso que ele devolve: o tácito, posto na mesa com nome e percentual, para a conversa com contador, advogado, sócios e equipe."))
    H.append(h3("Três ajudas para não se perder"))
    H.append(ul([
        "<b>Trilha no início de cada Parte</b>: os gráficos daquela Parte na ordem de uso, cada um com a página.",
        "<b>Rota em cada gráfico</b>: a linha “Etapa · Vem de” diz em que ponto a leitura entra e de onde se chega a ela; a coluna “O que fazer · vá para” traz, resultado por resultado, o próximo gráfico com a página (▶).",
        "<b>Mapa do método</b> (" + go("mapa", "a seguir") + "): o fluxo mestre de uma decisão empresarial e os treze cartões de bifurcação (“se der isto, vá para”). O " + go("glossario", "Glossário") + " define os termos.",
    ]))
    H.append(h3("Símbolos"))
    H.append(table(["Símbolo", "Significa"], [
        ['<span class="sym">▶</span> vá para (p. N)', "pule para a página indicada e continue de lá"],
        ['<span class="sym">✎</span> registre', "anote no caderno ou na ficha de decisão antes de interpretar"],
        ['<span class="sym">⚠</span> encaminhe', "o assunto saiu do que o pêndulo mede: contador, advogado, engenheiro, consultor, RH, ou atendimento pessoal"],
        ['<span class="sym">?</span> pergunta', "a frase exata a dizer em voz alta antes de pegar o pêndulo; troque [nome], [empresa], [opção] pelos da sessão"],
        ['<span class="sym">G</span> gráfico', "o biômetro a usar, impresso à parte e reproduzido aqui em tamanho reduzido com a interpretação e a rota; a numeração é a mesma do Manual de Radiestesia Terapêutica, e os gráficos G111 a G120 são deste manual"],
    ]))
    H.append(h3("Regras que valem o tempo todo"))
    H.append(ul([
        "A pergunta é escrita antes de pegar o pêndulo, com sujeito, verbo e tempo, e lida como está. Opções entram numeradas; critérios e pesos entram antes das opções.",
        "Toda resposta só vale depois do trio de permissão e da autoauditoria (influência do desejo abaixo de 30). Decisões de dinheiro são as que mais contaminam o operador.",
        "Uma pergunta, uma vez, por sessão. Duas ou três formulações precisam convergir; se divergirem, a resposta é “sem resposta hoje”.",
        "O pêndulo mede a empresa, a relação, a proposta, o projeto, o lugar e a própria decisão. Não mede o caráter, a competência nem a vida de ninguém: candidatos, funcionários, sócios, clientes e fornecedores entram só como função, momento e relação, do lado de quem pediu.",
        "Tudo o que sai daqui é tendência para a conversa, nunca ordem. Número de contrato, cláusula, laudo, diagnóstico e seleção de pessoas ficam com os profissionais da área.",
        "Registro e revisão em 90 dias não são opcionais: são a única maneira de saber se a leitura do operador merece peso.",
    ]))
    H.append(box("nota", "Cortes que não estão em gráfico algum", "Favorável de <b>70</b> para cima; incerto de <b>40 a 69</b>; desfavorável abaixo de <b>40</b>. <b>Empate</b> é diferença menor que <b>10 pontos</b> entre opções. Autoauditoria acima de <b>30</b>: parar. Risco acima de <b>70</b>: plano de saída antes. Bovis de um lugar abaixo de <b>6.500</b>: o espaço vem antes de qualquer decisão. Sociedade: abaixo de <b>50</b> não; <b>50 a 69</b> por projeto, com prazo; <b>70</b> ou mais, contrato. Emissores com testemunho da empresa renovados a cada <b>14 dias</b>; revisão de toda decisão em <b>90 dias</b>."))
    H.append(box("variacao", "Três modos de uso", "<b>Com o dono na sala</b>: ele escreve a pergunta e as opções, o operador pendula, os dois leem a tabela. <b>À distância</b>: testemunho da empresa (razão social, endereço, nome de quem decide, a lápis) no centro dos gráficos. <b>Autoatendimento</b>: o próprio empreendedor pendula as suas decisões; vale com autoauditoria rigorosa, cartões virados e revisão em 90 dias, e nunca sozinho em decisão que tenha dado disponível."))
    H.append(end())

    # ---------------- MAPA ----------------
    H.append(h1("mapa", "Mapa do método", brk=False))
    H.append(p("O fluxo abaixo é o esqueleto de toda decisão empresarial neste manual: oito portas, três bifurcações (terceiro sem pedido?, algo trava?, tendência favorável?) e um retorno. Cada Parte do manual é o aprofundamento de uma porta: a Parte III diagnostica a empresa, a IV a sociedade, a V a proposta, a VI o projeto, a VIII os bloqueios, a IX o lugar; a Parte II é a decisão em si, a XIII o coaching e o desbloqueio, e a XII o registro. A Parte XIII é a camada de coaching: rodas, foco, metas e o protocolo de desbloqueio. Os treze cartões abaixo do fluxo são os pontos em que o resultado muda o caminho."))
    import content_rotas
    H.append(content_rotas.mapa_topo([
        ["Abertura", go("p1-abertura", "Permissão, autoauditoria, pergunta escrita"), "G1, G2"],
        ["Decisão do dono", go("dec", "Parte II"), "G84 a G88, G111"],
        ["A empresa como um todo", go("neg", "Parte III"), "G3, G92, G114, G115, G109, G110"],
        ["Sócios, parceiros e investidores", go("soc", "Parte IV"), "G89, G90, G91, G106, G118"],
        ["Propostas e contratos", go("prop", "Parte V"), "G112, G113"],
        ["Projetos, produtos e preços", go("proj", "Parte VI"), "G107"],
        ["Pessoas, equipe e liderança", go("eq", "Parte VII"), "G95, G101, G103"],
        ["Interferências e bloqueios", go("blo", "Parte VIII"), "G119, G28, G62, G59, G9, G10, G67"],
        ["Espaço, ponto, terreno e empreendimento", go("esp", "Parte IX"), "G66, G69, G70, G71, G82, G83, G116, G117, G120"],
        ["Finanças e prosperidade", go("fin", "Parte X"), "G94"],
        ["O empreendedor como pessoa", go("pes", "Parte XI"), "G24"],
        ["Coaching empresarial: rodas, foco, metas, desbloqueio", go("coach", "Parte XIII"), "G121 a G129"],
        ["Registro, revisão e calibração", go("reg", "Parte XII"), "fichas"],
    ]))
    H.append(content_rotas.mapa_rotas())
    H.append(end())

    # ---------------- PARTE I ----------------
    H.append(h1("p1", "Fundamentos para quem decide", "Parte I · Fundamentos"))
    H.append(p("Esta Parte é lida uma vez e consultada sempre. Traz o material e a convenção de respostas, a abertura de toda sessão, o testemunho da empresa e do lugar, a ética que protege o operador e o cliente, os dez controles de higiene de decisão e a leitura de cada tipo de gráfico. Nada do que vem depois funciona sem ela."))
    H.append(h2("p1-material", "Material e convenção de respostas"))
    H.append(p("Pêndulo (qualquer material; o mesmo sempre), os gráficos impressos à parte, bússola para orientar os gráficos ao norte quando o manual pedir, lápis, papel branco novo para testemunhos, caderno ou as fichas do arquivo à parte. Neste manual não se escreve: ele é a caixa de ferramentas; a sessão fica no caderno. A convenção de respostas (G1) é programada no início de cada sessão e conferida com três perguntas de resposta conhecida; se acertar menos de duas, não se decide nada importante naquele dia."))
    H.append(chart_group(["G1", "G2"]))
    H.append(chart_group(["G3", "G4"]))
    H.append(h2("p1-abertura", "Abertura: permissão, autoauditoria e pergunta escrita"))
    H.append(steps([
        "Enquadrar em uma frase o que está em jogo: decisão, empresa, sociedade, proposta, projeto, equipe, lugar ou o próprio dono. A situação no G108 (" + dest("G108", label="porta de entrada") + ") abre a Parte certa.",
        "Trio de permissão para " + pergunta("esta leitura sobre [assunto] de [nome ou empresa]") + ": posso? devo? estou pronto? Em negócios a terceira inclui “tenho pedido de quem responde por isto?”. Qualquer não encerra o assunto nesta sessão.",
        "Autoauditoria no G2: " + pergunta("Quanto o meu desejo influencia esta leitura, de 0 a 100?") + ". Acima de 30, parar; recomeçar mais tarde ou passar o testemunho a outro operador. Decisões de dinheiro são as que mais contaminam.",
        "Pergunta escrita no caderno com sujeito, verbo e tempo (“aceitar a proposta X neste mês é favorável para a empresa Y?”). Opções numeradas. Critérios e pesos declarados antes de olhar as opções, quando a decisão for de critérios.",
        "Taxa de base, quando houver: quantas decisões desse tipo deram certo antes, na empresa ou no mercado. É dito em voz alta antes do pêndulo.",
        "Convenção (G1) conferida; só então o primeiro gráfico da Parte em que a decisão está.",
    ]))
    H.append(chart("G108"))
    H.append(h2("p1-testemunho", "Testemunho da empresa, do lugar e da pessoa"))
    H.append(p("O testemunho representa o que se mede. Testemunhos e gráficos são desimpregnados antes do uso e entre usos (Desimpregnador, ou giro anti-horário até parar), e o testemunho de uma sessão não se reaproveita em outra."))
    H.append(table(["O que se mede", "Testemunho", "Observação"], [
        ["Quem decide", "nome completo, a lápis, em papel branco novo", "é a única pessoa pendulada como pessoa, e só com pedido dela"],
        ["A empresa", "razão social e endereço, mais o nome de quem decide", "os Servranx admitem a empresa como sujeito de medição; o testemunho a representa como conjunto"],
        ["Uma sociedade, parceria ou negociação", "o nome de quem pede e a descrição da relação (“a sociedade com o candidato A no projeto X”)", "nunca o nome completo e a data de nascimento do outro sem consentimento dele: é dado pessoal"],
        ["Uma proposta, contrato ou projeto", "resumo em uma linha, numerado, no caderno", "o número vai para os leques em branco G109 e G110"],
        ["Um imóvel, ponto ou terreno", "endereço completo, planta orientada com o norte, foto da fachada ou matrícula", "a planta é o testemunho da planta quadriculada (Parte IX)"],
        ["Uma opção entre várias", "lista numerada e datada no caderno", "o mesmo leque serve a muitas listas, por isso a data"],
    ], cls="small"))
    H.append(h2("p1-etica", "Ética: o que se mede, o que não se mede, e como se diz"))
    H.append(box("alerta", "O que não se faz", "Avaliar candidatos, funcionários, sócios ou clientes por foto, nome ou pêndulo: caráter, honestidade, competência, “qualidades morais”. É discriminação sem critério verificável, mede um terceiro sem consentimento e expõe quem opera. Os cursos que ensinam isso descendem do psicométrico de Bélizal e da frase dos Servranx sobre “escolher empregados, vendedores, associados”; este manual veta. Também não se faz: prever faturamento, bolsa ou resultado de licitação; decidir por pêndulo valor de contrato, multa ou preço final; emitir gráfico sobre terceiro sem consentimento; prometer resultado."))
    H.append(ul([
        "<b>Regra do terceiro.</b> Sócio, funcionário, cliente, fornecedor e candidato entram só como parte da relação de quem pede, como função e momento, ou como conjunto (clima da equipe). Pendular a pessoa deles exige autorização explícita; “acho que ele deixaria” não é autorização.",
        "<b>Código de Ética empresarial da ABRAD</b>, adotado aqui: manter registro do histórico de cada cliente e respeitar a confidência dos dados; não interferir na avaliação ou consulta de qualquer outro profissional (administrador, contador, advogado, psicólogo); não discriminar; não anunciar soluções fáceis para problemas pessoais ou financeiros.",
        "<b>Dados pessoais.</b> Nome completo e data de nascimento de terceiros são dados pessoais: não entram em testemunho sem consentimento; o caderno é guardado como ficha clínica.",
        "<b>Frase de abertura para o empresário.</b> “O que sai daqui é tendência para a sua conversa com contador, advogado, sócios e equipe. Eu indico áreas para olhar; não substituo nenhum deles e não avalio pessoas.”",
        "<b>Linguagem.</b> Pode-se dizer: ritual estruturado para trazer à tona e registrar o palpite; o pêndulo amplifica movimentos que a pessoa faz sem perceber; “energia” é palavra da tradição, dita como tal. Evita-se: “comprovado pela física quântica”, promessa de acerto, de lucro ou de “atrair clientes”, e qualquer leitura sobre a vida de quem não pediu.",
    ]))
    H.append(h2("encaminhar", "Quando encaminhar a outro profissional"))
    H.append(table(["Sinal na sessão", "Para quem", "O que o pêndulo ainda faz"], [
        ["A decisão depende de um número (preço, multa, aporte, imposto, viabilidade)", "contador, consultor financeiro", "ordena critérios e nomeia a trava; não dá o número"],
        ["Cláusula, rescisão, garantia, sociedade, terreno, matrícula", "advogado", "aponta o ponto de atenção (G112); não lê a cláusula"],
        ["Solo, estrutura, água, radônio, campos eletromagnéticos, passivo ambiental", "engenharia, sondagem, laudo ambiental, medição por instrumento", "mapeia zonas na planta como complemento declarado"],
        ["Contratar, promover, desligar, avaliar alguém", "RH, entrevista, referências, período de teste", "mede só a função, o momento e, com consentimento, a relação de trabalho"],
        ["Sofrimento, insônia, pânico, exaustão de quem decide", "médico, psicólogo; atendimento pessoal pelo Manual de Radiestesia Terapêutica", "registra e encaminha; não trata"],
        ["Conflito grave entre sócios ou na família empresária", "mediação, governança, acordo de sócios ou de família", "nomeia o tipo de tensão e o que cabe a quem está na sala"],
    ], cls="small"))
    H.append(h2("p1-higiene", "Higiene de decisão: dez controles"))
    H.append(p("A ciência da decisão não valida o pêndulo; valida os controles em volta dele. Estes dez reduzem ruído e viés em qualquer decisão, com ou sem pêndulo, e são a parte deste manual que um empresário cético aceita primeiro."))
    H.append(steps([
        "<b>Pergunta escrita antes</b>, com prazo, métrica e respostas possíveis.",
        "<b>Critérios antes das opções</b>, com pesos. A matriz da ficha de decisão existe para isso.",
        "<b>Taxa de base primeiro</b>: quantas decisões desse tipo deram certo, historicamente.",
        "<b>Avaliação independente</b>: o dono e ao menos uma outra pessoa registram o palpite por escrito, sem se ver; depois estimam de novo juntos.",
        "<b>Cegamento parcial</b>: cartões virados e embaralhados quando a carga emocional é alta; no treino, dez “sim” e dez “não” para medir a própria taxa de acerto.",
        "<b>Formulações convergentes</b>: a mesma pergunta de dois ou três modos; inconsistência derruba a confiança.",
        "<b>Pré-mortem</b>: antes de decidir, imaginar que deu errado daqui a doze meses e listar as causas (" + go("proj-premortem", "Parte VI") + ").",
        "<b>Registro e revisão</b>: pergunta, resposta, confiança e decisão; em 90 dias, o que aconteceu, julgando o processo e não só o resultado.",
        "<b>Taxa de acerto</b> por tipo de pergunta, ao longo de dezenas de decisões, antes de dar peso ao ritual.",
        "<b>Palpite como insumo</b>, com peso explícito e pequeno; nunca como veredito nem no lugar de dado disponível.",
    ]))
    H.append(h2("p1-leitura", "Leitura por tipo de gráfico"))
    H.append(table(["Tipo", "Como ler", "Exemplos"], [
        ["Leque (semicírculo com setores)", "pêndulo no ponto azul do vértice, testemunho no retângulo; oscilação neutra; a pergunta; a oscilação se alinha a um setor. Confirmar com “é o setor N?”. Pedir “há um segundo?” quando o manual mandar", "G84, G92, G106, G107, G108, G111 a G117, G119, G120"],
        ["Escala (régua ou semicírculo numerado)", "começar no ponto de partida (50, 6.500 ou 0) e deslizar até a oscilação virar giro; repetir no sentido oposto; aceitar se as duas leituras ficarem a até 5 pontos (250 no Bovis)", "G2, G3, G4, G118"],
        ["Lista pendulável", "bissecção por sim ou não: coluna, metade das linhas, linha, item. Nunca varrer item a item", "G9, G59, G66, G71, G88, G94, G103"],
        ["Relógio (anéis)", "um anel por vez, lido como escala; primeiro o mês, depois o dia; semana e hora só se fizerem diferença", "G87"],
        ["Réguas por cômodo", "alvo para o giro (horário ou anti-horário) e régua para o percentual, uma linha por cômodo", "G69"],
        ["Leque em branco", "opções escritas e numeradas no caderno; o leque indica o número; percentual de cada opção no G2 antes de aceitar", "G109 (oito), G110 (doze)"],
    ], cls="small"))
    H.append(end())
    return "".join(H)
