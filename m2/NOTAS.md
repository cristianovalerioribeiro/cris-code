# M2 · Fachada — notas para o Cristiano

## A receita em 5 linhas
1. Fio: as decisões que ninguém vê. O prédio aparece na rua; o que o sustenta (produto, orçamento, caixa, capital, cronograma, vendas) foi decidido antes e não aparece na fachada.
2. Tese decidida como espinha: "Cada escolha de um empreendimento muda todas as outras" (hero) → "Cada decisão muda a seguinte" (a cadeia de consequências, em seção própria).
3. Corpo de precisão da V2: o quadro das quatro estruturas (−88% de capital próprio no pior mês, mesmo resultado), premissas escritas, "lado a lado", número sempre com a premissa do exemplo.
4. Método com Modelar como o movimento que muda o resultado; os três diferenciais na redação nova; papéis claros ("Executar é seu ofício. Estruturar, o nosso."); capital como meio em /capital/.
5. Tom Sábio 75%: sereno, concreto, sem adjetivo vazio. Hero centrado, 3D atrás, com os seis rótulos da cadeia: Produto | Orçamento | Caixa | Capital | Cronograma | Vendas (herói e jornada).

## CTA único
**"Contar o que quero realizar"** — em `"cta"` no meta das 6 páginas (menu, barra do celular), em todos os botões primários e no `botao` dos fechos. Vem da bancada de convites do digest; escolhido porque parte da ambição (regra-mãe) e não soa como diagnóstico gratuito ("Analisar meu caso", publicado hoje, soava como laudo).

## Ordem da home (9 seções do meio)
Hero (com a prova curta na faixa de credenciais) → jornada 3D (três batidas) → **a cadeia** (escura, única seção escura) → a conta (quadro) → método + três diferenciais → em que momento você está → papéis claros (+ insight decidido) → ferramentas → quem conduz → inteligência → perguntas (2) → fecho. Fundidos: método com diferenciais; papel com papéis; "dois passos" saiu (o fecho e /como-comeca/ cobrem).

## H1 e lead por página

- **/** — H1: "O que sustenta um prédio *não aparece na fachada.*" · Lead: "Cada escolha de um empreendimento muda todas as outras. Colocamos as escolhas lado a lado, com número, antes de comprometer capital. E ficamos enquanto o escolhido vira obra." · Fecho: "A fachada vem depois. A conversa, agora."
- **/empresas/** — H1: "O que a empresa decide hoje aparece no caixa do próximo ciclo" · Lead: "Três obras em andamento, um quarto terreno na mesa e sócios que querem o rumo por escrito. A empresa chegou ao estágio em que decidir bem vale tanto quanto construir bem." · Fecho: "Conte para onde a empresa quer ir no próximo ciclo".
- **/empreendimentos/** — H1: "O mesmo terreno cabe em negócios diferentes. A conta mostra qual fecha melhor." · Lead: "A proposta do terreno está na mesa e a primeira conta fechou. Você sabe construir o que cabe ali. A pergunta seguinte é quanto caixa o projeto pede no mês 14, e de onde vem." · Fecho: "Traga o terreno, o projeto ou a dúvida entre dois caminhos".
- **/capital/** — H1: "Capital para fazer maior, na forma que o negócio pede" · Lead: "O projeto está desenhado, e é o maior que a empresa já fez. O recurso existe. A dúvida é como ele entra, em que mês e com que exigências." · Seção escura: "Primeiro o negócio. Depois o capital." · Fecho: "Conte o que o capital precisa tornar possível".
- **/como-comeca/** — H1: "Começa com uma conversa. Nenhum passo obriga o seguinte." · Lead: "Ninguém contrata uma estruturação no primeiro contato, e nós não vendemos uma. Primeiro, uma conversa sem custo. Depois, se fizer sentido, o diagnóstico, com escopo, prazo e valor por escrito." · Fecho: "Comece pela conversa de enquadramento" (única página, com /contato/, que usa a frase "Devolvemos uma primeira leitura…").
- **/sobre/** — H1: "Dar estrutura para que bons empreendimentos imobiliários realizem seu potencial" (o propósito decidido, ao pé da letra) · Lead: "Quem construiu uma empresa tem arquiteto, engenheiro, contador e advogado, e cada um responde bem pela sua parte. A pergunta que cruza todas, qual caminho faz o negócio fechar melhor, fica sem dono. É nessa cadeira que a DALETH senta." · Fecho: "Conte o que trouxe você até aqui".

## De onde veio cada escolha
| Peça | Origem |
|---|---|
| H1 da home, tese "Cada escolha…", cadeia produto → … → vendas, três diferenciais, papéis claros, método numa frase, "Primeiro o negócio. Depois o capital.", "capital é um insumo…", frase de categoria, propósito, frase-conceito do nome, prova (324 mi · 30 · 19, via TRAL3, "trabalhadas") | Decisões do dono / plataforma (digest) |
| CTA "Contar o que quero realizar"; "Executar é seu ofício. Estruturar, o nosso."; insight "Muitas construtoras crescem pela capacidade de executar…" | Bancada do digest (propostas do estudo) |
| "Tudo começa como uma possibilidade"; "Escolher com número, antes de comprometer capital"; "quem aprova é o financiador" (só em FAQ); FAQs de custo e de contador; roteamento "Em que momento você está?" | Site atual (trechos mais fortes da ANALISE-COPY) |
| Quadro como "A conta"; "pior mês"; "A mesma empresa, organizada de outra forma, dá outro caixa"; "quatro contas de caixa"; "A estrutura de capital muda o pior mês, não o resultado"; hero centrado | V2 Precisão |
| "decisões que ninguém vê" como fio; "ficamos enquanto o escolhido vira obra"; "obra, caixa e contrato"; "A conversa, agora" | V3 Parceria (sem "legado" nem "capítulos") |
| "Capital para fazer maior, na forma que o negócio pede"; lead de /empresas/ pela ambição; "Você sabe construir o que cabe ali" | V1 Ambição e reescritas da ANALISE-COPY |

## Conferência
`python3 build.py --local && python3 qa/qa.py`: nenhuma falha em /m2/. Tamanho em palavras (texto visível, sem SVG e meta), atual → M2: home 772 → 761 · empresas 465 → 456 · empreendimentos 375 → 369 · capital 347 → 335 · como-comeca 302 → 294 · sobre 271 → 265.

## 5 pontos para validar
1. **A prova sem "R$".** Escrevi "324 milhões em VGV" porque `qa/qa.py` ainda bloqueia o padrão "R$ 324" (regra anterior à liberação). Quando o QA for atualizado, trocar para "R$ 324 mi" na home e em /sobre/. A palavra "trabalhadas" segue A TESTAR; "19 construtoras e incorporadoras · Com obras financiadas nessas operações" é inferência da redação do deck: confirmar.
2. **O botão do menu em 1280px.** O rótulo "Contar o que quero realizar" transborda 9px no cabeçalho gerado pelo build (m1 e m3 também transbordam). Pus um `<style>` de uma linha no topo de cada página de M2 para o QA passar; o lugar certo é `assets/site.css` (regra para CTAs longos entre 1024 e 1340px). Decidir se o rótulo fica ou se o menu recebe uma versão curta.
3. **A cadeia como seção escura.** "Cada decisão muda a seguinte" usa o componente `.cadeia` (seis caixas com setas) e tomou o lugar do bloco "Depois da recomendação". A presença ficou em "Papéis claros" e no hero ("ficamos enquanto o escolhido vira obra"). Validar se Conduzir perdeu peso demais na home.
4. **H1 de /sobre/ é o propósito literal** e usa "potencial" (três vezes na página, contando a frase-conceito e a explicação do nome; zero no resto do site). A frase-conceito do nome entrou como destaque. Validar se o H1 soa como missão de parede ou como frase viva; alternativa: "A cadeira que faltava na mesa da construtora."
5. **Vocabulário de capital sem "garantia".** O digest lista "garantia" entre as palavras proibidas; troquei por "o que o protege" / "proteção" nos itens de investidor (/capital/ e /como-comeca/). Se "garantia" no sentido técnico (garantia da operação) for aceitável, vale voltar, porque é a palavra que o investidor usa. Também pendente, como nas outras variantes: "dos dois lados do crédito imobiliário" continua marcado [confirmar].
