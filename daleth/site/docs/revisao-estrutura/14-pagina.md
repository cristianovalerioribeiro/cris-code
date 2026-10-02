# DALETH · Estrutura do site · parecer do agente 14 (página que converte)

02/10/2026 · base: as 14 páginas em `daleth/site/paginas/`, README, PENDENCIAS, Caderno Estratégico v02 (§01, §07, §08, §09, §12), Regras e achados das revisões, Caderno de Definições do Site, dossiês de concorrentes (D1, D2, `_dossies.json`) e frases do mercado.

**Como adaptei o método.** O meu esqueleto é de página de vendas: hero, problema, mecanismo, prova, oferta, garantia, FAQ que vende, CTAs posicionados. Para a DALETH, cada peça vira o seu equivalente B2B. O **mecanismo único** é o MODELAR. A **prova** são as ferramentas, o repertório e a trajetória. A **oferta** é a conversa de enquadramento. A **garantia** são as três garantias (sem compromisso, escopo escrito, confidencialidade). A **FAQ** responde às objeções de quem compra. Saem: escassez, urgência, preço, value stack, depoimento, cenário A×B emocional e promessa de resultado. O que fica é o que decide uma venda complexa: o visitante se reconhece, entende a diferença, vê como começa e tem um próximo passo de baixo risco.

---

## 1. Diagnóstico estrutural franco

O Cristiano tem razão. O visual melhorou, e os textos são bons e quase todos aprovados. O que está mal é a **arquitetura**: as páginas não têm papéis distintos, a mesma ideia é explicada em quatro lugares, e o caminho até o contato depende de o visitante decidir sozinho para onde ir. Abaixo, os problemas em ordem de gravidade.

### 1.1 Problemas de arquitetura (o site inteiro)

**A. Cinco páginas disputam o mesmo papel: "explicar como pensamos".** Home (Tese, Método, Repertório), `/metodo/`, `/repertorio/`, `/como-comeca/` e `/sobre/` (princípios) explicam variações da mesma coisa:
- **O método em quatro movimentos** aparece completo na home (seção "O método") e em `/metodo/`. Em `/metodo/` ainda tem a seção "Do primeiro contato à implantação", com os 4 passos comerciais.
- **Os passos comerciais** (conversa → diagnóstico → estruturação → condução) aparecem em três lugares: na home ("Dois passos, nesta ordem"), em `/como-comeca/` e em `/metodo/` ("Do primeiro contato à implantação").
- **A frase "vender, permutar, incorporar, fasear, associar ou financiar"** aparece na home (bloco MODELAR) e em `/metodo/` (02 · Modelar). O repertório repete o mesmo raciocínio na home ("Repertório", 4 cartões) e em `/repertorio/`.
- **"Quem conduz"** está quase igual na home e em `/sobre/`.
- **"Conduzimos, verificamos, cobramos o combinado e corrigimos a rota"** aparece 6 vezes: home, Empresas (duas), Empreendimentos e `/metodo/` (duas).

Efeito: quem navega três páginas lê o mesmo argumento três vezes, e nenhuma página tem um trabalho que só ela faz.

**B. As três vertentes não são paralelas, e as fronteiras entre elas vazam.**
- **Empreendimentos** tem três filhas (terreno, simulador, obra parada). Empresas e Capital não têm nenhuma. Isso é aceitável, mas a página-mãe precisa rotear melhor (ver 1.3).
- **"Preparar para banco e investidor"** está em dois lugares. Em `/empresas/` é a frente "Preparação para análise externa" e a linha "Quero preparar a empresa para banco, investidor ou novo sócio" na home. Em `/capital/` são as seções "Apresentação da operação" e "O que uma análise costuma olhar primeiro". O visitante não sabe qual das duas abrir.
- **O trilho "Do terreno à entrega"** (`/empreendimentos/`) lista "Empresa" e "Capital" como **etapas** de Empreendimentos. Isso contradiz a ideia de três vertentes e não leva a elas.
- **O lead de `/empreendimentos/` diz "É por aqui que a maior parte dos trabalhos começa."** É uma alegação de frequência não verificável: o log de 28/09 já tinha derrubado "Começa quase sempre pelo empreendimento" por isso. Ela também contradiz a regra de que Empresas é a vertente prioritária (ICP).

**C. O menu gasta lugar nobre com material de referência e esconde a prova.**
- Menu atual: Empresas · Empreendimentos · Capital · Método · Repertório · Sobre · [Analisar meu caso].
- **Repertório** é um catálogo de referência, de baixa intenção, e ocupa um lugar no topo.
- **O simulador**, que é a prova mais forte (nenhum dos 63 concorrentes tem ferramenta de alternativas), só aparece no rodapé ("Para decidir") e no corpo da home. Em 28/09 o dono decidiu "simulador fica no topo" (log v10/v11), e a reconstrução tirou.
- **"Como começa"**, a página que explica a conversão, não está no menu.

**D. Não está escrito o que acontece depois do formulário.** O site descreve a entrada de três jeitos que não batem:
- home e quase todos os fechos: "Devolvemos uma **primeira leitura** e, se fizer sentido, a proposta do diagnóstico";
- fecho de `/como-comeca/`: "**Marque** a conversa de enquadramento";
- `/contato/recebido/`: "a resposta **já traz o desenho do diagnóstico**: escopo, prazo e valor". Esta versão pula a conversa de enquadramento.

O dono de construtora não sabe se vai receber um e-mail, uma ligação ou uma proposta. Em venda complexa isso derruba conversão, porque o risco percebido do primeiro contato é a principal objeção ("mais um vendedor que promete e some", Caderno §01, barreiras).

**E. Um CTA com dois nomes na mesma página.** Na home o hero e o fecho dizem "Conversar sobre uma oportunidade", e o cabeçalho e o bloco "Como começa" dizem "Analisar meu caso". Dois rótulos para a mesma ação, na mesma tela, criam escolha desnecessária (Hick). O teste A/B previsto no Caderno é entre páginas ou períodos, e não dentro da mesma página.

**F. Uma única conversão possível, e ela não funciona.** Hoje tudo termina no formulário, que não envia (pendência 1.1). Ninguém pode guardar o que fez no simulador, levar esses números para a conversa ou levar a lista de documentos da obra parada. Todo visitante que ainda não está pronto para falar sai sem deixar rastro.

### 1.2 Home, seção por seção

Ordem atual: Hero + credenciais → MODELAR + quadro → Como começa → Por onde entrar → A tese (escura) → O método → Repertório → Quem conduz → Fecho.

| Seção | O que funciona | O que está mal estruturado |
|---|---|---|
| **Hero** | Categoria visível, cliente nomeado, cenário próprio. | O CTA secundário "Conhecer o método" manda o visitante mais interessado para a página mais abstrata do site. O ideal é mandá-lo para o diferencial, logo abaixo (o quadro). Nada no hero diz que o primeiro passo não custa nada, e essa é a melhor redução de risco que a DALETH tem. |
| **MODELAR + quadro** | É o diferencial confirmado e está em 2º lugar, como deve. O quadro calculado é a melhor peça do site. | O texto à esquerda repete "vender, permutar, incorporar…", que depois volta em `/metodo/`. Os dois links "Teste você mesmo" estão bem colocados. |
| **Como começa** | Subiu para a 3ª posição, como pedido pela revisão. | Vem **antes** de "Por onde entrar": o site pede o passo antes de o visitante confirmar que o caso dele é atendido. A ordem lógica é "é o meu caso?" e depois "como começa". |
| **Por onde entrar** | Linhas por situação. Era a lição nº 1 dos dossiês (Requity). | **Roteamento falso**: duas linhas de Empresas apontam para o mesmo `/empresas/` (topo), e o mesmo acontece com as duas de Capital. Quem clica em "Quero preparar a empresa para banco" cai no H1 genérico de Empresas e precisa achar o assunto sozinho. **Falta o investidor como contratante**: "Já tenho investidor…" é a fala da incorporadora, não do investidor. O lead diz "E também para proprietários de terreno, investidores e grupos", mas nenhuma linha fala com o investidor. |
| **A tese** (escura) | Texto forte, cadeia de consequências. | Tese, Método e Repertório formam **três seções seguidas de "como pensamos"**, cerca de 40% da altura da home, sem nenhum CTA entre elas. A tese e o MODELAR dizem coisas vizinhas, e o leitor sente repetição. |
| **O método** | Os quatro movimentos, com Modelar em destaque. | É a 2ª vez que o raciocínio aparece na página (a 1ª foi o bloco MODELAR). |
| **Repertório** | — | É a 3ª explicação de "existem vários caminhos" na mesma página. Os 4 cartões são conteúdo de referência e não fazem o visitante andar. |
| **Quem conduz** | Formação e trajetória. | Sem foto nem LinkedIn (pendência 1.3) é pouco verificável. Está bem posicionada como "guia" (StoryBrand). |
| **Fecho** | Pergunta boa, garantias. | Não há **nenhuma resposta a objeção** na home: quanto custa, se capta recursos, se substitui o contador, se atende fora de MG, se é preciso estar com problema. As respostas existem, espalhadas em FAQs internas. |

### 1.3 Páginas de serviço

**`/empresas/`** (é a página do ICP)
- **Ordem invertida.** A sequência é Abertura → Ganhos → **catálogo de 8 frentes** → **Sinais** (autoidentificação) → Depois da recomendação + entregas → FAQ. O visitante vê o catálogo antes de se reconhecer, e os "Sinais" deveriam vir logo depois da abertura.
- **O diferencial não aparece.** A página do cliente prioritário não tem o MODELAR: nenhuma comparação de alternativas. O mais perto é um item de lista, "Desenho societário e tributário comparado".
- **Os entregáveis estão escondidos** dentro da seção escura "Depois da recomendação", misturados com Conduzir.
- **Faltam três objeções do mapa de empatia (Caderno §01):** "isso vai burocratizar a empresa ou tirar velocidade?", "os sócios precisam participar?" e "quanto custa e como começa?".
- **As interfaces** (contador e jurídico) só aparecem numa resposta de FAQ.

**`/empreendimentos/`**
- **"O que estruturamos" (8 itens) e "Planejamento integrado" (obra, caixa, vendas) são a mesma lista dita duas vezes.**
- **Os três pontos de partida** (terreno, simulador, obra parada) só aparecem na 4ª seção. Quem tem um terreno passa por duas listas antes de achar a porta dele, e o hero só oferece "Tenho um terreno".
- **Ferramenta misturada com situação.** O simulador é uma ferramenta, não "um caso que já tem nome", mas está no mesmo bloco que terreno e obra parada.
- **O quadro de alternativas** (o diferencial em forma visual) existe na home e **não** aparece na vertente onde ele mais pesa.
- **A frase de frequência** "É por aqui que a maior parte dos trabalhos começa" deve sair.

**`/capital/`**
- **Não há seção de situações.** Não diz quando a vertente entra: empreendimento novo pede mais capital do que a empresa quer imobilizar, financiamento à produção, investidor já definido, ou investidor do outro lado da mesa.
- **Não há modelagem visível**, apesar de o quadro da home ser, literalmente, uma comparação de estruturas de capital.
- **"Papéis claros" é a melhor resposta a objeção do site** (quem aprova é o financiador). Hoje está no meio da página e pode subir.
- O lead da abertura tem 4 frases e pode ser encurtado.

**`/empreendimentos/obra-parada/`**
- É a página mais bem estruturada do site: entrega valor antes de pedir ("Seis passos", "O que reunir"), separa quem contrata, diz por onde começa e responde objeções. Serve de modelo para as outras.
- Falta apenas uma seção explícita de interfaces (jurídico) e um bloco do que sai do diagnóstico, que hoje está diluído em "Medir antes de prometer".

**`/empreendimentos/terreno/`**
- **Não tem CTA na abertura** (sem `acoes`). É a página que mais vai receber tráfego de busca ("permuta de terreno vale a pena") e é a única de serviço sem botão no topo.
- **Falta dizer o que a DALETH entrega para um terreno**, além da lista "O que olhamos no seu caso".
- Cita "estudo de viabilidade", que não tem página (pendência 4.4).

**`/empreendimentos/simulador/`**
- Funciona como ferramenta.
- **Falta a ponte entre "o exemplo" e "o seu projeto"**: o que o diagnóstico faz que a ferramenta não faz (premissas reais, custo dos instrumentos, tributação, cronograma real). Isso só aparece numa FAQ.
- **Os números do visitante se perdem.** O "Levar estes números para a conversa" não existe.

**`/metodo/`**
- Duplica `/como-comeca/` com a seção "Do primeiro contato à implantação".

**`/repertorio/`**
- É boa como prova de repertório (Caderno §07: "as nove modelagens entram como prova do repertório").
- Não é página de menu e **não tem fecho de conversão próprio no corpo**, só o padrão.

**`/como-comeca/`**
- Conteúdo certo, mas fora do menu.
- **"O que varia" (6 cartões) repete as opções do select do contato** e não leva a lugar nenhum. Cada cartão poderia abrir o contato já com o momento escolhido.

**`/contato/`**
- O lado direito ("O que ajuda na primeira mensagem") é bom.
- Faltam o **que acontece depois** (a sequência), um **campo oculto de origem** (de qual página ou CTA veio, item do checklist de mensuração do Caderno §12) e o **momento pré-selecionado** quando o visitante vem de uma página específica.

**`/sobre/`**
- Correta no papel. O bloco "Quem conduz" é cópia do da home: na home ele deve ficar curto e mandar para cá.

### 1.4 Onde o leitor se perde, em uma linha cada

1. Na home, entre o quadro e o "Por onde entrar": a página pede o passo antes do roteamento.
2. Ao clicar numa linha de situação e cair no topo genérico da vertente.
3. Ao decidir entre Empresas e Capital para "preparar para banco".
4. Em Empreendimentos, procurando a própria situação abaixo de duas listas.
5. Ao terminar o simulador sem ter o que fazer com o resultado.
6. Ao enviar o formulário sem saber se vem uma ligação, um e-mail ou uma proposta.
7. Sendo investidor: não existe porta com o nome dele.

---

## 2. Benchmarks: o que copiar e o que não

**Limite desta leitura.** Os sites do **Grupo Escalar** (`grupoescalar.com`) e da **Miravo** estão **bloqueados pelo proxy de rede** deste ambiente, e a busca não encontrou a Miravo. A leitura abaixo usa:
- para o Escalar: a busca pública e o que já está registrado no Caderno (§12, cujo template de página e checklist vêm do "Relatório Benchmark Grupo Escalar"; §12B) e no Caderno de Definições (3.1);
- para os concorrentes: os dossiês verificados em 28/09 (D1, D2), que trazem a anatomia das homes seção por seção.

Para eu analisar Escalar e Miravo ao vivo, o Cristiano precisa mandar o endereço da Miravo e liberar os dois domínios na rede do ambiente, ou mandar capturas de página inteira.

### Grupo Escalar (BH · consultoria B2B de pré-vendas e outbound, 200+ empresas atendidas)
É um benchmark **de forma**, não de setor: uma consultoria B2B de venda complexa, da mesma cidade.
- **Copiar.**
  - O **template de página de solução** que o Caderno herdou: resultado → situação → riscos → como atuamos → entregáveis → interfaces → case → FAQ → CTA específico, com "consequência antes da técnica".
  - O **checklist antes de publicar** ("em 5 segundos eu entendo o território?", "o cliente se reconhece por situação?", "existe um próximo passo simples?").
  - O princípio do §12B: **o site não pode depender do Cristiano explicando**. O método vira material (entregáveis descritos, perguntas respondidas por escrito).
  - **Botão flutuante de contato no celular**, quando o canal existir.
  - O efeito de aproximação no hero, feito em CSS e sem biblioteca, que já foi adotado.
- **Não copiar.**
  - **"Cases" e "Inteligência" no menu sem conteúdo.** Isso é proibido pela regra de não inventar.
  - **A cadência agressiva de prova numérica** ("+200 empresas"), enquanto não houver número próprio liberado.

### Miravo
O que se sabe (Caderno de Definições 3.1) é visual: malha 3D em three.js e botão flutuante de WhatsApp. **Nada estrutural foi registrado.**
- **Copiar.** Só o botão flutuante, quando houver canal.
- **Não copiar.** Ornamento pesado (cerca de 600 KB) no lugar de argumento.

### Requity (advisory imobiliário, concorrente mais próximo em discurso)
- **Copiar.**
  - O bloco **"Por onde começar"** em **4 situações com CTA próprio** e **prazo de resposta declarado** ("em até 1 dia útil"). O prazo da DALETH precisa ser decidido pelo Cristiano: é proibido inventar.
  - **O método nomeado visível na navegação.**
  - **Fecho por tese** ("Decisões imobiliárias exigem experiência, método e independência").
- **Não copiar.**
  - 14 blocos, com o mesmo CTA repetido 6 vezes.
  - Silêncio sobre o que acontece depois da recomendação: aqui a DALETH já ganha com o Conduzir.

### Viestra (estruturação econômico-financeira, mesmo público)
- **Copiar.**
  - **Autodiagnóstico como item de menu de primeiro nível** (oferta de entrada que entrega algo antes de pedir). Para a DALETH, isso é o simulador agora e o "Radar de Estruturação" depois (Caderno §08, A TESTAR).
  - **A FAQ que enfrenta a objeção real**: "Já fazemos nossas próprias viabilidades. Por que contratar?". A DALETH precisa da sua: "Já tenho contador, advogado e engenheiro".
- **Não copiar.** A seção "O Problema" com dor frontal ("Decidir sem fundamento é aposta"), que fere a regra-mãe.

### Mid by Falconi (página do setor de construção)
- **Copiar.**
  - O esqueleto da página de setor: perfis "empresas que mais se beneficiam" antes do método.
  - **A FAQ que qualifica o porte com honestidade** ("empresas muito pequenas ainda não têm complexidade para capturar valor"). É o equivalente B2B do "para quem não é" e protege a agenda do Cristiano.
- **Não copiar.** A página-molde igual para todo setor, sem um diferencial próprio no centro.

### Moradda (GERIC)
- **Copiar.**
  - O tom de "O Ponto de Partida": **"Sua empresa pode estar pronta para construir"**, que reconhece a competência antes de mostrar a lacuna.
  - **Explicar o jargão que o cliente busca** (GERIC), o que serve para SEO. Depende da pendência 4.3.
- **Não copiar.** "Conduzir a habilitação" e o formulário logo no hero.

**Síntese do que vale para a DALETH:**
1. Roteamento por situação, com destino específico.
2. Uma oferta de entrada que entrega algo (ferramenta).
3. Uma FAQ que enfrenta a objeção real e qualifica o porte.
4. O próximo passo descrito com sequência.
5. Um diferencial no centro de cada página de serviço.

Nenhum dos 63 concorrentes tem o item 5 em forma de ferramenta. É aí que a estrutura tem de apostar.

---

## 3. Proposta de estrutura da HOME

**Princípio.** A home tem uma tarefa só: **fazer o visitante certo se reconhecer, ver a diferença e escolher uma porta**. Quem explica é cada vertente, e a home não repete a explicação. Ela cai de 9 para **8 blocos**, com três CTAs no corpo (hero, roteamento, como começa) mais o fecho.

**Cabeçalho (todas as páginas).**
- Logo · **Empresas · Empreendimentos · Capital** · **Simulador** · Método · Sobre · [**Analisar meu caso**].
- A faixa do slogan "Ao seu lado na construção da sua história." fica logo abaixo, como hoje.
- **Repertório sai do menu**: fica acessível pelo Método, pelo rodapé e pelos links contextuais.
- **Simulador volta ao topo**, como o dono decidiu em 28/09 (a URL continua dentro de Empreendimentos).
- **Como começa** fica no rodapé, em todos os fechos e como link ao lado do botão no menu móvel.
- **No celular:** depois que o hero sai da tela, aparece uma barra fina fixa com "Analisar meu caso". Ela some em `/contato/`.

### Bloco 1 · Hero
- **Pergunta que responde:** "O que é isto, e é para mim?"
- **Conteúdo:**
  - rótulo "Estruturação de negócios imobiliários";
  - H1 em teste, "Para realizar mais, é preciso estruturar melhor.";
  - lead atual (cita construtoras e incorporadoras).
- **CTA primário:** **"Analisar meu caso"**. O mesmo rótulo do cabeçalho resolve a duplicidade. Se o Cristiano preferir "Conversar sobre uma oportunidade", troca nos dois lugares, nunca um só.
- **Microcopy sob o botão (novo):** *"O primeiro passo é uma conversa de enquadramento, sem custo."* É a porta de entrada visível acima da dobra, sem precisar de uma seção.
- **CTA secundário:** **"Ver o mesmo empreendimento em quatro estruturas"**, âncora para o Bloco 2, no lugar de "Conhecer o método".
- **Faixa de credenciais:** fica como está. É a vaga reservada para os R$ 324 mi quando a atribuição com a TRAL3 fechar (pendência 1.4).
- **Sai:** nada além da troca do CTA secundário.

### Bloco 2 · O diferencial: "Antes de escolher um caminho, colocamos os caminhos lado a lado"
- **Pergunta que responde:** "O que vocês fazem que os outros não fazem?" É o mecanismo único.
- **Conteúdo:** fica como está, com rótulo, H2, lead e **o quadro calculado**. O parágrafo da esquerda é encurtado para uma frase só: *"Cada escolha muda risco, caixa, retorno, tributação, produto e prazo. Modelar é comparar essas consequências com número, antes de comprometer capital."*
- **CTA:** os dois links "Teste você mesmo" (simulador e comparador de terreno). É a chamada transicional do StoryBrand.
- **Sai:** a enumeração "vender, permutar, incorporar, fasear, associar ou financiar". Ela fica só em `/metodo/`.

### Bloco 3 · "Em que momento você está?" (roteamento)
- **Pergunta que responde:** "Vocês atendem o meu caso? Por onde eu entro?"
- **Posição:** sobe para 3º, **antes** de Como começa. A ordem fica: reconhecer, depois o passo.
- **Estrutura:** duas colunas com os estados de entrada do Caderno §01, "Quero realizar" (oportunidade) e "Quero destravar" (barreira). Em cada linha há uma etiqueta discreta com a vertente. **Cada linha leva a um destino próprio** (página ou âncora); chega de duas linhas para o mesmo topo.
- **Conteúdo (copy final, a partir das linhas aprovadas):**

| Estado | Linha | Vertente | Destino |
|---|---|---|---|
| Realizar | A empresa cresceu, e a estrutura de decisão precisa acompanhar | Empresas | `/empresas/` |
| Realizar | Quero preparar a empresa para banco, investidor ou novo sócio | Empresas | `/empresas/#analise-externa` |
| Realizar | Tenho um terreno e quero saber o que ele vale como empreendimento | Empreendimentos | `/empreendimentos/terreno/` |
| Realizar | Tenho um empreendimento e quero saber qual estrutura faz ele fechar melhor | Empreendimentos | `/empreendimentos/` |
| Realizar | Quero estruturar o capital da operação, próprio ou de terceiros | Capital | `/capital/` |
| Realizar | **Sou investidor e avalio entrar numa operação** (nova) | Capital | `/capital/#investidor` |
| Destravar | Já tenho investidor e preciso que o recurso entre bem estruturado | Capital | `/capital/#recurso-definido` |
| Destravar | Uma operação travou e preciso de um caminho técnico | Empreendimentos | `/empreendimentos/obra-parada/` |

- **CTA ao fim do bloco:** *"Não achou o seu caso? Conte em poucas linhas."* Leva para `/contato/` com o momento "Ainda estudando o assunto".
- **Sai:** os cabeçalhos de vertente com parágrafo descritivo e os três links "Ver Empresas / Ver Empreendimentos / Ver Capital". As definições das três vertentes vão para o topo de cada página de vertente.

### Bloco 4 · Como começa: "Dois passos, nesta ordem"
- **Pergunta que responde:** "O que acontece se eu entrar em contato? Quanto risco eu corro?"
- **Conteúdo:** os dois cartões atuais (Conversa de enquadramento · Diagnóstico de estruturação), mais **a sequência depois do formulário**, que hoje não existe (ver §5). Proposta de texto, pendente das duas lacunas que só o Cristiano decide:
  > *Você conta o momento pelo formulário. Respondemos [canal a definir, pendência 1.1] para marcar a conversa de enquadramento, online. Se houver aderência, a proposta do diagnóstico chega por escrito, com escopo, prazo e valor, antes de qualquer compromisso.*
- **Garantias:** as três, aqui, porque é aqui que pesam.
- **CTA:** "Analisar meu caso", mais o link "Como funciona cada passo" (`/como-comeca/`).
- **Sai:** nada; o bloco só muda de lugar.

### Bloco 5 · Método: "Nenhuma decisão de um empreendimento é tomada sozinha" (tese + método fundidos)
- **Pergunta que responde:** "Como vocês pensam? Por que isso funciona?"
- **Conteúdo:**
  - H2 e lead da **tese** atual;
  - a **cadeia de consequências** (produto → orçamento → caixa → capital → cronograma → sociedade);
  - **os quatro movimentos** em uma linha cada, com Modelar em destaque ("Onde a decisão se forma");
  - no movimento Modelar, um link inline: *"as nove modelagens"* → `/repertorio/`.
- **Visual:** a seção escura passa a ser esta, e há uma só seção escura na home além do hero e do fecho.
- **CTA:** "O método em detalhe" → `/metodo/`.
- **Sai:** **o bloco Repertório inteiro** (a terceira explicação de "há vários caminhos") e **a tese como seção separada**. Isso elimina uma seção e o efeito "três aulas seguidas".

### Bloco 6 · Quem conduz
- **Pergunta que responde:** "Quem está por trás? Posso confiar?"
- **Conteúdo:** **versão curta**, com nome, a linha de formação e uma frase ("Atuou nos dois lados do crédito imobiliário…"). Quando houver, entram **foto e LinkedIn**: é o que torna isso verificável (pendência 1.3).
- **CTA:** "Sobre a DALETH" → `/sobre/`.
- **Sai:** o segundo parágrafo, que fica só em `/sobre/`.

### Bloco 7 · Perguntas frequentes (novo, 5 perguntas)
- **Pergunta que responde:** "Quais as objeções que me impedem de clicar?" É a FAQ que vende, em versão B2B.
- **Conteúdo** (respostas montadas com frases já aprovadas no site):
  1. **Quanto custa?** Depende do escopo, que sai da conversa de enquadramento. O valor é definido antes de começar e fica escrito na proposta, junto com o prazo e o que será entregue.
  2. **Vocês captam recursos ou garantem crédito?** Não, e ninguém pode garantir. Preparamos a operação para chegar pronta: quem aprova é o financiador, e quem decide investir é o investidor.
  3. **Já tenho contador, advogado e arquiteto. Ainda faz sentido?** Faz, e o trabalho não substitui nenhum deles. Cada um responde muito bem pela própria parte; o que costuma faltar é alguém olhando as partes juntas.
  4. **Vocês executam o que foi estruturado?** A execução continua com a empresa e seus fornecedores. Nós conduzimos, verificamos, cobramos o combinado e corrigimos a rota. *Esta é a única ocorrência da frase na home.*
  5. **Atendem fora de Minas Gerais?** Sim. A base é Belo Horizonte e a atuação é nacional, à distância, com presença quando o caso pede.
- **CTA:** nenhum próprio. O fecho vem logo depois.

### Bloco 8 · Fecho
- **Pergunta que responde:** "Qual é o próximo passo?"
- **Conteúdo:** fica o atual ("Seu próximo empreendimento já está estruturado para avançar?"), com o texto ajustado para a sequência real: *"Conte o momento da empresa ou do empreendimento. A primeira conversa é de enquadramento, sem custo; se houver aderência, a proposta do diagnóstico vem por escrito, com escopo, prazo e valor."*
- **CTA:** "Analisar meu caso", mais o secundário "Testar o simulador". O secundário é para quem ainda não está pronto: a ferramenta é a conversão intermediária.
- **Garantias:** saem daqui, porque já estão no Bloco 4. Não repetir.

**Mapa final da home:** Hero (CTA) → Diferencial + quadro (ferramentas) → Em que momento (CTA) → Como começa (CTA + garantias) → Método → Quem conduz → FAQ → Fecho (CTA).
Quem decide rápido converte no Bloco 3 ou 4. Quem precisa de mais lê até o fim, e cada bloco responde uma pergunta diferente.

---

## 4. Templates

### 4.1 Página de SERVIÇO (Empresas · Empreendimentos · Capital, e as filhas de situação: terreno, obra parada, futura viabilidade)

Aplica o template do Caderno §12 (resultado · situação · riscos · como atuamos · entregáveis · interfaces · case · FAQ · CTA). O case é substituído por um bloco de prova possível até haver cases autorizados. A ordem foi ajustada para que **a situação venha antes do catálogo** e **o diferencial (MODELAR) tenha seção própria em toda vertente**.

| # | Seção | Pergunta do visitante | Regra | Tamanho |
|---|---|---|---|---|
| 0 | **Abertura (resultado)** | "Isto resolve o que eu quero?" | Rótulo "Vertente · para quem". H1 de **consequência**, antes da técnica (os H1 atuais de Empresas e Empreendimentos já seguem essa regra). Lead de 2 frases, no máximo, que nomeia o cliente. **CTA contextual** + link-âncora "Em que situação isso entra". Microcopy: "Primeiro passo: conversa de enquadramento, sem custo." | Uma dobra |
| 1 | **Quando faz sentido (situação)** | "É o meu caso?" | 4 a 6 situações escritas pela ambição (Caderno §01, "linguagem de abordagem"). Cada uma com `id`, para a home linkar direto. Uma frase de normalização: *"Nenhum deles é sinal de empresa mal administrada."* | Lista curta |
| 2 | **O que muda (ganhos)** | "O que eu ganho?" | 3 a 5 ganhos concretos, sem número e sem promessa de retorno. | Lista |
| 3 | **As alternativas que comparamos (MODELAR na vertente)** | "Por que com vocês e não com quem eu já tenho?" | **O diferencial em forma visual**: uma tabela de natureza (como em terreno) ou o quadro calculado (como na home). Fecha com a frase de riscos do template: *"Quanto mais cedo as decisões críticas são estruturadas, menor a necessidade de corrigir o projeto durante a execução."* Link para a ferramenta. | Tabela ou quadro |
| 4 | **Como atuamos** | "Como funciona na prática?" | Os 4 movimentos **aplicados a esta vertente**, com uma linha cada sobre "o que fazemos aqui". As frentes do catálogo (8 cartões em Empresas, 6 em Capital) viram uma **lista compacta** "Frentes que podem entrar no escopo". | 4 linhas + lista |
| 5 | **O que você recebe (entregáveis)** | "O que eu tenho na mão no fim?" | Separado em **Diagnóstico** (o que sai sempre) e **Estruturação e condução** (o que pode seguir). Descritos, sem nome próprio enquanto a pendência 4.6 não fechar. | 2 colunas |
| 6 | **Com quem trabalhamos (interfaces)** | "Vai atropelar meu contador, advogado, projetista?" | Contador, jurídico, projetistas, banco, investidor, sócios. **Aqui, e só aqui na página**, entra a frase "A execução continua com a empresa e seus fornecedores. Nós conduzimos, verificamos, cobramos o combinado e corrigimos a rota." | Curta |
| 7 | **Prova possível** | "Por que acreditar?" | Sem cases: (a) a ferramenta da vertente; (b) a credencial que pesa ali (por exemplo, "crédito imobiliário dos dois lados" em Capital, ainda marcada "[confirmar]" no Caderno §09); (c) **vaga reservada** para case autorizado, ou nível 4 da escada de sigilo, desde que **escrito pelo Cristiano a partir de experiência real**. Nunca preencher sem ele. | Pequena |
| 8 | **Perguntas frequentes (FAQ que vende)** | "E se…?" | 5 a 7 perguntas. Pelo menos uma de **objeção de compra** ("já tenho X"), uma de **limite** ("vocês executam / captam?"), uma de **qualificação de porte** (modelo Mid) e uma de **como começa / quanto custa**. | 5–7 |
| 9 | **Fecho específico** | "Qual o meu próximo passo?" | O título e o botão contextuais atuais são bons. O texto do fecho descreve a sequência real (ver Bloco 8 da home). As garantias aparecem **ou** aqui **ou** perto do CTA da abertura, nunca nos dois. | Fecho |
| 10 | **Para continuar** | "E o resto?" | Os links cruzados que já existem. | 1 linha |

**CTAs por página de serviço:** abertura · depois da seção 3 (link para a ferramenta, transicional) · fecho. São três, todos levando a `/contato/?momento=<vertente>&origem=<página>`.

**Aplicação nas três vertentes, com o que muda em cada uma:**

**Empresas** (`/empresas/`)
- **0.** Fica o H1 atual. CTA "Falar sobre a minha empresa".
- **1.** A seção "Sinais" **sobe** e vira "Quando faz sentido", com os 5 itens atuais. Acrescentar o item `id="analise-externa"`: *"Banco, investidor ou novo sócio passaram a fazer parte da rotina, e cada um pede a informação de um jeito."* O texto já existe nos Sinais.
- **2.** "Clareza para decidir o próximo ciclo" fica.
- **3. Nova.** "A mesma empresa, formas diferentes de se organizar". É uma tabela de natureza, sem números, nos moldes do comparador de terreno:
  - colunas: empreendimentos na própria empresa × SPE por empreendimento × holding com SPEs;
  - linhas: onde fica o risco de cada obra; como o resultado de cada empreendimento é apurado; o que o banco analisa; o que muda na entrada e saída de sócios; custo e rotina de manter.
  - **As células precisam ser escritas ou validadas pelo Cristiano** (conteúdo tributário e societário). Eu só proponho a estrutura.
  - CTA transicional: "Ver o efeito no caixa de cada estrutura" → simulador.
- **4.** Os 4 movimentos aplicados à empresa. Os 8 cartões viram lista compacta.
- **5.** As "Entregas típicas" **saem** da seção escura e viram a seção 5.
- **6.** Contador, jurídico e sócios. A frase de condução sai da seção escura e da FAQ ("Vocês assumem a rotina financeira?" pode ficar, mas sem repetir a frase inteira).
- **8. Acrescentar:**
  - *"Organizar a empresa vai tirar velocidade?"* Resposta (copy): "O objetivo é o contrário: tirar decisões da cabeça de uma pessoa sem perder o ritmo. A rotina é desenhada com quem decide hoje, no tamanho que a empresa precisa."
  - *"Para que porte de empresa isso faz sentido?"* Qualificação honesta pelo ICP: "quem já tem mais de um empreendimento, ou um pipeline real, e sente que a estrutura começa a limitar o próximo estágio".
  - *"Quanto custa e como começa?"*
- **Sai:** a seção escura "Depois da recomendação" como bloco à parte. O conteúdo se divide entre as seções 4, 5 e 6.

**Empreendimentos** (`/empreendimentos/`)
- **0.** Fica o H1 atual. **Corta-se** "É por aqui que a maior parte dos trabalhos começa." Na abertura, **três atalhos** em vez de um: "Tenho um terreno", "Uma operação travou", "Testar o simulador".
- **1. Nova.** "Quando faz sentido": um terreno a decidir; uma proposta de permuta ou parceria na mesa; um projeto a testar antes de lançar; um empreendimento em andamento em que obra, vendas e caixa precisam voltar ao mesmo plano; uma operação travada. Cada item linka para a filha correspondente.
- **2.** Ganhos (usar o lead de "Planejamento integrado": "O ganho maior não está em acertar cada conta, e sim em fazer as três frentes conversarem desde o começo").
- **3.** **O quadro calculado entra aqui** (`{{QUADRO}}`), mais links para o comparador de terreno e o simulador.
- **4.** Os 4 movimentos no empreendimento. "O que estruturamos" (8 itens) vira a lista compacta, e **"Planejamento integrado" sai** por ser duplicata.
- **5.** Entregáveis do diagnóstico de um empreendimento. Hoje não estão escritos; o conteúdo-base está em `/metodo/` (o que sai de Mapear e Modelar).
- **6.** Projetistas, jurídico, comercial, banco. Junta a frase de condução.
- **7.** As filhas: terreno e obra parada como **situações**; o simulador como **ferramenta**, em linha separada ("Para testar antes de conversar").
- **8.** FAQ atual, mais *"Quanto custa e como começa?"*.
- **Trilho "Do terreno à entrega":** pode ficar como apoio visual depois da seção 4, mas **"Empresa" e "Capital" deixam de ser etapas**. Viram marcos com link: "aqui entra a vertente Empresas" e "aqui entra a vertente Capital".

**Capital** (`/capital/`)
- **0.** H1 "Primeiro o negócio. Depois o capital." O lead é cortado para 2 frases ("A DALETH não começa procurando dinheiro. Primeiro verifica se a operação está estruturada para recebê-lo e qual forma de capital faz sentido.").
- **1. Nova.** "Quando faz sentido" (copy):
  - *Um novo empreendimento pede mais capital do que a empresa quer imobilizar.*
  - *A operação vai à análise de um financiador e precisa chegar pronta, inclusive para financiamento à produção.*
  - `id="recurso-definido"`: *O investidor ou o sócio capitalista já existe, e falta definir como o recurso entra, com qual garantia e qual regra de saída.*
  - *Você quer comparar capital próprio, de terceiros e combinações antes de escolher.*
  - `id="investidor"`: *Você é o investidor e avalia entrar numa operação: precisa medir a estrutura de entrada, as garantias e a saída antes de decidir.* Isso **não** é captação; é estruturar a entrada de quem já decidiu olhar. A redação passa pela mesma revisão jurídica da frase de proteção (4.5).
- **2.** "Ampliar o que é possível realizar" fica.
- **3.** **"Papéis claros" sobe e se junta ao MODELAR de capital**: o quadro calculado (é literalmente a comparação de estruturas de capital), mais a frase "Quem aprova é o financiador. Quem decide investir é o investidor."
- **4.** Os 4 movimentos em capital. Os 6 cartões viram lista compacta.
- **5.** Entregáveis. "Apresentação da operação" e "O que uma análise costuma olhar primeiro" viram o conteúdo desta seção. **Capital passa a ser a dona do tema "preparar para análise"**, e Empresas linka para cá em vez de repetir.
- **8.** FAQ atual (já tem "Como é definido o valor?"), mais *"Vocês trabalham para o investidor ou para a incorporadora?"* (resposta: para quem contrata, com papéis escritos).
- **Pendente:** a frase de proteção regulatória (4.5) entra na seção 3 depois da revisão jurídica.

**Filhas de situação (terreno, obra parada, futura viabilidade):** usam o mesmo template de forma enxuta.
- **Terreno:**
  - ganha **CTA na abertura** ("Falar sobre o meu terreno");
  - ganha a **seção 5** ("O que o diagnóstico entrega para um terreno": potencial construtivo levantado, produtos possíveis, os três caminhos comparados com número, o efeito de cada forma de aquisição no caixa, o parceiro adequado, se for parceria);
  - mantém o comparador como seção 3, que já é.
- **Obra parada:** só precisa da seção 6 (jurídico), explícita, e do bloco "O que sai do diagnóstico" separado de "Medir antes de prometer".

### 4.2 Página de FERRAMENTA (simulador; e o comparador de terreno, se um dia virar página própria)

O papel da ferramenta é ser **a oferta de entrada que entrega algo antes de pedir** (lição Viestra). Ela é a prova do diferencial e a conversão intermediária. A estrutura existe para levar do "brinquei" ao "quero isto com os meus números".

| # | Seção | Pergunta | Regra |
|---|---|---|---|
| 0 | **Abertura** | "O que esta ferramenta me mostra?" | Rótulo "Empreendimentos · Simulador". H1 de consequência ("A mesma obra, estruturas de capital diferentes"). Lead de 2 frases. **Sem CTA de contato no topo**: aqui o CTA é usar a ferramenta. Uma linha de aviso: "Números de exemplo; não é leitura de um projeto real." |
| 1 | **A ferramenta** | — | No celular, o resultado vem antes dos controles (como já está). Os arranjos de partida servem de atalhos. |
| 2 | **Como ler o resultado** | "O que significa este número?" | A seção atual "O que é exposição máxima de caixa", em 3 parágrafos, no máximo. |
| 3 | **Do exemplo ao seu projeto (nova)** | "O que falta para isto valer para mim?" | É a ponte, e a seção que converte. Copy: *"A simulação usa premissas fixas e não cobra o custo de cada instrumento. No seu projeto, o diagnóstico usa o custo, o prazo, o preço e o ritmo de vendas reais, inclui juros, prêmio da permuta e desconto da venda na planta, e compara as estruturas pelo efeito no caixa **e** na margem."* Fecha com um **botão contextual** (seção 4). |
| 4 | **CTA "Levar estes números para a conversa" (novo)** | — | Abre `/contato/?origem=simulador&momento=empreendimento` e **preenche a mensagem** com o cenário atual (VGV, % terreno, % permuta, % planta, % crédito, exposição e mês do pico). Ao lado, o link "Salvar ou imprimir este cenário": a impressão já tem regras próprias. |
| 5 | **FAQ** | "E se…?" | As 3 atuais bastam. |
| 6 | **Fecho + para continuar** | — | Fecho atual ("Se a curva lembrou o seu caso, vale conversar"), mais os links para a outra ferramenta e para a vertente (Capital ou Empreendimentos). |

**Regra para ferramentas:** nunca pedir dado de contato para usar. O valor vem primeiro, e o pedido vem depois, com os números do visitante já dentro do formulário. A mesma lógica vale para o **Radar de Estruturação** (Caderno §08, A TESTAR), quando o Cristiano decidir fazê-lo: o Radar seria a ferramenta de entrada de Empresas, a vertente que hoje não tem nenhuma.

---

## 5. Fluxo de conversão: três visitantes

**Peças que os três caminhos exigem, valendo para o site todo:**
- **Formulário que envia**, com o canal definido (pendência 1.1). Sem isso, nada abaixo funciona.
- **`/contato/` aceita parâmetros:**
  - `momento` pré-seleciona o select;
  - `origem` vai num campo oculto (página ou CTA de onde veio);
  - a mensagem pode vir pré-preenchida (simulador).
  - Acrescentar ao select a opção *"Sou investidor e avalio entrar numa operação"*.
- **Sequência escrita do pós-envio**, a mesma em quatro lugares: Bloco 4 da home, `/como-comeca/`, lado direito de `/contato/` e `/contato/recebido/`.
  1. Você conta o momento.
  2. Respondemos por [canal] para marcar a conversa de enquadramento.
  3. Conversa online, sem custo.
  4. Se houver aderência, a proposta do diagnóstico por escrito.
  - **Duas lacunas que só o Cristiano preenche:** o canal e o **prazo de resposta** (a Requity promete 1 dia útil; aqui é proibido inventar).
  - Em `/contato/recebido/`, corrigir a frase que pula a conversa ("a resposta já traz o desenho do diagnóstico").
- **`/contato/recebido/` por momento:** em vez de "Voltar ao início", uma leitura útil enquanto espera. Terreno → comparador; capital → simulador; obra parada → "O que reunir".

### Visitante A · Dono de construtora de médio porte (ICP)
**Como chega:** por indicação (contador, correspondente, parceiro; Caderno §01, "jornada de compra"). Digita "DALETH" e cai na **home**. Às vezes vem do LinkedIn do Cristiano.

**Caminho:**
1. **Hero:** lê "construtoras e incorporadoras" e se reconhece. A microcopy "conversa sem custo" baixa a guarda.
2. **Bloco 2:** o quadro mostra que a mesma obra pede capital próprio muito diferente conforme a estrutura (os números são os calculados no build, de exemplo). É o momento "isso eu não tenho". Pode clicar em "Teste você mesmo".
3. **Bloco 3:** "A empresa cresceu, e a estrutura de decisão precisa acompanhar" → `/empresas/`.
4. **`/empresas/`:**
   - seção 1, "Quando faz sentido": reconhece "o caixa é um só para tudo";
   - seção 3: vê as estruturas comparadas;
   - seção 8: a FAQ responde "vai tirar velocidade?" e "já tenho contador";
   - fecho "Falar sobre a minha empresa" → `/contato/?momento=empresa&origem=empresas`.
5. **Volta antes de enviar**, porque em B2B ele quase sempre volta: verifica quem conduz (Bloco 6 → `/sobre/`). **É aqui que a falta de foto e LinkedIn derruba a conversão.** Ele também pode mostrar o site ao sócio: as páginas precisam se sustentar sozinhas, sem o Cristiano explicando (Caderno §12B).
6. Envia o formulário. Em `/recebido/` vê a sequência e o simulador.

**O que cada página precisa ter para isso funcionar:**
- **Home:** CTA único, quadro, linha de roteamento para Empresas, FAQ com "quanto custa" e "já tenho contador".
- **Empresas:** situação antes do catálogo, a tabela de alternativas (MODELAR), FAQ de "velocidade" e "porte", fecho com a sequência.
- **Sobre:** foto e LinkedIn (pendência 1.3).
- **Contato:** momento pré-selecionado, origem gravada.

### Visitante B · Dono de terreno
**Como chega:** por busca ("vender ou permutar terreno", "permuta financeira", "quanto vale meu terreno para incorporação") direto em **`/empreendimentos/terreno/`**, ou depois de receber uma proposta de uma incorporadora. Às vezes pela home → Bloco 3, "Tenho um terreno".

**Caminho:**
1. **Abertura de terreno:** H1 "Vender, permutar ou incorporar: três negócios diferentes". Precisa de um **CTA logo aqui** ("Falar sobre o meu terreno"), que hoje falta. Quem chega com uma proposta na mão quer falar, não ler.
2. **Comparador:** entende que os três caminhos têm natureza diferente. Para quem pensa em incorporar, o link "Ver o efeito de cada uma" leva ao simulador.
3. **"Uma proposta diz quanto alguém quer pagar":** é o gancho mais forte da página. Ganha um CTA inline: *"Antes de responder à proposta, conte o que ofereceram."*
4. **Nova seção 5:** o que o diagnóstico entrega para um terreno. Responde "o que eu compro?".
5. **FAQ:** "Preciso ter dinheiro para incorporar?" e "Já tenho corretor e advogado".
6. **Fecho:** "Conte onde fica o terreno e o que já ofereceram" → `/contato/?momento=terreno&origem=terreno`. O lado direito do contato pode sugerir: *"se recebeu proposta, diga o tipo (compra, permuta física, financeira) e o prazo para responder"*.

**O que cada página precisa ter para isso funcionar:**
- **Terreno:** CTA na abertura, CTA na seção "proposta", entregáveis, fecho (que já existe).
- **Simulador:** "Levar estes números para a conversa".
- **Contato:** momento pré-selecionado.
- **Futuro:** a página de viabilidade (pendência 4.4) captura a busca de maior volume e alimenta este mesmo funil. O terreno costuma ser a porta para a incorporadora parceira, então vale o investimento.

### Visitante C · Investidor
**Como chega:** por indicação ou LinkedIn, avaliando entrar num empreendimento (aportar numa SPE, numa parceria ou assumir uma obra parada), ou já sócio capitalista de uma incorporadora. Cai na **home** ou em **`/capital/`**.

**Caminho:**
1. **Home, Bloco 3:** precisa existir a linha **"Sou investidor e avalio entrar numa operação"**. Hoje não existe, e esse visitante não acha a porta dele.
2. **`/capital/#investidor`:**
   - situação: medir estrutura de entrada, garantias e regra de saída antes de decidir;
   - seção 3: "Papéis claros" (a DALETH não capta nem administra recursos; estrutura a entrada), que é o ponto de confiança desse público;
   - seção 5: os entregáveis para quem investe (leitura do empreendimento, alternativas de entrada comparadas, garantias, regra de saída, interlocução com a incorporadora).
3. **Se o ativo é uma obra parada:** `/empreendimentos/obra-parada/` já tem "Um investidor: avalia assumir o empreendimento e precisa medir o passivo antes de entrar".
4. **FAQ:** "Vocês trabalham para o investidor ou para a incorporadora?"
5. **Fecho:** "Falar sobre o capital do meu projeto". Vale uma variante, ou a âncora `?momento=investidor`, no formulário.

**O que cada página precisa ter para isso funcionar:**
- **Home:** a linha do investidor.
- **Capital:** a situação com `id="investidor"`, "Papéis claros" no alto e a FAQ de lado da mesa.
- **Contato:** a opção "Sou investidor…".
- **Revisão jurídica** da redação desse trecho, junto com a 4.5.

---

## 6. Resumo executivo: o que muda, por arquivo

| Arquivo | Mudança estrutural |
|---|---|
| `build.py` | `MENU_APOIO`: sai Repertório, entra **Simulador** (`/empreendimentos/simulador/`). CTA do cabeçalho com o mesmo rótulo do hero. Barra de CTA fixa no celular depois do hero (fora de `/contato/`). `GARANTIAS` uma vez por página. |
| `paginas/00-inicio.html` | Nova ordem: Hero → Diferencial → **Em que momento** (com investidor e destinos por âncora) → Como começa (com sequência e garantias) → **Método com a tese fundida** → Quem conduz (curto) → **FAQ (5)** → Fecho. Saem o bloco Repertório e a tese isolada. CTA secundário do hero → âncora do quadro. |
| `paginas/10-empresas.html` | Sinais sobem. **Nova tabela de alternativas** (células a validar pelo Cristiano). Catálogo vira lista. Entregáveis e interfaces em seções próprias. FAQ +3. `id="analise-externa"`. |
| `paginas/20-empreendimentos.html` | Sai a frase de frequência. Três atalhos na abertura. Nova "Quando faz sentido". **`{{QUADRO}}` entra.** "Planejamento integrado" sai. Simulador separado das situações. O trilho para de chamar Empresa e Capital de etapa. |
| `paginas/21-terreno.html` | CTA na abertura e na seção "proposta". Nova seção de entregáveis. |
| `paginas/22-simulador.html` | Nova seção "Do exemplo ao seu projeto". Botão "Levar estes números para a conversa", com a mensagem preenchida pelo `ferramentas.js`. |
| `paginas/30-capital.html` | Lead curto. Nova "Quando faz sentido" (com `#investidor` e `#recurso-definido`). "Papéis claros" + quadro sobem. Capital passa a ser dona de "preparar para análise". FAQ +1. |
| `paginas/40-metodo.html` | Sai "Do primeiro contato à implantação": vira um link para `/como-comeca/`. Repertório linkado dentro de Modelar. |
| `paginas/60-como-comeca.html` | Ganha a sequência pós-formulário. Os 6 cartões de "O que varia" viram links para o contato com momento pré-selecionado. |
| `paginas/80-contato.html` / `81-recebido.html` | Parâmetros `momento`, `origem` e mensagem. Nova opção "investidor". Sequência no lado direito. Corrige a frase do recebido. Recebido com sugestão por momento. |

**Decisões que só o Cristiano toma e que esta estrutura expõe:**
1. Canal de contato e **prazo de resposta** declarado.
2. Rótulo único do CTA (Analisar meu caso × Conversar sobre uma oportunidade).
3. Foto e LinkedIn.
4. As células da tabela societária de Empresas.
5. A redação do trecho do investidor (com revisão jurídica).
6. A página de viabilidade (4.4).
7. A volta do Simulador ao menu, que ele mesmo tinha decidido em 28/09.

**Checklist §12, aplicado a esta proposta:**
- Território em 5 segundos: hero.
- Crença clara: método com a tese.
- Método nomeável: 4 movimentos.
- Serviços como sistema: roteamento e "Para continuar".
- Reconhecimento por situação: Bloco 3 e a seção 1 de cada vertente.
- Prova: ferramentas e credenciais; **cases continuam faltando, sem inventar**.
- Próximo passo simples: CTA único e sequência escrita.
- Formulário que qualifica: momento e origem.
- Sem garantias que não se controlam: FAQ "captam / garantem crédito".
