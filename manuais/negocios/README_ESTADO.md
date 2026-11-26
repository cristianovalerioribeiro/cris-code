# Manual de Radiestesia para Negócios — estado do projeto (edição 1, novembro de 2026)

Leia este arquivo antes de qualquer alteração. Ele complementa `../radiestesia/README_ESTADO.md`, que guarda as regras do motor (diagramação, armadilhas do WeasyPrint e do Word, ferramentas) e vale integralmente aqui.

## O que é
Manual completo e independente para quem responde por um negócio: dono, sócio, empreendedor, profissional liberal, incorporador. Doze Partes (fundamentos; decisão; a empresa como um todo; sócios, parceiros e investidores; propostas e contratos; projetos, produtos e preços; pessoas e equipe; interferências e bloqueios; espaço, ponto, terreno e empreendimento imobiliário; finanças e prosperidade; o empreendedor como pessoa; registro e calibração), mapa do método com fluxo mestre empresarial e dez cartões de bifurcação (D1 a D10), glossário. Base de conteúdo: nota de pesquisa `../research_notes/Protocolos de radiestesia/14_radiestesia_negocios_mapeamento.md` (bibliografia, evidência, ética) e as Partes XII a XIV do manual terapêutico.

## Entregáveis
- `Manual_de_Radiestesia_para_Negocios.pdf` — A4 deitado, frente e verso, PAGINAS páginas, 45 gráficos.
- `Fichas_de_Decisao_Empresarial.pdf` — 7 páginas: matriz opções × critérios, diagnóstico 360, sociedade, proposta, laudo complementar de terreno ou ponto, Roda da Vida, diário de decisões (`build_fichas.py`, `content_fichas.py`).
- `Graficos_para_Impressao_Negocios.pdf` — só os gráficos, dois por folha, listas em paisagem (`build_print.py`).

## Gráficos: numeração compartilhada
- G1 a G110 reaproveitados do manual terapêutico **sem alteração do desenho** e com a mesma numeração (regra fixa dos dois manuais): G1, G2, G3, G4, G9, G10, G24, G28, G59, G62, G66, G67, G69, G70, G71, G82, G83, G84 a G92, G94, G95, G101, G103, G106 a G110 (35). `gen_charts.py` copia os SVG de `../radiestesia/charts/` e escreve `charts/manifest.json`.
- G111 a G120 são deste manual: G111 Trava da decisão (leque 12), G112 Proposta ou contrato: pontos de atenção (12), G113 Onde trava a negociação (8), G114 Modelo de negócio: bloco frágil (9), G115 Fase do negócio (8), G116 Terreno para empreender: critérios (12), G117 Empreendimento: onde está o peso (12), G118 Compatibilidade para um objetivo (escala 0 a 100 com dois testemunhos e campo Objetivo), G119 Interferência no negócio: onde está (8), G120 Ponto comercial: critérios (12). Gráfico novo seguinte: **G121**. Cartão novo seguinte: **D11**.
- Interpretações (`interp.py`): as dos gráficos reaproveitados foram reescritas onde apontavam para chakras, Nível 2, Partes VII e VIII ou gráficos que aqui não existem; a remissão padrão é "atendimento pessoal pelo Manual de Radiestesia Terapêutica". Rotas (`routes.py`) só apontam para gráficos deste manifest ou para âncoras deste manual (`check_all.py` confere).
- G82 e G83 mantêm os setores de família do desenho; a interpretação manda ler parceiro, filho, pai, mãe, irmão e outro morador como sócio, funcionário e demais usuários do espaço, e quarto, sala e trabalho fora como posto próprio, mesa compartilhada e home office.

## Montar e checar
- `python3 gen_charts.py` → `charts/`; `python3 build_book.py` (seis passagens, ~45 s cada) → PDF; `python3 check_all.py` e `python3 audit_breaks.py`; `python3 build_fichas.py`; `python3 build_print.py`.
- Motor copiado de `../radiestesia/` sem mudança de lógica. Diferenças só de dados: `bookkit.py` (ANCHOR_LABELS, SHORT, TAB_LABEL e `page_group`: abas I–III, IV–VIII, IX–XII), `build_book.py` (importa `content_front` e `content_parts`; título e nome do PDF), `content_rotas.py` (fluxo mestre com oito portas, três bifurcações e um retorno; cartões e glossário genéricos), nomes de arquivo nas ferramentas.
- Word: `python3 word/html2ir.py && node word/build_docx.js && python3 word/fix_docx.py Manual_de_Radiestesia_para_Negocios.docx` (não gerado nesta edição).

## Convenções fixas (não mudar sem pedido)
- Faixas: favorável 70 a 100; incerto 40 a 69; desfavorável abaixo de 40; empate = diferença menor que 10 pontos; autoauditoria acima de 30 = parar; risco acima de 70 = plano de saída; Bovis de lugar abaixo de 6.500 = o espaço vem antes; sociedade abaixo de 50 não, 50 a 69 por projeto com prazo, 70 ou mais contrato; emissores a cada 14 dias; revisão de toda decisão em 90 dias; remedida de espaço em 7 dias.
- Giro horário = sim, favorável; anti-horário = não; parado = neutro.
- Regra do terceiro e veto absoluto à seleção, avaliação, promoção ou desligamento de pessoas por pêndulo; funcionários e candidatos só como função, momento e, com consentimento, relação. Sem nome completo e data de nascimento de terceiros no testemunho.
- O laudo de terreno ou ponto leva o cabeçalho fixo "análise radiestésica complementar; não substitui sondagem geotécnica, laudo ambiental, medição de radônio e de campos eletromagnéticos por instrumento, nem a análise jurídica da matrícula".
- Nada de "física quântica" como prova, promessa de resultado ou de atrair clientes; "energia" como palavra da tradição, declarada como tal.
- Terminologia: "formações brasileiras", "de referência", "acervo de referência" no lugar de nomes de arquivo, Drive ou sites. Os Servranx são citados nominalmente como fonte histórica (gráficos nº 10, 11, 14, 18 e a passagem comercial de *Vos débuts en radiesthésie*).

## Limites conhecidos
- G114 (modelo de negócio) e G115 (fase) são construções de gestão, declaradas como tal; G116, G117, G120 são construções deste manual moldadas no G107 e no G92; não há método publicado para ponto comercial.
- O "mapa empresarial Servranx" dos cursos brasileiros não tem fonte Servranx identificada; a tradução do acervo termina no gráfico nº 30 de 66.
- Sem posologia, sem previsão, sem bolsa. Os emissores de prosperidade são os de referência do mercado luso-brasileiro, não dos Servranx.

## Edição 1 (nov. 2026)
- Primeira montagem: PAGINAS páginas, 0 órfãos e restos, sem link vazio nem página vazia; caudas acima de 45 mm só no sumário, no fim do mapa (abertura da Parte I) e no fim do livro.
