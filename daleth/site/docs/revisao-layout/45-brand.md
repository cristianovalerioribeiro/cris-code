# DALETH · Revisão de expressão visual do site (45-design-brand)

Base: capturas da home desktop (fatias 00–10), celular (fatia 00), Empresas (fatias 00 e 02), Método (página inteira), `assets/site.css` e os SVGs de marca. Estratégia e textos ficam como estão. Aqui trato só de **como o site parece** e se isso diz "DALETH".

---

## 1. Diagnóstico: onde o visual trai a marca

**Resumo franco:** o dono tem razão. O conteúdo é de Sábio, mas a roupa é de template de consultoria ou SaaS. Quem tira o logo do topo não identifica a DALETH: poderia ser uma fintech, uma proptech ou uma consultoria de gestão qualquer. O site é organizado e limpo, mas falta **voz visual**. Ele não tem a calma, a precisão nem o ar editorial que a marca promete.

### 1.1 Wordmark serifado em cima de um site 100% grotesco
O wordmark é uma serifa romana de alto contraste, em caixa-alta, com o triângulo dourado no A. Todo o resto do site está em Manrope 700, com tracking negativo (-0.025em), mais Inter. A Manrope é a fonte padrão de landing page de startup. O resultado é que o logo parece colado de outra empresa. O H1 "Para realizar mais, é preciso estruturar melhor." em Manrope 700, com 64px, fala **alto e pesado**, e a marca é "a pessoa mais calma da mesa". Sábio + Governante pedem voz editorial, e o site tem voz de pitch.

### 1.2 Excesso de cartões, o ponto que o Manual proíbe
Contei cerca de **20 caixas com borda 1px, raio 6px e fundo branco** só na home:
- 6 cartões em "Para quem";
- 2 em "Como começa";
- 4 colunas em "O método";
- 3 em "Atuação";
- 4 em "Repertório";
- 1 quadro no gráfico de capital.

Na página Empresas aparecem mais 8 cartões em grade 4×2. No Método, cada movimento tem o seu cartão "O que sai daqui". O Manual diz textualmente "evitar excesso de molduras e cartões". Cartões iguais e lado a lado formam um **cardápio de serviços**. Isso puxa para o "vendedor" e achata a hierarquia, porque tudo pesa igual. O hover com sombra e `translateY(-2px)` em `.momento` é linguagem de app.

### 1.3 Ritmo monótono: o mesmo molde 9 vezes
Nove seções repetem o mesmo cabeçalho:
1. rótulo dourado com tracinho;
2. H2 Manrope;
3. lead cinza;
4. grade logo abaixo.

O fundo alterna branco → névoa → marinho de forma previsível. A home tem 12 blocos de peso equivalente:

> hero → credenciais → Modelar → Como começa → Para quem → Tese → Método → Atuação → Trilho → Repertório → Quem conduz → Próximo passo

Nenhum desses blocos é claramente "o capítulo principal". O princípio do Manual, "um assunto por página", virou "doze assuntos com o mesmo tamanho". O usuário rola 10 telas sem mudança de cadência: nenhuma seção respira e nenhum momento muda de escala.

### 1.4 Dourado virou código de seção, e não destaque
Na home, o dourado aparece:
- em todos os rótulos com tracinho (9×);
- na borda da faixa do slogan;
- nos botões de CTA (2×);
- nas etiquetas ("PRIMEIRO TRABALHO", "ONDE A DECISÃO SE FORMA");
- nas 5 bolinhas do trilho;
- nos marcadores da cadeia da Tese;
- nos fios das notas;
- nos títulos do rodapé;
- na barra "Estrutura combinada".

São mais de 25 ocorrências. O Manual diz "o dourado é destaque, não código de seção". Quando tudo é dourado, o único dourado que importa, a **estrutura combinada a R$ 1,98 mi**, se perde.

### 1.5 Hero: cenário de proptech
Os blocos isométricos azuis (#14456A) chapados, em três camadas com parallax e gradiente lateral, leem como "render de cidade de startup imobiliária". A boa ideia do hero é o **volume dourado tracejado** (o modelado, o possível), mas ele está afogado entre uns 20 blocos sólidos. A cena fala de "metrópole e escala" quando deveria falar de "um empreendimento sendo desenhado com precisão". No celular, o cenário cai para `opacity:.6` atrás de um gradiente e praticamente some (fatia celular 00).

### 1.6 Faixa do slogan com cara de barra promocional
A tarja marinho com fio dourado entre o menu e o hero, presente em todas as páginas, é a linguagem de "frete grátis acima de R$ 199". O slogan "Ao seu lado na construção da sua história" é **assinatura** e merece lugar de assinatura (fecho, rodapé, sob o wordmark), não de aviso. Nas internas, a tarja ainda empurra um bloco marinho para o topo de páginas que deveriam abrir claras.

### 1.7 Quem conduz: avatar de aplicativo
O símbolo D dentro de um círculo marinho de 120px faz o papel de "foto de perfil". As formações aparecem em pills de raio 999px, linguagem de LinkedIn ou de tag de app. As duas coisas caem no "informal demais" e enfraquecem justamente a seção que deveria dar autoridade técnica.

### 1.8 Diagramas que não explicam
A cadeia da Tese (produto → orçamento → caixa → capital → cronograma → estrutura societária) é um **sistema de dependências**, mas está desenhada como timeline vertical de bolinhas, genérica e linear. O "Do terreno à entrega" usa bolinhas cheias e vazadas, também genéricas. O Manual pede "diagramas para explicar", e estes só enfeitam uma lista.

### 1.9 O que já está certo (preservar e promover)
- **O gráfico "Um empreendimento de exemplo, quatro estruturas de capital"** é o objeto mais DALETH do site: número antes de opinião, comparação lado a lado, destaque único. Hoje está encaixotado num cartão cinza com cabeçalho. Deve virar **protagonista**, maior, sem caixa, com linguagem de prancha.
- O destaque do **02 Modelar** em marinho dentro do método está correto em intenção (o diferencial ganha ênfase), mas deve ser feito sem caixa (ver seção 5).
- Paleta base, contraste de texto e espaçamentos já são disciplinados. O problema é de linguagem, não de higiene.

### 1.10 Detalhes que somam "genérico"
- Três linguagens de canto convivem: raio 6px nos cartões e botões, 3px nas etiquetas e 999px nas pills.
- Todas as seções terminam em "botão dourado + botão contorno" ou em "link → sublinhado". O CTA duplo onipresente soa vendedor.
- As internas (Empresas, Método) abrem com gradiente névoa→branco e um H1 enorme sem nenhum objeto ao lado. A metade direita fica vazia, e todas as aberturas internas são idênticas.
- No Método, a seção "Do primeiro contato à implantação" saiu esmaecida na captura de página inteira. A animação `.surge` deixa conteúdo invisível até o scroll. É risco para impressão, captura e leitores lentos, e o conteúdo deveria ser visível por padrão.

---

## 2. Direção visual recomendada

**A ideia: "a prancha de estruturação".** O site deve parecer o documento que a DALETH entrega, e não um anúncio do que ela faz:
- papel claro, grade de 12 colunas evidenciada por fios finos;
- títulos em serifa editorial, calma e de peso médio;
- números grandes e tabulares;
- diagramas desenhados a traço marinho, como numa prancha de projeto executivo, com cotas, legendas de premissa e numeração de folhas;
- o dourado aparece **só onde está a decisão**, como o triângulo no A do wordmark: um ponto por tela, nunca um tema.

O marinho entra como abertura de capítulo (hero e fecho), e não como faixa decorativa. Assim a marca diz, sem adjetivo nenhum, "aqui o negócio é desenhado antes de ser construído". É o Sábio (rigor, leitura, número) com a postura do Governante (ordem, estrutura, institucional), e o tom continua próximo porque é claro e legível, não monumental.

**Referências (inspirar, não copiar):**
1. **Cartas trimestrais e relatórios de gestoras independentes brasileiras** (o padrão Dynamo/Squadra, ou relatório anual de banco de investimento): texto denso e bem composto, tabela no lugar de ícone, quase nenhuma imagem, autoridade pela clareza.
2. **Prancha técnica de projeto executivo e revistas de arquitetura** (pranchas de arquitetura com carimbo; revistas como *Monolito* ou *a+u*): fios de 0,5pt, cotas, numeração de folhas, desenho de linha monocromático, muito branco.
3. **Gráficos editoriais do *Financial Times* e da *The Economist***: título que afirma a conclusão, uma única cor de destaque contra cinzas, legenda de fonte e premissas sempre visível.

**Anti-referências:**
1. **Landing page de SaaS ou proptech**: cartões com sombra e hover, gradientes, render isométrico 3D azul brilhante, ícones de linha em círculos, pills. É onde o site está hoje.
2. **Incorporadora de alto padrão ou private banking ostentoso**: preto com dourado metálico, Didone fina e alta (Playfair, Bodoni), foto de cobertura ao pôr do sol, "exclusividade". Isso é luxo e rentabilidade como promessa, exatamente o que o Manual veta.

---

## 3. Tipografia

### Dupla recomendada (Google Fonts)
| Papel | Família | Pesos | Por quê |
|---|---|---|---|
| Títulos, numerais de destaque | **Source Serif 4** (variável, eixos `opsz` 8–60 e `wght`) | 500, 600 (+ itálico 400 para ênfase pontual) | É uma serifa transicional de contraste moderado, desenhada para leitura técnica. O eixo de tamanho óptico deixa os títulos grandes com mais contraste, o que conversa com o wordmark, enquanto os pequenos ficam robustos. Tem numerais lining e tabulares bons para finanças e cobre todo o PT-BR. É editorial sem "parecer Word" (resolve o ponto do Caderno contra a Cambria) e não é Didone (luxo) nem Trajan/Cinzel (copiaria o logo e seria monumental). |
| Corpo, interface, tabelas, rótulos | **Inter** (já instalada) | 400, 500, 600 | Neutra, com excelente `tnum` para tabelas e simulador e ótima em telas pequenas. Em caixa-alta espaçada, ecoa o descritor "ESTRUTURAÇÃO DE NEGÓCIOS" do logo. Manter a Inter reduz o retrabalho, e a Manrope sai do site. |

**Alternativa B**, se quiserem mais jornal e menos relatório: **Newsreader** (títulos) + Inter.
**Evitar:** Cormorant, Playfair Display, Cinzel, Libre Caslon Display (luxo ou imitação do logo) e Lora/Merriweather (blog genérico).

### Escala modular
**Razão 1,25 (terça maior) no desktop, base 17px; razão 1,2 no celular, base 16px.**

O 1,25 dá hierarquia editorial clara sem drama: o H1 fica em ~65px, e não em 80–90px. O 1,333 ou mais seria dramático, contra o "não é: dramática". O 1,2 no celular evita H1 gigante em 390px.

| Token | Família / peso | Desktop (1,25) | Celular (1,2) | Entrelinha | Tracking |
|---|---|---|---|---|---|
| `--display` (H1 home) | Source Serif 4 · 600 · opsz 60 | 65px | 40px | 1.05 | -0.015em |
| `--h1` (internas) | Source Serif 4 · 600 | 52px | 33px | 1.1 | -0.01em |
| `--h2` | Source Serif 4 · 600 | 42px | 28px | 1.15 | -0.01em |
| `--h3` | Source Serif 4 · 600 | 26.5px | 23px | 1.25 | 0 |
| `--h4` (título de item, lista) | Inter · 600 | 21px | 19px | 1.35 | -0.005em |
| `--lead` | Inter · 400 · grafite | 21px | 19px | 1.5 | 0 |
| `--corpo` | Inter · 400 | 17px | 16px | 1.65 | 0 |
| `--legenda` (premissas, fontes) | Inter · 400 · grafite-2 | 14px | 14px | 1.5 | 0 |
| `--rotulo` (eco do descritor) | Inter · 600 · CAIXA-ALTA | 12px | 12px | 1.2 | 0.14em |
| `--numeral` (01–04, R$ de destaque) | Source Serif 4 · 400 · `tnum lnum` | 83–104px | 52px | 1 | -0.02em |

Use `font-variant-numeric: tabular-nums lining-nums` em tabelas, no simulador e nos valores. Valores monetários de destaque ("R$ 16,4 mi") vão em Source Serif 600, e os valores de tabela em Inter 500 `tnum`.

### Como conversar com o wordmark sem imitá-lo
- O wordmark é **caixa-alta**, alto contraste e com triângulo. O site usa serifa sempre em **caixa-baixa (sentence case)**, peso 600 e contraste moderado. É parente, não cópia.
- Nunca componha "DALETH" em Source Serif caixa-alta como título. O nome em destaque é sempre o SVG oficial, e no corpo de texto vai em Inter ou Source Serif normais.
- O **descritor espaçado** do logo vira a regra dos rótulos: Inter 600, 12px, tracking 0.14em, caixa-alta. É o único lugar com caixa-alta no site.
- O itálico da Source Serif (400) é o recurso "linguístico" da marca: um termo por título, no máximo um por página (ex.: "Antes de escolher um caminho, colocamos os caminhos *lado a lado*").

---

## 4. Paleta de uso

### Tokens
| Token | Hex | Função |
|---|---|---|
| `--marinho` | `#082538` | Primária: títulos, texto principal, botão primário, bloco de abertura e fecho |
| `--marinho-2` | `#0F3550` | Hover do botão; segunda superfície dentro do marinho (raro) |
| `--fio-escuro` | `#2A4A62` | Fios e grades sobre marinho (decorativo) |
| `--dourado` | `#B58A44` | Destaque: preenchimento de forma (triângulo, barra destacada, fio de decisão). **Não é cor de texto em fundo claro** |
| `--dourado-texto` | `#85622A` | Único dourado permitido como texto em fundo claro (rótulo, número de destaque pequeno) |
| `--dourado-claro` | `#D4B37C` | Dourado como texto ou fio sobre marinho |
| `--branco` | `#FFFFFF` | Fundo principal |
| `--nevoa` | `#F4F6F8` | Fundo alternativo das páginas de análise (neutro com viés para o marinho) |
| `--nevoa-2` | `#E8EDF1` | Trilho de barra de gráfico, fundo de célula de tabela |
| `--fio` | `#D3DCE3` | Fios de grade e divisores (decorativo) |
| `--fio-forte` | `#7A8D9E` | Borda de campo de formulário e de controle (precisa de 3:1) |
| `--grafite` | `#47586A` | Lead e texto secundário |
| `--grafite-2` | `#5E6E7D` | Legendas e metadados |
| `--aco` | `#5B7790` | Apoio em dados: série secundária de gráfico, linha de referência. Nunca é cor de marca |

### Proporção de uso (área de tela, média por página)
**72% claros (branco + névoa) · 20% marinho (texto + 1–2 blocos) · 5% grafite, aço e fios · ≤ 3% dourado.**

### Regras para o dourado
1. **Uma ocorrência de dourado por viewport**, no máximo três por página inteira (fora o logo).
2. Dourado marca **decisão ou resultado**: a barra da estrutura escolhida, o movimento Modelar, as etapas em que a DALETH decide e o ponto em destaque de um diagrama. Rótulo de seção não é decisão, então rótulo vai em `--grafite-2`, e não em dourado.
3. **Nunca** usar dourado em texto corrido, títulos, ícones genéricos, bordas de faixa ou rodapé.
4. Botão dourado só em fundo marinho e só um por página (o CTA do fecho). No claro, o CTA é marinho.
5. Dourado `#B58A44` sobre névoa dá 2.90:1, o que não serve nem para UI. Sobre névoa, use `--dourado-texto`, ou mude o fundo para branco.
6. Sem gradiente dourado, brilho ou efeito metálico. É sempre cor chapada.

### Contraste WCAG 2.2 (calculado em Python, fórmula de luminância relativa)
| Texto / elemento | Fundo | Razão | Uso permitido |
|---|---|---|---|
| marinho #082538 | branco #FFFFFF | 15.77:1 | AAA, qualquer texto |
| marinho #082538 | névoa #F4F6F8 | 14.55:1 | AAA |
| marinho #082538 | névoa-2 #E8EDF1 | 13.37:1 | AAA |
| grafite #47586A | branco | 7.31:1 | AAA, lead e corpo secundário |
| grafite #47586A | névoa | 6.75:1 | AA |
| grafite-2 #5E6E7D | branco | 5.25:1 | AA, legendas de 14px |
| grafite-2 #5E6E7D | névoa | 4.84:1 | AA |
| dourado-texto #85622A | branco | 5.56:1 | AA, rótulo dourado no claro |
| dourado-texto #85622A | névoa | 5.13:1 | AA |
| dourado #B58A44 | branco | 3.14:1 | Só forma/UI ou texto ≥ 24px (evitar como texto) |
| dourado #B58A44 | névoa | 2.90:1 | Decorativo, **reprovado** para UI |
| marinho #082538 | dourado #B58A44 | 5.02:1 | AA, texto do botão dourado (no fecho) |
| branco #FFFFFF | dourado #B58A44 | 3.14:1 | **Não usar** texto branco em botão dourado |
| branco #FFFFFF | marinho #082538 | 15.77:1 | AAA |
| gelo-marinho #B9C8D4 (texto secundário no escuro) | marinho | 9.22:1 | AAA |
| dourado-claro #D4B37C | marinho | 7.91:1 | AAA, rótulo e número no escuro |
| dourado #B58A44 | marinho | 5.02:1 | AA, fio ou forma no escuro |
| branco | marinho-2 #0F3550 | 12.76:1 | AAA |
| gelo-marinho #B9C8D4 | marinho-2 | 7.46:1 | AAA |
| dourado-claro #D4B37C | marinho-2 | 6.40:1 | AA |
| aço #5B7790 | branco | 4.68:1 | AA, série de gráfico com rótulo |
| aço #5B7790 | marinho | 3.37:1 | Só UI e gráfico no escuro |
| fio-forte #7A8D9E | branco / névoa | 3.43 / 3.16:1 | Borda de campo (1.4.11) |
| fio #D3DCE3 | branco | 1.39:1 | Decorativo apenas |
| fio-escuro #2A4A62 | marinho | 1.69:1 | Decorativo apenas |
| dourado-texto #85622A | marinho | 2.84:1 | **Não usar** no escuro (use dourado-claro) |

Adicionar `--gelo-marinho: #B9C8D4` aos tokens para texto secundário no escuro, no lugar dos atuais `#C9D5DF`, `#A9BAC8` e `#B8C7D3`. São três tons para a mesma função, e devem virar um só.

---

## 5. Linguagem gráfica própria

### Elementos que a DALETH deve ter
1. **Grade de prancha.** São 12 colunas, max 1180px, gutter de 24px. Os capítulos são separados por **fio horizontal de 1px `--fio`** que atravessa a grade, e não por mudança de fundo. Os blocos-chave ganham um **fio superior de 2px marinho** sobre a largura do conteúdo. Esse é o "carimbo" de início de seção e substitui as caixas.
2. **Numeração de folha.** Cada seção da home e das internas leva o número em Source Serif 400 tabular, com 104px no desktop e 52px no celular, em marinho com 12% de opacidade sobre o fio, ou em marinho cheio no método (01 Mapear, **02 Modelar**…). O rótulo em caixa-alta fica ao lado ("02 · MODELAR"). Isso substitui o "tracinho dourado + rótulo".
3. **Cotas técnicas.** É uma linha fina de 1px com terminais em traço de 45° e o valor no meio, em Inter 500 tnum. Use cotas para **anotar números** em vez de usar badges. Exemplo no gráfico de capital: uma cota vertical entre a barra "Capital próprio R$ 16,4 mi" e a "Estrutura combinada R$ 1,98 mi", com a legenda "−88% de capital no pico". É a linguagem de engenharia a serviço do "número antes de opinião".
4. **Módulos do símbolo D.** São quatro barras verticais crescentes, de larguras iguais, com alturas de 40/60/80/100%, derivadas das hastes do D. Usos permitidos:
   - **indicador de etapa do método**: de 1 a 4 módulos preenchidos em marinho, e o módulo do Modelar em dourado;
   - **marca de fim de capítulo**, com 24px de altura;
   - favicon e estados de carregamento.

   **Não** usar como textura repetida de fundo.
5. **Triângulo de decisão.** O triângulo do A, com 8–10px e em dourado, é o único marcador dourado do site. Marca onde a DALETH participa da decisão: no trilho "Do terreno à entrega", no lugar das bolinhas, e no nó principal dos diagramas. É usado com parcimônia, para continuar sendo um sinal.
6. **Diagramas a traço.** Traço marinho de 1.5px, nós retangulares sem raio, setas de ponta aberta, rótulos em Inter 500 de 14px. A Tese vira um **diagrama de dependências**: os 6 nós (produto, orçamento, caixa, capital, cronograma, societária) em anel ou matriz, com setas mostrando "define" e "muda", e o nó "negócio" ao centro com o triângulo. O "Do terreno à entrega" vira uma **régua de cronograma**: um eixo com marcos, onde as etapas de decisão levam o triângulo e um trecho de fio dourado de 2px, e as de acompanhamento ficam em fio `--aco`.
7. **Gráficos de comparação.** Barras horizontais sem raio (no máximo 1px), trilho `--nevoa-2`, séries em marinho e **uma única barra em dourado** (a recomendada). O título afirma a conclusão, e as premissas ficam em legenda de 14px abaixo ("VGV R$ 20 mi · terreno 15% · obra 24 meses · exemplo ilustrativo"), como nas pranchas. Sem moldura em volta.
8. **Tabelas.** Só fios horizontais, cabeçalho em rótulo caixa-alta, números alinhados à direita em `tnum`.

### Cenário isométrico do hero
- **Manter a ideia e trocar a técnica**: sai o volume chapado e entra o **desenho de linha**. Os blocos de contexto viram wireframe de traço 1px em `#B9C8D4` com 25–35% de opacidade, sem preenchimento azul. São no máximo 8 volumes, e não ~20.
- O protagonista é **um único empreendimento sobre um lote demarcado**, com contorno do terreno tracejado e cotas, dentro de uma malha de quadra:
  - a parte "existente" fica em linha cheia;
  - a parte "modelada" fica em tracejado dourado (o volume possível);
  - o corpo do prédio é construído pelos **módulos verticais do D**, um eco sutil do símbolo.
- Movimento: parallax de no máximo 16px, ou nenhum. Pode haver uma animação única de "desenho" do tracejado dourado (stroke-dashoffset, 1.2s, ease-out) ao carregar, respeitando `prefers-reduced-motion`.
- Composição: o desenho ocupa as colunas 7–12, alinhado ao topo do H1, sem gradiente cobrindo. Ele deve ser legível, não fundo.
- Celular: o desenho vai **abaixo** dos botões, cortado a 220px de altura e alinhado à direita. Não pode ficar escondido atrás do texto.
- Quando houver fotografia real de terreno ou obra, o hero pode virar foto (dessaturada, em P&B ou com leve tom marinho) com o mesmo desenho de linha e as cotas sobrepostos. Essa é a assinatura de longo prazo.

### Eliminar
- Cartões com borda, raio de 6px, hover com sombra e deslocamento (`.momento`, `.cartao`, `.dimensao`, `.passo`, `.movimento`, `.modelagem`).
- A faixa do slogan no topo, que vai para o hero (abaixo do H1, em Source Serif itálico 21px), para o fecho e para o rodapé.
- O tracinho dourado de 28px antes de todo rótulo.
- As etiquetas coloridas ("SEM CUSTO", "PRIMEIRO TRABALHO", "ONDE A DECISÃO SE FORMA"), que viram rótulo em texto puro, caixa-alta, cor grafite-2.
- As pills de formação e o monograma em círculo. Em "Quem conduz" entra uma ficha tipográfica (nome em Source Serif 42px, formação em lista com fios), e foto real quando houver. Enquanto não houver foto, não se põe nada no lugar.
- O gradiente névoa→branco das aberturas internas.
- As bolinhas da cadeia e do trilho.
- A seta "→" como caractere nos links e cartões.
- O CTA duplo (botão + botão contorno) em toda seção.
- O raio de 999px em qualquer componente (filtros do repertório, FAQ).

---

## 6. Regras práticas de composição (para o desenvolvedor)

1. **Marinho só abre e fecha.** No máximo **um bloco marinho por página além do fecho**. Na home, o hero mais o fecho. No Método, o capítulo 02 Modelar mais o fecho. As demais internas abrem **claras** e só têm o fecho marinho. A faixa marinho do slogan sai.
2. **Dourado: ≤ 1 por viewport, ≤ 3 por página**, fora o logo. É só forma (triângulo, barra destacada, fio de decisão, tracejado do hero) e o CTA do fecho. Texto dourado só em rótulo de 12px: `#85622A` no claro e `#D4B37C` no escuro.
3. **Zero cartões em listas.** Listas de 3 ou mais itens viram **colunas separadas por fio vertical de 1px `--fio`**, ou linhas separadas por fio horizontal. Moldura só para objeto interativo (simulador, formulário). Raio padrão de **2px**, com botões e campos incluídos, e nenhum `999px`.
4. **Um assunto, um objeto.** Cada seção tem uma ideia e **um** objeto de apoio (gráfico, diagrama, tabela, lista ou citação), nunca dois. A home fica com **no máximo 8 seções**: fundir Credenciais no hero (linha de 4 itens sob os botões, separados por fio) e "Como começa" no fecho.
5. **Grade de prancha.** O texto ocupa as colunas 1–6 ou 1–7 (máx. 64ch) e o objeto vai em 8–12 ou na largura total. O H2 tem no máximo 18ch. Tudo é **alinhado à esquerda**, sem bloco centralizado. Toda abertura interna tem um objeto à direita (diagrama, número-chave ou módulos do D), sem metade vazia.
6. **Cadência vertical.** A seção tem 128px de padding no desktop e 80px no celular. O separador é um fio de 1px na largura da grade. O fundo `--nevoa` vale para no máximo 1 seção a cada 3, e só para "páginas de análise" (gráfico, tabela, simulador). Entre o título e o corpo ficam 24px, e entre o corpo e o objeto, 48px. A base é 8.
7. **Um CTA primário por seção, quando houver.** O botão é marinho cheio, raio de 2px, altura de 48px, Inter 600 16px. No escuro, é fundo branco com texto marinho, e o botão dourado aparece só no fecho. A ação secundária é **link sublinhado** (fio de 1px, offset de 4px), nunca um segundo botão.
8. **Número antes de opinião.** Toda página interna mostra um gráfico, diagrama ou número-chave **antes da metade da rolagem**. Os numerais de destaque vão em Source Serif `tnum`. Todo número ilustrativo leva legenda de premissa em 14px `--grafite-2`. Conteúdo com animação de entrada (`.surge`) deve ficar **visível por padrão**, e só animar se o JS confirmar que está fora da tela.

### Tokens para colar (referência)
```css
:root{
  --marinho:#082538; --marinho-2:#0F3550; --fio-escuro:#2A4A62;
  --dourado:#B58A44; --dourado-texto:#85622A; --dourado-claro:#D4B37C;
  --branco:#FFFFFF; --nevoa:#F4F6F8; --nevoa-2:#E8EDF1;
  --fio:#D3DCE3; --fio-forte:#7A8D9E;
  --grafite:#47586A; --grafite-2:#5E6E7D; --gelo-marinho:#B9C8D4; --aco:#5B7790;
  --serif:"Source Serif 4",Georgia,serif; --sans:Inter,system-ui,sans-serif;
  --display:600 clamp(2.5rem,1.6rem + 3.2vw,4.06rem)/1.05 var(--serif);
  --h1:600 clamp(2.06rem,1.5rem + 2.2vw,3.25rem)/1.1 var(--serif);
  --h2:600 clamp(1.75rem,1.3rem + 1.6vw,2.6rem)/1.15 var(--serif);
  --h3:600 clamp(1.44rem,1.3rem + .5vw,1.66rem)/1.25 var(--serif);
  --h4:600 clamp(1.19rem,1.1rem + .3vw,1.31rem)/1.35 var(--sans);
  --lead:400 clamp(1.19rem,1.1rem + .3vw,1.31rem)/1.5 var(--sans);
  --corpo:400 clamp(1rem,.96rem + .15vw,1.0625rem)/1.65 var(--sans);
  --legenda:400 .875rem/1.5 var(--sans);
  --rotulo:600 .75rem/1.2 var(--sans); /* + letter-spacing:.14em; uppercase */
  --r:2px; --max:1180px;
}
```
