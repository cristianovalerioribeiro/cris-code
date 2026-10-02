# Briefing consolidado do redesenho · DALETH · outubro de 2026

Formato do agente 44 (briefing de design). Junta as revisões dos agentes 47 (UI/UX) e 45
(Brand), que estão nesta pasta, e registra como cada divergência foi resolvida.

## 1. Contexto
O Cristiano viu a prévia v01 e disse que o layout não estava bom. As duas revisões chegaram ao
mesmo diagnóstico: o texto fala como Sábio, mas o visual parecia template de consultoria ou SaaS.
- 13 faixas iguais na home.
- Cerca de 20 cartões.
- Tudo em sans, enquanto o wordmark é serifado.
- Dourado em mais de 25 lugares.
- MODELAR e ferramentas sem protagonismo.

## 2. Objetivo
O site deve parecer o documento que a DALETH entrega: **a prancha de estruturação**.
- Papel claro e títulos em serifa editorial.
- Fios no lugar de caixas.
- Números grandes e diagramas a traço.
- Dourado só onde há decisão.

A ação principal continua a mesma: "Analisar meu caso".

## 3. Decisões
| Tema | Decisão | Origem |
|---|---|---|
| Tipografia | Source Serif 4 (títulos, numerais) + Inter (corpo). A Manrope sai. | 45 e 47 concordam |
| Slogan | **Continua no topo de todas as páginas** (decisão do Cristiano), em faixa clara fina, com serifa itálica e fio dourado de 1px. O 45 sugeria tirar do topo: recusado. | 47 + regra do dono |
| Fundo alternativo | Névoa fria `#F2F5F8`, com viés para o marinho. O 47 sugeria papel quente `#F6F3EE`: recusado, porque creme + serifa + dourado é o clichê de site gerado por IA e puxa para o luxo. | 45 |
| Marinho | Abre e fecha: hero e fecho, mais no máximo um capítulo por página. Nunca dois marinhos seguidos. O rodapé passa a ser claro. | 45 e 47 |
| Dourado | No máximo um por tela. Só em forma (barra escolhida, nó do MODELAR, triângulo de decisão, tracejado do hero) e no botão do fecho. Texto dourado só em rótulo: `#7A5A28` no claro e `#D4B37C` no escuro. | 45 |
| Cartões | Saem. Listas viram linhas com fio de 1px. Moldura só no simulador, no formulário e na tabela do terreno. Raio de 2px. | 45 (o 47 queria manter nas 9 modelagens) |
| Rótulos | Inter 600, 12px, caixa-alta com 0.14em, em grafite. Sai o tracinho dourado. | 45 |
| CTA | Um botão por seção. A segunda ação vira link sublinhado. No celular, o botão "Conversar" fica visível ao lado do menu. | 47 |
| `.surge` | Não esconde mais conteúdo: tudo fica visível por padrão. | 45 e 47 |
| Hero | Desenho a traço: um empreendimento sobre o lote demarcado, poucos volumes de entorno em wireframe e volumetrias alternativas tracejadas em dourado. Sem gradiente cobrindo. No celular, vai abaixo dos botões. | 45 |
| Credenciais | Linha de 4 itens no pé do hero, separados por fio. | 45 |

## 4. Home (9 blocos)
| # | Bloco | Fundo |
|---|---|---|
| 1 | Hero + credenciais | marinho |
| 2 | Modelar: gráfico das 4 estruturas sem moldura, com cota "−88%", e as duas ferramentas em linhas-link | branco |
| 3 | Como começa: 01 → 02 em diagrama, sem caixas | névoa |
| 4 | Por onde entrar: Empresas · Empreendimentos · Capital em 3 colunas, com os momentos como links | branco |
| 5 | Tese: cadeia de consequências em diagrama horizontal com retorno | marinho |
| 6 | Método: stepper de 4 nós, com o MODELAR em dourado | branco |
| 7 | Repertório: 4 linhas em 2×2 | névoa |
| 8 | Quem conduz: ficha tipográfica, sem monograma nem pílulas | branco |
| 9 | Fecho com garantias em 3 colunas | marinho |

O "Do terreno à entrega" sai da home e vai para /empreendimentos/.

## 5. Páginas internas
- **Abertura:** clara, com migalhas no topo e H1 em serifa de 2 linhas no máximo.
- **"Nesta página":** índice gerado automaticamente a partir dos H2, à direita no desktop.
- **Corpo:** título em 4 colunas (sticky) e conteúdo em 7.
- **Ferramentas:** o simulador abre direto no resultado (indicadores e gráfico antes dos controles no celular).
- **Terreno no celular:** um bloco por critério.

## 6. Critério de aceitação
- Em 5 segundos se entende o território.
- Um único foco dourado por tela.
- Nenhuma seção depende de cartão.
- Contraste AA em todos os textos.
- QA automático verde em 6 larguras.
