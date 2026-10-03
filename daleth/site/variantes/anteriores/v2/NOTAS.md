# V2 · Precisão — notas para o Cristiano

## Conceito (5 linhas)
Autoridade técnica serena: a DALETH é quem coloca número e premissa escrita onde havia intuição.
Tom de engenheiro-economista que fala como gente: frases curtas, verbos concretos, nenhum adjetivo vazio.
A prova é o raciocínio, não a promessa: o quadro de alternativas (−88% de capital próprio no pior mês, mesmo resultado no fim), o simulador e o comparador.
Storytelling pela consequência: cada decisão muda o caixa, mostrado em cenas de planilha e mesa de reunião, nunca em caso inventado.
Home com `classe_body: home home-b hero-centrado`; rótulos 3D do hero = as 6 variáveis do modelo (VGV | Terreno | Permuta | Vendas | Crédito | Caixa).

## CTA único
**"Colocar meu caso em números"** — em todos os botões primários e fechos das 6 páginas. (O menu gerado pelo build continua com o CTA padrão do site; muda só quando a variante for escolhida.)

## H1 e lead por página
- **/** — H1: "O mesmo empreendimento. Quatro estruturas. *Uma pede 88% menos capital.*" · Lead: "Permuta, vendas na planta e crédito de obra, combinados, levam o pior mês do caixa de R$ 16,4 mi para R$ 1,98 mi. Mesmo resultado no fim. Fazemos essa conta para o seu caso, com premissas escritas, antes de comprometer capital." · Fecho: "Comece pela conversa. Os números vêm no diagnóstico."
- **/empresas/** — H1: "Três obras, um caixa. Cada uma com a sua conta." · Lead: "Três planilhas abertas, uma por obra, e uma quarta que tenta somar as três. O banco pede o fluxo num formato, o investidor em outro. A pergunta que fica é qual das três está dando resultado." · Fecho: "Conte quantas obras rodam hoje e o que vem no próximo ciclo"
- **/empreendimentos/** — H1: "Descubra em que mês o caixa aperta, e qual estrutura aperta menos" · Lead: "O terreno está na mesa e a conta rápida fecha. O que ela não responde é quanto dinheiro falta no pior mês da obra, e de onde ele vem." · Fecho: "Traga o terreno, o projeto ou a dúvida entre dois caminhos"
- **/capital/** — H1: "Quanto falta, em que mês e em que forma. Só depois, de quem." · Lead: "O projeto está desenhado e o banco já foi procurado. A análise voltou com uma lista de perguntas. O recurso existe. A operação ainda não está na forma em que ele é analisado." · Fecho: "Conte o que o capital precisa tornar possível"
- **/como-comeca/** — H1: "Primeiro a conversa. Depois, escopo, prazo e valor por escrito. Só então o trabalho." · Lead: "Ninguém contrata uma estruturação no primeiro contato, e nós não vendemos uma. Primeiro, uma conversa sem custo. Depois, se fizer sentido, a proposta do diagnóstico, por escrito." · Fecho: "Comece pela conversa de enquadramento" (única página, com /contato/, que usa a frase da "primeira leitura").
- **/sobre/** — H1: "Número antes de opinião. Premissa antes de decisão." · Lead: "Olhamos para uma empresa ou um empreendimento pelo que ainda pode ser realizado, e colocamos isso em números antes de recomendar. Depois ficamos ao lado de quem decide até virar rotina." · Fecho: "Conte o que trouxe você até aqui"

## O que mudou na estrutura da home (dentro do permitido)
8 seções do meio (antes 9): saiu o bloco "Dois passos" (o fecho e /como-comeca/ já cobrem). Ordem: jornada 3D → quadro (A conta) → por onde começar → ferramentas → presença (escura, com o método) → quem conduz → inteligência → perguntas. Rótulos do canvas da jornada: Produto | Orçamento | Caixa | Capital | Prazo | Sociedade.

## 5 decisões de copy para validar
1. **O número no H1.** "88%" e "R$ 16,4 mi → R$ 1,98 mi" estão escritos à mão no H1, no lead e no og_titulo, copiados de modelo.py. Se as premissas do modelo mudarem, o quadro se atualiza sozinho e o H1 não. Vale decidir se o H1 aceita essa dependência (ou se o build passa a injetar o número).
2. **O CTA "Colocar meu caso em números".** Promete número, e a conversa de enquadramento não entrega número: o diagnóstico entrega. O fecho da home ("Comece pela conversa. Os números vêm no diagnóstico.") e a microcopy tentam fechar essa distância. Alternativa mais prudente: "Conversar sobre o meu caso".
3. **"Pior mês" como palavra-chave da variante.** Aparece em todas as páginas no lugar de "exposição máxima de caixa". É mais concreto, mas é jargão da casa, não do mercado. Confirmar se o termo pode virar vocabulário oficial (o simulador ainda fala em "exposição").
4. **A cena de abertura de /empresas/** ("Três planilhas abertas… qual das três está dando resultado"). É a cena mais perto da fragilidade. Está na voz da pergunta do dono, não do diagnóstico, mas é o ponto onde a regra-mãe (partir da ambição) fica mais tensa.
5. **Em /sobre/:** "Conhece as perguntas da análise porque já esteve do lado que as faz" é inferência a partir do fato autorizado ("atuou nos dois lados do crédito"). E em /capital/, a frase "O capital é um insumo, como o terreno e o prazo" vem do caderno (§07, capital como meio); confirmar se pode aparecer como destaque público.

## Conferência
`python3 build.py --local && python3 qa/qa.py`: 43 páginas, "tudo certo". Tamanho (palavras, arquivo inteiro) igual ou menor que o atual nas 6 páginas.
