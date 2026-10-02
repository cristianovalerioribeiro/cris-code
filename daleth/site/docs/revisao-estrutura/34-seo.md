# 34 · Marketing SEO: arquitetura da informação do site DALETH

**02/10/2026 · agente 34-marketing-seo · escopo: arquitetura de busca e navegação** (páginas, hierarquia, menu, URLs, links internos, intenção de busca, title/description). Fica de fora desta peça, para uma segunda passada: auditoria técnica completa de 50 itens, Core Web Vitals medidos e CSV de palavras-chave com volume.

**Base de dados desta análise.** Li as 14 páginas em `daleth/site/paginas/`, o `build.py`, o Caderno Estratégico v02 (§01, §07, §12), o Caderno de Definições do Site e o briefing da pesquisa de concorrentes v02. Também fiz buscas no Google (amostra pequena, sem ferramenta de volume).

**O que eu não tenho.** O site está em `noindex` e `Disallow: /`, então não há Search Console, posição nem CTR. Também não há Ahrefs, Semrush nem Keyword Planner. **Nenhum volume citado aqui é medido. Toda prioridade de palavra-chave é estimativa qualitativa**, baseada em que tipo de página aparece hoje na busca e em quanto a consulta é comercial. Os volumes precisam ser validados no Keyword Planner antes de o site sair da prévia.

---

## 0. A conclusão em cinco linhas

1. **O site está organizado pela lógica interna da DALETH** (vertentes, método, repertório), **e não pelo que o cliente digita.** As três páginas-mãe usam rótulos internos ("Empresas", "Capital", "Repertório") e ninguém busca "estruturação de negócios imobiliários".
2. **As consultas comerciais mais fortes do mercado não têm uma página dona.** "Estudo de viabilidade" está espalhado em 6 páginas e não é o assunto de nenhuma. "Financiamento à produção" aparece duas vezes em /capital/, de passagem (item de lista e FAQ). "Plano Empresário", "Apoio à Produção", "SBPE" e "GERIC" têm zero ocorrências.
3. **Três páginas contam a mesma história** (Início, Método e Como começa repetem conversa → diagnóstico), **e duas páginas institucionais não têm intenção de busca** (Repertório e Método competem pelo mesmo conceito).
4. **O momento de corrigir URL é agora.** Com o site em noindex, mudar endereço custa zero. Depois da indexação, cada mudança exige 301 e perde sinal.
5. **A mudança proposta é mais de nomes, endereços e ligações do que de conteúdo novo.** De verdade, só três páginas novas importam agora: Estudo de viabilidade, Financiamento à produção e Privacidade. O resto é reorganizar o que já existe.

---

## 1. Diagnóstico da arquitetura atual

### 1.1 Mapa atual

```
/                                  Início
├── /empresas/                     vertente
├── /empreendimentos/              vertente
│   ├── /empreendimentos/terreno/        vender × permutar × incorporar
│   ├── /empreendimentos/simulador/      ferramenta
│   └── /empreendimentos/obra-parada/    recuperação de obras
├── /capital/                      vertente
├── /metodo/                       institucional
├── /repertorio/                   institucional (9 modelagens)
├── /como-comeca/                  conversão (conversa + diagnóstico)
├── /sobre/                        EEAT
├── /contato/                      conversão
├── /contato/recebido/             noindex
└── /404/                          noindex
```

A profundidade é boa: tudo fica a 2 cliques ou menos e as migalhas estão corretas, com schema BreadcrumbList. **O problema não é a profundidade. É o que cada página tenta ser.**

### 1.2 Página por página: intenção de busca

| Página | Intenção que deveria capturar | O que acontece hoje | Veredito SEO |
|---|---|---|---|
| `/` | marca + categoria | ok para busca pela marca | mantida |
| `/empresas/` | "gestão / financeiro / societário de construtora" | o title começa com o rótulo interno "Empresas ·". "Preparação para análise externa" é a frente com mais demanda comercial (o GERIC) e aparece só como um item de lista | mantida, renomeando o title |
| `/empreendimentos/` | "planejamento / incorporação de empreendimento" | **página-ônibus**: tenta ser terreno, produto, viabilidade, cronograma, incorporação e acompanhamento ao mesmo tempo. Leva 6 das 11 ocorrências de "viabilidade" e por isso canibaliza a página que deveria existir | mantida como página-pilar, entregando "viabilidade" a uma filha |
| `/empreendimentos/terreno/` | "permuta de terreno", "vender ou permutar terreno" | conteúdo bom e claro, mas a URL `/terreno/` não carrega a palavra que o proprietário digita (permuta) | mantida, mudando a URL |
| `/empreendimentos/simulador/` | "fluxo / exposição de caixa de incorporação" | boa ferramenta, mas fala de permuta 8 vezes e disputa assunto com `/terreno/` (12) | mantida, delimitando o assunto |
| `/empreendimentos/obra-parada/` | "obra parada, retomada", "comprar obra parada" | a busca é dominada por escritórios de advocacia (direito do comprador). A DALETH entra pelo ângulo técnico e financeiro, que é outra intenção | mantida, com um title que diferencie |
| `/capital/` | "crédito para construtora", "financiamento para incorporação" | o title usa "funding imobiliário", que é jargão. As linhas que o cliente nomeia (Plano Empresário, Apoio à Produção, SBPE) não aparecem | mantida, com uma filha nova |
| `/metodo/` | navegação, EEAT | não tem intenção de busca, o que é normal. Mas repete o passo a passo de `/como-comeca/` e não linka para nenhuma vertente | mantida, enxugando a repetição |
| `/repertorio/` | nenhuma | "Repertório" é um nome interno. O conteúdo (as 9 modelagens) é bom, mas é a semente da Inteligência, não uma página de menu | fundida sob Método |
| `/como-comeca/` | "como funciona / quanto custa / diagnóstico" (fundo de funil) | conteúdo certo, mas **nenhum link no corpo** e fora do menu, só no rodapé e no fecho de 2 páginas | mantida e promovida |
| `/sobre/` | marca + nome do fundador (EEAT) | **nenhum link no corpo**. O title fica "Sobre a DALETH · DALETH", com a marca repetida | mantida, title corrigido |
| `/contato/` | navegação | ok | mantida |

### 1.3 Canibalização encontrada

Contei termos em `paginas/*.html`:

| Termo | Onde aparece | Problema |
|---|---|---|
| **viabilidade** | empreendimentos (6), terreno, simulador, repertório, como-começa, sobre (1 cada) | nenhuma página é dona. A FAQ de `/empreendimentos/` chega a responder "O estudo de viabilidade diz se vai dar certo?" e "O simulador substitui o estudo de viabilidade?", sinal de que o assunto pede página própria |
| **permuta** | terreno (12), simulador (8), home (4), repertório (4), empreendimentos (2), método, sobre | terreno e simulador disputam. Regra proposta: **terreno é dono de "permuta de terreno"** (o lado do proprietário); **simulador é dono de "exposição de caixa"**, e a permuta aparece ali só como variável |
| **conversa de enquadramento → diagnóstico** | home ("Dois passos, nesta ordem"), método ("Do primeiro contato à implantação"), como-começa (página inteira) | três versões do mesmo bloco. **Dono: `/como-comeca/`.** Home e método resumem em duas linhas e linkam |
| **9 modelagens** | home (4 exemplos), método, repertório | ok na home (que resume); método e repertório disputam o conceito, e por isso a fusão |
| **"Quanto tempo leva?"** (FAQ) | empresas, como-começa, obra-parada | gera FAQPage com perguntas repetidas entre páginas. Fica a versão geral em `/como-comeca/` e as outras ficam específicas ("Quanto tempo leva para organizar uma empresa?" já está bom) |

### 1.4 Vocabulário que o cliente usa e o site não tem

| O cliente digita | Ocorrências no site | Quem ranqueia hoje (amostra das buscas) |
|---|---|---|
| estudo de viabilidade (imobiliária / de incorporação) | 11, espalhadas, sem página | software de gestão (guia da Sienge), portais (Portas), cursos (CREA, FGV), TCCs. **Quase nenhuma consultoria com página de serviço**, o que é uma brecha |
| financiamento à produção / Plano Empresário / Apoio à Produção | 2 / 0 / 0 | página oficial da Caixa, blog da Sienge, sindicatos (Sinduscon) |
| SBPE (construtora / incorporadora) | 0 | Caixa, imprensa econômica |
| GERIC | 0 | **uma concorrente (Planning) tem página dedicada a GERIC**, além de sites de perguntas e respostas. É sinal de intenção comercial: quem busca GERIC é a construtora que vai ao banco |
| permuta física × financeira | só na FAQ de terreno | escritórios de advocacia, CRECI, Sinduscon, FGV Direito |
| SPE × SCP × holding | SPE 6 (de passagem), SCP 0, holding 2 | advocacia e contabilidade (Jornal Contábil, Jus, escritórios) |
| patrimônio de afetação / RET | 2 / 0 | advocacia |
| obra parada o que fazer | 4 | notícias (casos reais em SP) e advocacia |
| consultoria para construtora / incorporadora | **0** (a marca evita a palavra) | escritórios de advocacia, marketplaces de consultores |

**Tensão a decidir (dono):** o cliente digita "consultoria", e a marca se posiciona contra "consultoria tradicional" (Caderno §07). Recomendação: não usar a palavra em title nem em H1, mas aceitá-la uma vez no corpo das vertentes, em frase de contraste ("não é consultoria que entrega relatório e sai: acompanhamos a implantação"). Assim a página fica legível para essa busca sem mudar a categoria.

### 1.5 Menu, rodapé e links internos hoje

- **Menu atual:** Empresas · Empreendimentos · Capital | Método · Repertório · Sobre | [Analisar meu caso]. Problemas:
  - "Repertório" é um rótulo interno.
  - "Como começa", "Obras paradas" e as ferramentas não estão no menu.
  - O menu previsto no Caderno §12 (Início | Método | Atuação | Cases | Inteligência | Sobre) ainda não foi aplicado.
  - Os cases não existem, e eles não devem entrar no menu antes de existirem.
- **Páginas sem links no corpo:** `/como-comeca/` e `/sobre/`. São becos sem saída, salvo pelo menu e pelo fecho.
- **Páginas pouco linkadas** (links no corpo de outras páginas): `/como-comeca/` (1, da home), `/empreendimentos/obra-parada/` (2), `/sobre/` (2), `/metodo/` (3).
- **Ligações que faltam entre vertentes:** `/metodo/` não linka nenhuma vertente; `/terreno/` não linka `/capital/` nem `/como-comeca/`; `/simulador/` não linka `/empreendimentos/` no corpo (só pela migalha).
- **Texto âncora:** "Tenho um terreno", "Ver o efeito de cada uma" e "Simulador de exposição" estão bons para a pessoa, mas fracos para busca. A regra proposta é que pelo menos um link para cada página use a palavra-chave dela ("estudo de viabilidade", "permuta de terreno").

### 1.6 Titles e descriptions hoje

- **9 de 12 descriptions passam de 155 caracteres** (vão de 151 a 193) e saem cortadas na busca.
- **Os titles das vertentes começam pelo rótulo interno** ("Empresas ·", "Capital ·", "Método ·", "Repertório ·") e gastam os primeiros caracteres, que são os que mais pesam.
- **Marca duplicada:** o `build.py` acrescenta " · DALETH" a todo title menos a home, e por isso sai "Sobre a DALETH · DALETH". Um title que já começa por "Método DALETH" precisaria de uma marca no metadado que dispense o sufixo, algo como `"sem_sufixo": true`.
- **Jargão no title:** "funding imobiliário" (Capital) e "Repertório".

### 1.7 Pontos estruturais de publicação (fora da arquitetura, mas travam o SEO)

- **Domínio.** O site está em `daleth.iajudite.com.br`, um subdomínio de outra marca. **Se o domínio definitivo vai ser outro, publicar direto nele.** Indexar no subdomínio e migrar depois obriga a fazer 301 em massa e perde sinal (anti-padrão: "migrar URLs sem 301"). **Decisão do dono, e precede a saída da prévia.**
- **Política de privacidade.** Não existe, e o formulário coleta dados. É exigência da LGPD e sinal de confiança (o T de EEAT). Está no checklist do Caderno §12.
- **EEAT.** O tema é financeiro e de crédito, próximo de YMYL. Pesam aqui: Sobre com foto, LinkedIn e `sameAs` (Definições 1.3), prova verificável (1.4) e autor identificado nos artigos de Inteligência. Sem isso os artigos rendem pouco.

---

## 2. Mapa do site proposto

Legenda: **[M]** mantida · **[M→URL]** mantida com URL nova · **[N]** nova · **[F]** fundida · **[D]** depende de decisão do dono (com o item do Caderno de Definições).

```
/                                                  [M]  Início
│
├── /empresas/                                     [M]  pilar Empresas
│   └── /empresas/preparacao-para-credito/         [N][D 4.3]  preparar a construtora para a análise de crédito (GERIC)
│
├── /empreendimentos/                              [M]  pilar Empreendimentos
│   ├── /empreendimentos/estudo-de-viabilidade/    [N][D 4.4]  ★ prioridade 1
│   ├── /empreendimentos/permuta-de-terreno/       [M→URL]  era /empreendimentos/terreno/
│   ├── /empreendimentos/simulador/                [M]  ferramenta (exposição de caixa)
│   └── /empreendimentos/obra-parada/              [M]  recuperação de obras paradas
│
├── /capital/                                      [M]  pilar Capital
│   └── /capital/financiamento-a-producao/         [N][D 4.3]  Plano Empresário, Apoio à Produção, SBPE
│
├── /metodo/                                       [M]  institucional
│   └── /metodo/modelagens/                        [F]  era /repertorio/
│
├── /como-comeca/                                  [M]  diagnóstico de estruturação (fundo de funil)
│
├── /inteligencia/                                 [N][D 4.2]  hub: ferramentas + artigos
│   ├── /inteligencia/spe-holding-ou-scp/                  [N][D 4.2]
│   ├── /inteligencia/patrimonio-de-afetacao/              [N][D 4.2]
│   ├── /inteligencia/permuta-fisica-ou-financeira/        [N][D 4.2]
│   └── /inteligencia/faseamento-e-exposicao-de-caixa/     [N][D 4.2]
│
├── /cases/                                        [D 4.1]  NÃO criar até haver caso autorizado ou anonimizado
├── /sobre/                                        [M]  EEAT
├── /contato/                                      [M]  conversão
│   └── /contato/recebido/                         [M]  noindex
├── /privacidade/                                  [N]  LGPD (não depende de decisão de conteúdo)
└── /404/                                          [M]  noindex
```

**Princípios do desenho:**

1. **A URL acompanha o serviço e os hubs agregam.** O simulador fica em `/empreendimentos/simulador/` (é onde ele faz sentido para o cliente) e o hub `/inteligencia/` só linka para ele, sem mudar o endereço. Assim nenhuma URL depende de a Inteligência existir.
2. **Uma consulta tem uma página dona.** Cada palavra-chave abaixo tem exatamente uma página dona. As outras páginas tratam o assunto de passagem e linkam para a dona.
3. **As páginas de serviço seguem o template do Caderno §12:** resultado, situação, riscos, como atuamos, entregáveis, interfaces, case (quando houver), FAQ e CTA específico. As páginas novas nascem nesse formato.
4. **Não há páginas por cidade.** MG e SP aparecem em Sobre, Contato e na FAQ "Vocês atendem fora de Minas?". Páginas como "estudo de viabilidade em BH" e "… em SP" agora seriam conteúdo raso duplicado, e o Caderno §01 manda não depender de "BH" no título. Isso pode ser reavaliado com dados do Search Console.
5. **Mudança de URL sem custo agora:** só `/terreno/` → `/permuta-de-terreno/` e `/repertorio/` → `/metodo/modelagens/`. Por segurança, deixar 301 das URLs antigas. A página 404 já fala em "páginas reorganizadas".

### 2.1 Ficha de cada página

Prioridade de palavra-chave (matriz do agente, **estimativa qualitativa, sem volume medido**): **Q1** fácil + volume alto · **Q2** fácil + volume baixo (ganho rápido) · **Q3** difícil + volume alto (longo prazo) · **Q4** ignorar. Site novo, sem autoridade de domínio: os primeiros 6 meses vivem de Q2 e de cauda longa.

| URL | Status | Intenção principal | Palavra-chave alvo (linguagem do cliente) | Secundárias | Papel na conversão | Prior. |
|---|---|---|---|---|---|---|
| `/` | M | marca / navegação | DALETH estruturação de negócios imobiliários | estruturação imobiliária construtoras | distribui para as situações e as vertentes; CTA "Conversar sobre uma oportunidade" | marca |
| `/empresas/` | M | comercial | gestão de construtora e incorporadora | planejamento financeiro construtora; reestruturação de construtora; governança construtora | pilar: dono que sente que a empresa chegou ao limite → diagnóstico | Q2 |
| `/empresas/preparacao-para-credito/` | N · D 4.3 | comercial | como preparar a construtora para o GERIC da Caixa | análise de risco Caixa construtora; rating GERIC; documentação para crédito construtora | **alta intenção**: quem busca está prestes a ir ao banco. Faz a ponte com `/capital/` | Q2 → Q1 |
| `/empreendimentos/` | M | comercial | planejamento de empreendimento imobiliário | estruturação de empreendimento; incorporação imobiliária do terreno à entrega | pilar: distribui para viabilidade, permuta, simulador e obra parada | Q3 |
| `/empreendimentos/estudo-de-viabilidade/` | **N · D 4.4** | **comercial (a de maior demanda do mercado)** | estudo de viabilidade de incorporação imobiliária | estudo de viabilidade de empreendimento; viabilidade econômica de terreno; análise de viabilidade imobiliária | **a principal porta de entrada orgânica** (o próprio site diz que "é por aqui que a maior parte dos trabalhos começa") → diagnóstico | **Q1** |
| `/empreendimentos/permuta-de-terreno/` | M→URL | comercial (lado do proprietário) | permuta de terreno com construtora | vender ou permutar terreno; vale a pena permutar terreno; incorporar o próprio terreno | proprietário com proposta na mesa → "Falar sobre o meu terreno" | Q2 |
| `/empreendimentos/simulador/` | M | ferramenta / informacional | exposição de caixa de incorporação | fluxo de caixa de empreendimento imobiliário; capital próprio na incorporação | **CTA transicional** (StoryBrand): captura quem ainda não quer conversar | Q2 |
| `/empreendimentos/obra-parada/` | M | comercial (lado técnico e financeiro, não jurídico) | retomada de obra parada | como retomar obra parada; comprar obra parada; obra parada incorporadora o que fazer | adquirentes, incorporadora ou investidor → conversa | Q2 |
| `/capital/` | M | comercial | crédito para incorporação imobiliária | financiamento para construtora; investidor para empreendimento imobiliário; captação para incorporação (com cuidado: nunca prometer) | pilar: "primeiro o negócio, depois o capital" → diagnóstico | Q3 |
| `/capital/financiamento-a-producao/` | N · D 4.3 | comercial (alta intenção) | financiamento à produção Caixa para construtora | Plano Empresário Caixa; Apoio à Produção Caixa; crédito SBPE para incorporadora | construtora que vai pedir crédito de obra → preparação | Q1 |
| `/metodo/` | M | navegacional / EEAT | método DALETH | mapear, modelar, estruturar, conduzir | prova de método nomeado → como começa | marca |
| `/metodo/modelagens/` | F | informacional / EEAT | modelagem de negócio imobiliário | alternativas de estrutura para empreendimento | repertório que mostra a profundidade técnica → Inteligência | Q4 (vale como prova, não como busca) |
| `/como-comeca/` | M | transacional / fundo de funil | diagnóstico de estruturação | como contratar estruturação imobiliária; quanto custa (sem preço: "definido por escrito antes de começar") | **página de decisão**: quem chega aqui está perto de preencher o formulário | marca |
| `/inteligencia/` | N · D 4.2 | hub | — | — | reúne artigos e ferramentas; cada artigo leva a uma página de serviço | — |
| `/inteligencia/spe-holding-ou-scp/` | N · D 4.2 | informacional | SPE ou SCP na incorporação | holding imobiliária construtora; SPE incorporação vantagens | topo de funil → `/empresas/` | Q3 (domínio dos advogados; diferenciar pelo ângulo de decisão) |
| `/inteligencia/patrimonio-de-afetacao/` | N · D 4.2 | informacional | patrimônio de afetação incorporação | RET incorporação 4%; patrimônio de afetação e SPE | → `/empreendimentos/` e `/obra-parada/` | Q3 |
| `/inteligencia/permuta-fisica-ou-financeira/` | N · D 4.2 | informacional (**lado da incorporadora**, para não canibalizar a página de permuta, que fala com o proprietário) | permuta física ou financeira | permuta financeira incorporação; permuta e tributação | → `/simulador/` e `/permuta-de-terreno/` | Q2 |
| `/inteligencia/faseamento-e-exposicao-de-caixa/` | N · D 4.2 | informacional | faseamento de empreendimento imobiliário | lançamento em fases; reduzir capital próprio na obra | → `/simulador/` e `/estudo-de-viabilidade/` | Q2 |
| `/sobre/` | M | navegacional / EEAT | Cristiano Valério Ribeiro | DALETH Belo Horizonte | confiança: quem conduz, verificável | marca |
| `/contato/` | M | transacional | — | — | formulário que qualifica etapa, ativo, cidade e momento (Caderno §12) | — |
| `/privacidade/` | N | — | — | — | confiança / LGPD | — |

**Sobre GERIC (regra):** a definição é do dono, porque é nomenclatura do financiador e precisa sair correta. Pela amostra de busca, a leitura de mercado é que o GERIC é a avaliação da Caixa sobre a capacidade financeira, técnica e de gestão da empresa. **Não publiquei definição.** A página só nasce quando o texto dele chegar. Até lá, `/empresas/` ganha um parágrafo sem a sigla: "preparação da empresa para a análise de risco do banco".

---

## 3. Menu principal e rodapé propostos

### 3.1 Menu principal

```
[DALETH]   Atuação ▾   Método   Inteligência*   Sobre        [Analisar meu caso]
                │
                ├─ Empresas                     ├─ Por situação
                │   Preparação para crédito*    │   Tenho um terreno → /permuta-de-terreno/
                ├─ Empreendimentos              │   Quero saber se o empreendimento fecha → /estudo-de-viabilidade/
                │   Estudo de viabilidade*      │   Preciso de crédito para a obra → /financiamento-a-producao/*
                │   Permuta de terreno          │   A obra parou → /obra-parada/
                │   Obras paradas               │   Simulador de exposição de caixa
                └─ Capital
                    Financiamento à produção*
```
`*` = só entra quando a página existir.

**Por quê:**
- Segue o menu do Caderno §12 (Início | Método | **Atuação** | Cases | **Inteligência** | Sobre | Analisar meu caso), **sem Cases** até haver caso publicável (D 4.1), e sem "Início", porque a marca já leva à home.
- O dropdown **Atuação** mantém a ordem Empresas · Empreendimentos · Capital (regra) e expõe as filhas. Os links do dropdown ficam no HTML, então o Google os vê em todas as páginas e cada filha recebe link do site inteiro.
- A coluna **Por situação** traduz para o menu o bloco "Em que momento você está?" do Caderno. É a linguagem do cliente, e ela coincide com as palavras-chave.
- **Repertório sai do menu** e vira `/metodo/modelagens/`, linkado pelo Método.
- **Inteligência:** se o dono decidir "só ferramentas" (opção 1 de D 4.2), o item se chama **Ferramentas** e leva ao hub com simulador + comparador. Se decidir "deixar para depois", o item não aparece e as ferramentas seguem na coluna Por situação.
- **Mobile:** o menu atual já separa vertentes e apoio. A proposta mantém o CTA fixo "Conversar" no topo.

**Alternativa mais conservadora [D]:** manter as três vertentes visíveis no menu (como hoje), sem dropdown, e trocar só "Repertório" por "Como começa". Isso rende menos link interno para as filhas, mas é a mudança mínima.

### 3.2 Rodapé

```
DALETH (marca + descrição + slogan)     ATUAÇÃO                     PARA DECIDIR                      DALETH
Estruturação de negócios imobiliários   Empresas                    Estudo de viabilidade*            Como começa um trabalho
para construtoras, incorporadoras,      Empreendimentos             Permuta de terreno                Método
investidores e proprietários.           Capital                     Simulador de exposição de caixa   Sobre
"Ao seu lado na construção da           Obras paradas               As nove modelagens                Contato
 sua história."                         Financiamento à produção*   Inteligência*                     Política de privacidade
                                                                                                      Belo Horizonte · atuação nacional
                                                                                                      (MG e SP)  [CNPJ: D 1.3]
```
- O texto âncora usa a palavra-chave de cada página ("Permuta de terreno" no lugar de "Vender, permutar ou incorporar"; "Estudo de viabilidade").
- "Política de privacidade" entra no rodapé assim que a página existir.
- Mantém o aviso "Os números das ferramentas são exemplos ilustrativos".

---

## 4. Plano de links internos

Regras:
- **(a)** Toda página filha linka a mãe no corpo, não só pela migalha.
- **(b)** Toda página-pilar linka todas as filhas.
- **(c)** Todo artigo de Inteligência linka uma página de serviço e uma ferramenta.
- **(d)** Pelo menos um link para cada página usa a palavra-chave dela como âncora. O resto pode variar ("veja o efeito no caixa").
- **(e)** Nenhuma página fica sem link no corpo.

| De | Para (âncora sugerida) | Status |
|---|---|---|
| `/` cards "Em que momento você está?" | `/empreendimentos/permuta-de-terreno/` ("tenho um terreno"), `/empreendimentos/estudo-de-viabilidade/` ("saber se o empreendimento fecha"), `/empresas/`, `/capital/`, `/empreendimentos/obra-parada/` | ajustar (viabilidade é nova) |
| `/` bloco "Dois passos" | `/como-comeca/` ("como começa um trabalho") | já existe; manter só resumo |
| `/` bloco Método | `/metodo/` | existe |
| `/` bloco Repertório | `/metodo/modelagens/` ("as nove modelagens") | trocar URL |
| `/empresas/` | `/empresas/preparacao-para-credito/` ("preparar a empresa para a análise de crédito"), `/capital/`, `/como-comeca/` | novo / adicionar |
| `/empresas/preparacao-para-credito/` | `/empresas/`, `/capital/financiamento-a-producao/` ("financiamento à produção"), `/como-comeca/` | novo |
| `/empreendimentos/` | **`/empreendimentos/estudo-de-viabilidade/` ("estudo de viabilidade")** no item "Viabilidade" e na FAQ, `/permuta-de-terreno/`, `/simulador/`, `/obra-parada/`, `/capital/` | ajustar |
| `/empreendimentos/estudo-de-viabilidade/` | `/empreendimentos/`, `/simulador/` ("simule a exposição de caixa"), `/permuta-de-terreno/` ("se o terreno entra por permuta"), `/capital/`, `/metodo/modelagens/`, `/como-comeca/` | novo |
| `/empreendimentos/permuta-de-terreno/` | `/empreendimentos/`, `/estudo-de-viabilidade/` (onde hoje diz "saem do estudo de viabilidade"), `/simulador/`, `/capital/` ("Preciso ter dinheiro para incorporar?"), `/inteligencia/permuta-fisica-ou-financeira/`* | ajustar |
| `/empreendimentos/simulador/` | `/empreendimentos/` (no corpo), `/estudo-de-viabilidade/` (FAQ "Esta simulação serve para o meu projeto?"), `/capital/financiamento-a-producao/`* ("crédito de obra"), `/permuta-de-terreno/` | ajustar |
| `/empreendimentos/obra-parada/` | `/empreendimentos/`, `/capital/`, `/sobre/`, `/inteligencia/patrimonio-de-afetacao/`* ("Descubra o regime") | ajustar |
| `/capital/` | `/capital/financiamento-a-producao/` (item "Crédito bancário" e FAQ "Vocês trabalham com financiamento à produção?"), `/empresas/preparacao-para-credito/`, `/simulador/`, `/como-comeca/` | ajustar |
| `/capital/financiamento-a-producao/` | `/capital/`, `/empresas/preparacao-para-credito/`, `/simulador/`, `/estudo-de-viabilidade/` | novo |
| `/metodo/` | as três vertentes (cada movimento cita onde se aplica), `/metodo/modelagens/`, `/como-comeca/` (no lugar de repetir os passos) | **ajustar: hoje não linka vertentes** |
| `/metodo/modelagens/` | cada modelagem para a página de serviço ou artigo correspondente: societária → `/inteligencia/spe-holding-ou-scp/`*; aquisição do terreno → `/permuta-de-terreno/`; funding → `/capital/`; financeira → `/simulador/`; estrutura do empreendimento → `/inteligencia/faseamento…`* | ajustar |
| `/como-comeca/` | cada card "Cada caso começa num ponto" para a página da situação (empresa → `/empresas/`, terreno → `/permuta-de-terreno/`, empreendimento → `/estudo-de-viabilidade/`, capital → `/capital/`, obra parada → `/obra-parada/`) e `/contato/` | **ajustar: hoje tem zero links** |
| `/sobre/` | `/metodo/` (princípios), as três vertentes ("onde as decisões se encontram"), `/contato/` | **ajustar: hoje tem zero links** |
| `/inteligencia/*` (cada artigo) | 1 página de serviço + 1 ferramenta + `/inteligencia/` + 1 artigo irmão | novo |
| todas | `/contato/` pelo fecho (já existe) | ok |

---

## 5. Title e meta description propostos

Todos os titles têm até 60 caracteres e todas as descriptions até 155 (medido). O sufixo " · DALETH" já está contado. As linhas marcadas "sem sufixo" precisam de uma marca no metadado para o `build.py` não repetir a marca. Nenhum texto promete crédito, captação ou retorno, e nenhum cita preço.

| URL | Title (car.) | Meta description (car.) |
|---|---|---|
| `/` | DALETH · Estruturação de negócios imobiliários (46) | Para construtoras e incorporadoras: empresa, empreendimento e capital estruturados numa mesma decisão, do terreno à implantação. BH, atuação nacional. (150) |
| `/empresas/` | Gestão, financeiro e societário de construtoras · DALETH (56) | Para construtoras que cresceram pela execução: planejamento, financeiro, societário, tributário e governança, com acompanhamento até a rotina funcionar. (152) |
| `/empresas/preparacao-para-credito/` [D] | Preparar a construtora para a análise de crédito · DALETH (57) | Balanços, gestão, capacidade técnica e documentação organizados antes de a empresa ir ao banco. Quem aprova é o financiador; a preparação é nossa. (146) |
| `/empreendimentos/` | Empreendimentos imobiliários, do terreno à entrega · DALETH (59) | Terreno, produto, viabilidade, cronogramas, incorporação e vendas planejados juntos. Comparamos caminhos antes de comprometer capital. (134) |
| `/empreendimentos/estudo-de-viabilidade/` [D] | Estudo de viabilidade de incorporação · DALETH (46) | Antes de comprar o terreno ou lançar: cenários de preço, ritmo de vendas, custo, exposição de caixa e estrutura comparados com número. (134) |
| `/empreendimentos/permuta-de-terreno/` | Permuta de terreno, venda ou incorporação? · DALETH (51) | Vender, permutar ou incorporar: três negócios com risco, prazo e capital diferentes. Compare lado a lado antes de responder a uma proposta. (139) |
| `/empreendimentos/simulador/` | Simulador de exposição de caixa da incorporação · DALETH (56) | Veja como permuta, vendas na planta e crédito de obra mudam o capital próprio que um empreendimento exige até a entrega. Números de exemplo. (140) |
| `/empreendimentos/obra-parada/` | Obra parada: como avaliar a retomada · DALETH (45) | Incorporadora, grupo de adquirentes ou investidor: medimos o estado real da obra, do contrato e do caixa e comparamos caminhos de retomada. (139) |
| `/capital/` | Crédito e capital para incorporação imobiliária · DALETH (56) | Antes de buscar recurso, verificamos se a operação está pronta para recebê-lo e qual fonte faz sentido: banco, investidor ou mercado de capitais. (145) |
| `/capital/financiamento-a-producao/` [D] | Financiamento à produção: como preparar a operação · DALETH (59) | Plano Empresário, Apoio à Produção e SBPE pedem empresa, projeto e cronograma prontos para análise. Preparamos a operação; quem aprova é o banco. (145) |
| `/metodo/` (sem sufixo) | Método DALETH: mapear, modelar, estruturar, conduzir (52) | Quatro movimentos, uma mesma lógica de decisão: entender a situação real, comparar caminhos, estruturar o escolhido e acompanhar até funcionar. (143) |
| `/metodo/modelagens/` | As nove modelagens de um negócio imobiliário · DALETH (53) | Societária, tributária, financeira, funding, terreno, técnica, produto e estrutura do empreendimento: o repertório para comparar caminhos. (138) |
| `/como-comeca/` | Diagnóstico de estruturação: como começa · DALETH (49) | Uma conversa de enquadramento, sem custo, e o diagnóstico de estruturação, com escopo, prazo e valor definidos por escrito antes de começar. (140) |
| `/inteligencia/` [D] | Inteligência: incorporação, permuta e capital · DALETH (54) | Artigos e ferramentas sobre as decisões de um negócio imobiliário: estrutura societária, permuta, faseamento, exposição de caixa e crédito. (139) |
| `/inteligencia/spe-holding-ou-scp/` [D] | SPE, holding ou SCP na incorporação? · DALETH (45) | Três formas de organizar um empreendimento, com efeitos diferentes em risco, tributo, sócios e crédito. Quando cada uma costuma fazer sentido. (142) |
| `/inteligencia/patrimonio-de-afetacao/` [D] | Patrimônio de afetação e RET: o que muda · DALETH (49) | O que o patrimônio de afetação protege, como se relaciona com SPE e RET e o que ele exige da incorporadora durante a obra. (122) |
| `/inteligencia/permuta-fisica-ou-financeira/` [D] | Permuta física ou financeira: efeito no caixa · DALETH (54) | Como cada tipo de permuta muda o capital próprio, o risco e o tributo da incorporadora, e o que comparar antes de propor ao proprietário. (137) |
| `/inteligencia/faseamento-e-exposicao-de-caixa/` [D] | Faseamento de empreendimento e exposição de caixa · DALETH (58) | Dividir o empreendimento em fases pode reduzir o capital próprio exigido, ou aumentar o custo. Como comparar antes de decidir. (126) |
| `/sobre/` (sem sufixo) | Sobre a DALETH e Cristiano Valério Ribeiro (42) | Estruturação de negócios imobiliários que nasce da vivência em incorporação e crédito imobiliário, dos dois lados da análise. BH, atuação nacional. (147) |
| `/contato/` | Analisar meu caso · DALETH (26) | Conte o momento da empresa ou do empreendimento. Respondemos com uma primeira leitura e, se fizer sentido, a proposta do diagnóstico. (133) |
| `/privacidade/` | Política de privacidade · DALETH (32) | Como a DALETH trata os dados enviados pelo formulário e pelos canais de contato, conforme a LGPD. (97) |

**H1:** os H1 atuais são bons para a pessoa ("Descubra se o empreendimento fecha…", "Primeiro o negócio. Depois o capital."). **Não precisam mudar.** O Caderno manda pôr a consequência antes da técnica, e o title cumpre o papel de busca. Nas páginas novas, a palavra-chave entra no H1 ou no rótulo acima dele. Exemplo, com o rótulo "Estudo de viabilidade": H1 "Saiba se o empreendimento fecha antes de comprometer o terreno".

**Schema:** acrescentar `Service` em `/estudo-de-viabilidade/`, `/permuta-de-terreno/` e `/financiamento-a-producao/`. Acrescentar `Article` com `author` (Person, com `sameAs` quando houver LinkedIn) em cada artigo de Inteligência. O FAQPage já é gerado automaticamente; basta não repetir a mesma pergunta em várias páginas.

---

## 6. Prioridade de implementação

### Agora: não depende de decisão nova, custo baixo, e é o momento sem custo de URL

| # | Ação | Por quê |
|---|---|---|
| 1 | **Titles e descriptions** da tabela 5 nas 12 páginas existentes, mais a marca "sem sufixo" no `build.py` | 9 descriptions passam do limite; os titles abrem com rótulo interno; corrige "DALETH · DALETH" |
| 2 | **URLs:** `/empreendimentos/terreno/` → `/empreendimentos/permuta-de-terreno/`; `/repertorio/` → `/metodo/modelagens/`, com 301 das antigas | em noindex, custo zero. Depois de indexar, custa sinal |
| 3 | **Links internos** da tabela 4 para as páginas que já existem, com foco em `/como-comeca/`, `/sobre/` e `/metodo/`, que hoje são becos sem saída | distribui autoridade e reduz a saída sem conversão |
| 4 | **Tirar a repetição** de conversa → diagnóstico da home e do Método (resumo + link para `/como-comeca/`) | acaba com a canibalização de três páginas |
| 5 | **Menu:** trocar "Repertório" por "Como começa" (mudança mínima) ou aplicar o dropdown Atuação (3.1) | Repertório é rótulo interno; Como começa é a página de decisão |
| 6 | **Página `/privacidade/`** e link no rodapé | LGPD + confiança; pré-requisito para ligar o formulário (D 1.1) |
| 7 | **Delimitar o assunto entre `/permuta-de-terreno/` e `/simulador/`** (o simulador fala de exposição; a permuta é variável e linka a página de permuta) | evita que duas páginas disputem "permuta" |

### Logo depois da decisão do dono: maior impacto comercial

| # | Ação | Depende de | Recomendação |
|---|---|---|---|
| 8 | **`/empreendimentos/estudo-de-viabilidade/`** | D 4.4 | **Criar. É a prioridade 1 de SEO.** É a consulta comercial de maior demanda (estimativa qualitativa); a SERP tem pouca página de serviço (software, cursos, TCCs), o conteúdo já existe espalhado e a própria página Empreendimentos diz que é por ali que os trabalhos começam. Cuidado: não prometer que "o estudo diz se vai dar certo" (a FAQ atual já trata isso bem) |
| 9 | **`/capital/financiamento-a-producao/`** | D 4.3 (termos) | Criar. Alta intenção, público exatamente o ICP. Os nomes das linhas (Plano Empresário, Apoio à Produção, SBPE) precisam ser conferidos pelo dono com as regras vigentes da Caixa |
| 10 | **`/empresas/preparacao-para-credito/`** | D 4.3 (**definição de GERIC escrita pelo dono**) | Criar quando o texto chegar. Há concorrente com página dedicada a GERIC, o que indica demanda comercial |
| 11 | **Domínio definitivo** antes de virar `noindex` → `index` | D 1.2 | Publicar já no domínio final; não indexar `iajudite.com.br` |
| 12 | **EEAT de Sobre:** foto, LinkedIn, `sameAs`, CNPJ | D 1.3 | Sem isso, artigos e páginas de crédito (próximas de YMYL) rendem pouco |

### Quando houver decisão e capacidade de produção

| # | Ação | Depende de | Recomendação |
|---|---|---|---|
| 13 | **Hub `/inteligencia/`** | D 4.2 | Se a decisão for "só ferramentas", criar o hub com simulador + comparador já, sem mover URLs. Se for "com artigos", começar pelos 2 temas Q2: **permuta física × financeira** (lado da incorporadora) e **faseamento e exposição de caixa**, que puxam para o simulador. SPE × holding × SCP e patrimônio de afetação são Q3 (dominados por advocacia) e entram depois, com ângulo de decisão e não jurídico. Ritmo realista: 1 a 2 artigos por mês, com autor identificado |
| 14 | **Cluster com página-pilar** (método do agente): pilar = `/empreendimentos/estudo-de-viabilidade/`; clusters = faseamento, permuta física × financeira, exposição de caixa, "maior VGV não é melhor produto", produto × capacidade de financiamento do comprador (temas do Caderno §12) | 8 + 13 | É o cluster com mais chance de gerar lead orgânico |
| 15 | **`/cases/`** e o item no menu | D 4.1 | Só com caso autorizado ou anonimizado (nível 4 da escada de sigilo). Nunca inventar |
| 16 | **Sair do noindex** e trocar `Disallow: /` por `Allow` + sitemap no Search Console | D 1.1, 1.2 | Depois de 1 a 7 e de pelo menos a página de viabilidade |
| 17 | **Validação com dados:** Keyword Planner para os volumes desta tabela; Search Console 60 a 90 dias após a indexação para checar canibalização real (duas URLs na mesma consulta) | 16 | Reordenar as prioridades Q1/Q2 com número |

### O que **não** fazer
- Páginas por cidade ("estudo de viabilidade BH / SP") agora.
- Página de glossário com GERIC/SBPE antes de o dono validar as definições.
- Usar "captação", "aprovação garantida" ou "retorno" como palavra-chave em title.
- Pôr Cases ou Inteligência no menu antes de terem conteúdo.

---

**Fontes das buscas (amostra qualitativa, 02/10/2026):** [Sienge, guia de estudo de viabilidade](https://sienge.com.br/guia-de-estudo-de-viabilidade/) · [Portas, glossário](https://portas.com.br/glossario-imobiliario/estudo-de-viabilidade/) · [CREA-SC, curso de viabilidade](https://portal.crea-sc.org.br/agenda_evento/curso-analise-de-viabilidade-de-empreendimentos-verticais/) · [Caixa, Plano Empresário](https://www.caixa.gov.br/empresa/construcao-civil/plano-empresario-caixa/Paginas/default.aspx) · [Sienge, casas financiadas pela Caixa](https://sienge.com.br/blog/como-construir-casas-financiadas-pela-caixa/) · [Planning, GERIC](https://planning.com.br/geric/) · [FGV Direito SP, permuta financeira](https://direitosp.fgv.br/sites/default/files/arquivos/permuta-financeira-em-negocios-imobiliarios.pdf) · [Sinduscon-PR, permuta](https://sindusconpr.com.br/ambiente-favoravel-ao-mercado-imobiliario-e-a-permuta-de-terreno-por-area-construida/) · [Jornal Contábil, planejamento tributário na incorporação](https://jornalcontabil.com.br/noticia/planejamento-tributario-na-incorporacao-imobiliaria/) · [Barbieri Advogados, patrimônio de afetação e SPE](https://www.barbieriadvogados.com/?p=1093) · [Migalhas, retomada pelos adquirentes](https://www.migalhas.com.br/coluna/migalhas-edilicias/319868/paralisacao-de-obras-pelo-incorporador-imobiliario-e-sua-retomada-pelos-adquirentes) · [Gazeta SP, obra parada](https://www.gazetasp.com.br/cotidiano/obra-da-you-inc-esta-parada-desde-2025-e-nova-promessa-de-retomada-em-outubro-deixa-compradores-em-alerta/)
