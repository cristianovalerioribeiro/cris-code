// Termo de Responsabilidade (v3, revisado) e Parecer de Revisão Jurídica.

const termo = {
  file: 'Termo_de_Responsabilidade',
  footer: 'Termo de Responsabilidade · v3 · rubricas: ________  ________',
  blocks: [
    { t: 'banner', title: 'Termo de Responsabilidade', sub: 'Compromisso de regularização cadastral e ciência sobre o financiamento · parte integrante do contrato de compra da unidade' },

    { t: 'form', rows: [
      [['Comprador(a) 1', ''], ['Comprador(a) 2', '']],
      [['CPF', ''], ['CPF', '']],
      [['RG', ''], ['RG', '']],
      [['Endereço', ''], ['Endereço', '']],
      [['WhatsApp', ''], ['WhatsApp', '']],
      [['E-mail', ''], ['E-mail', '']],
    ], head: true },
    { t: 'form', rows: [
      [['Vendedora', ''], ['CNPJ', '']],
      [['Empreendimento', ''], ['Unidade / bloco', '']],
      [['Contrato nº', ''], ['Previsão das chaves', '___/___/______']],
      [['Saldo a financiar', 'R$'], ['Prazo para financiar', 'até ____ dias após o habite-se']],
    ] },
    { t: 'small', text: 'Havendo dois compradores, tudo o que está neste Termo vale para os dois, que respondem juntos (solidariamente). Este Termo faz parte do contrato acima e não substitui o quadro-resumo. Ele não afasta o direito de arrependimento de 7 dias previsto em lei quando o contrato é assinado em estande de vendas ou fora da sede da vendedora.' },

    { t: 'h', text: '1. Estou ciente de que' },
    { t: 'numlist', items: [
      'O saldo do imóvel será pago com **financiamento da Caixa Econômica Federal**, pelo Minha Casa Minha Vida, **depois que a obra ficar pronta** — ou com recursos próprios ou outro banco — **dentro do prazo acima**.',
      '**Quem aprova o financiamento é só a Caixa**, na data da assinatura. Para isso preciso estar **sem restrições no nome**, com renda compatível e dentro das regras do programa. A vendedora **não garante** a aprovação.',
      'Recebi o **resultado da análise prévia de crédito** feita em ___/___/______ e a explicação do que pode impedir o financiamento: restrições no nome, novas dívidas e mudança de renda.',
      '**Dívidas com a própria Caixa** e dívidas de banco registradas no Banco Central podem impedir o financiamento **mesmo depois de pagas**.',
    ] },

    { t: 'h', text: '2. Minhas dívidas hoje' },
    { t: 'p', text: '(   )  **Não tenho** nenhuma restrição no nome.' },
    { t: 'p', text: '(   )  Tenho **somente** as restrições abaixo:' },
    { t: 'table', widths: [30, 26, 14, 14, 16], head: ['Credor', 'Tipo', 'Valor (R$)', 'Desde', 'Limpar até'], rows: [
      { cells: [' ', ' ', ' ', ' ', ' '] }, { cells: [' ', ' ', ' ', ' ', ' '] }, { cells: [' ', ' ', ' ', ' ', ' '] },
    ] },
    { t: 'small', text: 'Tipo: negativação (Serasa/SPC), protesto, banco, cheque ou governo.' },

    { t: 'h', text: '3. Eu me comprometo a' },
    { t: 'numlist', items: [
      '**Limpar as dívidas acima até a data indicada** e entregar o comprovante de pagamento e da baixa.',
      '**Manter o nome limpo** até assinar o financiamento.',
      '**Avisar em até 15 dias** se fizer nova dívida (empréstimo, financiamento, crediário, cartão) ou for fiador — sabendo que isso pode **reduzir ou impedir** o financiamento.',
      '**Pagar a entrada em dia.**',
      '**Avisar em até 15 dias** se mudar de emprego, renda, estado civil, endereço, telefone ou e-mail.',
      '**Não comprar outro imóvel residencial** nem fazer outro financiamento habitacional antes deste (regra do Minha Casa Minha Vida).',
      '**Entregar os documentos** pedidos, inclusive o Registrato do Banco Central, em até 10 dias, e **comparecer** para assinar o financiamento.',
    ] },

    { t: 'h', text: '4. Uso dos meus dados' },
    { t: 'p', text: 'Estou ciente de que a vendedora e o correspondente Caixa indicado por ela vão **consultar meu nome** (Serasa, SPC, cartórios, Receita) e **compartilhar meus dados com a Caixa**, hoje e **periodicamente até o financiamento**, só para acompanhar a aprovação deste imóvel. Isso é necessário para cumprir este contrato e para a proteção do crédito (LGPD, art. 7º, V e X). Os dados ficam guardados durante o contrato e pelo prazo que a lei exigir. Posso pedir informações, cópia ou correção pelo canal ______________________.' },

    { t: 'h', text: '5. Se aparecer restrição' },
    { t: 'steps', items: [
      { title: 'Aviso', body: 'por WhatsApp, e-mail ou carta' },
      { title: '30 dias', body: 'para limpar o nome' },
      { title: '+30 dias', body: 'último prazo, com reunião' },
      { title: 'Soluções', body: 'outro comprador, unidade menor, mais entrada/FGTS ou cessão' },
    ] },
    { t: 'small', text: 'Faltando menos de 120 dias para as chaves, os prazos caem pela metade. Devo manter meus contatos atualizados.' },

    { t: 'h', text: '6. Se o financiamento não sair' },
    { t: 'table', widths: [36, 64], head: ['Motivo', 'O que acontece'], boldFirst: true, rows: [
      { color: 'red', cells: ['Por minha causa:\nrestrição não resolvida nos prazos, dívida escondida, informação falsa, nova dívida, documentos não entregues ou outro imóvel comprado', 'A vendedora me envia **notificação formal (judicial ou por cartório)** com **15 dias** para eu pagar o saldo ou regularizar. Se eu não resolver, o contrato é desfeito **por minha culpa**, com as deduções previstas no **quadro-resumo** e na **Lei 13.786/2018** (Lei do Distrato).'] },
      { color: 'yellow', cells: ['Sem culpa minha:\nmudança nas regras do programa ou da Caixa, ou reprovação sem restrição e sem descumprimento meu', 'Buscamos juntos as soluções do item 5. Se nenhuma funcionar, o contrato é desfeito **sem multa**, com devolução do que paguei nas condições do quadro-resumo para esse caso.'] },
    ] },
    { t: 'small', text: 'Se a vendedora tolerar algum atraso, isso não é renúncia aos seus direitos.' },

    { t: 'p', text: '**Li este Termo, tirei minhas dúvidas, recebi uma via e rubriquei todas as páginas.**' },
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
    { t: 'p', text: 'A versão anterior do Termo tinha, porém, **três pontos que o tornariam frágil em juízo** e seis ajustes importantes. Todos foram corrigidos na **versão 3 do Termo** e na **versão 3 da Política**, entregues junto com este parecer.' },

    { t: 'h', text: '1. Quadro dos achados' },
    { t: 'table', widths: [4, 30, 11, 55], head: ['#', 'Ponto', 'Risco', 'Ajuste feito'], rows: [
      { color: 'red', cells: ['1', 'Desfazimento do contrato só com aviso por WhatsApp/e-mail', '**Alto**', 'Desfazimento exige **notificação judicial ou por cartório (RTD)** com **15 dias** para purgar a mora. WhatsApp e e-mail ficam para avisos do dia a dia.'] },
        { color: 'red', cells: ['2', '"A culpa é minha" em qualquer caso de não financiamento', '**Alto**', 'Separadas as causas **do comprador** (lista objetiva) das causas **alheias** (mudança de regra, reprovação sem restrição), com consequências diferentes.'] },
        { color: 'red', cells: ['3', 'Sem prazo para contratar o financiamento após o habite-se', '**Alto**', 'Campo "Prazo para financiar" no Termo; o prazo deve constar do quadro-resumo (art. 35-A da Lei 4.591/1964).'] },
        { color: 'orange', cells: ['4', 'Proibição de novas dívidas e teto de 35% da renda', 'Médio', 'Virou **dever de avisar em 15 dias** e ciência do risco. O teto de 35% fica só na política interna.'] },
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

    { t: 'h', text: '5. Normas e jurisprudência consultadas' },
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
