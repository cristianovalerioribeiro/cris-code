# Pendências do site · decisões do Cristiano

Espelha o *Caderno de Definições do Site (02/10/2026, v01)*. Nada aqui foi decidido
por quem construiu: onde foi preciso escolher algo para o site existir, ficou o que
já estava no ar ou o que as Regras mandam, e está marcado abaixo.

## Travam a publicação

| Item | Como está no site novo | Onde muda |
|---|---|---|
| **1.1 Canal de contato** | Formulário pronto, mas **não envia**: avisa que é prévia. | `FORMULARIO_ATIVO` no `build.py` liga o Netlify Forms; falta definir e-mail, WhatsApp, telefone e LinkedIn. |
| **1.2 Sair da prévia** | `noindex` em todas as páginas, `robots.txt` bloqueando e aviso no rodapé. | `PREVIA = False` no `build.py` e apagar a linha `X-Robots-Tag` em `_headers`. |
| **1.3 Quem você é, de forma verificável** | "Quem conduz" com formação e trajetória, **sem foto, sem LinkedIn, sem CNPJ**. No lugar da foto, o símbolo da marca. Schema `Person` sem `sameAs`. | Foto e URL do LinkedIn entram em `paginas/00-inicio.html` e `paginas/70-sobre.html`; `sameAs` em `json_ld()` do `build.py`. |
| **1.4 A prova** | **Nenhum número de experiência**. Os R$ 324 mi não aparecem (atribuição com a TRAL3 pendente). | Faixa de credenciais logo abaixo do hero, em `paginas/00-inicio.html`. |

## Divergências entre documentos

| Item | O que foi usado | Observação |
|---|---|---|
| **2.1 Tipografia** | **Source Serif 4 (títulos) + Inter (corpo)**, desde a revisão de layout de 02/10. Os agentes 47 (UI/UX) e 45 (Brand) recomendaram trocar a Manrope por uma serifa editorial que converse com o wordmark sem imitá-lo; é a "terceira opção com serifa" que o Caderno de Definições já cogitava. | Confirmar. O Manual v2.0 ainda diz Cambria + Arial e precisa ser atualizado. Voltar atrás é trocar as variáveis `--serif`/`--sans` em `assets/site.css`. |
| **2.2 Nome do trabalho inicial** | "Diagnóstico de estruturação", como está no ar e como você pediu. | O Manual v2.0 ainda diz "Setup de Estruturação" e precisa ser corrigido. |
| **2.3 Ordem das vertentes** | **Empresas · Empreendimentos · Capital** em todo o site (menu, home, rodapé), como nas Regras e no Manual p8. | A inconsistência do v12 (menu numa ordem, cards em outra) acabou. Se a ordem for outra, muda em `VERTENTES` no `build.py` e nos blocos da home. |

## Visual

| Item | Como está |
|---|---|
| **3.1 Intensidade do cenário** | Redesenhado na revisão de 02/10 como **desenho a traço**: lote demarcado com cotas, o volume escolhido montado com as hastes do símbolo D e duas volumetrias alternativas tracejadas em dourado (o MODELAR desenhado). Movimento máximo de 16px. No celular vai abaixo dos botões. |
| **3.2 Marinho no hero** | Mantido (o marinho "abre capítulos", Manual p37). Páginas internas claras. A faixa do slogan deixou de ser marinho: virou uma linha clara em serifa itálica, ainda no topo de todas as páginas. |
| **3.3 Movimento nas internas** | Só a home tem cenário. |

## Conteúdo que falta

| Item | Como está |
|---|---|
| **4.1 Cases** | Sem bloco de cases. |
| **4.2 Seção "Inteligência"** | Não criada. Simulador e comparador ganharam destaque **dentro de Empreendimentos**, na home (quadro de alternativas) e no rodapé ("Para decidir"). |
| **4.3 GERIC, plano empresário, apoio à produção, SBPE** | Fora do site. Só "financiamento à produção na Caixa" numa FAQ de Capital, como no v12. |
| **4.4 Página de estudo de viabilidade** | Não criada. |
| **4.5 Frase de proteção regulatória** | **Não publicada** (aguarda revisão jurídica). |
| **4.6 Nomes fixos dos entregáveis** | Não usados: os entregáveis estão descritos, sem nome próprio. |

## Textos em teste

| Onde | No ar | Alternativa do Caderno |
|---|---|---|
| H1 da home | Para realizar mais, é preciso estruturar melhor. | Entre uma oportunidade e sua realização existe muito a estruturar. |
| CTA do hero | Conversar sobre uma oportunidade | Analisar meu caso (é o CTA do cabeçalho) |
| "Advisor estratégico" | Não usado | Uso público ainda em aberto |

## Outros pontos que surgiram na reconstrução

- **Endereços novos**: `/setup/` virou `/como-comeca/` (o nome "setup" foi abandonado) e
  terreno, simulador e obra parada passaram para dentro de `/empreendimentos/`. Os
  antigos redirecionam (`_redirects`).
- **"Crédito imobiliário dos dois lados"** aparece na faixa de credenciais e em /sobre/,
  como no site atual. No Caderno §09 esse item ainda está como "[confirmar]".
- **Imagem de compartilhamento (`og.png`)** é a do v12. Vale refazer quando o H1 fechar.

## Revisão de layout de 02/10/2026

Feita com os agentes 47 (UI/UX) e 45 (Brand) da gaveta de design. Relatórios completos e o briefing consolidado em `docs/revisao-layout/`. O que mudou de forma visível:
- **Home:** caiu de 13 para 9 blocos. "Do terreno à entrega" foi para /empreendimentos/.
- **Sem cartões:** as listas viraram linhas com fio, e o dourado aparece só onde há decisão.
- **Rodapé claro.** O marinho fica para o hero, o fecho e no máximo um capítulo por página.
- **Simulador no celular:** mostra o resultado antes dos controles. Gráfico com eixo em R$ mi e texto legível.
- **Terreno no celular:** um bloco por critério.
- **Páginas internas:** índice "Nesta página" no desktop.

## Reestruturação de 02/10/2026 (agentes 14 Página, 09 Copy e 34 SEO)

Relatórios em `docs/revisao-estrutura/`. Aplicado sem depender de decisão nova:
- **Menu:** Empresas · Empreendimentos · Capital | Simulador · Método · Sobre. O Simulador volta ao topo (decisão de 28/09), e o Repertório virou `/metodo/modelagens/`.
- **Home** em 9 blocos:
  1. Hero
  2. Diferencial
  3. Roteamento por situação, com destino próprio e o investidor
  4. Como começa, com a sequência e as garantias
  5. Por que conversar cedo, com o método
  6. Presença
  7. Quem conduz
  8. Perguntas frequentes
  9. Fecho
- **Páginas de serviço** no modelo do Caderno §12: situação → ganhos → alternativas → como atuamos → entregas → interfaces → perguntas frequentes.
- **Endereço novo** `/empreendimentos/permuta-de-terreno/`, com 301 do antigo.
- **SEO:** novos titles e descriptions.
- **Formulário:** recebe momento, origem e o cenário do simulador.
- **Celular:** barra de contato fixa.
- **Repetições:** a frase de fecho repetida e as FAQs duplicadas saíram.

Decisões que a reestruturação expôs e seguem com o Cristiano:
- **H1 da home:** "Para realizar mais, é preciso estruturar melhor." é quase literal de uma frase recusada no V4 de 30/09. Propostas do agente 09: "Seu próximo empreendimento pode ser o maior até aqui." e "Todo grande empreendimento se apoia em decisões que ninguém vê."
- **Rótulo do CTA:** unificado em "Analisar meu caso" em todo o site; era "A TESTAR" contra "Conversar sobre uma oportunidade".
- **Prazo de resposta declarado** (ex.: "em até 1 dia útil"): não publicado, porque é proibido inventar.
- **Investidor como contratante** (`/capital/#investidor`): redação a revisar junto com a frase regulatória.
- **Páginas novas recomendadas pelo SEO:** estudo de viabilidade (prioridade 1), financiamento à produção, preparação para crédito (GERIC) e política de privacidade.

## Versão 04 de 02/10/2026: site revisado e mais completo

Feito para depois podar. Tudo está na prévia e pode sair.
- **Três modelos de home** com seletor fixo no canto da tela e comparação em `/modelos/`:
  - **B Cinematográfico** (`/`): fundo vivo em WebGL, aproximação na rolagem, vitrine de ferramentas.
  - **A Prancha** (`/modelos/a/`): a home anterior.
  - **C Narrativa** (`/modelos/c/`): cinco capítulos.

  Ao escolher, apague as outras duas páginas (`paginas/01-modelo-a.html`, `paginas/02-modelo-c.html`) e `paginas/03-modelos.html`, tire `"modelo"` do meta e a linha de `MODELOS` some sozinha.
- **Efeitos:**
  - **Fundo vivo** (`assets/js/fundo.js`): inspirado no Miravo, com código próprio sem three.js (~9 KB).
  - **Aproximação** (`.aproxima` no CSS e `site.js`): é o mesmo princípio do Grupo Escalar, uma variável CSS guiada pela rolagem.

  Os dois respeitam "movimento reduzido", pausam fora da tela e têm versão estática.
- **Menu:** submenus nas vertentes, "Ferramentas" (simulador, comparador, radar) e "Inteligência".
- **Páginas novas:**
  - estudo de viabilidade
  - financiamento à produção
  - preparação para crédito
  - Inteligência, com 4 artigos
  - Radar de estruturação
  - privacidade (rascunho para revisão jurídica, `noindex`)
- **Textos:** todas as páginas de serviço e institucionais foram encurtadas, com abertura em cena (storytelling), sem caso inventado.

O que precisa de decisão está no *Caderno de refinamento do site (v04)*, no Claude Docs.

## Versão 05 de 02/10/2026: 3D e responsividade

- **Motor 3D próprio** (`assets/js/cena3d.js`, sem biblioteca). As cenas são marcadas no HTML com `<canvas data-cena="heroi|jornada|rede">`; `data-tema="claro"` dá a versão clara e `data-rotulos` os rótulos.
  - **Hero da home B:** terreno de pontos, lote, quatro torres e rede de decisões com pulsos.
  - **Aproximação:** a mesma cena guiada pela rolagem, em três atos.
  - **Fecho:** a rede ao fundo, em todas as páginas.
  - **Modelo C:** a versão clara.
- **Imagens renderizadas da própria cena** (`assets/img/`):
  - pôster do hero, para antes do 3D carregar e para aparelhos sem WebGL;
  - `og.png` com o H1;
  - pranchas 3D de Empresas, Empreendimentos, Capital e Inteligência, que entram com `"imagem"` no meta da página.

  Para refazer, use os scripts em `docs/render/`.
- **Revisão de responsividade** (21 pontos de um agente revisor), entre eles:
  - lista do método;
  - botão do topo entre 1080 e 1200px;
  - gráfico do simulador e formulário de contato;
  - trilho, migalhas, menu do celular e rodapé;
  - índice "Nesta página" também no celular;
  - fecho em duas colunas, com o que acontece depois.

## Versão 06 de 02/10/2026: modelo B escolhido e site no ar

- **Modelo B (cinematográfico) é o site.** A, C, `/modelos/` e o seletor saíram; `/modelos/` redireciona para a home.
- **No ar** em https://cristianovalerioribeiro.github.io/cris-code/ (GitHub Pages, `./publicar.sh`).
  Segue com `noindex` até o domínio definitivo (Caderno 1.3); o aviso de prévia no rodapé saiu (`AVISO_PREVIA`).
- **Formulário:** sem canal definido, diz que o envio está em configuração. Basta preencher `CONTATO["email"]`
  e trocar `FORMULARIO = "email"` (funciona no GitHub Pages) ou usar `"netlify"` no Netlify.
- **Pranchas 3D** em 15 páginas e nos cards de artigo; endereços antigos (v12) viram páginas de redirecionamento.
