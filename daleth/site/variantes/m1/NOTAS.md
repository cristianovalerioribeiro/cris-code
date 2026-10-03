# M1 · Trajetória — notas para o Cristiano

## A receita em 5 linhas
1. Espinha da V1 (Ambição): o cliente é o protagonista, a DALETH é quem dá estrutura ao próximo passo. "Executar levou você até aqui. Estruturar leva além." é a frase vencedora dos júris e carrega a V1 sem o dramático.
2. Corpo da V2 (Precisão): quadro de alternativas em três páginas, "premissas escritas" e "lado a lado" como vocabulário fixo; nenhum número além dos de `modelo.py` (quadro) e do digest (R$ 324 mi · 30 · 19).
3. Fecho da V3 (Parceria): "Uma coisa é dizer o que fazer. Outra é estar lá enquanto é feito." vira a dobradiça do método na home; Conduzir aparece em toda página, sem "até funcionar".
4. Ordem da home conforme o Caderno: hero → prova (faixa) → tese → jornada 3D → quadro → método numa frase + 4 movimentos → em que momento você está → três dimensões + capital como meio + papéis (fundidos) → ferramentas → quem conduz → inteligência → FAQ → fecho. Nove seções do meio.
5. Decisões do dono respeitadas: conversa gratuita nunca chamada de diagnóstico; preço caso a caso; marca na frente, fundador em "Quem conduz"; nome só em /sobre/; nada de anos, cases ou "advisor".

## CTA único
**"Conversar sobre uma oportunidade"** (recomendado pelos júris), em `"cta"` do meta das 6 páginas, nos botões primários e no `botao` de todos os fechos.
Layout da home: `home home-b`. Rótulos 3D: hero `Executar|Estruturar|Empresa|Empreendimento|Capital|Decisão`; jornada `Produto|Orçamento|Caixa|Capital|Cronograma|Vendas` (a cadeia de consequências decidida).

## H1 e lead por página (e de onde veio)
- **/** — H1: "Executar levou você até aqui. *Estruturar leva além.*" (júri, R). Lead: "A DALETH integra empresa, empreendimento e capital para modelar, estruturar e conduzir negócios imobiliários, da oportunidade à implantação." (subtítulo R, inteiro). Tese: "Realizar mais exige estruturar melhor." (R) + insight decidido. Batidas: V1/site atual, com "O mesmo terreno gera negócios diferentes." (deck). Fecho: "Estrutura à altura da sua ambição" (bancada de assinaturas).
- **/empresas/** — H1: "A execução fez a empresa crescer. A estrutura faz o próximo ciclo caber." (nova, trajetória; "caber" vem da V1). Lead: cena da V1 reescrita para reconhecer a competência antes da tensão ("A empresa entrega bem, e por isso banco, investidor e sócios perguntam mais."). Corpo: V1/atual. Fecho: "Conte o ciclo que a empresa quer realizar agora" (V1).
- **/empreendimentos/** — H1: "O mesmo terreno gera negócios diferentes. Compare antes de escolher." (deck, modelagem). Lead: V1 ("Você já sabe o que cabe ali." é o reconhecimento). Lead do quadro traz vender/permutar/incorporar do deck. Fecho: "Traga o terreno, o projeto ou a oportunidade ainda sem forma" (V1, com "oportunidade" no lugar de "ambição").
- **/capital/** — H1: "Primeiro o negócio. Depois o capital." (decidido). Lead: V1. Seção escura: "Quem aprova é o financiador. Quem decide investir é o investidor." (site atual) + "Capital não é o fim da atuação. É um meio…" e o destaque do insumo (decididos). Fecho: V1.
- **/como-comeca/** — H1: "O próximo passo começa com uma conversa. Os seguintes são decisões suas." (nova, a partir do atual e da V3). Lead: atual/V1 com "conversa de enquadramento" nomeada. Fecho: o reservado (frase da primeira leitura).
- **/sobre/** — H1: "Existimos para o passo que a sua empresa ainda não deu" (V1). Lead: V1 (a cadeira sem dono). H2 "Por que existimos" = propósito decidido; lead = frase de categoria aprovada; cartões = os três diferenciais recomendados; "A prova" completa (R$ 324 mi via TRAL3, 30 operações, 19 construtoras); "O nome" traz a frase-conceito (f05) literal. Fecho: V1.

## Para o Cristiano validar
1. **A palavra da prova.** Usei "trabalhadas"/"trabalhado" (home e Sobre), como pede o digest. "Aprovados" ou "estruturados" mudam a leitura do número; a redação atribui ao fundador "via TRAL3" nos dois lugares.
2. **R$ 324 mi na faixa do hero.** Com o lead recomendado, a faixa fica: R$ 324 mi · 30 operações · 19 construtoras · formação. Belo Horizonte saiu da faixa e ficou só na FAQ ("Atendem fora de Minas?"). Confirmar se a cidade precisa voltar ao hero.
3. **Fusão "Três dimensões + capital como meio + papéis" numa seção só.** Economiza uma tela, mas "Primeiro o negócio. Depois o capital." aparece como destaque dentro de "Empresa, empreendimento e capital se decidem juntos." Se preferir cada frase com a sua tela, a home passa a 10 seções e estoura o limite.
4. **H1 de /empresas/ e de /como-comeca/ são novos** (não estavam na bancada). Alternativas prontas: "O próximo ciclo pode ser o maior, sem perder a velocidade" (V1) e "Começa com uma conversa. Nenhum passo obriga o seguinte." (atual).
5. **"Não é crédito, não é curso, não é BPO, não assumimos a execução. É estruturação."** entrou como lead em /sobre/, pela primeira vez no site. É a frase de categoria aprovada, mas em público soa como lista de negações; validar se fica em Sobre ou volta para uso interno.

## Conferência
`python3 build.py --local && python3 qa/qa.py`: links e console limpos nas 6 páginas. Dois apontamentos que não estão nas páginas e não pude corrigir (qa/, assets/ e build.py são de outra pessoa):
- `qa/qa.py` ainda proíbe `r$ 324` (regra do briefing de 30/09, anterior à liberação da prova). Aponta a home e /sobre/ desta variante. Pede atualização da lista `PROIBIDO`.
- Transbordo de 68 px a 1280 px no cabeçalho (`.menu-cta` com `white-space:nowrap`): acontece em M1, M2 e M3 com qualquer CTA maior que "Analisar meu caso". Resolve-se no CSS do menu (ou com rótulo curto só no cabeçalho), não no texto da página.
Tamanho (bytes do arquivo-fonte, já com a linha `"cta"`): igual ou menor que `paginas/` nas 6 páginas.
