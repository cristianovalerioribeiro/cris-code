// Termo de Responsabilidade (v4, versão rigorosa) e Parecer de Revisão Jurídica.

const termo = {
  file: 'Termo_de_Responsabilidade',
  footer: 'Termo de Responsabilidade · v4 · rubricas: ________  ________',
  blocks: [
    { t: 'banner', title: 'Termo de Responsabilidade e Compromisso', sub: 'Obrigações do comprador para o pagamento do saldo por financiamento · parte integrante e inseparável do contrato de compra da unidade' },

    { t: 'form', rows: [
      [['Comprador(a) 1', ''], ['Comprador(a) 2', '']],
      [['CPF', ''], ['CPF', '']],
      [['RG', ''], ['RG', '']],
      [['Endereço', ''], ['Endereço', '']],
      [['WhatsApp', ''], ['WhatsApp', '']],
      [['E-mail', ''], ['E-mail', '']],
      [['Renda bruta', 'R$'], ['Renda bruta', 'R$']],
    ], head: true },
    { t: 'form', rows: [
      [['Vendedora', ''], ['CNPJ', '']],
      [['Empreendimento', ''], ['Unidade / bloco', '']],
      [['Contrato nº', ''], ['Previsão das chaves', '___/___/______']],
      [['Saldo a pagar', 'R$'], ['Prazo para pagar', '____ dias após o aviso do habite-se']],
    ] },
    { t: 'small', text: 'Havendo dois compradores, os dois respondem juntos (solidariamente) por tudo o que está aqui, e a restrição ou o descumprimento de **qualquer um** vale para ambos. Este Termo faz parte do contrato e do quadro-resumo; não afasta o direito de arrependimento de 7 dias previsto em lei para contratos assinados em estande de vendas ou fora da sede da vendedora.' },

    { t: 'h', text: '1. Como o saldo será pago' },
    { t: 'numlist', items: [
      'Devo pagar o saldo **dentro do prazo acima**, com financiamento que eu obtiver, com FGTS ou com recursos próprios.',
      '**Obter o financiamento é responsabilidade minha.** A aprovação **não é condição** deste contrato: se o financiamento não sair, continuo obrigado a pagar o saldo no prazo.',
      'Quem aprova é só a Caixa. A vendedora **não garante** aprovação, valor financiado, subsídio nem taxa de juros. **Se o valor aprovado ou o subsídio for menor, pago a diferença no mesmo prazo.**',
      'O prazo só é prorrogado se o atraso for causado **exclusivamente** pela Caixa, pelo cartório ou pela vendedora, estando minha documentação completa e em dia.',
      '**As chaves só são entregues depois de assinado o financiamento ou pago o saldo.** Até o pagamento, o saldo é corrigido como prevê o contrato.',
    ] },

    { t: 'h', text: '2. O que me foi explicado antes de assinar' },
    { t: 'table', widths: [86, 14], head: ['Declaro que me foi explicado e entendi', 'Rubrica'], rows: [
      { cells: ['O resultado da **análise prévia de crédito** de ___/___/______, com valor estimado de R$ ______________ — é só uma estimativa e pode mudar.', ' '] },
      { cells: ['Restrição no nome, dívida com a Caixa, nova dívida ou queda de renda podem **impedir o financiamento**, algumas mesmo depois de pagas.', ' '] },
      { cells: ['As regras, os valores e os subsídios do Minha Casa Minha Vida **podem mudar** até a data do financiamento.', ' '] },
      { cells: ['Se o saldo não for pago por **motivo ligado a mim**, o contrato pode ser desfeito com as **deduções do quadro-resumo**.', ' '] },
      { cells: ['Recebi cópia do contrato, do quadro-resumo e deste Termo, e tive tempo para ler e tirar dúvidas.', ' '] },
    ] },

    { t: 'h', text: '3. Declarações (sob as penas da lei)' },
    { t: 'p', text: '(   )  **Não tenho** nenhuma restrição no nome.' },
    { t: 'p', text: '(   )  Tenho **somente** as restrições abaixo:' },
    { t: 'table', widths: [30, 26, 14, 14, 16], head: ['Credor', 'Tipo', 'Valor (R$)', 'Desde', 'Limpar até'], rows: [
      { cells: [' ', ' ', ' ', ' ', ' '] }, { cells: [' ', ' ', ' ', ' ', ' '] }, { cells: [' ', ' ', ' ', ' ', ' '] },
    ] },
    { t: 'bullets', items: [
      'Não tenho imóvel residencial nem financiamento habitacional, e nunca tive financiamento pelo Sistema Financeiro da Habitação.',
      'Não tenho dívida, acordo ou atraso com a Caixa, salvo o que listei acima.',
      'A renda informada e os documentos que entreguei são **verdadeiros**.',
      '**Informação falsa ou omitida** é descumprimento grave deste Termo.',
    ] },

    { t: 'h', text: '4. Minhas obrigações até assinar o financiamento' },
    { t: 'numlist', items: [
      '**Limpar as dívidas listadas até a data de cada uma** e entregar o comprovante de pagamento e da baixa em até 5 dias úteis.',
      '**Manter o nome sem restrições** em birôs de crédito, cartórios de protesto, Banco Central (SCR), CADIN, Receita Federal e Caixa.',
      '**Não fazer** empréstimo, financiamento, crediário ou cartão novo, nem ser fiador ou avalista, **sem avisar antes, por escrito**. Nova dívida que reduza ou impeça o financiamento é de minha responsabilidade.',
      '**Pagar a entrada em dia.** Atraso de mais de 30 dias em qualquer parcela também é descumprimento deste Termo.',
      '**Avisar em até 10 dias** qualquer mudança de emprego, renda, estado civil, endereço, telefone ou e-mail.',
      '**Não comprar imóvel residencial** nem fazer outro financiamento habitacional.',
      '**Entregar documentos**, inclusive o Registrato do Banco Central, em até 5 dias úteis do pedido, e **comparecer para assinar o financiamento** em até 10 dias da convocação. Faltar sem justificativa comprovada é descumprimento.',
      '**Manter meus contatos atualizados.** Avisos enviados para os contatos deste Termo são considerados recebidos.',
    ] },

    { t: 'h', text: '5. Consultas e uso dos meus dados' },
    { t: 'p', text: 'A vendedora e o correspondente Caixa indicado por ela vão **consultar meu nome** (birôs, cartórios, Receita) e **compartilhar meus dados com a Caixa**, hoje e periodicamente até o financiamento. **Autorizo a Caixa e o correspondente a consultar meus dados no Sistema de Informações de Crédito do Banco Central (SCR).** O tratamento é necessário para cumprir este contrato e para a proteção do crédito (LGPD, art. 7º, V e X), e não depende de consentimento que possa ser revogado. Os dados ficam guardados durante o contrato e pelo prazo legal. Canal para pedidos sobre meus dados: ______________________.' },

    { t: 'h', text: '6. Se aparecer restrição ou descumprimento' },
    { t: 'steps', items: [
      { title: 'Aviso', body: 'pelos contatos deste Termo' },
      { title: '30 dias', body: 'para regularizar (15 se faltarem menos de 120 dias para as chaves)' },
      { title: 'Vendedora decide', body: 'nova chance ou soluções, **sem obrigação** de oferecê-las' },
      { title: 'Notificação formal', body: 'judicial ou por cartório, 15 dias para pagar ou regularizar' },
    ] },
    { t: 'small', text: 'Soluções possíveis, a critério da vendedora: outro comprador para somar renda, troca por unidade de menor valor, mais entrada/FGTS ou cessão do contrato — sempre com nova análise de crédito.' },

    { t: 'h', text: '7. Se o saldo não for pago' },
    { t: 'table', widths: [42, 58], head: ['Motivo', 'Consequência'], boldFirst: true, rows: [
      { color: 'red', cells: ['Motivos ligados a mim:\ndescumprimento deste Termo; restrição não resolvida; reprovação pela Caixa por renda, cadastro, análise de risco, documentação ou enquadramento no programa; perda ou redução de renda; desistência; falta à assinatura', 'Após a **notificação formal** sem pagamento em 15 dias, o contrato é **desfeito de pleno direito, por minha culpa**, com as **deduções do quadro-resumo** (Lei 13.786/2018), e a unidade fica livre para nova venda.'] },
      { color: 'yellow', cells: ['Motivos não ligados a mim:\nproblema do imóvel ou da documentação da vendedora; mudança de lei ou regra do programa, posterior a esta data, que me torne inelegível', 'O contrato é desfeito **sem multa**, com devolução nas condições do quadro-resumo para esse caso.'] },
    ] },
    { t: 'small', text: 'Tolerar um atraso não é renúncia a direitos. Se alguma cláusula for considerada inválida, as demais continuam valendo.' },

    { t: 'p', text: '**Li, entendi e concordo com este Termo. Recebi uma via e rubriquei todas as páginas.**' },
    { t: 'p', text: 'Local e data: ______________________________, ___/___/______' },
    { t: 'sign', names: [['Comprador(a) 1', 'CPF'], ['Comprador(a) 2', 'CPF'], ['Vendedora', 'CNPJ'], ['', ''], ['Testemunha 1', 'CPF'], ['Testemunha 2', 'CPF']] },
    { t: 'small', text: 'Assinado eletronicamente com assinatura válida, as testemunhas são dispensadas (CPC, art. 784, § 4º).' },
  ],
};

const parecer = {
  file: 'Parecer_Revisao_Juridica',
  footer: 'Parecer de Revisão Jurídica · Termo e Política de Crédito MCMV · set/2026',
  blocks: [
    { t: 'banner', title: 'Parecer de Revisão Jurídica', sub: 'Termo de Responsabilidade e Política de Crédito MCMV · direito imobiliário, contratual, do consumidor e de proteção de dados · setembro de 2026' },
    { t: 'callout', color: 'gray', text: '**Natureza deste documento:** análise técnica preparada com apoio de inteligência artificial a partir de legislação e jurisprudência públicas. Não substitui a opinião de advogado inscrito na OAB, que deve validar o contrato, o quadro-resumo e o Termo antes do uso.' },

    { t: 'h', text: 'Conclusão' },
    { t: 'p', text: 'Os documentos são **coerentes e juridicamente plausíveis**. A política está alinhada ao **dever de crédito responsável** do CDC (art. 54-D, incluído pela Lei 14.181/2021), que obriga quem concede crédito — inclusive a entrada parcelada pela própria incorporadora — a avaliar a situação do consumidor, consultando bancos de dados de proteção ao crédito.' },
    { t: 'p', text: 'A versão anterior do Termo tinha, porém, **três pontos que o tornariam frágil em juízo** e seis ajustes importantes. Todos foram corrigidos. A pedido da empresa, o Termo foi depois endurecido na **versão 4** (seção 6), fechando as brechas que a defesa de um comprador exploraria, sem incluir cláusulas que um juiz anularia.' },

    { t: 'h', text: '1. Quadro dos achados' },
    { t: 'table', widths: [4, 30, 11, 55], head: ['#', 'Ponto', 'Risco', 'Ajuste feito'], rows: [
      { color: 'red', cells: ['1', 'Desfazimento do contrato só com aviso por WhatsApp/e-mail', '**Alto**', 'Desfazimento exige **notificação judicial ou por cartório (RTD)** com **15 dias** para purgar a mora. WhatsApp e e-mail ficam para avisos do dia a dia.'] },
        { color: 'red', cells: ['2', '"A culpa é minha" em qualquer caso de não financiamento', '**Alto**', 'Separadas as causas **do comprador** (lista objetiva) das causas **alheias** (mudança de regra, reprovação sem restrição), com consequências diferentes.'] },
        { color: 'red', cells: ['3', 'Sem prazo para contratar o financiamento após o habite-se', '**Alto**', 'Campo "Prazo para financiar" no Termo; o prazo deve constar do quadro-resumo (art. 35-A da Lei 4.591/1964).'] },
        { color: 'orange', cells: ['4', 'Proibição de novas dívidas e teto de 35% da renda', 'Médio', 'Virou **aviso prévio por escrito**, com o risco da nova dívida assumido pelo comprador. O teto de 35% fica só na política interna.'] },
        { color: 'orange', cells: ['5', 'LGPD apoiada em "autorizo" (consentimento revogável)', 'Médio', 'Base legal trocada para **execução do contrato e proteção do crédito** (LGPD, art. 7º, V e X), com finalidade, prazo e canal do titular.'] },
        { color: 'orange', cells: ['6', 'Retenção de até 50% no distrato apresentada como certa', 'Médio', 'Divergência entre as Turmas do STJ, com **Temas 1.464 a 1.466 afetados** ao rito repetitivo em jun/2026. Projeções com 25%.'] },
        { color: 'orange', cells: ['7', 'Direito de arrependimento de 7 dias não mencionado', 'Médio', 'Ressalvado no Termo e incluído na rotina da política (art. 67-A, § 10).'] },
        { color: 'orange', cells: ['8', 'Sem prova de que o cliente foi informado antes', 'Médio', 'Cliente declara ter recebido o resultado da análise prévia (CDC, arts. 6º, III, e 54-D, I).'] },
        { color: 'orange', cells: ['9', 'Reserva com sinal na classe "Alta"', 'Médio', 'Sinal devolvido se o crédito não for aprovado; retenção só de despesas comprovadas.'] },
        { color: 'yellow', cells: ['10', 'Pontuação da matriz aplicada de forma automática', 'Baixo', 'Decisão final humana e direito de revisão (LGPD, art. 20).'] },
        { color: 'green', cells: ['11', 'Solidariedade, testemunhas, rubricas, "a vendedora não garante a aprovação"', 'OK', 'Mantidos. Solidariedade expressa (CC, art. 265); título executivo com 2 testemunhas ou assinatura eletrônica (CPC, art. 784, III e § 4º).'] },
        { color: 'green', cells: ['12', 'Consulta a birôs, análise de renda e monitoramento na política', 'OK', 'Amparados no CDC, art. 54-D, II, e na LGPD, art. 7º, X.'] },
    ] },

    { t: 'h', text: '2. Pontos de risco alto, explicados' },
    { t: 'p', text: '**2.1 Como desfazer o contrato.** Na promessa de compra e venda de imóvel, o Decreto-Lei 745/1969 (art. 1º, com a redação da Lei 13.097/2015) exige que o comprador seja **interpelado judicialmente ou notificado pelo Registro de Títulos e Documentos**, com **15 dias** para purgar a mora, **mesmo com cláusula resolutiva expressa**. Cumprido esse rito, o STJ admite a resolução sem ação judicial (REsp 1.789.863/MS, 4ª Turma, 2021). A notificação por e-mail aceita pela 2ª Seção do STJ em 2025 (REsp 2.183.860/DF) trata de **alienação fiduciária** e não deve ser estendida ao compromisso de compra e venda sem cautela. **Consequência prática:** o aviso por WhatsApp serve para a rotina de crédito, mas o desfazimento precisa do cartório.' },
    { t: 'p', text: '**2.2 A culpa pelo financiamento negado.** A jurisprudência é dividida e depende da causa. Quando a Caixa nega por **restrição no nome do comprador**, os tribunais tendem a ver inadimplemento do comprador, e o TJSP já recusou a devolução integral a quem não provou a negativa nem a sua causa. Quando a negativa decorre de **fato alheio às partes**, ou quando o vendedor **não informou** os requisitos do financiamento, há decisões que afastam a culpa do comprador e mandam devolver tudo (Súmula 543 do STJ). Uma cláusula que declara a culpa do comprador em qualquer hipótese tende a ser considerada abusiva (CDC, art. 51, IV) e poderia contaminar o Termo inteiro. **Separar as duas hipóteses dá força à primeira.**' },
    { t: 'p', text: '**2.3 Prazo para quitar após o habite-se.** O art. 35-A da Lei 4.591/1964 exige que o quadro-resumo traga, entre outros itens, o **prazo para o comprador quitar suas obrigações após o auto de conclusão da obra** e as **consequências do desfazimento, com as penalidades em negrito**. Sem esse prazo, não há como caracterizar o atraso no pagamento do saldo, que é o fato que efetivamente permite o desfazimento. As obrigações do Termo funcionam como **prova da causa** desse atraso.' },

    { t: 'h', text: '3. Pontos de atenção' },
    { t: 'bullets', items: [
      '**Perda de emprego do comprador:** não está listada como culpa nem como fato alheio. Os tribunais tendem a ser sensíveis a esse caso. Recomendação: tratar como hipótese de soluções do item 5 e, sem solução, distrato com a retenção do quadro-resumo, sem multa adicional. **Decisão do jurídico.**',
      '**Retenção e prazos de devolução:** a Lei 13.786/2018 fixa 25% (ou até 50% com patrimônio de afetação) e a devolução em 180 dias, ou 30 dias após o habite-se com afetação. O TJSP (Súmulas 1, 2 e 3) e o STJ (Súmula 543) exigem devolução em parcela única. Para contratos posteriores a 2018, prevalecem os prazos da lei, mas o percentual de 50% pode cair até o julgamento dos Temas 1.464 a 1.466.',
      '**Corretagem:** só pode ser cobrada do comprador ou retida no distrato se informada **antes**, com o valor destacado do preço (Tema 938 do STJ).',
      '**Foro:** em contrato de adesão com consumidor, vale o domicílio do comprador (CDC, art. 101, I). Não prever foro diferente.',
      '**Baixa das restrições:** o credor tem 5 dias úteis após o pagamento para dar baixa (Súmula 548 do STJ). Os prazos de 60 e 90 dias da política são folgados e razoáveis.',
    ] },

    { t: 'h', text: '4. Checklist para o contrato principal' },
    { t: 'bullets', items: [
      'Quadro-resumo completo (art. 35-A), com **as duas hipóteses de financiamento não aprovado** (com e sem culpa) e as penalidades em negrito.',
      'Prazo para contratar o financiamento após o habite-se.',
      'Cláusula que incorpora o Termo como anexo e parte do contrato.',
      'Cláusula resolutiva expressa + rito do Decreto-Lei 745/1969 (notificação judicial ou por RTD, 15 dias).',
      'Patrimônio de afetação averbado na matrícula e cláusula de retenção destacada, ciente da divergência no STJ.',
      'Corretagem destacada no preço (Tema 938).',
      'Direito de arrependimento de 7 dias para vendas em estande ou fora da sede (art. 67-A, § 10).',
      'Prazos de devolução do art. 67-A, §§ 5º e 6º.',
      'Foro do domicílio do comprador.',
    ] },

    { t: 'h', text: '5. Termo v4: brechas fechadas' },
    { t: 'table', widths: [38, 62], head: ['Brecha que o comprador poderia usar', 'Como a v4 fecha'], boldFirst: true, rows: [
      { cells: ['"O financiamento era condição do negócio; se não saiu, devolvam tudo."', 'Item 1: o financiamento é **meio de pagamento escolhido pelo comprador**, e a aprovação **não é condição** do contrato. O saldo é devido de qualquer forma.'] },
      { cells: ['"Ninguém me explicou os requisitos." (argumento que mais leva a devolução integral)', 'Item 2: cada ponto explicado tem **rubrica própria**, incluindo o resultado e o valor da análise prévia.'] },
      { cells: ['"A Caixa aprovou menos / o subsídio caiu, então não consigo pagar."', 'Item 1.3: diferença de valor ou de subsídio é paga pelo comprador no mesmo prazo.'] },
      { cells: ['"Fui reprovado sem ter restrição, não tenho culpa."', 'Item 7: reprovação por renda, cadastro, análise de risco, documentação ou enquadramento entra nos **motivos ligados ao comprador**. Só ficam fora problemas da vendedora/imóvel e mudança de lei posterior.'] },
      { cells: ['"Perdi o emprego."', 'Item 7: **perda ou redução de renda** é motivo ligado ao comprador, com as deduções do quadro-resumo.'] },
      { cells: ['Enrolar com prazos sucessivos', 'Item 6: **um único prazo de 30 dias** (15 perto das chaves); nova chance só se a vendedora quiser.'] },
      { cells: ['"Não recebi o aviso."', 'Item 4.8: avisos aos contatos do Termo contam como recebidos; o desfazimento usa notificação formal, que tem prova própria.'] },
      { cells: ['Não comparecer para assinar o financiamento ou não entregar documentos', 'Item 4.7: prazos de 5 dias úteis e 10 dias; faltar sem justificativa é descumprimento.'] },
      { cells: ['"A restrição era do outro comprador."', 'Cabeçalho: solidariedade e restrição de **qualquer** comprador vale para ambos.'] },
      { cells: ['Pedir as chaves antes de pagar o saldo', 'Item 1.5: chaves só após assinatura do financiamento ou pagamento.'] },
      { cells: ['Revogar a autorização de consulta (LGPD)', 'Item 5: base legal de contrato e proteção do crédito, sem consentimento revogável; autorização expressa de consulta ao SCR.'] },
      { cells: ['Anular o Termo inteiro por uma cláusula abusiva', 'Cláusula de conservação: se uma cláusula cair, as outras continuam.'] },
    ] },
    { t: 'h', text: '6. Limites: o que não entrou, e por quê' },
    { t: 'p', text: 'Estas cláusulas parecem mais "duras", mas seriam anuladas pelo Judiciário e dariam argumento para questionar o Termo inteiro:' },
    { t: 'bullets', items: [
      '**Proibir o cliente de fazer qualquer dívida:** interfere na vida financeira do consumidor além do necessário (CDC, art. 51, IV). A v4 exige aviso prévio e transfere o risco — mesmo efeito prático, sem nulidade.',
      '**Reter 100% ou mais que o quadro-resumo:** a Lei 13.786/2018 limita a 25% (até 50% com afetação, em discussão no STJ). Multa extra no Termo seria cobrança em duplicidade.',
      '**Desfazer o contrato só com aviso por WhatsApp:** a lei exige notificação judicial ou por cartório com 15 dias (Decreto-Lei 745/1969).',
      '**Renunciar ao arrependimento de 7 dias:** direito legal irrenunciável (art. 67-A, § 10).',
      '**Cobrar condomínio e IPTU antes das chaves:** a jurisprudência atribui esses encargos a quem tem a posse.',
      '**Foro em outra cidade:** em contrato de adesão vale o domicílio do consumidor (CDC, art. 101, I).',
      '**Linguagem ambígua:** no CDC, a dúvida é resolvida a favor do consumidor (art. 47). Por isso a v4 usa listas fechadas e prazos em números.',
    ] },

    { t: 'h', text: '7. Normas e jurisprudência consultadas' },
    { t: 'table', widths: [30, 70], head: ['Referência', 'O que diz'], boldFirst: true, rows: [
      { cells: ['Decreto-Lei 745/1969, art. 1º (Lei 13.097/2015)', 'Mora do promitente comprador exige interpelação judicial ou notificação via RTD, com 15 dias para purgar, mesmo com cláusula resolutiva expressa.'] },
      { cells: ['STJ, REsp 1.789.863/MS (4ª T., 2021)', 'Com cláusula resolutiva expressa e mora constituída, a resolução dispensa ação judicial.'] },
      { cells: ['STJ, REsp 2.183.860/DF (2ª Seção, 2025)', 'Notificação por e-mail válida para constituir em mora o devedor fiduciante (alienação fiduciária).'] },
      { cells: ['Lei 4.591/1964, arts. 35-A e 67-A (Lei 13.786/2018)', 'Quadro-resumo obrigatório; retenção de 25% ou até 50% com afetação; arrependimento em 7 dias; prazos de devolução.'] },
      { cells: ['STJ, retenção de 50%', '4ª Turma valida com afetação e previsão expressa (jun/2026); 3ª Turma com decisões limitando a 25% em relação de consumo (jan/2026); Temas 1.464 a 1.466 afetados (jun/2026).'] },
      { cells: ['STJ, Súmula 543', 'Resolução sob o CDC: devolução imediata; integral se a culpa for do vendedor, parcial se for do comprador.'] },
      { cells: ['STJ, Súmula 548', 'Credor deve dar baixa da negativação em 5 dias úteis após o pagamento.'] },
      { cells: ['STJ, Temas 938 e 1.002', 'Corretagem transferível se informada previamente e destacada; juros de mora no distrato pedido pelo comprador (contratos anteriores à Lei 13.786).'] },
      { cells: ['TJSP, Súmulas 1, 2 e 3', 'Comprador inadimplente pode pedir a rescisão; devolução em parcela única; retorno ao estado anterior.'] },
      { cells: ['TJSP, financiamento negado', 'Negativa por restrição do comprador tende a caracterizar culpa dele; negativa por fato alheio ou falta de informação do vendedor afasta a culpa.'] },
      { cells: ['CDC, arts. 6º III, 51 IV, 54 § 4º, 54-D e 101 I', 'Informação clara; nulidade de cláusulas iníquas; destaque das cláusulas limitativas; crédito responsável; foro do consumidor.'] },
      { cells: ['LGPD, arts. 7º V e X, 8º § 5º, 9º, 18 e 20', 'Bases legais de contrato e proteção do crédito; consentimento revogável; transparência; direitos do titular; revisão de decisões automatizadas.'] },
      { cells: ['CC, arts. 265, 397, 417 a 420 e 474; CPC, art. 784', 'Solidariedade expressa; mora; arras; cláusula resolutiva expressa; título executivo.'] },
    ] },

    { t: 'h', text: 'Fontes' },
    { t: 'small', text: 'Planalto — Decreto-Lei 745/1969 (planalto.gov.br/ccivil_03/decreto-lei/1965-1988/del0745.htm) · Planalto — Lei 13.786/2018 (planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13786.htm) · STJ — Notícia REsp 1.789.863 (stj.jus.br, 24/08/2021) · STJ — Notificação extrajudicial por e-mail, Segunda Seção (stj.jus.br, 25/06/2025) · Conjur — Em relação de consumo, retenção limitada a 25% (23/01/2026) · Queiroz Cavalcanti — 4ª Turma reafirma retenção de 50% (2026) · TJMG — Tema 1.466 STJ · ANOREG/BR — STJ valida retenção de até 50% · Conjur — Financiamento negado não justifica quebra de contrato (21/02/2017) · Jusbrasil — Financiamento negado e distrato · TJSP — Súmulas da Seção de Direito Privado · STJ — Tema 938 (TJRO/NUGEPNAC) · TJDFT — Tema 1.002 · LegJur — CDC, art. 54-D · Roncato Advogados — Análise de crédito e LGPD · Buscador Dizer o Direito — Súmula 548.' },
  ],
};

module.exports = { termo, parecer };
