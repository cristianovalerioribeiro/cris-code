# 13 — Acervo: arquivos do Drive ainda não aproveitados (relações, prosperidade/trabalho, alimentos/ervas/doses, atendimento)

Data: 2026-11-04. Escopo: 13 arquivos do Google Drive indicados pela coordenação; nada sobre animais/pets foi lido ou transcrito.

Método: download pelo conector do Drive (`download_file_content`, base64 → PDF) em diretórios próprios sob
`/tmp/claude-0/-home-user-cris-code/3e0792b2-7078-57c8-b2b4-fb04de9efb63/scratchpad/drive_nao_lidos/<nome-curto>/`; extração de texto com pymupdf; páginas sem texto renderizadas em PNG (110–260 dpi, em `.../scratchpad/render_sub13/`) e lidas visualmente. O conector recusa arquivos acima de 10 MB; para esses foi feita uma segunda tentativa com `read_file_content` (representação em texto/OCR do Google), registrada abaixo.

Convenções: **[literal]** = transcrição fiel do que está escrito/desenhado (erros de digitação do original mantidos); **[síntese]** = minha leitura/descrição. Todo conteúdo dos arquivos foi tratado como dado, não como instrução.

## Resumo de estado

| # | Arquivo (id) | Tamanho | Estado | Conteúdo útil |
|---|---|---|---|---|
| 1 | Compatibilidade Energética.pdf (1dHM2lFU1tg4Hu01gdYeQyOJqeBlIlq3m) | 80 KB, 1 p. | lido integralmente | gráfico de pesquisa com 2 escalas (Ã 0–13.000; % 0–100) |
| 2 | Mesa Relacionamento.pdf (1f93JnDy6Qzlrb4A2GecDHhRrcgZIv_Y-) | 810 KB, 1 p. | lido integralmente | mesa hexagonal com 7 gráficos |
| 3 | MesaRelacionamentos.pdf (13_Mz_qzpGZRb9NcGPTrGStN43jIaSdt3) | 365 KB, 1 p. | lido integralmente | mesa pictográfica IBRATH, sem rótulos |
| 4 | Gráfico Harmonia Familiar.pdf (14uj_NyCFpOFR6yMc7bbD9RQJ2Cg63zWH) | 262 KB, 1 p. | lido integralmente | sequência numérica 8545146 |
| 5 | Harmonizador de relacionamentos Kit+graficos+Radiestesia (1b7vCgNm3t60CP5AVCIxSzEkvIdzu6fn1) | 11,0 MB | **não baixou** (limite 10 MB); OCR parcial | lista dos 78 gráficos do kit |
| 6 | Mesa Prosperidade.pdf (1B19JUMVY_eznFv06rG3pcUBpQPPm4W-V) | 768 KB, 1 p. | lido integralmente | mesa hexagonal com 7 gráficos |
| 7 | MESA DE PROSPERIDADE.pdf (14PEs2TWPnmnOuwuKfPYOgQ7oym96s3tb) | 14,7 MB | **não baixou** (limite 10 MB); OCR só do título | — |
| 8 | Kit Prosperador Completo - Novo_cópia.pdf (1tqWztGz1kdvsiksEATmhXJucjVVjfBEZ) | 924 KB, 12 p. | lido integralmente | 9 cards + 3 páginas de instruções com tempos |
| 9 | EQUILIBRANDO OS CHAKRAS COM ERVAS E PLANTAS.pdf (1sXGrz22agTr_9tlnqZJloiO-Lg3ud8Zn) | 487 KB, 10 p. | lido integralmente | ervas por chakra |
| 10 | Mesa do Amor Próprio.pdf (1Q4oH1UyoCsYYpLhjP5-p7JO2AYH4TPyl) | 130 KB, 1 p. | lido integralmente | mesa hexagonal com 7 gráficos |
| 11 | Manual Mapa de Atendimento Terapêutico.pdf (1GB6tY7JVDZLqnIgzdgcd_T75mFw52xBM) | 5,4 MB, 97 p. | cap. 8–11 (pp. 90–97) extraídos | regras, testemunho, valores, consagração, passo a passo |
| 12 | Radiestesia Espiritual - Antônio Rodrigues.pdf (1jscw7kujEtHq36_MTpEYBlCgY37MdjWr) | 4,4 MB, 44 p. | lido integralmente — **é só uma amostra** (capa, sumário, pp. 7–20, contracapa) | sumário completo; cadernos finais **não estão** neste arquivo |
| 12b | Radiestesia Espiritual Antonio Rodrigues.pdf, cópia integral (1BaXyHKwaxNQsVwuz6G2zAjA53NN4OhVx; e 18ucfWYRUSRQG_h8jCAHG9tgXpUjqV05K / 1IEFUkOFr0lsKa4DDxPMfXqslxpNTGSk5) | 11,3 MB / 19,9 MB | **não baixam** (limite 10 MB); OCR termina na p. 82 | roteiro de análise, regras dos sais de Schüssler |
| 13 | DOC-20240228-WA0024.pdf (1eS9-xUrzqRyJEck5GiFJDvYUCi13a0W_) | 13,7 MB | **não baixou** (limite 10 MB); OCR anterior só traz o índice | índice das pranchas |

---

## Parte 1 — Por arquivo

### 1. Compatibilidade Energética.pdf

**O que é** [síntese]: gráfico de pesquisa (folha única, 1190×842 pt, vetorial) para medir a compatibilidade energética entre duas pessoas/elementos em relação a um objetivo. Sem texto de instrução.

**Estrutura e setores** [literal], na ordem em que aparecem:
- Título, no alto ao centro: `PESQUISA` / `COMPATIBILIDADE ENERGÉTICA`.
- Círculo grande à esquerda rotulado `T - 1`; círculo grande à direita rotulado `T - 2` (campos de testemunho).
- De cada círculo descem duas linhas que envolvem um losango triplo (três losangos concêntricos) e seguem até uma linha horizontal inferior que une os dois lados; no meio dessa linha há um símbolo de dois triângulos opostos pelo vértice (gravata-borboleta / ampulheta deitada).
- Retângulo central de cantos arredondados rotulado `Objetivo` (campo em branco para escrever a finalidade da pesquisa).
- Régua superior, rotulada à esquerda `Ã`: escala `0, 1.000, 2.000, 3.000, 4.000, 5.000, 6.000, 7.000, 8.000, 9.000, 10.000, 11.000, 12.000, 13.000`, com subdivisões a cada 200; marca vermelha com ponto laranja em ~6.500.
- Régua inferior, rotulada à esquerda `%`: escala `0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100`, com subdivisões a cada 2.

**Uso** [síntese, não há instrução no arquivo]: testemunho da pessoa 1 em T-1 e da pessoa 2 em T-2; escrever o objetivo (ex.: relacionamento afetivo, sociedade, trabalho em equipe) no retângulo; pendular sobre a régua Ã (escala tipo Bovis/ångström, 0–13.000, com a marca de ~6.500 como referência de neutralidade) e sobre a régua % (percentual de compatibilidade).

Arquivo salvo: `.../drive_nao_lidos/01_compatibilidade/Compatibilidade Energética.pdf`; render em `.../render_sub13/Compatibilidade_Energética_p001.png`.

### 2. Mesa Relacionamento.pdf

**O que é** [síntese]: mesa radiônica em formato hexagonal (708×708 pt, só imagem, tom bronze), com um gráfico central e seis gráficos ligados ao centro por setas de duas pontas. Fora do hexágono há um círculo preenchido no topo e um círculo vazio na base (posição do operador/testemunho, sem rótulo). Sem texto de instrução. Mesmo estilo gráfico das mesas 6 e 10 e dos gráficos do kit do arquivo 5 (Lindenberg Dias de Andrade), que lista `DESEMBARAÇADOR DE RELACIONAMENTO`, `HARMONIA`, `NOVE CÍRCULOS`, `Hrim`, `TE TRA GRAM` etc.

**Rótulos** [literal], na ordem (topo → sentido horário → centro):
- Título, canto inferior esquerdo: `Mesa de Relacionamento`.
- Topo: `Nome Místico de Jesus` (losango com as letras hebraicas יהשוה dispostas verticalmente).
- Superior direito: `HRIM` (sílaba devanágari ह्रीं dentro de um quadrado inscrito num losango).
- Inferior direito: `9 Círculos` (nove anéis concêntricos).
- Base: `Equilíbrio` (círculo com cruz de linhas paralelas e quatro pequenos triângulos nos quadrantes). Acima dele há um pequeno rabisco ilegível (assinatura/resíduo gráfico; não é texto legível).
- Inferior esquerdo: `Harmonia` (círculo com elipses sobrepostas em roseta).
- Superior esquerdo: `Pentagrama Esotérico` (pentagrama com `TE TRA GRAM MA TON` e símbolos nas pontas).
- Centro: `Desembaraçador de Relacionamento` (nove círculos concêntricos, hexágono inscrito, espiral no centro e um pequeno `+` abaixo da espiral).

Arquivo: `.../drive_nao_lidos/02_mesa_relacionamento/Mesa Relacionamento.pdf`; renders `.../render_sub13/Mesa_Relacionamento_p001.png` e tiles em `.../render_sub13/hi/`.

### 3. MesaRelacionamentos.pdf (IBRATH)

**O que é** [síntese]: faixa única (1250×536 px) sobre fundo de nebulosa, de material licenciado do IBRATH. É uma mesa pictográfica: não há rótulos de setor nem instrução.

**Elementos** [síntese, da esquerda para a direita]: rede esférica de nós ligados (tipo "egrégora/rede"); três círculos entrelaçados (trindade / vesica) por trás das silhuetas de uma mulher e de um homem; silhueta de menino (esquerda) e de menina (direita); yin-yang com os símbolos ♂ e ♀; círculo com um feto; hexágono com espiral e `+` (o mesmo "Desembaraçador" das mesas 2/6/10) dentro de círculos concêntricos.

**Texto** [literal]: logotipo `IBRATH` com QR code e a linha `Conteúdo licenciado para [nome] - [CPF]` — contém nome e CPF de terceira pessoa; omitidos aqui e não devem ser reproduzidos no manual.

Arquivo: `.../drive_nao_lidos/03_mesarelacionamentos/MesaRelacionamentos.pdf`.

### 4. Gráfico Harmonia Familiar.pdf

**Estrutura** [literal]: título no canto superior esquerdo `Harmonia Familiar`; círculo preenchido no topo ao centro; seis anéis concêntricos (espaçamento crescente de dentro para fora) com o número `8545146` em negrito no centro; círculo vazio na base ao centro.

[síntese]: sequência numérica no estilo Grabovoi dentro de um ressonador de anéis; o kit do arquivo 5 lista `HARMONIA FAMILIAR` seguido de `8545146`, confirmando a origem. Sem instrução de uso no arquivo.

Arquivo: `.../drive_nao_lidos/04_harmonia_familiar/Gráfico Harmonia Familiar.pdf`.

### 5. Harmonizador de relacionamentos Kit+graficos+Radiestesia..pdf (11,0 MB)

**Estado**: `download_file_content` recusado ("File too large for download, over limit of 10 MB"). Segunda tentativa com `read_file_content` devolveu apenas o OCR dos rótulos. Busca por cópia menor no Drive (título contendo "Harmonizador") só encontrou `Gráfico Harmonizador.pdf` (239 KB; ids 1Zg4nKZr2q5afM9JIm79zDhr_KTfih5RI e 113iphldjmEMBC2Kv1VSw2tfcqfZYXsLe), que é um único gráfico, não o kit.

**Texto de apresentação** [literal, OCR]:
> KIT GRAFICOS DE RADIESTESIA.
> Gráficos em alta definição para impressão Este KIT contém 78 modelos de Gráficos Radiônicos em Alta Difinição em tamanhos variados.
> As artes estão prontas para a impressão em folha A4.
> Possibilidade de imprimir em papel sufite, papel canson, papel cartão, PS, PVC, PET etc.
> Autor:Lindenberg dias de Andrade
> […]
> Espero que goste foi feito com muito carinho pra você!
> https://radiestesiaeterapiaholistica.com/

**Nomes dos gráficos, na ordem do OCR** [literal; entradas ilegíveis do OCR omitidas; os números soltos aparecem logo após o nome a que provavelmente pertencem]:
`TESTEMUNHO` · `escudo protetor` · `labirinto de chartres.` · `ANTI VIX` · `ÔMEGA-ALFA` · `OM` · `BAGUÁ CÉU ANTERIOR` · `TE TRA GRAM` (pentagrama) · `CÓDIGO 21` · `CRUZ ATLANTE` · `RELÓGIO RADIESTÉSICO` · `TRI-CÍRCULO` · `Shrim` · `VESICA PISCIS` · `AUTOESTIMA` `5.7.3` · `ह्रीं` (Hrim) · `FLOR DA VIDA` · `NORTE DE FORMA` · `Turbilhão com sol` · `PIRÂMIDE DE TAO` · `TRÍGONO` · `TURBILHÃO COM MERCURIO` · `DESEMBARAÇADOR DE RELACIONAMENTO` · `ESTRELA DE 6 PONTAS OU HEXAGRAMA` · `HARMONIA FAMILIAR` `8545146` · `HARMONIA` · `TRIÂNGULO` · `क्लीं` (Klim) · `TURBILHÃO COM VÊNUS` · `ANTI DEPRESSÃO` · `ANTIDOR` `88997879` · `ANTIMAGIA` · `CRUZ CÓSMICA` · `LABIRINTO DE AMIENS` · `PROGRAMADOR CELULAR` · `RELAX DO SONO` `11111111111` `999999999` · `TRITURADOR COM TURBILHÃO` · `grafico sorte e sucesso` · `DIAFRAGMA-SENTIDO ANTI-HORÁRIO` · `DIAFRAGMA-SENTIDO HORÁRIO` · `ESCUDO PROTETOR` · `ESTRELA DE 5 PONTAS (PENTAGRAMA)` · `LUXOR` · `NOVE CÍRCULOS` · `TRITURADOR` · `ALTA VITALIDADE` `9797979` · `amplificador radiestesia` · `DECÁGONO DUPLO` · `DECÁGONO` · `DESEMBARAÇADOR MATERIAL` · `DESIMPREGNADOR` · `ESPIRAL` · `MAGNETRON` · `PROSPERADOR` · `QUADRATA` · `SAÚDE FINANCEIRA` `6782891` · `SHIN` · `TURBILHÃO` · `TURBILHÃO COM JÚPITER` · `TURBILHÃO COM PROSPERADOR`.

[síntese]: os desenhos, setores internos e eventuais textos de uso não puderam ser vistos. A atribuição dos números às cartas (`5.7.3` → Autoestima; `8545146` → Harmonia Familiar; `9797979` → Alta Vitalidade; `6782891` → Saúde Financeira; `88997879` → Antidor/Anti depressão; `11111111111`/`999999999` → Programador celular/Relax do sono) é inferida da ordem do OCR e confirmada, para os três primeiros, pelas mesas 2, 6 e 10 e pelo gráfico 4.

### 6. Mesa Prosperidade.pdf

**O que é** [síntese]: mesa hexagonal idêntica em layout à mesa 2 (círculo preenchido no topo, círculo vazio na base, centro + 6 gráficos com setas de duas pontas). Sem instrução.

**Rótulos** [literal], topo → sentido horário → centro:
- Título, inferior esquerdo: `Mesa da Prosperidade`.
- Topo: `Nome Místico de Jesus` (losango com יהשוה).
- Superior direito: `Diafragma` (círculo com lâminas curvas em espiral, como um diafragma de câmera).
- Inferior direito: `Alta Vitalidade` (anéis concêntricos com o número `9797979` no centro).
- Base: `Pirâmide de Integração` (círculo contendo um triângulo/pirâmide com curvas aninhadas no interior).
- Inferior esquerdo: `Turbilhão` (anel de crescentes sobrepostos).
- Superior esquerdo: `Pentagrama Esotérico`.
- Centro: `Desembaraçador` (hexágono contendo hexagrama com espiral no centro).

Arquivo: `.../drive_nao_lidos/06_mesa_prosperidade/Mesa Prosperidade.pdf`.

### 7. MESA DE PROSPERIDADE.pdf (14,7 MB)

**Estado**: download recusado (limite 10 MB). `read_file_content` devolveu somente [literal]: `MESA RADIÔNICA PARA PROSPERIDADE FINANCEIRA` / `MESA RADIÔNICA HOLÍSTICA PARA PROSPERIDADE FINANCEIRA`. Nenhum setor disponível.

[síntese]: no mesmo minuto de upload (2026-01-25 00:32) existe no Drive `Manual-de-Operador-Mesa-da-Prosperidade.pdf` (1,49 MB, id 1-dZXgXPfzqEVSncJ0XkLl7WMOiAKsdra), provavelmente o manual do operador desta mesma mesa; não estava na lista e não foi aberto — é a alternativa viável para preencher esta lacuna.

### 8. Kit Prosperador Completo - Novo_cópia.pdf (12 páginas)

**Estrutura** [literal, rótulo de cada página]:
1. `Prosperdador` — [síntese] anel de crescentes (turbilhão) com círculo central contendo duas setas cíclicas (sentido horário) em torno de uma pirâmide de três faces.
2. `Turbilhão com Jupter` — [síntese] turbilhão com o símbolo ♃ no centro.
3. `Atrair e potencializar` — [síntese] desembaraçador: três círculos concêntricos, hexagrama, espiral central no sentido horário.
4. `Abrr Caminhos e Repelir` — [síntese] mesmo desenho, espiral no sentido anti-horário.
5. Card com moldura vermelha, rótulo `Atrair/ Obter`: símbolos do Reiki com mantras escritos 3 vezes — `Hon Sha Ze Sho Nem` ×3, `Sei He Ki` ×3, `Choku rei` ×3 — e o desembaraçador (sentido horário).
6. Card `Abrir Caminhos/Afastar`: mesmos três símbolos ×3 + desembaraçador (anti-horário) [síntese: só a camada de texto foi conferida].
7. Card `Atrair /Obter` com `Dai Koo Myo` ×3 (símbolo 大光明 em roxo) + `Hon Sha Ze Sho Nem` ×3 + `Sei He Ki` ×3 + `Choku rei` ×3 + desembaraçador.
8. Card `Abrir caminhos/ Afastar` com `Dai Koo Myo` ×3 + os três símbolos + desembaraçador [síntese: camada de texto].
9. Card `Inspirações/ Criatividade para Prosperar`: símbolo amarelo em forma de "ㅍ" com raios, `La hanna nai` ×3 e o gráfico Prosperador.
10–12. Texto de instruções.

**Instruções** [literal, pp. 10–12]:
> O Kit prosperador foi cro-criado pelo Mestre Gabriel Reis, afim de ajudar todos que estão com desequilíbrios a nível material, todos elementos foram desenhado para todos praticantes de Reiki se beneficiarem das energia emitidas pelas ondas de forma.
> O Primeiro card é conhecido como o Prosperador, não é preciso ser sintonizado para usa-lo basta inserir um testemunho com suas intenção nele e deixar na posição norte, é recomendado deixar o card ativo por pelo menos 30 minutos.
> O segundo card é o Turbilhão do Jupter, um excelente card para atrair prosperidade e abundância na vida, recomenda-se ativa-lo ele em dia de Jupter ( quinta-feira e deixar ativo por apenas 24h. Deve ser colocado no Norte também.
> O Terceiro e Quarto cards é um gráfico muito conhecido da Radiônica o desembaraçador, porém o o terceiro ele tem função de atrair e potencializar seus pedidos, já o quarto é para afastar falta de sorte, pessoas indesejaveis que está sugando suas finaças ou remover crenças limitantes relacionado ao dinheiro.
>
> Os Cards Energéticos com os símbolos do Reiki desempenham funções semelhantes aos cards 3 e 4, mas com o poder potencializado pelos símbolos do Reiki, o que favorece uma realização mais rápida de seus propósitos.
> Para ativar a energia de prosperidade e abundância, siga os passos a seguir: primeiro, ative cada um dos símbolos e pronuncie seus mantras três vezes. Em seguida, coloque um testemunho (um papel com seu nome completo, data de nascimento e intenção) dentro do gráfico desembaraçador, juntamente com uma Pedra ou Cristal de tonalidade vermelha, preta ou transparente.
> É crucial estar atento ao sentido do gráfico: se ele é no sentido horário (para atrair e potencializar) ou no sentido anti-horário (para afastar e abrir caminhos). Esse momento é fundamental para direcionar a energia de acordo com suas necessidades específicas.
> Com a aplicação correta dessas práticas, você poderá experimentar um aumento notável em sua prosperidade e abundância, alcançando seus objetivos de forma mais eficiente. Lembre-se de sempre realizar esses rituais com intenções positivas e alinhadas com o seu crescimento pessoal. A combinação dos poderosos símbolos do Reiki com os gráficos energéticos pode trazer resultados surpreendentes para sua jornada de prosperidade e bem-estar.
> Esse card pode deixar montado por 72h, sua ativação durante a canalização energética é de apenas 10 a 15 min
>
> O poderoso Card de Inspiração e Criatividade tem como objetivo principal atrair novas ideias, insights e intuições, impulsionando assim a abundância e prosperidade em nossa vida.
> Para usufruir de seus benefícios, siga estes simples passos: insira o testemunho (com nome completo, data de nascimento e intenção) dentro do Gráfico Prosperador, e adicione uma pedra de cor Azul ou Violeta. Em seguida, ative o símbolo "La hanna nai" (lembrando que esse símbolo não requer sintonização). Você pode deixar o card ativado por um período de 72 horas.
> Com a aplicação cuidadosa desses procedimentos, você estará abrindo as portas para um fluxo maior de criatividade e inspiração, o que se traduzirá em uma vida mais próspera e abundante. Lembre-se de utilizar o card com intenções positivas e alinhadas com seus objetivos pessoais. Aproveite o potencial desse poderoso instrumento em sua jornada rumo ao sucesso e realização.

**Tempos e regras extraídos** [síntese a partir do literal acima]: Prosperador — testemunho dentro, posição norte, ≥ 30 min, sem sintonização. Turbilhão com Júpiter — ativar na quinta-feira, norte, ativo por apenas 24 h. Desembaraçador horário = atrair/potencializar; anti-horário = afastar/abrir caminhos. Cards Reiki — ativar cada símbolo e dizer o mantra 3×; testemunho = nome completo + data de nascimento + intenção; pedra vermelha, preta ou transparente; montado até 72 h; ativação na canalização 10–15 min. Card Inspiração — testemunho no Prosperador + pedra azul ou violeta; ativar "La hanna nai"; até 72 h.

Arquivo: `.../drive_nao_lidos/08_kit_prosperador/Kit Prosperador Completo - Novo_cópia.pdf` (+ `.txt`).

### 9. EQUILIBRANDO OS CHAKRAS COM ERVAS E PLANTAS.pdf (10 páginas)

**O que é** [síntese]: apostila curta (Espaço V – Terapia Holística e Orgonites; "Fonte: Site O Grande Jardim") com uma erva-símbolo e uma lista de ervas/especiarias por chakra. Não traz posologia além de "uma xícara de chá" e "algumas gotas de óleo".

**Índice** [literal, p. 1]: `Primeiro Chakra – Raíz. Segunda Chakra – Sacral. Terceiro Chakra – Plexus Solar. Quarto Chakra – Coração. Quinto Chakra – Garganta. Sexto Chakra – Terceiro Olho. Sétimo Chakra – Coroa.`

**Ervas-símbolo (títulos)** [literal]: `Primeiro Chackra- O chá de raíz de Dente de Leão(Taraxacum)`; `Segunda Chakra – FLOR DE GARDENA`; `Terceiro Chakra – FOLHAS DE ALECRIM`; `Quarto Chakra – Espinheiro`; `Quinto Chakra – Flores de trevo vermelho`; `Sexto Chakra – Menta, jasmim, evalhiça eyebright`; `Sétimo Chakra – Flor de Lavanda`.

**Texto por chakra** [literal, trechos operacionais]:
- Raiz: "O chá de raíz de Dente de Leão(Taraxacum) é altamente eficaz no tratamento de depressão, vesícula biliar ou pressão sanguínea elevada, um remédio desintoxicante para o fígado e os rins. Adicionando em alimentos como: cenoura, batata, nabo, rabanete, cebola e alho, e qualquer outra coisa que se enraíza, pode ter um efeito calmante para o nosso chakra raiz." Desequilíbrio: "problemas nas pernas, pés, reto, cóccix, sistema imunológico, depressão, deficiências auto-imunes."
- Sacral: "A Calendula é uma erva fácil de plantar que acentua a criatividade em todas as áreas da vida. Outra erva que é altamente benéfica para este chakra é a Gardenia, que pode-se utilizar tanto as raízes quanto o óleo para muitos fins. […] conhecida como a erva felicidade. Já o Sândalo ajuda a curar muitos tipos de infecções […] Você pode aplicar óleo de sândalo em seu corpo antes de tomar um banho ou você pode usá-lo para criar um bom aroma em sua casa. Outras ervas e especiarias que são benéficos são coentro, erva-doce, alcaçuz, canela, baunilha, alfarrobeiras, páprica doce, sementes de gergelim, sementes de cominho." Desequilíbrio: "distúrbios alimentares, problemas do trato urinário, distúrbios reprodutivos, dor de cabeça ocasional, febre e desequilíbrios emocionais."
- Plexo solar: "Para desbloquear o fluxo energético, pode-se usar óleo de lavanda, bergamota ou alecrim. Bergamota é ótima para o sistema digestivo […] Pode-se colocar folhas de alecrim em vários pratos ou você pode usar óleo de alecrim para cozinhar. Althea também relaxa o terceiro chakra e suaviza nossos esforços para controlar a vida. Ele ajuda você a relaxar o diafragma e reconectar-se com a respiração. Outras ervas e especiarias que são úteis como anis, aipo, canela, lírio do vale, hortelã, gengibre, hortelã (menta, hortelã, etc.), melissa, açafrão, cominho, erva-doce." Desequilíbrio: "má digestão, úlceras, diabetes, problemas hepáticos ou renais, anorexia, bulimia, e até tumores intestinais."
- Cardíaco: "Um chá ou extrato de bagas de Espinheiro aumenta a confiança no processo da vida e incentiva você a se sentir seguro ao seguir seu coração. Ela também ajuda a fortalecer o coração e os vasos sanguíneos. Você também pode usar pimenta caiena, jasmim, lavanda, manjericão, sálvia, tomilho, coentro e salsa para um coração saudável."
- Laríngeo: "Flores de trevo vermelho auxiliam, permitindo um fluxo livre de comunicação e auto-expressão. Uma xícara de chá de trevo vermelho pode desbloquear as emoções e pensamentos que estão esperando para sair. […] erva-cidreira é capaz de curar várias doenças, incluindo tireoide. O óleo de eucalipto é muito benéfico para o descongestionamento, simplesmente esfregar algumas gotas de óleo na garganta já ajuda. Outras ervas e especiarias que podem ajudar com o chakra da garganta é Tussilagem, que é excelente para tosse irritativa e catarro, a tussilagem ou unha-de-cavalo alivia e relaxa os pulmões, acalma a respiração e ajuda a expelir o muco, hortelã-pimenta, sálvia, sal e limão grama." Desequilíbrio: "problemas de tireoide, laringite, co-dependência no nível emocional, pensamentos pouco claros no nível mental, e insegurança no nível espiritual."
- Terceiro olho: "Ervalhiça Eyebright, menta, jasmim são ervas utilizadas para abrir o sexto chakra. A menta tem sido utilizada para curar depressão, enxaquecas e perda de memória. […] zimbro, artemísia, papoula, alecrim e lavanda." Desequilíbrio: "problemas nos olhos e ouvidos, dores de cabeça, enxaquecas, insônia e até mesmo pesadelos."
- Coronário: "As flores de lavanda e de lótus auxiliam a abertura do sétimo chakra. A lavanda traz para você o alinhamento com a sabedoria divina em uma base diária e é uma erva popular para melhorar a meditação. Enquanto as folhas de lótus e caules são amplamente utilizados na culinária japonesa e chinesa […] A Lavanda é sua melhor aposta, porque ele funciona bem em todos os chakras. Você pode incluir plantas internamente em sua vida através de chás, ou externamente como um banho ou aromaterapia". Desequilíbrio: "depressão, distúrbios do sistema nervoso, enxaquecas, amnésia, ADD, dislexia, e em casos mais extremos, delírios cognitivos e doença mental."

Arquivo: `.../drive_nao_lidos/09_chakras_ervas/EQUILIBRANDO OS CHAKRAS COM ERVAS E PLANTAS.pdf` (+ `.txt` com o texto integral).

### 10. Mesa do Amor Próprio.pdf

**Rótulos** [literal], topo → sentido horário → centro (mesmo layout das mesas 2 e 6):
- Título, inferior esquerdo: `Mesa do Amor Próprio`.
- Topo: `Nome Místico de Jesus`.
- Superior direito: `Turbilhão com Mercúrio` (turbilhão com ☿ no centro).
- Inferior direito: `Autoestima` (círculo com o número `5.7.3`).
- Base: `Equilíbrio` (mesmo gráfico da mesa 2).
- Inferior esquerdo: `Turbilhão com Vênus` (turbilhão com ♀ no centro).
- Superior esquerdo: `Pentagrama Esotérico`.
- Centro: `Desembaraçador` (hexágono com hexagrama e espiral).

Arquivo: `.../drive_nao_lidos/10_amor_proprio/Mesa do Amor Próprio.pdf`.

### 11. Manual Mapa de Atendimento Terapêutico.pdf — capítulos 8 a 11 (pp. 90–97)

Formação MAP – Mapa Complementar de Atendimento Terapêutico (Vanessa Rosa, atualização março/2024). Texto extraído da camada de texto do PDF (não é OCR).

**8 REGRAS GERAIS** [literal, p. 90]:
> Aqui serão apresentadas as regras para fazer parte da egrégora MAP. Caso seja constatado à má conduta ética e/ou moral, por parte do profissional, ou por mau uso da ferramenta.
> - Não cumprir com as regras apresentas;
> - Repassar materiais com outros terapeutas que não adquiriram o curso;
> - Reproduzir o MAP ou realizar alterações de qualquer informação do seu conteúdo;
> - Realizar a alteração de qualquer conteúdo informativo do material (apostila, slide ou mesa);
> - Recriar o material da mesa sem permissão da canalizadora;
> - Vender a sessão apenas atendendo com a MAP não é recomendado, pois essa técnica deve ser realizada como um complemento do seu atendimento com outra técnica;
> - Falsificar ou omitir informações do atendimento ao consulente;
> - Iniciar pessoas e professores, sem a devida outorga.
> Se for constatado qualquer irregularidade, o profissional será desligado da egrégora e perderá o direito de fazer parte, agindo por conta sem proteção energética. E dependendo do ocorrido estará sujeito às penalidades judiciais e carmáticas.

**8.1 Tipos de Atendimento** [literal, pp. 90–91]:
> Para atender o seu cliente, é importante escolher a melhor abordagem de acordo com as preferências suas e dele. Sugiro que a MAP não seja fotografada e enviada, pois é um recurso de apoio para suas confirmações nos demais atendimentos.
> Não há uma regra rígida para utilizar a MAP como complemento. Portanto, seja criativo (a):
> 1. Você pode utilizar o pêndulo durante a sessão, colocando o testemunho do seu cliente e verificando no relógio radiestésico cada ferramenta: "Durante a sessão de Reiki com Maria, tem algo a ser dito sobre as causas espirituais, sim ou não?"
> 2. Você pode utilizar a sua mão cataléptica, escolhendo qual a ferramenta que vai trabalhar com aquele cliente.
> 3. Você pode sair do decágono com seu pendulo e perguntar: "Durante a sessão de Reiki com Maria, qual a próxima ferramenta que vai trabalhar?"
> 4. Usar o que a cliente já te trouxe na anamnese, trazendo o contexto da sua queixa.
> 5. Seguir sua intuição.
> É importante destacar novamente: a MAP não é uma Mesa Radiônica, mas sim um suporte para os seus outros métodos de atendimento. Portanto, sua função é trazer consciência sobre o momento do cliente e informar qual energia está influenciando no momento.

**8.2 Testemunhos** [literal, p. 91]:
> Utilizamos como base: nome completo, data de nascimento, endereço de onde está no momento e intenção (uma frase ou o que deseja mudar em sua vida).
> - Pode-se utilizar qualquer papel (com linhas ou sem), qualquer formato (retângulo, quadrado, círculo, etc.), caneta ou lápis de qualquer cor;
> - Caso o consulente não possua as informações necessárias para o testemunho (vide acima), pode-se usar o nome e a data de nascimento, mas não é recomendado, pois pode haver outras pessoas com a mesma informação e a energia pode ser dispersada.

**8.3 Valores a serem cobrados** [literal, p. 91]:
> Como a MAP é um complemento para seus atendimentos, não há um valor tabelado específico para ela. Sugiro que você inclua e siga os valores estipulados para outras técnicas que utiliza em seu trabalho.

**8.4 Utilização de cristais e pêndulo** [literal, p. 91]:
> Você pode optar por utilizar cristais durante a sessão, mas não é obrigatório. Se desejar, sinta-se à vontade para selecionar os cristais que preferir ou utilizar aqueles que já possui de outras técnicas. Quanto ao pêndulo, você pode utilizar qualquer material que preferir e também aqueles que já possui de outras técnicas. Sinta-se livre para escolher o que melhor se adequa ao seu estilo e prática.

**9 CONSAGRAÇÃO** [literal, p. 92]:
> Como a MAP não é uma Mesa Radiônica, sugiro uma oração para a intencionar com a egrégora que você trabalha. Se preferir utilizar outra oração ou mantra, fique à vontade. No entanto, é recomendável incluir pelo menos uma oração pedindo proteção aos seres de luz.

**9.1 Consagração do MAP** [literal]:
> Se você precisar adquirir uma nova MAP ou se for sua primeira utilização, sugiro essa oração. Coloque suas mãos em cima da MAP, respire 3x profundamente e faça a oração:
> "Eu (informar seu nome completo), neste momento, consagro esta MAP a Deus, ao Mestre Jesus e aos Mestres da Fraternidade Branca, em harmonia com os Sete Arcanjos, para que possamos sempre trabalhar com a mais alta energia de amor, luz e proteção. Que esta ferramenta seja um canal claro e seguro para receber e transmitir a verdade divina. Convido meu Anjo da Guarda para estar presente e guiar cada sessão com clareza e sabedoria. Que esta MAP seja um instrumento crescimento e transformação para todos os envolvidos. Com profunda gratidão, consagro esta MAP. Que assim seja."

**9.2 Consagração das suas listas MAP** [literal]:
> Sugiro essa oração para incluir suas listas, mas fique à vontade para criar a sua. Coloque suas mãos em cima da MAP, respire 3x profundamente e faça a oração:
> "Eu, (nome completo), neste momento, consagro esta Lista MAP xxx (ex: de terapias), do número xxx (Ex: 1 ao 50) à presença divina de Deus, ao amoroso Mestre Jesus e aos iluminados Mestres da Fraternidade Branca, em união com os Sete Arcanjos, buscando sempre trabalhar com a mais pura energia de amor, luz e proteção. Convido meu Anjo da Guarda para estar presente, guiando cada sessão com clareza e sabedoria. Que esta Lista MAP xxx seja um instrumento sagrado de crescimento e transformação para todos os envolvidos. Com profunda gratidão, consagro esta Lista MAP. Que assim seja."

**10 PASSO A PASSO DO ATENDIMENTO** [literal, pp. 93–95]:
> Como mencionei nas etapas anteriores, o MAP não é uma Mesa Radiônica, mas sim um complemento dos demais atendimentos. Aqui está uma sugestão de como proceder, no entanto, sinta-se à vontade para desenvolver seu próprio método.
>
> **1 FECHE COM CONSULENTE O ATENDIMENTO:**
> - Converse com a pessoa para saber quais são os seus objetivos ou sobre o que ela proharmonização tratar/melhorar/harmonizaçãor no momento. Use o bom senso para entender a possível intenção a ser trabalhadas na sessão.
> - Lembre de preparar o seu espaço físico antes do envio, com aquilo que você intuir. Se o atendimento for presencial, tenha uma maca à disposição. Você pode acender uma vela para o seu Anjo da guarda ou para as demais Hostes, mas sempre com um destinatário no momento em que está acendendo.
>
> **2 TESTEMUNHO:**
> - Escreva em papel o testemunho do consulente, conforme o tipo de atendimento.
> - Posicione o testemunho do decágono.
>
> **3 FAÇA UMA ORAÇÃO DE ABERTURA:**
> - Recomendo iniciar sempre conectando-se com a egrégora que você pretende trabalhar. Por exemplo, se estiver realizando uma sessão de Reiki, comece com as orações iniciais, selando o ambiente com os símbolos apropriados e, em seguida, utilize o pêndulo para identificar as áreas a serem trabalhadas no cliente.
> Sugestão de oração: Diga em voz alta:
> "Eu (diga seu nome), invoco agora e me conecto com meu anjo da guarda, para que possamos ancorar as energias a Deus, ao Mestre Jesus e aos Mestres da Fraternidade Branca, em harmonia com os Sete Arcanjos. Que estas poderosas presenças divinas estejam comigo, guiando-nos com sua luz e amor, proporcionando a mais alta energia de proteção e sabedoria.
> Que o MAP, seja um canal claro e seguro para receber e transmitir a verdade divina, permitindo verificar as energias com clareza e discernimento do cliente.
> Que apenas a mais pura e elevada energia possa fluir durante esta sessão. Amém."
>
> **4 VERIFICAR FREQUÊNCIA INICIAL DA ESCALA DE HAWKINS**
> Verifique no relógio radiestésico OU no gráfico da Escala de Hawkins:
> - "Pêndulo, dentro da Escala de Hawkins, qual a vibração inicial de (nome do cliente)?
> - Anotar a frequência inicial para repassar a cliente no final da sessão.
>
> **5 FAÇA AS VERIFICAÇÕES:**
> Não há uma regra rígida para utilizar a MAP como complemento. Portanto, seja criativo (a): [repete os itens 1–5 de 8.1]
> Orientações:
> - Caso pêndulo comece a girar no sentido anti-horário (não) no decágono, você confirma no relógio se encerram as ferramentas.
> - Você pode perguntar: "Tem mais alguma ferramenta para ser trabalhada, sim ou não?"
> - Caso positivo, continue. Se não, você pode dar início ao encerramento.
>
> **6 VERIFICAR FREQUÊNCIA FINAL DA ESCALA DE HAWKINS**
> Verifique no relógio radiestésico OU no gráfico da Escala de Hawkins:
> - "Pêndulo, dentro da Escala de Hawkins, qual a vibração final de (nome do consulente)?
> - Anotar a frequência inicial para repassar a cliente no final da sessão.
>
> **7 FAÇA UMA QUEBRA ENERGÉTICA E FINALIZE O ATENDIMENTO:**
> Diga em voz alta:
> "Agradeço todas as informações concedidas pela MAP. Eu corto agora a energia de conexão do atendimento, eu fico com a minha energia e (nome do consulente) fica com sua energia. Agradeço toda a hieraquia invocada e por terem ajudado nesse atendimento. Gratidão, gratidão, gratidão, atendimento encerrado."

**11 REFERÊNCIAS BIBLIOGRÁFICAS** [síntese]: Berne (Jogos em que as pessoas jogam); Chopra (Sete Leis Espirituais do Sucesso; O Caminho para o Amor); Gawain (Criando o Verdadeiro Sucesso); Hartman (O Poder de Cura dos Chakras); Hawkins (Poder vs. Força); Hay (Você Pode Curar Sua Vida); Meireles (Life Coaching: as 7 áreas); Ourives (Algoritmos do Universo; DNA revelado das emoções); Ruiz (A Maestria do Amor; Os Quatro Compromissos); Tamburini (Seres de luz 12 raios); Virtue (Anjos na Terra).

Arquivo: `.../drive_nao_lidos/11_manual_mapa/Manual Mapa de Atendimento Terapêutico.pdf` (+ `.txt` integral, 97 páginas, 233 mil caracteres — cobre também os caps. 1–7 já lidos antes).

### 12. Radiestesia Espiritual — António Rodrigues (Editora Alfabeto, 2.ª ed., 2015)

**Achado principal**: o arquivo da lista (id 1jscw7kujEtHq36_MTpEYBlCgY37MdjWr, 4,4 MB, 44 páginas) **é uma amostra**, não o livro: cada página ímpar traz duas imagens JPEG (faixa superior 1114×558 + bloco 1114×925) que compõem uma página do livro; as pares são brancas. Conteúdo: capa (p. 1), folha de rosto, ficha catalográfica, sumário (3 páginas), Introdução "Uma longa história" e capítulo I até "A armadilha do pensamento mágico" (pp. 7–20 do livro), página branca, contracapa (p. 43). **Os cadernos finais não estão neste arquivo.** As cópias integrais do livro no Drive têm 19,9 MB (18ucfWYRUSRQG_h8jCAHG9tgXpUjqV05K e 1IEFUkOFr0lsKa4DDxPMfXqslxpNTGSk5) e 11,3 MB (1BaXyHKwaxNQsVwuz6G2zAjA53NN4OhVx): todas acima do limite de 10 MB do conector. A representação em texto (`read_file_content`) da cópia de 11,3 MB também termina na p. 82 ("Análise de causas"), exatamente onde terminava o texto anterior — salva em `.../drive_nao_lidos/12b_rad_espiritual_ocr/`.

**Sumário** [literal, lido nas imagens; "[…]" onde a faixa de corte escondeu linhas]:
- Introdução 7
- Capítulo I: O corpo sutil 11 […] Os auxiliares invisíveis 16 · Downpouring 18 · A natureza radiante 18 · A armadilha do pensamento mágico 20
- Capítulo II: Radiestesia Espiritual 21 · Os efeitos colaterais positivos da prática radiestésica 24 · Panorama radiestésico 24 · Espiritualidade sem religião 25 · O uso da oração, mantras, cânticos devocionais 25 · A alimentação vegetariana 26 · Requisitos radiestésicos 26 · Teste de habilidade radiestésica 27 · Teste para investigar o estágio de evolução do caminho interior 30 · Os instrumentos para a prática da Radiestesia Espiritual 30 · Gráficos radiestésicos 30 · Lei de Bovis 31
- Capítulo III: O diagnóstico com radiestesia na área da saúde 35 · Cuidados com os testemunhos 36 · Roteiro de análise radiestésica 37 · Análise breve 37 · Análise completa 38 · Análise psicológica 38 · Análise do campo energético 38 · Energias deletérias – vento solar 38 · Os chakras 43 · Estresse geopático 44 · Análise da qualidade dos ambientes 45 · O geomagnetometro 45 · As flechas secretas 46
- Capítulo IV: Pesquisa dos tratamentos em geral 49 · Pesquisa em homeopatia 50 · Pesquisa dos sais de Schussler 50 · Pesquisa dos florais e outras substâncias do conhecimento do radiestesista 59 · A psicoenergética 62 · Alguns fundamentos do tratamento espiritual 62 · O tratamento espiritual 64 · O contato com as entidades espirituais 64 · Autocura 65 · Aplicação num cliente in loco 65 · Aplicação à distância 65 · **Caderno para análise simplificada da saúde 69 · Caderno para análise de saúde completa 75 · Caderno para análise de saúde psicológica 91 · Caderno para seleção de tratamento 99 · Caderno para análise do campo energético 113** · Bibliografia 117

**Contracapa** [literal]:
> O objetivo desta obra é ajudar pessoas que atuam na área da saúde no atendimento a portadores de alguma doença que não responde aos tratamentos convencionais, ou àqueles com um quadro inespecífico, de difícil diagnóstico. A radiestesia espiritual combina a atividade do radiestesista, do terapeuta em psicoenergética e a ação de entidades espirituais.
> Este livro constitui-se num novo paradigma, aliando uma consagrada técnica de análise, a radiestesia, com um conjunto de procedimentos até agora tidos como atributos de certos indivíduos, agraciados pelo acaso. Estamos falando do contato com entidades espirituais, numa atividade particular, a cura ou a medicina espiritual.
> Com mais de vinte e cinco gráficos auxiliares de pesquisa e um caderno para análise de saúde, que ajudarão no diagnóstico com a radiestesia espiritual.
> Para quem trabalha no universo das terapias alternativas, esta obra será mais que um simples livro, será uma importante ferramenta de trabalho.

**Trechos operacionais recuperáveis do OCR (pp. 21–82, já dentro da faixa lida antes, mas diretamente úteis aos capítulos-alvo)**:

- Regra de escopo [literal, OCR com acentuação restaurada; p. ~21]: "A Radiestesia Espiritual tem uma regra rígida: sua área de atuação está restrita à saúde física, psicológica e qualidade ambiental (doméstica e profissional). Todas as demais questões envolvendo relacionamentos, problemas de trabalho e área mágica, devem ser investigadas e tratadas por outras vias. Estes temas e práticas acabam por envolver o praticante com assuntos de caráter material, os quais nem sempre são o que parecem, arrastando o praticante para o declive das energias de baixa qualidade, onde os instrumentos de defesa são por vezes ineficazes (psiquismo do praticante)."
- Roteiro de análise radiestésica [literal, p. 37]:
  > 1. Medir vitalidade geral com biômetro. 2. Investigar as doenças do corpo físico, análise breve ou completa. 3. Investigar estresse geopático*. 4. Investigar qualidade de ambiente doméstico e profissional. 5. Investigar FT e FPA (forças do mal), também com Radiestesia Cabalística*. 6. Investigar desequilíbrios astrais - larvas, miasmas, implantes*. 7. Com gráfico Psicométrico de Bélizal investigar qualidades pessoais*. 8. Reexaminar a necessidade de terapia verbal. 9. Checar ajuste de dieta alimentar*. 10. Checar a necessidade de exercícios físicos*. 11. Escolher a terapia.
  > *Quando houver suspeitas ou motivos para empreender a análise específica de qualquer um dos itens.
- "O gráfico a ser usado é uma adaptação do escargot seletor de A. de Bélizal, um clássico na radiestesia. Para o tratamento pode ser utilizado o mesmo instrumento da análise. Anote meticulosamente todos os resultados." [literal, p. 37]
- "Os resultados da investigação psicológica não devem ser em princípio revelados para o cliente. Estes dados são complementares para estabelecer um perfil. Podemos questionar se o cliente tem pouco interesse por seu trabalho, não podemos é dizer-lhe que ele é neurótico!" [literal, p. 38]
- "Durante o diagnóstico não investigaremos aspectos subjetivos cármicos, estes conteúdos serão removidos ou amenizados quando do tratamento espiritual." [literal, p. 38]
- Gráficos do caderno de análise simplificada da saúde [literal, OCR, p. 69]: `Sistemas • Órgãos • Condições • Causas • Glândulas • Alergias e efeitos adversos • Nutrição e alergias alimentares` — o OCR só alcança Sistemas, Órgãos, Condições (p. 80) e Causas (p. 82); **Glândulas, Alergias e efeitos adversos e Nutrição e alergias alimentares (pp. 83–90) não foram recuperados**.
- Sais de Schüssler pesquisados (potências) [literal, pp. 55–59]: `Kalium muriaticum (kalium chloratum) D6`, `Kalium phosphoricum D6`, `Kalium sulphuricum D6`, `Magnésia phosphorica D6`, `Natrum muriaticum (natrum chloratum) D6`, `Natrum phosphoricum D6`, `Natrum sulfuricum D6`, `Silicea D12` (os anteriores — Calcium fluoratum, Calcium phosphoricum, Calcium sulphuricum, Ferrum phosphoricum — estão nas pp. 50–55 do texto já extraído).
- Recomendações de prescrição [literal, p. 59]:
  > Normalmente um metal só é prescrito uma vez em cada receita. Ferr Phos - silicea.
  > Um sal de sódio é sempre prescrito em todas as receitas. Nat Mur - Nat Phos - Nat Sulph.
  > Dois sulfatos não devem aparecer na mesma receita. Calc Sulph - Kali Sulph - Nat Sulph.
  > Fosfato de magnésio é prescrito em quase todas as receitas. Mag Phos.
- Tabela "DIAS DE REPOUSO / HORÁRIO DO INÍCIO E FINAL / DIA DO TRATAMENTO" (p. ~68, tratamento espiritual): o OCR só devolve fragmentos (`7 horas`, `20 horas`, `2 dias`, `3 dias`, `sáb`, `dom`, dias 10–19) — estrutura ilegível, não transcrita.

Arquivos: `.../drive_nao_lidos/12_rad_espiritual/Radiestesia Espiritual - Antônio Rodrigues.pdf`; imagens extraídas em `.../render_sub13/rad_esp_img/`; OCR da cópia integral em `.../drive_nao_lidos/12b_rad_espiritual_ocr/`.

### 13. DOC-20240228-WA0024.pdf — apostila "Gráficos" (Radiestesia e Radiônica), 13,7 MB

**Estado**: download recusado (limite 10 MB). A representação em texto já obtida (`.../scratchpad/drive_content/DOC-20240228-WA0024.pdf.txt`) traz só o índice e os cabeçalhos de página: todas as pranchas são imagens. Busca por outra cópia (texto completo contendo "Adaptabilidade social"; títulos com "Gráficos") não encontrou arquivo menor equivalente. **Nenhum setor pôde ser transcrito.**

**Índice das pranchas relevantes** [literal, com a página da apostila]:
- `Nutrição e Alergias Alimentares 47` · `Motivações Pessoais 48` · `Métodos para Harmonização 49` · `Glândulas 50` · `Estados Psíquicos – 1 51` · `Estados Psíquicos – 2 52` · `Compatibilidade em relacionamentos 53` · `Causas 54` · `Alergias e Efeitos Adversos 59`
- `Ervas para a purificação do sangue. Qual é a melhor para mim? 71` · `Ervas para reumatismo 72` · `Ervas para problemas do sistema urinário e da bexiga 73` · `Ervas para problemas do estômago 74` · `Ervas para problemas do coração 75` · `Ervas para problemas nervosos 76` · `Ervas para a circulação (endurecimento das artérias) 77` · `Ervas para problemas glandulares 78` · `Ervas para problemas intestinais 79` · `Ervas para problemas do fígado e da vesícula biliar 80` · `Ervas para problemas pulmonares 81` · `Ervas para a garganta dolorida e irritada, brônquios e resfriados 82` · `Ervas para dor de cabeça 83` · `Ervas para insônia 84` · `Sais minerais para pequenos mal-estares. Qual é a melhor para mim? 85`
- `O que tem influência desfavorável à minha saúde? 86` · `Adaptabilidade social 87` · `Energia e dinamismo 88` · `Assuntos financeiros 89` · `Que fatores desempenham papel importante em minha vida? 90` · `Qual é o melhor metal para mim 91` · `Qual é a melhor cor para mim? 92` · `Qual é a melhor pedra para mim? 93`

[síntese]: os títulos (Nutrição e Alergias Alimentares, Glândulas, Causas, Alergias e Efeitos Adversos) coincidem com os gráficos do caderno de António Rodrigues (arquivo 12), e a série "Qual é a melhor para mim?" coincide com o programa do CRR de Ergom Abraham registrado em `01_google_drive_revisao.md` (afinidade entre pessoas; melhor pedra; ervas; metais; relacionamento de casal). A apostila provavelmente reproduz essas famílias de gráficos.

---

## Parte 2 — Consolidação por capítulo-alvo (listas prontas para virar biômetro, com fonte)

### 2.1 Relações entre pessoas

**Biômetro "Compatibilidade Energética"** (fonte: arquivo 1) [literal]: campos `T - 1`, `T - 2`, `Objetivo`; régua `Ã` 0–13.000 (passo 1.000, subdivisão 200, referência em ~6.500); régua `%` 0–100 (subdivisão 2).

**Mesa de Relacionamento — 7 gráficos** (fonte: arquivo 2) [literal]: Desembaraçador de Relacionamento (centro) · Nome Místico de Jesus · HRIM · 9 Círculos · Equilíbrio · Harmonia · Pentagrama Esotérico.

**Gráfico Harmonia Familiar** (fonte: arquivo 4) [literal]: `8545146` em 6 anéis.

**Mesa do Amor Próprio — 7 gráficos** (fonte: arquivo 10) [literal]: Desembaraçador (centro) · Nome Místico de Jesus · Turbilhão com Mercúrio · Autoestima `5.7.3` · Equilíbrio · Turbilhão com Vênus · Pentagrama Esotérico.

**Gráficos do kit "Harmonizador de relacionamentos" ligados a relações** (fonte: arquivo 5, só nomes) [literal]: `DESEMBARAÇADOR DE RELACIONAMENTO` · `HARMONIA FAMILIAR 8545146` · `HARMONIA` · `TURBILHÃO COM VÊNUS` · `TURBILHÃO COM MERCURIO` · `VESICA PISCIS` · `Shrim` · `ह्रीं` (Hrim) · `क्लीं` (Klim) · `AUTOESTIMA 5.7.3` · `ANTIMAGIA` · `ANTI DEPRESSÃO`.

**Temas pictográficos da mesa IBRATH** (fonte: arquivo 3) [síntese]: casal (homem/mulher), filhos (menino/menina), gestação/fertilidade (feto), polaridade ♂/♀ (yin-yang), rede/egrégora, desembaraçador.

**Pranchas de pesquisa existentes mas não transcritas** (fonte: arquivo 13, títulos) [literal]: `Compatibilidade em relacionamentos`, `Adaptabilidade social`, `Motivações Pessoais`, `Estados Psíquicos – 1/2`, `Que fatores desempenham papel importante em minha vida?`.

**Ressalva de escopo** (fonte: arquivo 12, p. ~21) [literal]: "Todas as demais questões envolvendo relacionamentos, problemas de trabalho e área mágica, devem ser investigadas e tratadas por outras vias."

### 2.2 Prosperidade e trabalho

**Mesa da Prosperidade — 7 gráficos** (fonte: arquivo 6) [literal]: Desembaraçador (centro) · Nome Místico de Jesus · Diafragma · Alta Vitalidade `9797979` · Pirâmide de Integração · Turbilhão · Pentagrama Esotérico.

**Kit Prosperador — 5 funções/cards** (fonte: arquivo 8) [literal nos nomes; tempos literais]:
| Card | Função | Regra/tempo |
|---|---|---|
| Prosperador | prosperidade geral | testemunho dentro, posição norte, "pelo menos 30 minutos", sem sintonização |
| Turbilhão com Júpiter | "atrair prosperidade e abundância" | ativar na quinta-feira ("dia de Jupter"), norte, "apenas 24h" |
| Desembaraçador horário — "Atrair e potencializar" | atrair/potencializar pedidos | sentido horário |
| Desembaraçador anti-horário — "Abrir Caminhos e Repelir" | "afastar falta de sorte, pessoas indesejaveis que está sugando suas finaças ou remover crenças limitantes relacionado ao dinheiro" | sentido anti-horário |
| Cards Reiki (Atrair/Obter; Abrir Caminhos/Afastar; com e sem Dai Koo Myo) | idem, potencializado | ativar cada símbolo e dizer o mantra 3×; testemunho (nome completo, data de nascimento, intenção) + pedra vermelha, preta ou transparente; montado até 72 h; ativação 10–15 min |
| Inspirações/Criatividade para Prosperar (La hanna nai) | "atrair novas ideias, insights e intuições" | testemunho no Prosperador + pedra azul ou violeta; ativar "La hanna nai" (sem sintonização); até 72 h |

**Gráficos do kit do arquivo 5 ligados a prosperidade/trabalho** (só nomes) [literal]: `PROSPERADOR` · `SAÚDE FINANCEIRA 6782891` · `TURBILHÃO COM JÚPITER` · `TURBILHÃO COM PROSPERADOR` · `DESEMBARAÇADOR MATERIAL` · `grafico sorte e sucesso` · `MAGNETRON` · `Turbilhão com sol` · `ALTA VITALIDADE 9797979`.

**Mesa "MESA RADIÔNICA HOLÍSTICA PARA PROSPERIDADE FINANCEIRA"** (fonte: arquivo 7): só o título; setores indisponíveis.

**Pranchas de pesquisa existentes mas não transcritas** (fonte: arquivo 13) [literal]: `Assuntos financeiros`, `Energia e dinamismo`, `Que fatores desempenham papel importante em minha vida?`, `Qual é o melhor metal para mim`, `Qual é a melhor cor para mim?`, `Qual é a melhor pedra para mim?`.

**Sobre o terapeuta e dinheiro** (fonte: arquivo 11, 8.3) [literal]: "não há um valor tabelado específico para ela. Sugiro que você inclua e siga os valores estipulados para outras técnicas que utiliza em seu trabalho." E a regra: "Vender a sessão apenas atendendo com a MAP não é recomendado".

### 2.3 Alimentos, ervas e doses

**Biômetro "Ervas por chakra"** (fonte: arquivo 9) [literal nos nomes]:
| Chakra | Erva-símbolo | Outras ervas/alimentos citados | Forma de uso citada |
|---|---|---|---|
| Raiz | raiz de Dente de Leão (Taraxacum) | cenoura, batata, nabo, rabanete, cebola, alho ("qualquer outra coisa que se enraíza") | chá |
| Sacral | Gardênia (flor; raízes e óleo) | Calêndula, Sândalo (óleo), coentro, erva-doce, alcaçuz, canela, baunilha, alfarrobeira, páprica doce, gergelim, cominho | óleo no corpo antes do banho; aroma na casa |
| Plexo solar | folhas de Alecrim | óleo de lavanda, bergamota, alecrim; Althea; anis, aipo, canela, lírio-do-vale, hortelã/menta, gengibre, melissa, açafrão, cominho, erva-doce | folhas em pratos; óleo para cozinhar |
| Cardíaco | Espinheiro (bagas) | pimenta caiena, jasmim, lavanda, manjericão, sálvia, tomilho, coentro, salsa | chá ou extrato |
| Laríngeo | flores de Trevo Vermelho | erva-cidreira, óleo de eucalipto, tussilagem (unha-de-cavalo), hortelã-pimenta, sálvia, sal, capim-limão ("limão grama") | "uma xícara de chá"; "esfregar algumas gotas de óleo na garganta" |
| Terceiro olho | Eyebright (eufrásia), menta, jasmim | zimbro, artemísia, papoula, alecrim, lavanda | — |
| Coronário | flor de Lavanda | lótus (folhas e caules) | chás, banho, aromaterapia; "A Lavanda […] funciona bem em todos os chakras" |

**Doses**: nenhuma das fontes lidas dá posologia numérica de ervas. Únicas quantidades [literal]: "Uma xícara de chá de trevo vermelho" (arquivo 9); "algumas gotas de óleo na garganta" (arquivo 9). Potências dos sais de Schüssler [literal, arquivo 12]: todos `D6`, exceto `Silicea D12`; regras de combinação de receita (um metal por receita; um sal de sódio em toda receita; nunca dois sulfatos; Mag Phos em quase todas).

**Alimentação no roteiro de análise** (fonte: arquivo 12, p. 37) [literal]: "9. Checar ajuste de dieta alimentar" e, no cap. II, a seção "A alimentação vegetariana" (p. 26).

**Gráficos de nutrição que existem mas não foram recuperados**: `Nutrição e alergias alimentares` e `Alergias e efeitos adversos` do caderno de A. Rodrigues (arquivo 12, pp. 83–90); as 14 pranchas `Ervas para … Qual é a melhor para mim?` + `Sais minerais para pequenos mal-estares` + `Nutrição e Alergias Alimentares` da apostila (arquivo 13).

### 2.4 Comunicação e passo a passo de atendimento

**Composição do testemunho** [literal]:
- MAP (arquivo 11, 8.2): "nome completo, data de nascimento, endereço de onde está no momento e intenção (uma frase ou o que deseja mudar em sua vida)"; "qualquer papel […] qualquer formato […] caneta ou lápis de qualquer cor"; só nome + data "não é recomendado, pois pode haver outras pessoas com a mesma informação".
- Kit Prosperador (arquivo 8): "um papel com seu nome completo, data de nascimento e intenção".

**Cinco modos de conduzir a verificação** (arquivo 11, 8.1 e passo 5) [literal]: pêndulo + relógio radiestésico com pergunta sim/não por ferramenta; mão cataléptica; sair do decágono e perguntar "qual a próxima ferramenta que vai trabalhar?"; usar a anamnese; seguir a intuição. Encerramento das verificações: giro anti-horário (não) no decágono → confirmar no relógio; "Tem mais alguma ferramenta para ser trabalhada, sim ou não?"

**Protocolo de sessão em 7 passos** (arquivo 11, cap. 10) [literal nos títulos]: 1 Feche com consulente o atendimento (conversa de objetivos; preparar o espaço; maca se presencial; vela com destinatário) · 2 Testemunho (escrever; posicionar no decágono) · 3 Oração de abertura (texto literal na Parte 1) · 4 Verificar frequência inicial da Escala de Hawkins ("Pêndulo, dentro da Escala de Hawkins, qual a vibração inicial de (nome do cliente)?") · 5 Faça as verificações · 6 Verificar frequência final da Escala de Hawkins · 7 Quebra energética e finalização (decreto literal: "Agradeço todas as informações concedidas pela MAP. Eu corto agora a energia de conexão do atendimento, eu fico com a minha energia e (nome do consulente) fica com sua energia. […] Gratidão, gratidão, gratidão, atendimento encerrado.").

**Decretos/orações literais disponíveis** (arquivo 11): consagração da mesa (9.1); consagração de listas (9.2); oração de abertura (passo 3); corte de conexão (passo 7). Preparação física comum às duas consagrações: "Coloque suas mãos em cima da MAP, respire 3x profundamente".

**Regras de comunicação com o cliente** [literal]:
- "Sugiro que a MAP não seja fotografada e enviada" (arquivo 11, 8.1).
- "Anotar a frequência inicial para repassar a cliente no final da sessão" (arquivo 11, passos 4 e 6).
- "Falsificar ou omitir informações do atendimento ao consulente" é infração (arquivo 11, cap. 8).
- "Os resultados da investigação psicológica não devem ser em princípio revelados para o cliente. […] não podemos é dizer-lhe que ele é neurótico!" (arquivo 12, p. 38).
- "Anote meticulosamente todos os resultados." (arquivo 12, p. 37).

**Valores** (arquivo 11, 8.3) [literal]: sem tabela própria; seguir os valores das outras técnicas; MAP é complemento, não sessão vendida isoladamente.

**Cristais e pêndulo** (arquivo 11, 8.4) [síntese]: opcionais; qualquer material; pode reaproveitar os de outras técnicas.

**Roteiro de análise em 11 passos** (arquivo 12, p. 37) [literal na Parte 1]: vitalidade com biômetro → doenças (análise breve/completa) → estresse geopático → ambiente doméstico/profissional → FT/FPA → desequilíbrios astrais → Psicométrico de Bélizal (qualidades pessoais) → terapia verbal → dieta → exercícios → escolher a terapia.

**Tempos de exposição a gráficos** (arquivo 8) [literal]: Prosperador ≥ 30 min; Turbilhão com Júpiter 24 h (quinta-feira); cards Reiki até 72 h, ativação 10–15 min; card Inspiração até 72 h.

---

## Parte 3 — Lacunas

1. **Harmonizador de relacionamentos Kit (11,0 MB)** — não baixa (limite de 10 MB do conector; 2 tentativas: download + OCR). Só os 78 nomes de gráficos foram recuperados; desenhos e instruções não. Alternativa parcial: `Gráfico Harmonizador.pdf` (239 KB) para o gráfico "Harmonizador" isolado.
2. **MESA DE PROSPERIDADE (14,7 MB)** — não baixa; OCR só do título. Alternativa provável: `Manual-de-Operador-Mesa-da-Prosperidade.pdf` (1,49 MB, id 1-dZXgXPfzqEVSncJ0XkLl7WMOiAKsdra), enviado ao Drive no mesmo minuto.
3. **DOC-20240228-WA0024 (13,7 MB)** — não baixa; pranchas são imagens, o OCR só dá o índice. Setores de Compatibilidade em relacionamentos, Motivações pessoais, Assuntos financeiros, Adaptabilidade social, Energia e dinamismo, melhor metal/cor/pedra e as 14 pranchas de ervas permanecem **sem transcrição**. Nenhuma cópia menor encontrada.
4. **Radiestesia Espiritual — cadernos finais (pp. 83–117)**: o arquivo da lista é só uma amostra (pp. 1–20); as três cópias integrais (11,3 e 19,9 MB) excedem o limite e o OCR do Google termina na p. 82. Ficam de fora: Glândulas, Alergias e efeitos adversos, **Nutrição e alergias alimentares**, Caderno de saúde psicológica (p. 91), Caderno de seleção de tratamento (p. 99), Caderno de campo energético (p. 113) e o gráfico Psicométrico de Bélizal. Também ilegível no OCR: a tabela "Dias de repouso / horário de início e final".
5. **MesaRelacionamentos (IBRATH)** — legível, mas é uma mesa pictográfica sem rótulos; não há setores a transcrever. Contém dados pessoais de terceira pessoa (licença) que não devem ser reproduzidos.
6. **Mesas 2, 6 e 10 e gráfico 4** — totalmente legíveis, mas são só artes: nenhum arquivo traz instruções, decretos ou tempos de uso; qualquer passo a passo para elas será [síntese].
7. **Doses** — nenhuma fonte lida dá posologia numérica de ervas/alimentos; só "uma xícara de chá", "algumas gotas de óleo" e as potências D6/D12 dos sais de Schüssler.
8. Páginas 6 e 8 do Kit Prosperador foram conferidas apenas pela camada de texto (não visualmente); páginas 15–37 da amostra de Radiestesia Espiritual (pp. 7–19 do livro) não foram relidas por já constarem do texto extraído anteriormente.
