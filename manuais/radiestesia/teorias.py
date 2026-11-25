# -*- coding: utf-8 -*-
"""Fichas curtas das teorias em que os gráficos do manual se apoiam, e glossário.

Cada ficha: nome, origem, afirma (tese central), mede (o que o pêndulo mede com ela
neste manual), graficos (ids do manifest; "C{k}-x" vale para os sete chakras),
ler (como interpretar), limites (o que não garante / quando encaminhar).
"""

TEORIAS = [
    dict(nome="Convenção de respostas e permissões (Woods, Lonegren)",
         origem="Walt Woods (Letter to Robin, American Society of Dowsers, 2001) e Sig Lonegren; convenção brasileira de giro",
         afirma="Antes de perguntar, o operador combina com o pêndulo um movimento para cada resposta: pronto, sim, não, nenhuma das anteriores e “não posso ou não devo”. "
                "Depois pede licença com o trio “posso, devo, sou capaz”, repetido sempre que o assunto muda.",
         mede="Não mede a pessoa: calibra o operador. O G1 fixa os cinco movimentos; o G84 aplica a mesma lógica às decisões, com o quinto setor alinhado ao “não posso ou não devo”.",
         graficos=["G1", "G84"],
         ler="Giro horário é sim, anti-horário é não, parado é neutro. Um não no trio de permissão encerra o assunto sem insistência; o neutro pede reformular a pergunta.",
         limites="A convenção é combinada, não descoberta: só vale se for conferida no início de cada sessão com perguntas de resposta conhecida."),

    dict(nome="Efeito ideomotor e controles de confiabilidade",
         origem="Michel Chevreul (1833), termo de William Carpenter; testes controlados de Sydney (1980), Munique (1987–88) e Kassel (1991)",
         afirma="O pêndulo se move por microcontrações musculares involuntárias guiadas pela expectativa de quem o segura. "
                "Nos testes em que o operador não tinha acesso à resposta, o acerto não passou do acaso. Os próprios radiestesistas apontam a ideia preconcebida como a maior causa de erro.",
         mede="Mede o viés do operador: a pergunta de autoauditoria (influência dos meus sentimentos, 0 a 100, no G2) e o G88, que separa as causas de erro do operador dos obstáculos da pessoa.",
         graficos=["G1", "G2", "G88"],
         ler="Influência acima de 30: parar e recomeçar mais tarde. Resposta sem sentido: procurar a causa no G88, recalibrar no G1 e repetir uma vez só.",
         limites="Os controles reduzem o viés, não o eliminam; o pêndulo não serve como prova de nada nem como diagnóstico."),

    dict(nome="Escala Bovis e biômetro (Mermet, Bovis, Simoneton)",
         origem="Escola francesa clássica: abade Mermet, André Bovis e André Simoneton (primeira metade do século XX); usos brasileiros de Mutarelli, Rodrigues e Medeiros",
         afirma="Todo ser e todo lugar teriam uma vitalidade mensurável numa régua de 0 a 10.000 “unidades Bovis”, com o humano saudável em torno de 6.500. "
                "Mermet acrescenta a leitura por deslocamento: o valor é o ponto onde o movimento do pêndulo muda.",
         mede="Mede a vitalidade da pessoa, de um órgão, de um cômodo, da água ou de um alimento, antes e depois de cada sessão. O G20b usa a mesma leitura por deslocamento numa régua numérica.",
         graficos=["G3", "G20b", "G69"],
         ler="Partir de 6.500 e deslizar; aceitar se duas varreduras ficarem a até 250. Abaixo de 6.500 perde energia; abaixo de 4.500 (convenção deste manual) entra o pré-ciclo de limpeza.",
         limites="A unidade é convencional e só vale dentro da mesma régua: compara a pessoa com ela mesma, nunca substitui exame ou medida física."),

    dict(nome="Chakras: estados e movimentos (Brennan, Judith, Myss)",
         origem="Barbara Brennan (Mãos de Luz, método atribuído a John Pierrakos), Anodea Judith e Caroline Myss (anos 1980–90)",
         afirma="Cada chakra é um centro de energia ligado a órgãos e a temas de vida. Brennan lê a forma do giro sobre o corpo (aberto, fechado, elipse, desvio); "
                "Judith descreve deficiência como evitação e excesso como compensação; Myss liga cada centro a órgãos e questões emocionais.",
         mede="Mede percentual, giro, forma do movimento e aspecto anterior ou posterior de cada chakra, e os órgãos e sinais ligados a ele.",
         graficos=["G5", "G6", "G6b", "G7", "G29", "C{k}-sinais", "C{k}-corpo"],
         ler="Círculo horário é chakra aberto; anti-horário, fechado; as outras formas apontam a primeira hipótese de causa no G8. O encaminhamento forma → setor é convenção deste manual.",
         limites="Chakras são um modelo da tradição energética, sem correspondência anatômica comprovada; sintoma físico vai ao médico."),

    dict(nome="Corpos sutis e aura",
         origem="Tradição teosófica (sete corpos) usada nas formações brasileiras; vocabulário dos biômetros de aura de referência e do Pêndulo Hebraico",
         afirma="Em volta do corpo físico haveria camadas cada vez mais sutis (etérico, astral, mental inferior e superior, búdico, átmico) que formam a aura. "
                "Cada camada abrigaria um tipo de conteúdo: vitalidade no etérico, emoção no astral, crença no mental, votos no causal.",
         mede="O G60 mede em qual corpo a causa está alojada; o G63 mede o estado da aura em quatro anéis: tamanho, proteção, integridade e conteúdo.",
         graficos=["G60", "G63"],
         ler="O corpo indicado escolhe a técnica (astral: emoção e limpeza; mental: crença e comando; causal: votos no G59). Aura aberta ou com furos pede proteção antes de qualquer remoção.",
         limites="A correspondência corpo × tipo de causa e a montagem em quatro anéis são convenção deste manual; não há medida física da aura."),

    dict(nome="Emotion Code (emoções presas)",
         origem="Bradley Nelson, quiroprático norte-americano, 2007",
         afirma="Emoções intensas não processadas ficariam “presas” no corpo como energia e sustentariam dores e padrões. "
                "Um gráfico de 60 emoções em 6 linhas (pares de órgãos) e 2 colunas é navegado por sim e não; a emoção achada é liberada com passadas de ímã ou da mão ao longo da coluna.",
         mede="Mede se há emoção presa, qual é (bissecção no G9 ou lista do chakra), de onde veio (G19), em que fase da vida (G35), com quem (G36) e se é preciso decodificar mais.",
         graficos=["G9", "C{k}-emocoes", "G19", "G21", "G35", "G36", "G58", "G61"],
         ler="Coluna, metade das linhas, linha, emoção. Liberar com 3 passadas (10 se herdada) e reperguntar. Linhas 2, 3 e 5 do G9 são reconstruídas, a conferir; “coletiva” no G19 é acréscimo deste manual.",
         limites="Não há prova de que emoções fiquem presas em órgãos; a liberação não trata doença nem substitui psicoterapia em trauma grave."),

    dict(nome="Body Code (árvore de causas)",
         origem="Bradley Nelson; mapa de causas publicado em livro em 2023",
         afirma="Problemas físicos, mentais e emocionais teriam causas em seis áreas: energias (emocionais e ofensivas), circuitos e sistemas, toxinas, patógenos, desalinhamentos, nutrição e estilo de vida. "
                "O praticante desce a árvore por sim e não até o item.",
         mede="Mede a categoria da causa principal no G8 e, no setor físico, o subtipo no G57; o G58 pergunta o que sustenta a causa (“precisamos saber mais?”).",
         graficos=["G8", "G57", "G58"],
         ler="Um setor por vez, do geral ao item. Os setores ambiental e transgeracional do G8 e os itens dentária, álcool e drogas e cicatriz do G57 são acréscimos deste manual.",
         limites="Toda causa física é hipótese energética: sintoma persistente ou de alerta vai ao médico antes de qualquer harmonização."),

    dict(nome="Medicina chinesa: órgãos e emoções",
         origem="Medicina tradicional chinesa, adotada pelo Emotion Code para ordenar as linhas do gráfico de 60 emoções",
         afirma="Cada par de órgãos (coração e intestino delgado, baço e estômago, pulmão e cólon, fígado e vesícula, rim e bexiga, glândulas e órgãos sexuais) "
                "teria um grupo de emoções próprio: raiva no fígado, tristeza no pulmão, medo no rim, mágoa no coração.",
         mede="Mede em qual linha (par de órgãos) a emoção presa está, e por ela liga a emoção ao chakra do capítulo.",
         graficos=["G9", "C{k}-emocoes"],
         ler="A linha indica o tema (vínculo, digestão da vida, soltar, reação, medo, valor próprio) e o chakra provável. A seleção de emoções por chakra é convenção deste manual.",
         limites="É um mapa simbólico de uma tradição; não indica doença no órgão nem dispensa exame."),

    dict(nome="Conflito biológico (Germânica e biodescodificação)",
         origem="Ryke Geerd Hamer, Nova Medicina Germânica (anos 1980), adotada pela biodescodificação de Claude Sabbah, Christian Flèche e Enric Corbera",
         afirma="Um sintoma seria a resposta do corpo a um choque inesperado vivido em isolamento. Cada tipo de conflito atingiria tecidos de um folheto embrionário: "
                "“bocado” (endoderma), ataque ou ninho (mesoderma antigo), desvalorização (mesoderma novo), separação e território (ectoderma).",
         mede="O G27 mede o tipo de conflito por trás de um sintoma; o G61 pergunta se houve um evento específico (o choque).",
         graficos=["G27", "G61"],
         ler="O resultado é só uma ponte: o conflito leva a uma emoção (G9) ou a uma crença (G10), e é isso que se trata. Uso opcional.",
         limites="Sem reconhecimento científico; Hamer perdeu a licença médica. Nunca usar para explicar doença grave nem para adiar tratamento."),

    dict(nome="Louise Hay e o teste de frases (PSYCH-K)",
         origem="Louise Hay (Você pode curar sua vida, Cure seu corpo, anos 1980); teste de frases do PSYCH-K, de Rob Williams",
         afirma="Hay liga cada problema do corpo a um padrão mental (causa provável) e propõe um novo padrão de pensamento em forma de afirmação; as causas-mestras seriam crítica, raiva, ressentimento e culpa. "
                "O PSYCH-K testa frases como verdadeiras ou falsas para achar a crença instalada.",
         mede="Mede a família de crença (G10) e a frase exata que a pessoa carrega (G55); nos capítulos de chakra, a linha de Hay acompanha o órgão do C{k}-corpo.",
         graficos=["G10", "G55", "C{k}-corpo"],
         ler="A frase que testa sim vira afirmação invertida e é testada até 80. As oito famílias e as frases do G55 são construção deste manual.",
         limites="A ligação crença × doença é simbólica e sem prova; afirmação acompanha, não substitui, tratamento médico ou psicológico."),

    dict(nome="Cinco feridas de infância (Bourbeau)",
         origem="Lise Bourbeau, As Cinco Feridas Emocionais (Canadá, anos 2000)",
         afirma="Cinco feridas da infância (rejeição, abandono, humilhação, traição, injustiça) levariam a criança a criar máscaras: fugitivo, dependente, masoquista, controlador e rígido. "
                "Cada ferida teria um progenitor, uma idade de despertar e um maior medo.",
         mede="Mede qual ferida instalou a crença, com quem e em que idade, para dirigir a cadeia de decodificação.",
         graficos=["G11", "G10", "G55"],
         ler="A ferida leva à época (G35), à afirmação e ao chakra. Ferida e máscara são literais; idades e maior medo de três feridas vêm de memória da obra, a conferir.",
         limites="É uma tipologia de autoajuda, não diagnóstico psicológico; sofrimento intenso vai a psicólogo."),

    dict(nome="Barômetro do Comportamento",
         origem="Gordon Stokes e Daniel Whiteside, Three In One Concepts / One Brain (kinesiologia, anos 1980)",
         afirma="Um mesmo tema pode estar preso em três níveis: consciente (presente), subconsciente (passado) e corpo (memória celular). "
                "Cada nível tem pares positivo e negativo, como aceitação e antagonismo, segurança e medo de perder, escolha e sem escolha.",
         mede="O G56 mede o nível, o lado e a categoria em que a crença está; serve também para medir o depois.",
         graficos=["G56", "G10", "G55"],
         ler="Consciente pede conversa e afirmação; subconsciente, idade e evento; corpo, liberação. Depois do trabalho a mesma categoria deve passar ao lado positivo.",
         limites="As palavras de apoio são adaptação em português (o original tem cerca de 150); o barômetro organiza a conversa, não mede personalidade."),

    dict(nome="Psicogenealogia, constelações e linhagem",
         origem="Anne Ancelin Schützenberger (síndrome do aniversário), Ivan Boszormenyi-Nagy (lealdades invisíveis), Claude Sabbah (projeto-sentido), Bert Hellinger (constelações)",
         afirma="Dores e repetições podem vir da história da família: a pessoa repete o destino de um antepassado para pertencer, adoece na idade em que um avô viveu um drama, "
                "ou carrega o lugar de alguém excluído. A família funciona como um sistema com regras de pertença.",
         mede="O G17 mede linhagem, gerações, mecanismo e tema, um anel por vez; o setor transgeracional do G8 e a origem “herdada” do G19 levam até ele.",
         graficos=["G17", "G8", "G19"],
         ler="A causa herdada é liberada “em toda a linhagem” (10 passadas) com frase de reconhecimento. A montagem em quatro anéis é convenção deste manual.",
         limites="Valor heurístico, não causal: não acusa parentes nem revela fatos; temas pesados de família pedem terapeuta habilitado."),

    dict(nome="Ganho secundário",
         origem="Conceito da psicologia clínica",
         afirma="Um problema pode trazer, sem que a pessoa perceba, alguma vantagem: atenção, proteção contra um conflito, uma identidade, lealdade à família. "
                "Enquanto essa necessidade não for atendida de outro modo, a mudança não se sustenta.",
         mede="O G62 mede que ganho mantém o problema; entra antes de toda harmonização.",
         graficos=["G62"],
         ler="Devolver sem culpa: o ganho é uma necessidade legítima a atender de outro modo. “Nenhum ganho” libera a harmonização. Os itens são convenção deste manual.",
         limites="O pêndulo só abre a conversa; não é avaliação psicológica."),

    dict(nome="Escala de Hawkins (mapa da consciência)",
         origem="David R. Hawkins, Poder versus Força (1995)",
         afirma="Estados emocionais formariam uma escala de 20 (vergonha) a 700 (iluminação); abaixo de 200 (coragem) a pessoa operaria por força e contração, acima por poder próprio.",
         mede="Mede o estado emocional da pessoa no início e no fim da sessão, como fazem as mesas de referência (Mannah, Mapa de Atendimento).",
         graficos=["G54"],
         ler="O número é o “antes e depois” devolvido à pessoa. Abaixo de 200: trabalho emocional primeiro; meta da sessão é subir ao menos um nível.",
         limites="Os números de Hawkins são do autor, sem validação; nunca usar para julgar o valor de alguém."),

    dict(nome="Interferências espirituais (escolas brasileiras e Mannah)",
         origem="Cursos e serviços brasileiros de limpeza, definições espíritas, apometria; Mesa de Autodiagnóstico da escola Mannah; Domingues (origens)",
         afirma="Além de emoções e crenças, a pessoa ou o lugar carregaria energias alheias: miasmas, larvas, formas-pensamento, egrégoras, cordões, implantes, obsessores. "
                "Domingues as classifica pela origem: própria, captada, provocada ou telúrica. A mesa Mannah tem cosmologia própria de seres.",
         mede="Mede qual interferência está presente (G15, G34), de onde veio (G28), que influência ou ser nomeia (G50, G51) e de quem é a energia de um cômodo (G82).",
         graficos=["G15", "G18", "G28", "G34", "G50", "G51", "G64", "G82"],
         ler="Cada item pede uma técnica (Parte VII); seres recebem sempre o mesmo tratamento: encaminhar, nunca confrontar. Os nomes dos leques Mannah são da escola, mantidos por continuidade.",
         limites="São crenças de escola, sem lista oficial nem prova; medo intenso, vozes ou ideias de perseguição vão a médico ou psicólogo."),

    dict(nome="Comandos de Raymon Grace",
         origem="Raymon Grace, radiestesista norte-americano (Techniques That Work For Me, How to Balance and Clear a School, anos 2000)",
         afirma="A intenção do operador, dita como comando enquanto o pêndulo gira, mudaria a energia de pessoas e lugares: embaralhar (scramble) a frequência, neutralizar, "
                "transformar, ajustar à frequência desejada e preencher o vazio. Anti-horário remove; horário acrescenta.",
         mede="Mede a carga não benéfica ou benéfica de um item na escala −100 a +100 (G4) e escolhe o verbo do comando (G68) e a técnica (G22, G65).",
         graficos=["G4", "G22", "G65", "G68", "G71"],
         ler="Medir, comandar com giro anti-horário até o pêndulo parar, preencher com giro horário, remedir no G4. “Encaminhar”, “dissolver” e “selar” vêm das escolas brasileiras.",
         limites="Nenhuma escola brasileira ensina Grace por nome; o comando é ritual de intenção, sem efeito comprovado."),

    dict(nome="Pêndulo Hebraico",
         origem="Jean de La Foye (Ondes de vie, ondes de mort, 1975); escola Mitnik e cursos brasileiros",
         afirma="Palavras hebraicas escritas em etiquetas, presas a um pêndulo de madeira, emitiriam uma onda específica: limpeza, proteção, cura, paz, desapego. "
                "A sessão tem abertura, leitura, escolha da etiqueta, tratamento com o lado estriado e selamento.",
         mede="O G44 mede qual etiqueta usar em cada fase; o mesmo pêndulo aparece nas listas de intrusos (G64), nas técnicas de limpeza (G65) e no fechamento (G67).",
         graficos=["G44", "G64", "G65", "G67"],
         ler="Lado liso testa, estriado irradia; cerca de 1 minuto por chakra; parado indica fim. A etiqueta Tav não foi encontrada nas fontes.",
         limites="Não há conjunto padronizado de etiquetas e as traduções divergem; é técnica de harmonização, não de tratamento médico."),

    dict(nome="Gráficos radiônicos",
         origem="Radiônica francesa e belga (Servranx, Chaumery e De Bélizal) e brasileira (António Rodrigues); mesas seletoras das formações brasileiras",
         afirma="Desenhos geométricos com o testemunho no centro emitiriam uma “onda de forma” que age à distância sobre a pessoa ou o lugar representado. "
                "Cada gráfico tem uma função (limpar, proteger, prosperar) e um tempo de uso.",
         mede="O G41 mede qual gráfico usar, por categoria; o G23 mede o tempo; a eficácia vai ao G2.",
         graficos=["G41", "G23", "G22", "G65", "G67", "G71"],
         ler="Testemunho a lápis em papel novo, desimpregnar, potencializar, deixar o tempo indicado e confirmar com o pêndulo antes de retirar. O pêndulo escolhe, não a preferência do operador.",
         limites="Não há prova de efeito da onda de forma; gráfico nunca substitui remédio prescrito."),

    dict(nome="Cromoterapia",
         origem="Apostilas brasileiras de cromoterapia, sobre a tradição de cores por chakra",
         afirma="Cada chakra teria uma cor (do vermelho no básico ao violeta no coronário). A cor própria estimularia um chakra em falta e a complementar acalmaria um em excesso.",
         mede="Mede a cor para o chakra (G42), para a roupa (G100) e os alimentos por cor (G97).",
         graficos=["G42", "G100", "G97", "G22"],
         ler="Hipoativo: cor própria; hiperativo: complementar; de 20 segundos a 30 minutos conforme a fonte de luz. Verde é a cor de segurança quando há dúvida.",
         limites="As tabelas de complementares divergem entre escolas; não há efeito clínico comprovado."),

    dict(nome="Florais de Bach",
         origem="Edward Bach, médico inglês (anos 1930)",
         afirma="38 essências de flores, em sete grupos emocionais (medo, incerteza, desinteresse pelo presente, solidão, hipersensibilidade, desalento, preocupação excessiva com os outros), "
                "atuariam sobre o estado emocional, não sobre a doença. O Rescue reúne cinco essências para emergência.",
         mede="O G45 mede o grupo e a essência (até seis); o G96 mede a dose, passo a passo, com confirmação.",
         graficos=["G45", "G96", "G22"],
         ler="Primeiro o grupo, depois a essência. Posologia corrente: 4 gotas, 4 vezes ao dia; o G96 confirma ou ajusta para a pessoa.",
         limites="A seleção por pêndulo não é o método de Bach; floral não substitui medicação nem tratamento de quadro grave."),

    dict(nome="Cristais, óleos e frequências por chakra",
         origem="Tabelas de cristais, de aromaterapia e de sons das apostilas e cursos brasileiros; escala Solfeggio das mesas radiônicas",
         afirma="Cada chakra teria pedras, óleos essenciais e frequências afins: jaspe e hematita no básico, quartzo rosa no cardíaco, ametista no coronário; patchouli na base, lavanda e olíbano no alto; de 174 a 963 Hz.",
         mede="O G46 mede o cristal, o G47 o óleo e o G43 a frequência; o G104 as ervas por chakra.",
         graficos=["G46", "G47", "G43", "G104", "G22"],
         ler="Escolher pelo pêndulo dentro da lista do chakra; programar o cristal (limpar, energizar, declarar a intenção). As listas convergem no núcleo e divergem na periferia.",
         limites="Listas de uso corrente, sem fonte única; a ligação Solfeggio × chakra não tem base acústica; nenhuma fonte dá dose de ervas."),

    dict(nome="Geobiologia (Hartmann, Curry, veios d'água)",
         origem="Ernst Hartmann, Manfred Curry e Anton Benker (Alemanha, meados do século XX); escolas francesas e inglesas; curso CEAP",
         afirma="O solo emitiria redes de linhas (Hartmann norte-sul e leste-oeste; Curry em diagonal) e zonas nocivas sobre veios d'água e falhas. "
                "Dormir ou trabalhar sobre um cruzamento causaria estresse geopático, com distúrbio do sono como sinal mais citado.",
         mede="Mede a fonte que pesa no ambiente (G16, G66), o lugar de maior permanência (G25, G83) e a técnica de limpeza do espaço (G71).",
         graficos=["G16", "G25", "G66", "G71", "G83"],
         ler="O pior caso é cruzamento sob a cama ou a mesa: mover a cama 30 a 70 cm, isolar, usar gráfico e remedir em 7 dias. Campos de aparelhos têm evidência própria para reduzir no quarto.",
         limites="As redes não têm validação científica; mofo, umidade, ruído e fiação defeituosa se verificam com técnico."),

    dict(nome="Baguá e radiestesia de mapa",
         origem="Baguá do feng shui (tradição chinesa) aplicado à planta pelos cursos brasileiros; radiestesia de mapa das sociedades americana e canadense; António Rodrigues",
         afirma="O baguá divide a casa em oito áreas de vida e um centro, a partir da porta de entrada, cada uma com elemento, cor e forma. "
                "A radiestesia de mapa afirma que o pêndulo localiza algo sobre uma planta ou mapa por grade, bissecção e triangulação.",
         mede="O G70 mede a área de vida que pesa no imóvel; G72 a G75 localizam cômodo, objeto ou fonte (grade, direção, distância, altura).",
         graficos=["G70", "G72", "G73", "G74", "G75"],
         ler="Área fraca recebe cor, planta ou pedra e limpeza. Na localização, confirmar com sim ou não e ir ao local. G73, G74 e o anel de altura do G75 são construção deste manual.",
         limites="Localizar nunca serve para seguir pessoas; o resultado é hipótese a conferir no local."),
]

GLOSSARIO = [
    ("Testemunho", "Representação da pessoa ou do lugar medido à distância: nome completo e data de nascimento a lápis em papel branco novo, foto ou endereço."),
    ("Biômetro", "Gráfico de medida com escala ou setores (percentual, Bovis, leque) sobre o qual o pêndulo indica um valor ou uma categoria."),
    ("Leque", "Gráfico em semicírculo de 180 graus, com o vértice na base e setores; o pêndulo oscila no vértice e se alinha ao setor da resposta."),
    ("Bissecção", "Navegação de tabelas e grades por sim ou não, dividindo ao meio: coluna, metade das linhas, linha, célula, item. Nunca varrer."),
    ("Giro horário", "Na convenção do manual: sim, aberto, repõe energia. Anti-horário: não, fechado, extrai. Parado: neutro ou concluído."),
    ("Convenção de respostas", "Movimentos combinados no início da sessão para pronto, sim, não, nenhuma das anteriores e “não posso ou não devo” (G1)."),
    ("Permissão tripla", "Trio “posso, devo, estou pronto para medir?”, repetido a cada mudança de assunto; um não encerra o assunto sem insistência."),
    ("Setor “Outro”", "Setor presente em todo leque de causas; quando responde, a sessão vai às listas longas e às perguntas-ponte da Parte V."),
    ("Remedida", "Nova medida, no mesmo biômetro, ao fim da sessão e após 7 dias, para ver se o resultado se manteve; retorno em 21 a 30 dias."),
    ("Pré-ciclo", "Limpeza e proteção feitas antes da leitura dos chakras quando vitalidade, aura ou interferência ativa passam do gatilho (Bovis abaixo de 4.500)."),
    ("Bovis (unidade)", "Unidade convencional de vitalidade na régua de 0 a 10.000; 6.500 é a referência humana e só se compara dentro da mesma régua."),
    ("Cadeia de decodificação", "Sequência que desce da categoria da causa (G8) ao item, à origem, à época e ao que a sustenta, antes de harmonizar."),
    ("Emoção presa", "No Emotion Code, emoção não processada que ficaria retida no corpo e sustentaria um desequilíbrio; é liberada pelo Vaso Governador."),
    ("Vaso Governador", "Meridiano que corre pela coluna e sobre a cabeça; o Emotion Code libera a emoção com 3 passadas de ímã ou mão (10 se herdada)."),
    ("Afirmação invertida", "Frase positiva oposta à crença que testou sim; é testada no pêndulo até chegar a 80."),
    ("Ganho secundário", "Vantagem que a pessoa tem, sem perceber, em manter o problema; precisa ser atendida de outro modo para a mudança se sustentar."),
    ("Lealdade familiar", "Lealdade invisível (Boszormenyi-Nagy): a pessoa repete o destino de um antepassado para continuar pertencendo à família."),
    ("Conflito biológico", "Na biodescodificação, choque inesperado vivido em isolamento que daria origem a um sintoma num tecido de um folheto embrionário."),
    ("Ferida e máscara", "Em Bourbeau, dor de infância (rejeição, abandono, humilhação, traição, injustiça) e o comportamento criado para escondê-la."),
    ("Miasma", "Acúmulo individual de energia densa formado por pensamentos persistentes, segundo as escolas brasileiras e a definição espírita."),
    ("Larva astral", "Forma-pensamento parasita, de baixa frequência, que se alimentaria de emoção; removida com giro anti-horário e Triturador."),
    ("Forma-pensamento", "Pensamento repetido que se cristaliza como energia própria (crítica, medo) e passa a atuar sobre quem pensa ou recebe."),
    ("Egrégora", "Campo coletivo formado por um grupo, família ou instituição, ao qual a pessoa fica ligada; negativa quando pesa sobre ela."),
    ("Cordão", "Ligação energética com outra pessoa ou campo que drena ou prende; cortado com comando e visualização, com consentimento."),
    ("Implante", "Na linguagem das escolas, dispositivo energético alojado no campo (chip, sonda, capacete); tratado com comando de dissolução."),
    ("Corpo etérico", "Primeira camada sutil, colada ao físico; nela estariam a vitalidade e as fugas de energia."),
    ("Corpo astral", "Corpo emocional; abrigaria emoções presas, larvas e miasmas."),
    ("Corpo mental", "Mental inferior: crenças, formas-pensamento e programas. Mental superior ou causal: votos, contratos e temas kármicos."),
    ("Rede Hartmann", "Rede de linhas do solo orientada norte-sul e leste-oeste, com malha de cerca de 2 a 2,5 m; o cruzamento seria o ponto nocivo."),
    ("Rede Curry", "Rede de linhas do solo em diagonal, a cerca de 45 graus do norte; espaçamento divergente entre as fontes."),
    ("Veio d'água", "Curso de água subterrâneo que, pelo atrito com o solo, emitiria uma zona nociva; pior quando cruza uma falha (falha úmida)."),
    ("Baguá", "Octógono do feng shui com oito áreas de vida e um centro, sobreposto à planta a partir da porta de entrada."),
    ("Memória de parede", "Ideia das escolas brasileiras de que o ambiente registra o campo de quem mora e frequenta, e o cômodo passa a espelhar essas pessoas."),
    ("Ideomotor", "Movimento muscular involuntário guiado pela expectativa, que a ciência aponta como a causa do movimento do pêndulo."),
    ("Regra do terceiro", "Outra pessoa só entra como parte da relação de quem é atendido; medi-la como pessoa exige autorização explícita dela."),
]
