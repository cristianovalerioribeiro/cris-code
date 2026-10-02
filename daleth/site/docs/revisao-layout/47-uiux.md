# DALETH · Revisão de layout e especificação de redesenho (agente 47, UI/UX)

Base: `site/assets/site.css`, `paginas/00-inicio.html`, `build.py` e as capturas de 1440px e 390px (home, empresas, simulador, terreno, repertório, método e contato). O conteúdo e a estratégia não mudam. Mudam a forma, a ordem e o peso.

**Resumo em uma frase:** o site não tem um problema de acabamento. O problema é de **densidade e de igualdade**. São 13 faixas na home (8.471px no desktop e 14.337px no celular, ou seja, 17 telas), quase todas com o mesmo molde: rótulo dourado, H2, lead cinza e uma grade de cartões com borda. Como tudo tem o mesmo peso, nada se destaca: o MODELAR, as ferramentas e o CTA ficam no mesmo volume que a lista de credenciais. Somam-se a isso uma tipografia de startup (Manrope 700 apertada) para uma marca cujo wordmark é romano clássico, e a sensação de "não está bacana" se explica.

---

## 1. Diagnóstico: os 14 problemas mais graves, em ordem de impacto

| # | Onde | O que está errado | Princípio violado | Correção concreta |
|---|---|---|---|---|
| 1 | Home inteira | 13 faixas e 17 telas no celular. Para quem, Atuação, Método, Trilho e Repertório explicam a mesma ideia (três dimensões, uma decisão) cinco vezes em formatos diferentes. O CTA principal aparece só no hero e no fecho. | Nielsen #8 (estética e design minimalista); hierarquia visual | Reduzir para **9 seções** (ver §2): fundir *Para quem* com *Atuação*, levar o *Trilho* para /empreendimentos/ e as *Credenciais* para "Quem conduz". Meta: no máximo 6.000px no desktop e 10.000px no celular. |
| 2 | Home e internas: `.momento`, `.dimensao`, `.passo`, `.cartao`, `.movimento`, `.quadro` | Cartão com borda de 1px e raio de 6px é usado para tudo, inclusive texto estático que não é clicável. A home tem **19 caixas com borda**. O manual pede "evitar excesso de molduras, cartões". Além disso, cartão estático e cartão clicável (momentos) têm a mesma aparência. | Gestalt (similaridade: coisas iguais parecem fazer a mesma coisa); Nielsen #4 (consistência) | Cartão só para (a) unidade clicável num catálogo (as 9 modelagens), (b) contêiner de ferramenta (simulador) e (c) formulário. O resto vira **linha**: um fio de 1px em cima, 24px de respiro e nenhuma caixa. Ver §4.7. |
| 3 | Tipografia global | Manrope 700 com tracking de -0.025em é uma grotesca geométrica de fintech e SaaS. O wordmark é uma serifa romana de alto contraste. O título não conversa com a marca e o tom "Sábio e sereno" vira "startup confiante". No corpo, o lead (Inter 20,8px, #4E5D69) fica quase do tamanho do H3 (21px) e as camadas se confundem. | Hierarquia tipográfica; coerência de marca | Títulos em **Source Serif 4** (Google Fonts, eixo óptico) com peso 600, corpo e interface em **Inter**. Nova escala com saltos claros (§4.1). O lead fica menor que o H3 e com cor própria. |
| 4 | Topo de todas as páginas: cabeçalho + faixa do slogan + migalhas | Antes do conteúdo vêm três faixas empilhadas: branco 72px, marinho 46px com fio dourado e cinza 44px, somando **162px de cromo**. Na home, a faixa marinha encosta no hero marinho, então o slogan "some" justamente onde deveria aparecer mais. Nas internas, a faixa marinha pesa mais que o próprio H1. | Figura/fundo; hierarquia; Nielsen #8 | A faixa do slogan passa para **fundo claro quente (#F6F3EE), texto em serifa itálica marinho**, 40px de altura, acima do cabeçalho. As migalhas entram **dentro** da abertura, sem faixa própria. O cromo cai para 112px e o slogan ganha contraste com o hero marinho. Ver §5. |
| 5 | Celular: cabeçalho | O CTA "Analisar meu caso" fica escondido dentro do menu. Abaixo de 1080px, a única ação visível é o hambúrguer, e o próximo botão só aparece no fim do hero e depois no fecho, 15 telas abaixo. | Nielsen #6 (reconhecer em vez de lembrar); objetivo de conversão | Botão compacto "Conversar" (36px de altura visual, área de toque de 44px) ao lado do botão de menu a partir de 360px. Logo de 128px. Ver §5 e §6. |
| 6 | Simulador (desktop e celular) | No celular, os 5 controles vêm **antes** dos indicadores e do gráfico: a pessoa mexe no controle e não vê o efeito, que fica 900px abaixo. O gráfico é um SVG que escala junto com a viewBox, então os rótulos do eixo ficam com cerca de 6px a 390px. O eixo Y não tem valores (só o "0"), e o salto vertical no mês 27 parece erro. A ferramenta começa em y≈650px no desktop. | Nielsen #1 (visibilidade do estado); #2 (correspondência com o mundo real); WCAG 1.4.4 | Ordem no celular: **indicadores → gráfico → controles**, com o indicador principal grudado no topo (`position:sticky; top:56px`) enquanto os controles rolam. Gráfico com 320px de altura no desktop e 240px no celular, rótulos de eixo em HTML ou SVG com `font-size` fixo de 12px, eixo Y em "R$ mi" com 4 marcas e anotação do pico **fora** da linha. Abertura compacta para a ferramenta começar antes de 480px. |
| 7 | Terreno, celular | A tabela de 4 colunas ganha rolagem horizontal e mostra só "Critério | Vender". Para comparar três caminhos, a pessoa precisa memorizar a coluna anterior. | Nielsen #6; propósito da ferramenta (comparar) | Abaixo de 768px a tabela vira **6 blocos por critério**, cada um com 3 linhas rotuladas (Vender / Permutar / Incorporar), lidas na vertical. Mesmo HTML da tabela, com `display:block` e `data-label` nos `td`. A dica de "arraste a tabela" deixa de existir. |
| 8 | Páginas internas: `.abertura` | A abertura ocupa cerca de 580px, com H1 de 3 linhas à esquerda e 40% da largura vazia à direita, e o conteúdo começa abaixo da dobra. No Contato, o formulário (a página inteira existe por causa dele) começa em y≈730px. | Hierarquia; Nielsen #8 | Abertura com 64px em cima e 48px embaixo, H1 com até 2 linhas (máximo de 18ch em 48px) e lead de no máximo 2 linhas. Na coluna direita a partir de 1024px, um **índice "Nesta página"** com âncoras (páginas de texto) ou nada, com o texto ocupando 8 colunas. No Contato e nas ferramentas, a abertura é um bloco de cabeçalho dentro da própria seção da ferramenta e do formulário (§3). |
| 9 | Internas: padrão "título à esquerda, lista à direita" (Empresas: "Sinais", "Depois da recomendação"; Simulador: "Para entender a curva") | A coluna da esquerda acaba depois de 3 linhas e deixa um vão de 400 a 600px enquanto a direita continua. Visualmente parece que falta conteúdo. | Gestalt (proximidade e região); equilíbrio | A partir de 1024px, a coluna de título fica **sticky** (`position:sticky; top:96px`) em 4 colunas, com o conteúdo em 7 colunas e 1 coluna de respiro. Quando o conteúdo da direita é menor que 3 itens, uma coluna só com 8/12. |
| 10 | Home: ritmo de fundos | Alternância entre branco #FFF e papel #F3F5F7 com **contraste de 1,09:1**, praticamente imperceptível. As seções se separam apenas pelas caixas dentro delas. No fim, fecho marinho (#082538) e rodapé (#061C2B) têm **1,10:1** e viram um bloco escuro de cerca de 900px, onde o CTA final se perde. | Figura/fundo; Gestalt (região comum) | Papel com tom quente **#F6F3EE**, que se distingue do branco pela temperatura e não só pela luminância. No máximo 2 capítulos marinhos por página além do fecho, nunca adjacentes. **Rodapé claro** (papel quente) para separar do fecho marinho. Ver ritmo em §2. |
| 11 | Home: "Tese" (`.cadeia`) e "Método" (`.movimentos`) | A cadeia de consequências, que é o diagrama mais importante da tese, aparece como lista vertical de 6 itens com 92px entre eles e linha #23506F quase invisível (1,84:1). O método são 4 cartões, e o MODELAR em bloco marinho parece botão ou cartão selecionado, não "o centro". | O manual pede "diagramas para explicar relações"; hierarquia | **Cadeia** vira diagrama horizontal a partir de 1024px: 6 nós ligados por seta, com o último fazendo um arco de volta ("interfere em…"), e linha #4A7A9C. **Método** vira *stepper* horizontal de 4 nós numa linha contínua, com o MODELAR marcado por nó dourado maior (16px contra 10px) e o selo "Onde a decisão se forma" acima, sem caixa marinha. |
| 12 | Home: Repertório (`.duas-colunas.inverte` + `.grade.g2`) | 4 cartões numa coluna de 460px, com 25 a 32 caracteres por linha e texto que quebra a cada 3 palavras. No celular, o texto termina em "Quatro delas…:" e o link "As nove modelagens" aparece **antes** dos 4 itens que o dois-pontos anuncia. | Legibilidade (medida da linha); ordem de leitura (WCAG 1.3.2) | Sem cartões: 4 itens em linhas de 2 colunas na largura total (título em serifa 22px e uma linha de texto), com o link "As nove modelagens, uma a uma" **depois** dos itens em todos os breakpoints. |
| 13 | Home: MODELAR (`.quadro`) | É o diferencial, mas aparece como mais uma caixa cinza com borda, parecida com os cartões. O texto à esquerda diz "Ao lado, um exemplo", e no celular o exemplo está **embaixo**. As barras douradas (#B58A44) sobre o trilho #E9EEF2 têm 2,69:1, e a barra que é o ponto do argumento é a de menor contraste. | Hierarquia (o diferencial precisa ser o maior elemento depois do hero); WCAG 1.4.11 | O quadro perde a moldura e vira **gráfico de barras sem caixa**, com 7 de 12 colunas. Barra de destaque em **#9C7535** (4,19:1 sobre branco). O texto troca "Ao lado" por "Abaixo / ao lado" via layout, ou o quadro vem antes do texto no celular (`order:-1`). Abaixo do quadro, as **duas ferramentas** (Simulador e Comparador de terreno) aparecem como 2 linhas de link com título e uma linha de descrição. Hoje o comparador de terreno nem aparece na home. |
| 14 | Global: `.surge` (entrada suave) | O conteúdo começa com `opacity:0` até o IntersectionObserver disparar. Na captura de página inteira do Método, os 4 passos de "Do primeiro contato à implantação" saem **apagados**. Se o JS falhar parcialmente, a impressão e as ferramentas de leitura também perdem o conteúdo. | Nielsen #1; robustez | Animar só `transform` (12px → 0) com `opacity` mínima de 0.01 → 1 em 400ms **e** um *failsafe*: depois de 1,5s do `load`, adicionar `.visivel` a todos. Ou simplesmente remover a animação: uma marca serena não precisa de coisas surgindo. |

**Problemas menores para corrigir junto:**
- **Rodapé.** O fio de `.rodape-base` está no `.wrap`, então vai de 130 a 1310px enquanto o conteúdo vai de 162 a 1278px. Mover a borda para um `div` interno.
- **Pílulas de formação** em "Quem conduz" fazem a formação parecer tags de filtro. Usar texto corrido separado por " · ".
- **Monograma** num círculo marinho de 120px funciona como avatar sem foto: parece placeholder. Remover.
- **Formulário no celular.** O par label+campo tem espaçamento interno de 6px, mas o espaço entre o campo e a label seguinte é de 12px (o `.linha` vira coluna sem `gap`), e a label "E-mail" parece pertencer ao campo de Nome (Gestalt, proximidade). Usar 8px entre label e campo e 24px entre campos.
- **Altura dos campos.** O `select` tem 48px e os `input` têm cerca de 54px. Igualar em 48px.
- **Etiquetas `.tags` do repertório** em 10,56px (.66rem) ficam abaixo do mínimo legível. Mínimo de 12px.
- **Números "01…04" do método** em #6B7A86 têm 4,42:1 e falham AA.
- **Trilho.** O nó vazio #D6DEE6 sobre branco tem 1,36:1 e é o que distingue as etapas "decide" das outras: o estado depende só de cor fraca (WCAG 1.4.1 e 1.4.11).
- **Foco.** O anel dourado sobre papel tem 2,87:1 e falha 2.4.11/1.4.11.

---

## 2. Nova arquitetura da home

De 13 faixas para 9 seções mais o rodapé. Nenhum conteúdo novo: tudo vem do que já está em `00-inicio.html`.

| # | Seção | Fundo | Propósito | Formato (o que muda) |
|---|---|---|---|---|
| 0 | Faixa do slogan | **papel quente #F6F3EE** com fio dourado de 1px embaixo | Assinatura, regra obrigatória | 40px de altura, Source Serif 4 itálico 16px (15px no celular), marinho, centralizada. Não fica sticky. |
| 1 | Hero | **marinho** | Dizer o que é, para quem, e oferecer a conversa | Duas colunas (7/5). Esquerda: rótulo, H1 em serifa 60px (até 3 linhas), lead em 2 frases a 19px #C9D5DF com até 52ch, CTA dourado "Conversar sobre uma oportunidade" e link secundário em texto "Conhecer o método →" (não um segundo botão de mesmo peso). Direita: o cenário isométrico **sai**. No lugar entra um diagrama linear simples de "um ponto que se abre em 4 caminhos", com 4 linhas finas de 1,5px #4A7A9C e uma em dourado, conversando com o quadro da seção 2. No celular o diagrama não aparece. Altura total de até 640px no desktop. |
| 2 | Modelar: "Antes de escolher um caminho…" | **branco** | O diferencial, e a maior peça visual depois do hero | Texto em 5 colunas e quadro em 7 colunas, **sem moldura**: título do quadro, premissas em 14px, 4 barras de 16px de altura com valor tabular à direita e a nota de rodapé do quadro em 14px com fio superior. Abaixo, em largura total, a faixa "Duas ferramentas para testar antes de decidir" com 2 linhas-link (Simulador de exposição de caixa · Vender, permutar ou incorporar), separadas por fio. O botão "Testar no simulador" fica como primário. "Ver as nove modelagens" sai daqui e vai para a seção 7. |
| 3 | Como começa: "Dois passos, nesta ordem" | **papel quente** | Reduzir o risco percebido e **converter** | Os cartões viram **diagrama de 2 passos**: dois blocos de texto ligados por uma seta horizontal (01 → 02), com etiqueta "Sem custo" e "Primeiro trabalho" acima de cada título, sem borda. À direita, ou abaixo no celular, o **CTA primário** "Analisar meu caso". Hoje só há um link de texto aqui, e este é o ponto de decisão. |
| 4 | Por onde entrar (funde *Para quem* + *Atuação*) | **branco** | Encaminhar cada perfil à sua vertente | H2 "Construtoras e incorporadoras que cresceram pela capacidade de executar" e o lead. Depois, **3 colunas na ordem Empresas · Empreendimentos · Capital**. Cada coluna tem H3 em serifa, a frase de papel (`papel-dim`) e, embaixo, os momentos daquela vertente como **linhas-link** (frase com seta e fio entre elas). Empresas: "A empresa cresceu…". Empreendimentos: "Tenho um empreendimento…", "Tenho um terreno…", "Uma operação travou…". Capital: "Quero estruturar o capital…", "Já tenho investidor…". Fecha com "Ver Empresas →" e equivalentes. Saem os 6 cartões de momento e os 3 cartões de dimensão. O lead "São dimensões que dependem umas das outras…" entra como uma frase abaixo do H2. |
| 5 | A tese: "Nenhuma decisão… é tomada sozinha" | **marinho** (capítulo) | Explicar por que integrar | O texto ocupa a largura toda em cima, com o lead e o destaque. Embaixo, a **cadeia vira diagrama horizontal** (6 nós em linha e um arco de retorno do último ao primeiro, rotulado "e tudo volta a se mover"). No celular, a lista fica vertical, compacta, com 56px entre os itens. A frase de apoio fica abaixo do diagrama. |
| 6 | O método: "Quatro movimentos…" | **branco** | Mostrar a sequência e o lugar do MODELAR | *Stepper* horizontal: linha contínua de 2px #082538 com 4 nós. O MODELAR tem nó dourado de 16px e o selo acima. Cada passo tem número, título em serifa e uma frase. Sem cartões e sem bloco marinho. Link "O método em detalhe →". |
| 7 | Repertório | **papel quente** | Mostrar amplitude sem virar catálogo | Título em 5 colunas à esquerda (sticky). À direita, em 7 colunas, os 4 itens em **linhas** de 2×2 com fio superior, título em serifa 22px e texto de 16px. Depois o link "As nove modelagens, uma a uma →". |
| 8 | Quem conduz | **branco** | Dar rosto sem foto | Nome em H2 serifa, formação em uma linha de texto separada por " · " e o parágrafo. As **credenciais** (Engenharia e economia · Incorporação · Crédito imobiliário · Belo Horizonte) entram aqui como lista de definição em 4 colunas com fio superior. A faixa logo abaixo do hero sai. Sem monograma. |
| 9 | Fecho | **marinho** com fio dourado de 2px em cima | Converter | Título, texto, CTA dourado, link secundário e garantias em 3 colunas abaixo, separadas por fio #23506F (não mais ao lado, em 5 colunas). |
| — | Rodapé | **papel quente #F6F3EE** | Navegação de apoio | Ver §5. |

**Saem da home:**
- *Credenciais* como faixa: vão para a seção 8.
- *Trilho "Em que momento a DALETH entra"*: vai para /empreendimentos/, logo após a abertura, onde é o assunto da página.
- Os 3 cartões de *Dimensões*: fundidos na seção 4.

**Ritmo:** marinho → branco → papel → branco → marinho → branco → papel → branco → marinho → papel (rodapé). Nunca dois marinhos seguidos, e papel nunca encosta em papel.

---

## 3. Template das páginas internas

```
[faixa do slogan · papel quente · 40px]
[cabeçalho · branco · 72px]
ABERTURA · branco · padding 64/48 (celular 40/32)
  migalhas (14px, dentro do .wrap, 24px acima do rótulo)
  rótulo → H1 (48/34px, até 18ch) → lead (até 2 linhas, 60ch)
  ações: 1 botão primário + 1 link de texto
  ≥1024: coluna direita 4/12 = "Nesta página" (âncoras das H2, 15px, fio esquerdo de 2px)
CORPO · blocos editoriais
  Bloco padrão: H2 sticky em 4/12 + conteúdo em 7/12 (1 coluna de respiro)
  Bloco "lista": linhas com fio superior, sem cartão
  Bloco "capítulo": marinho, no máximo 1 por página (Empresas: "Depois da recomendação"; Método: "Modelar")
  Bloco "ferramenta": contêiner com borda (o único cartão grande), no primeiro viewport
FAQ · branco ou papel (o oposto do bloco anterior)
  H2 em 4/12 sticky + acordeões em 8/12; resumo em 16px/600 Inter; ícone +/− com 32px de área
  "Para continuar": 2-3 linhas-link com seta, e não uma frase com 3 links sublinhados
FECHO · marinho (específico da página)
RODAPÉ · papel quente
```

**Regras de ritmo:**
1. O H1 nunca passa de 2 linhas no desktop. Se passar, o título está longo ou o `max-width` está errado.
2. Nas páginas de **ferramenta** (Simulador, Terreno) e no **Contato**, o primeiro elemento interativo aparece até **480px** do topo no desktop e até **640px** no celular. A abertura se reduz a rótulo + H1 de 40px + uma linha de lead, e a explicação ("O que é exposição máxima…") vem **depois** da ferramenta.
3. Seções: 96px de padding vertical no desktop, 72px no tablet e 56px no celular. Entre o cabeçalho da seção e o conteúdo, 48/40/32px.
4. Entre seções de **mesmo fundo**, um fio de 1px #D6DEE6 dentro do `.wrap`, nunca de borda a borda.
5. O FAQ nunca fica imediatamente antes de um capítulo marinho que não seja o fecho.
6. Contato: duas colunas (7/5). O formulário entra a 56px abaixo do H1, com "O que ajuda na primeira mensagem" à direita em fundo papel quente. No celular, essa lista vira um `<details>` fechado **acima** do formulário ("O que contar na mensagem").
7. Empresas, Capital e Empreendimentos: a grade "Oito frentes" (cartões 4×2) vira **lista em 2 colunas** com título e uma linha, com fio superior e sem caixa.

---

## 4. Design system revisado

### 4.1 Família tipográfica

- **Títulos (H1 a H3, destaque, slogan): Source Serif 4** (Google Fonts, variável, eixos `wght` 200–900 e `opsz` 8–60).
  - É uma serifa de transição, com contraste moderado. Em `opsz` 48–60 ganha o desenho mais fino e elegante que conversa com o wordmark romano, sem ser Cambria e sem parecer Word.
  - É sóbria e editorial, e não é luxuosa como Cormorant ou Playfair, que a marca deve evitar ("não ostentosa").
  - Suporte completo a acentos PT-BR e algarismos *old-style* e *lining*.
  - Alternativa equivalente, se o Cristiano quiser mais calor: **Newsreader**.
- **Corpo, interface, números das ferramentas: Inter** (já está self-hosted). Use `font-feature-settings:"tnum"` nos valores e `"ss01"` opcional.
- **Manrope sai.** Duas famílias bastam.
- Pesos: serifa 500 (H1 e display), 600 (H2 e H3). Inter 400 (corpo), 500 (UI), 600 (rótulos, botões, labels).
- Self-hosting: baixar `SourceSerif4-Variable` com subset latin (≈60–80 KB woff2), `font-display:swap` e *preload* só da serifa.

### 4.2 Escala (razão 1,25 no desktop, ≈1,2 no celular; base 17/16px)

| Token | Desktop (≥1024) | Celular (≤767) | Família / peso | Line-height | Tracking |
|---|---|---|---|---|---|
| display (H1 home) | 60px | 38px | Serif 4 · 500 · opsz 60 | 1.08 | -0.01em |
| h1 (internas) | 48px | 34px | Serif 4 · 500 | 1.1 | -0.01em |
| h2 | 36px | 28px | Serif 4 · 600 | 1.15 | -0.005em |
| h3 | 22px | 20px | Serif 4 · 600 | 1.3 | 0 |
| h4 / título de linha | 18px | 17px | Inter · 600 | 1.4 | 0 |
| lead | 20px | 18px | Inter · 400 | 1.55 | 0 |
| corpo | 17px | 16px | Inter · 400 | 1.65 | 0 |
| apoio | 15px | 14px | Inter · 400 | 1.55 | 0 |
| rótulo | 12px | 12px | Inter · 600 · CAIXA-ALTA | 1.2 | 0.12em |
| número de ferramenta | 32px | 26px | Inter · 600 · tnum | 1.1 | -0.01em |
| botão | 16px | 16px | Inter · 600 | 1 | 0.005em |
| slogan (faixa) | 16px itálico | 15px itálico | Serif 4 · 400 | 1.4 | 0.01em |

**Tablet (768–1023):** valores intermediários via `clamp()`. Exemplo: `h2: clamp(28px, 1.2rem + 1.6vw, 36px)`.

**Medida:** corpo com no máximo 66ch e lead com no máximo 58ch. O H2 tem `max-width:22ch` e `text-wrap:balance`.

**Cor do texto:**
- Corpo #082538.
- Lead e apoio #4E5D69.
- O tom #6B7A86 **deixa de ser usado em texto**. Para números e rótulos secundários, usar #5C6B77 (5,49:1).

### 4.3 Grid

- Contêiner: `max-width: 1200px` de conteúdo com padding lateral de 40px (≥1024), 32px (768–1023) e 20px (≤767). `.wrap` total de 1280px.
- 12 colunas, gutter de 32px a partir de 1024px, 24px no tablet. No celular, 4 colunas com gutter de 16px.
- Padrões:
  - **5/7** (texto + gráfico: Modelar).
  - **4/7+1** (título sticky + conteúdo).
  - **8** (texto corrido, FAQ).
  - **3×4** (três vertentes).
  - **4×3** (credenciais e passos do método).

### 4.4 Espaçamento vertical (base 8)

| Uso | Desktop | Tablet | Celular |
|---|---|---|---|
| padding de seção | 96 | 72 | 56 |
| hero (topo/base) | 112/120 | 80/88 | 48/56 |
| abertura interna | 64/48 | 56/40 | 40/32 |
| cabeçalho da seção → conteúdo | 48 | 40 | 32 |
| rótulo → título | 16 | 16 | 12 |
| título → lead | 16 | 16 | 12 |
| lead → ações | 32 | 32 | 24 |
| entre linhas de lista (padding) | 24 | 20 | 16 |
| entre parágrafos | 16 | 16 | 16 |

### 4.5 Raio

**4px** em botões, campos, contêiner de ferramenta e cartões de catálogo. **0** em blocos de seção, barras de gráfico (2px no máximo) e etiquetas. Pílulas (`999px`) só nos filtros do repertório. O raio de 6px atual mais as pílulas deixam o site "app" demais.

### 4.6 Bordas e cartões

- **Use cartão (borda #D6DEE6 de 1px, fundo branco, raio de 4px, padding de 24px)** apenas em:
  1. as 9 modelagens (catálogo filtrável e clicável);
  2. o contêiner do simulador;
  3. o formulário;
  4. a tabela do comparador.
- **Não use cartão** para passos, momentos, dimensões, frentes, entregas, "o que sai daqui" ou credenciais. No lugar: **fio superior de 1px #D6DEE6 e padding-top de 24px**. Em fundo marinho, fio #23506F.
- Hover de item clicável sem cartão: o fio superior vira 2px #082538, a seta anda 4px e o título ganha sublinhado. Nada de `translateY` com sombra.
- O fio dourado de 2px à esquerda (`.nota`, `.destaque-frase`, garantias) fica só no `.destaque-frase` (1 por página). As notas usam fio #D6DEE6.

### 4.7 Dourado

**Usos permitidos:**
1. CTA sobre marinho (fundo #B58A44, texto #082538, 5,02:1).
2. Indicador de página ativa no menu (sublinhado de 2px).
3. Traço de 24px antes do rótulo, só nos rótulos de seção, não nos de bloco.
4. **O dado em destaque** de um gráfico: em fundo claro use **#9C7535** (4,19:1 sobre branco); em marinho, #B58A44.
5. O nó do MODELAR e os nós "decide" do trilho.
6. Fio de 1px da faixa do slogan e fio de 2px no topo do fecho.

**Proibido:**
- Dourado em corpo de texto.
- Dourado em fundo de etiqueta (o #F4ECDD sai).
- Dourado como anel de foco em fundo claro (2,87:1 sobre papel).
- Mais de **2 elementos dourados por viewport** além do rótulo.

**Texto dourado** (rótulo, "Decide o rumo quando") só em #74572A, que tem 6,12:1 sobre papel e 6,69:1 sobre branco.

### 4.8 Botões

Todos com altura de 48px (44px no cabeçalho), padding horizontal de 24px, raio de 4px, Inter 600 16px e transição de 150ms.

| Botão | Padrão | Hover | Ativo | Foco (`:focus-visible`) | Desabilitado |
|---|---|---|---|---|---|
| **Primário** (fundo claro) | #082538 / texto #FFF | #14456A | #061C2B | anel 2px #082538 + offset 2px (15,8:1) | #D6DEE6 / texto #5C6B77, `aria-disabled` |
| **Dourado** (fundo marinho) | #B58A44 / texto #082538 | #C39A57 (6,07:1) | #A47B3A | anel 2px #D2B07A, offset 3px | não usar |
| **Linha** (fundo claro) | borda 1.5px #082538, texto #082538 | fundo #F6F3EE | fundo #E9EEF2 | anel 2px #082538 | borda #D6DEE6 |
| **Linha clara** (marinho) | borda 1.5px rgba(255,255,255,.7) (8,35:1) | fundo #FFF / texto #082538 | fundo #E9EEF2 | anel 2px #D2B07A | — |
| **Link com seta** (`.mais`) | texto #082538 600, fio de 1px #082538 | fio de 2px, seta +4px | — | anel 2px | — |

**Hierarquia:**
- Uma seção tem no máximo **1 botão**. A segunda ação é link com seta, e não botão de linha.
- O hero e o fecho podem ter 1 botão e 1 link.
- No Contato, o botão "Enviar" fica com `aria-disabled` enquanto `FORMULARIO_ATIVO=False`, com o aviso ligado por `aria-describedby`.

---

## 5. Cabeçalho, menu, faixa do slogan e rodapé

**Faixa do slogan (todas as páginas)**
- Acima do cabeçalho, fora do sticky: 40px de altura, fundo #F6F3EE e fio de 1px #B58A44 na base.
- Texto: Source Serif 4 itálico 16px #082538, centralizado.
- No celular, 36px e 15px. Se não couber numa linha a 320px, quebra em 2 linhas com `text-wrap:balance`.
- Assim o slogan aparece em todas as páginas, contrasta com o hero marinho e não parece um aviso de sistema.

**Cabeçalho (sticky)**
- 72px no desktop e 60px no celular. Fundo #FFF e fio inferior de 1px #D6DEE6, que só aparece depois de 8px de rolagem.
- Logo horizontal com 160px no desktop e 128px no celular.
- Navegação:
  - **Empresas · Empreendimentos · Capital** em Inter 600 15px #082538.
  - Divisor de 1px e 24px de altura.
  - **Método · Repertório · Sobre** em Inter 500 15px #4E5D69.
  - Área de clique de 40px de altura.
- Ativo: sublinhado dourado de 2px a 6px da base do texto, sem fundo.
- CTA "Analisar meu caso" como botão primário de 44px.
- Entre 1024 e 1179px, o divisor sai e o gap cai de 24 para 16px. Abaixo de 1024px, entra o menu de painel.
- **Celular e tablet (<1024):**
  - logo, depois o botão "Conversar" (primário compacto, 40px visual com 44px de alvo), depois o botão de menu (44×44, ícone de 20px, **sem** borda e sem a palavra "Menu" abaixo de 420px).
  - O painel abre em tela cheia, com as vertentes em serifa 24px e linhas de 56px, o apoio em Inter 17px, o CTA no fim (52px) e o slogan repetido no pé do painel.

**Migalhas:** dentro da abertura, em Inter 14px #4E5D69, separador "/" e item atual em #082538 600. Altura de toque dos links de 32px, com padding vertical de 6px. Sem faixa própria.

**Fecho (marinho):** fio de 2px #B58A44 em cima. Título serifa 36px em 8 colunas, texto em 7 colunas e ações. As garantias, quando existem, ficam em **3 colunas abaixo** com fio superior #23506F. Padding de 96px.

**Rodapé (claro, #F6F3EE)**
- Fio superior de 1px #D6DEE6.
- Logo **colorido** de 160px.
- 4 colunas (4/2/3/3): marca + descrição + slogan em serifa itálico · Atuação · Para decidir · DALETH.
- Títulos de coluna em rótulo 12px #74572A, **sem** traço.
- Links em Inter 15px #082538 com 36px de altura de linha (área de toque de 36px ou mais; hoje é cerca de 22px).
- A base fica com um fio de 1px **dentro** do conteúdo (corrige o fio que vaza 32px de cada lado), 14px #4E5D69, e o aviso de prévia em #74572A.
- No celular, as colunas viram 2 (Atuação | Para decidir) e depois 1 (DALETH).

---

## 6. Celular e breakpoints

| Breakpoint | Regras |
|---|---|
| **390 (≤767)** | Gutter lateral de 20px, 1 coluna. H1 home 38px e internas 34px; H2 28px. **Hero:** sem ilustração, padding 48/56, CTA dourado em largura total (`width:100%`), link secundário abaixo. **Modelar:** quadro **antes** do texto explicativo (`order:-1`), barras de 12px, valor abaixo do nome (não à direita) quando o nome passa de 1 linha. **Por onde entrar:** 3 vertentes empilhadas, cada uma com linhas-link de 56px de altura. **Tese:** cadeia vertical compacta. **Método:** *stepper* vertical com linha à esquerda (como o trilho atual). **Simulador:** indicador principal sticky abaixo do cabeçalho (56px), gráfico de 240px, controles depois, e botões de arranjo em grade 2×2 de 44px de altura. **Terreno:** tabela vira blocos por critério. **Contato:** campos em 1 coluna, 8px entre label e campo, 24px entre campos. **Toques:** todo link de lista com 44px de altura mínima, e links inline no texto isentos. |
| **768 (768–1023)** | Gutter de 32px, grid de 8 colunas. Hero em 1 coluna com o diagrama de caminhos opcional abaixo do texto, a 50% de opacidade. Vertentes em 3 colunas só se cada uma tiver pelo menos 220px; senão, 1 coluna com título à esquerda e links à direita (3/5). Método em *stepper* horizontal de 4 nós com texto de 15px. Repertório em 2 colunas. Simulador em 1 coluna, com controles em 2 colunas abaixo do gráfico. Comparador de terreno já em tabela (cabe com 4 colunas de cerca de 170px). Menu ainda em painel. |
| **1024 (1024–1439)** | Gutter de 40px, 12 colunas e menu completo. Títulos sticky ligados. Hero 7/5 com diagrama. Simulador com controles em 4/12 e resultados + gráfico em 8/12. Cadeia horizontal. Nunca mais que 4 itens por linha. |
| **1440 (≥1440)** | Conteúdo travado em 1200px, centralizado. Nada cresce além disso, nem a tipografia: o `clamp` para em 1280px de viewport. O fundo de seção vai de borda a borda e o conteúdo, não. |

**Regras transversais:**
- `scroll-padding-top` igual à altura do cabeçalho mais 16px.
- Nenhum `min-width` maior que o viewport em tabelas. O atual `min-width:760px` do comparador sai abaixo de 768px.
- A ilustração do hero não é carregada no celular (`display:none` não basta: usar `<picture>`/`media` ou injetar via JS acima de 768px).

---

## 7. Checklist WCAG 2.2 AA dos pares de cor

Calculado com a fórmula de luminância relativa do WCAG em Python (`scratchpad/revisao/contraste.py`).

### Pares em uso hoje

| Par | Contraste | Mínimo | Resultado |
|---|---|---|---|
| Texto marinho #082538 / branco | 15,77:1 | 4,5 | PASSA |
| Texto marinho / papel #F3F5F7 | 14,43:1 | 4,5 | PASSA |
| Grafite #4E5D69 / branco | 6,79:1 | 4,5 | PASSA |
| Grafite / papel | 6,21:1 | 4,5 | PASSA |
| Grafite / papel-2 #E9EEF2 (tags) | 5,81:1 | 4,5 | PASSA |
| **Grafite-claro #6B7A86 / branco** (números 01–04 do método) | 4,42:1 | 4,5 | **FALHA** |
| **Grafite-claro / papel** | 4,04:1 | 4,5 | **FALHA** |
| Ouro-texto #7F5F2C / branco (rótulos) | 5,87:1 | 4,5 | PASSA |
| Ouro-texto / papel | 5,37:1 | 4,5 | PASSA |
| Ouro-texto / bege #F4ECDD (etiqueta) | 5,00:1 | 4,5 | PASSA |
| **Ouro #B58A44 como texto / branco** | 3,14:1 | 4,5 | **FALHA**, nunca usar |
| Ouro #B58A44 como anel de foco / branco | 3,14:1 | 3,0 | passa, por pouco |
| **Ouro #B58A44 como anel de foco / papel** | 2,87:1 | 3,0 | **FALHA** |
| Marinho / ouro #B58A44 (btn-ouro) | 5,02:1 | 4,5 | PASSA |
| Marinho / ouro-claro #D2B07A (hover do btn-ouro) | 7,68:1 | 4,5 | PASSA |
| Ouro #B58A44 / marinho | 5,02:1 | 4,5 | PASSA |
| Ouro-claro #D2B07A / marinho (rótulo escuro) | 7,68:1 | 4,5 | PASSA |
| Ouro-claro / rodapé #061C2B | 8,46:1 | 4,5 | PASSA |
| Branco / marinho | 15,77:1 | 4,5 | PASSA |
| Branco / #14456A (hover primário) | 10,05:1 | 4,5 | PASSA |
| #C9D5DF / marinho (lead escuro) | 10,56:1 | 4,5 | PASSA |
| #B8C7D3 / marinho | 9,12:1 | 4,5 | PASSA |
| #A9BAC8 / marinho (.apoio escura) | 7,92:1 | 4,5 | PASSA |
| #B8C7D3 / rodapé #061C2B | 10,05:1 | 4,5 | PASSA |
| #E3EAF0 / rodapé (links) | 14,31:1 | 4,5 | PASSA |
| **Fio #D6DEE6 / branco** (nó vazio do trilho: indica estado) | 1,36:1 | 3,0 | **FALHA** (1.4.11) |
| **Borda de input #BCC8D3 / branco** | 1,70:1 | 3,0 | **FALHA** (1.4.11) |
| Borda btn-linha-clara rgba(255,255,255,.55) / marinho | 5,67:1 | 3,0 | PASSA |
| **Linha da cadeia #23506F / marinho** | 1,84:1 | 3,0 | **FALHA** (é parte do diagrama) |
| Barra marinho / trilho #E9EEF2 | 13,50:1 | 3,0 | PASSA |
| **Barra ouro #B58A44 / trilho #E9EEF2** (a barra de destaque!) | 2,69:1 | 3,0 | **FALHA** |
| Papel #F3F5F7 / branco (separação de seções) | 1,09:1 | — | imperceptível |
| Rodapé #061C2B / fecho #082538 | 1,10:1 | — | os dois se fundem |

### Correções propostas (todas verificadas)

| Novo par | Contraste | Resultado |
|---|---|---|
| Texto secundário #5C6B77 / branco · / papel | 5,49 · 5,02:1 | PASSA (substitui #6B7A86) |
| Ouro-texto #74572A / branco · / papel | 6,69 · 6,12:1 | PASSA (rótulos e "Decide o rumo quando") |
| Dado em destaque #9C7535 / branco · / papel | 4,19 · 3,84:1 | PASSA 3:1 (barras, nós "decide", gráfico do simulador) |
| Borda de campo e nó vazio #7D8D9B / branco · / papel | 3,41 · 3,12:1 | PASSA (substitui #BCC8D3 nos inputs e #D6DEE6 nos nós do trilho) |
| Linha de diagrama #4A7A9C / marinho | 3,42:1 | PASSA (cadeia, ilustração do hero) |
| Anel de foco #082538 / claro | 15,77:1 | PASSA (o foco em fundo claro passa a ser marinho; em fundo escuro, #D2B07A com 7,68:1) |
| Hover do btn-ouro #C39A57 com texto marinho | 6,07:1 | PASSA |
| Papel quente #F6F3EE: marinho 14,24 · grafite 6,13 · ouro-texto 5,31:1 | — | PASSA (novo fundo de seção, slogan e rodapé) |
| Borda btn-linha-clara rgba(255,255,255,.7) / marinho | 8,35:1 | PASSA |

**Observação:** #8A9AA8 (2,89:1) e #8797A5 (3,00:1, no limite exato) foram testados e **descartados**. Use #7D8D9B.

### Demais critérios WCAG 2.2 a verificar na implementação

- **2.4.11 Foco não obscurecido.** O cabeçalho sticky de 72px não pode cobrir o elemento focado. Usar `scroll-padding-top: 88px`, que já existe, e conferir também nos acordeões.
- **2.4.7 / 2.4.13 Foco visível.** Anel de 2px com offset de 2px em todos os interativos, inclusive `summary`, `input[type=range]` e as linhas-link.
- **2.5.8 Tamanho do alvo (24px mínimo, 44px recomendado).**
  - Hoje falham ou ficam no limite: links do rodapé (cerca de 22px de altura com 8px de gap), migalhas (cerca de 20px), `.mais` (cerca de 22px) e o ícone do FAQ (28px, mas o `summary` inteiro é clicável, então passa).
  - Meta: 44px em listas e menus, 32px nas migalhas.
- **1.4.1 Uso de cor.** O trilho diferencia "decide" só pela cor. Somar forma: nó preenchido contra vazado, mais texto "decisão" no `aria`/legenda. O mesmo vale para a barra de destaque do quadro, que precisa de rótulo textual "menor exposição".
- **1.4.4 / 1.4.10 Redimensionar e refluxo.** Os textos SVG do gráfico do simulador não podem cair abaixo de 12px, e não pode haver rolagem horizontal a 320px (comparador de terreno).
- **1.3.2 Sequência significativa.** No repertório da home, o link vem depois dos itens. No Modelar do celular, "Ao lado" não pode apontar para algo que está abaixo.
- **2.3.3 / movimento.** A entrada `.surge` precisa de *failsafe*, e `prefers-reduced-motion` deve desligar também o parallax do hero (hoje só desliga o `transform` do SVG).
- **3.3.2 Rótulos.** O formulário está ok (labels visíveis). Manter o "(opcional)" e adicionar `autocomplete` (name, email, tel, organization, address-level2).

---

**Ordem de implementação sugerida:**
1. Tokens de cor e tipografia (§4) e a faixa do slogan + cabeçalho (§5), que já mudam a percepção do site inteiro.
2. Home (§2).
3. Ferramentas no primeiro viewport e simulador e terreno no celular (#6, #7).
4. Template interno (§3).
5. Checklist WCAG (§7).
