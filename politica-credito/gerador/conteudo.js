// Conteúdo dos dois documentos, num formato neutro que render.js transforma em
// Word (.docx) e em HTML (que vira PDF). Negrito: **texto**.

const C = { navy: '1F3864', green: 'E2EFDA', yellow: 'FFF2CC', orange: 'FCE4D6', red: 'F8CBAD', blue: 'DDEBF7', gray: 'F2F2F2' };
const E = { green: '548235', yellow: 'BF9000', orange: 'C55A11', red: 'C00000', blue: '2F5597', gray: '7F7F7F' };

const politica = {
  file: 'Politica_de_Credito_MCMV',
  footer: 'Política de Crédito MCMV · v2',
  blocks: [
    { t: 'banner', title: 'Política de Crédito', sub: 'Vendas Minha Casa Minha Vida · entrada durante a obra · financiamento Caixa na entrega das chaves' },

    { t: 'callout', color: 'blue', text: '**Regra de ouro:** não basta o nome estar limpo hoje. Só vendemos para quem **vai ser aprovado pela Caixa no dia das chaves**, daqui a 12 a 18 meses. Cliente reprovado no repasse devolve a unidade pronta, com custo de distrato, revenda e risco de ação judicial — e esse risco é nosso.' },

    { t: 'h', text: '1. As três perguntas, nesta ordem' },
    { t: 'cards', items: [
      { color: 'blue', title: '1  Pode entrar no MCMV?', body: ['Renda dentro da faixa', 'Não tem imóvel', 'Nunca teve financiamento habitacional'] },
      { color: 'blue', title: '2  A dívida dá para limpar a tempo?', body: ['Quanto deve, para quem e desde quando', 'Seções 2 a 4'] },
      { color: 'blue', title: '3  A renda aguenta?', body: ['Parcela Caixa até 30% da renda', 'Tudo somado até 35%', 'Seção 5'] },
    ] },

    { t: 'h', text: '2. Quanto de "nome sujo" aceitamos' },
    { t: 'p', text: 'Some **todas** as restrições (negativações, protestos, cheques) e compare com a renda bruta da família. **Vale a linha mais rigorosa** entre o valor em reais e a proporção da renda.' },
    { t: 'table', widths: [16, 19, 19, 46], head: ['Classe', 'Soma das dívidas', 'ou, pela renda', 'Decisão'], boldFirst: true,
      rows: [
        { color: 'green', cells: ['Sem restrição', '—', '—', '**Assina.** Acompanhamento normal.'] },
        { color: 'green', cells: ['Leve', 'até R$ 1.000', 'até metade da renda', '**Assina com o Termo.** 60 dias para limpar.'] },
        { color: 'yellow', cells: ['Moderada', 'R$ 1.001 a R$ 3.000', 'até 1 renda', 'Dívida de loja/conta: **assina com o Termo**, 90 dias.\nDívida de banco: **só reserva** até quitar.'] },
        { color: 'orange', cells: ['Alta', 'R$ 3.001 a R$ 6.000', 'até 2 rendas', '**Não assina.** Reserva por 60 dias; assina só depois de quitar e nova análise Caixa.'] },
        { color: 'red', cells: ['Grave', 'acima de R$ 6.000', 'mais de 2 rendas', '**Não vende.** Orienta e reavalia em 6 meses.'] },
      ] },
    { t: 'cards', items: [
      { color: 'orange', title: 'Sobe um nível se tiver', body: ['4 ou mais credores', 'dívida com menos de 3 meses', 'acordo anterior quebrado', 'dívida de banco no Banco Central (SCR)', 'protesto ou ação de cobrança'] },
      { color: 'green', title: 'Desce um nível se', body: ['a dívida já foi paga, com comprovante, e só falta a baixa'] },
    ] },

    { t: 'h', text: '3. Tipo de dívida: fácil ou difícil de limpar?' },
    { t: 'cards', items: [
      { color: 'green', title: 'FÁCIL · dias', body: ['Telefone, internet, TV', 'Lojas e crediário', 'Luz e água', 'Escola e faculdade', '→ Pagou, a baixa sai em até 5 dias úteis'] },
      { color: 'yellow', title: 'MÉDIA · semanas', body: ['Protesto em cartório', 'Cheque sem fundo', 'CPF pendente na Receita', 'Dívida com o governo federal', 'Cartão/empréstimo de banco que ainda não virou prejuízo'] },
      { color: 'orange', title: 'DIFÍCIL · meses', body: ['Dívida de banco que virou prejuízo', 'Financiamento de carro atrasado', 'Ação judicial de cobrança', '→ Mesmo paga, fica no histórico do banco por 24 meses'] },
    ] },
    { t: 'callout', color: 'yellow', text: '**Cuidado com acordo parcelado:** tira o nome do Serasa na 1ª parcela, mas a parcela passa a comer renda. Acordo quebrado no meio da obra é pior que a dívida original.' },

    { t: 'h', text: '4. Não vender: não dá para limpar a tempo' },
    { t: 'callout', color: 'red', list: [
      '**Qualquer dívida, acordo ou atraso com a própria Caixa** — pesa por até 5 anos, mesmo quitada. Só a análise da Caixa (SICAQ) mostra.',
      '**Dívida de banco que virou prejuízo nos últimos 12 meses** — ainda aparece para a Caixa no dia das chaves.',
      '**Já teve financiamento habitacional ou tem imóvel no nome** — regra do programa, não tem solução.',
      '**Ação de cobrança ou busca e apreensão** em andamento, sem acordo.',
      '**CPF cancelado, suspenso** ou suspeita de documento falso.',
      '**Renda que não paga a parcela**, nem com subsídio, FGTS e entrada.',
    ] },

    { t: 'h', text: '5. Limite de comprometimento da renda' },
    { t: 'tiles', items: [
      { big: '30%', label: 'Parcela do financiamento Caixa', color: 'blue' },
      { big: '25%', label: 'Durante a obra: entrada + acordos de dívida', color: 'blue' },
      { big: '35%', label: 'Nas chaves: Caixa + saldo da entrada + acordos + empréstimos + cartão', color: 'blue' },
    ] },
    { t: 'small', text: 'Dívidas de banco em dia somando mais de 6 vezes a renda: cliente alavancado demais, só com aprovação do comitê.' },

    { t: 'h', text: '6. A rotina, do atendimento às chaves' },
    { t: 'table', widths: [22, 78], head: ['Quando', 'O que fazer'], boldFirst: true,
      rows: [
        { cells: ['Atendimento', 'Perguntar: renda e como comprova · já teve imóvel/financiamento · dívidas e com quem · algo com a Caixa. Cliente gera o **Registrato** (Banco Central) no celular pelo gov.br.'] },
        { cells: ['Até 5 dias', 'Consulta Serasa/SPC + Registrato + **SICAQ** no correspondente Caixa. Classificar pelas seções 1 a 5.'] },
        { cells: ['Assinatura', 'Contrato + **Termo de Responsabilidade** com as dívidas e o prazo de cada uma.'] },
        { color: 'gray', cells: ['Durante a obra', 'Com restrição: consulta **todo mês** até limpar, depois a cada 3 meses. Sem restrição: a cada **6 meses**. Atraso de mais de 15 dias na entrada: consulta na hora.'] },
        { color: 'gray', cells: ['Restrição nova', 'Aviso por escrito → **30 dias** → mais **30 dias** e reunião → comitê decide.'] },
        { color: 'blue', cells: ['180 dias antes', 'Consulta de todos os clientes.'] },
        { color: 'blue', cells: ['120 dias antes', '**Nova SICAQ para todos.**'] },
        { color: 'blue', cells: ['90 dias antes', 'Quem não vai passar: outro comprador para somar renda, unidade menor, mais entrada/FGTS, cessão ou distrato.'] },
      ] },

    { t: 'h', text: '7. Quem aprova' },
    { t: 'table', widths: [45, 55], head: ['Situação', 'Aprovação'], boldFirst: true,
      rows: [
        { cells: ['Sem restrição e SICAQ aprovada', 'Analista de crédito'] },
        { cells: ['Leve ou moderada', 'Coordenador de crédito'] },
        { cells: ['Alta (reserva)', 'Coordenador, e contrato só após nova SICAQ'] },
        { cells: ['Exceção a esta política', 'Comitê (comercial + financeiro + diretoria), por escrito, no máximo 2% das unidades'] },
      ] },
    { t: 'small', text: 'Teto da carteira: no máximo 20% das unidades vendidas com Termo de Responsabilidade em aberto.' },

    { t: 'h', text: '8. Antes de adotar' },
    { t: 'bullets', items: [
      'Os valores em reais são ponto de partida: calibrar após os primeiros 50 repasses.',
      'Confirmar com o correspondente Caixa o tratamento atual de prejuízo antigo e da restrição interna da Caixa.',
      'Revisão jurídica do contrato, do quadro-resumo (Lei 13.786/2018) e do Termo.',
      'Definir patrimônio de afetação: permite reter até 50% no distrato por culpa do comprador (sem ele, 25%).',
    ] },
  ],
};

const blank = '_______________________';
const termo = {
  file: 'Termo_de_Responsabilidade',
  footer: 'Termo de Responsabilidade · rubricas: ________  ________',
  blocks: [
    { t: 'banner', title: 'Termo de Responsabilidade', sub: 'Compromisso de manter o nome limpo até o financiamento · anexo ao contrato de compra da unidade' },

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
    ] },
    { t: 'small', text: 'Havendo dois compradores, tudo o que está neste Termo vale para os dois, que respondem juntos (solidariamente).' },

    { t: 'h', text: '1. Estou ciente de que' },
    { t: 'numlist', items: [
      'O saldo do imóvel será pago com **financiamento da Caixa Econômica Federal**, pelo Minha Casa Minha Vida, **depois que a obra ficar pronta**.',
      '**Quem aprova o financiamento é só a Caixa**, na data da assinatura. Para isso preciso estar **sem restrições no nome**, com renda compatível e dentro das regras do programa. A vendedora **não garante** a aprovação.',
      '**Dívidas com a própria Caixa** e dívidas de banco registradas no Banco Central podem impedir o financiamento **mesmo depois de pagas**.',
    ] },

    { t: 'h', text: '2. Minhas dívidas hoje' },
    { t: 'p', text: '(   )  **Não tenho** nenhuma restrição no nome.' },
    { t: 'p', text: '(   )  Tenho **somente** as restrições abaixo:' },
    { t: 'table', widths: [30, 26, 14, 14, 16], head: ['Credor', 'Tipo', 'Valor (R$)', 'Desde', 'Limpar até'], rows: [
      { cells: [' ', ' ', ' ', ' ', ' '] }, { cells: [' ', ' ', ' ', ' ', ' '] }, { cells: [' ', ' ', ' ', ' ', ' '] },
    ] },
    { t: 'small', text: 'Tipo: negativação (Serasa/SPC), protesto, banco, cheque ou governo. Esconder dívida ou informar errado é descumprimento deste Termo.' },

    { t: 'h', text: '3. Eu me comprometo a' },
    { t: 'numlist', items: [
      '**Limpar as dívidas acima até a data indicada** e entregar o comprovante de pagamento e da baixa.',
      '**Manter o nome limpo** até assinar o financiamento com a Caixa.',
      '**Avisar antes** de fazer empréstimo, financiamento (inclusive de carro), crediário, cartão novo ou ser fiador — e não comprometer mais de **35% da renda** da família com parcelas, contando a futura parcela da Caixa.',
      '**Pagar a entrada em dia.**',
      '**Avisar em até 15 dias** se mudar de emprego, renda, estado civil, endereço ou telefone.',
      '**Não comprar outro imóvel** nem fazer outro financiamento habitacional até receber as chaves.',
      '**Entregar os documentos** pedidos, inclusive o Registrato do Banco Central, em até 10 dias.',
    ] },

    { t: 'h', text: '4. Autorizo' },
    { t: 'p', text: 'A vendedora e o correspondente Caixa indicado por ela a **consultar meu nome** (Serasa, SPC, cartórios, Receita) e a enviar meus dados para a **análise de crédito da Caixa**, hoje e **periodicamente até o financiamento**, só para acompanhar a aprovação deste imóvel, conforme a LGPD (Lei 13.709/2018).' },

    { t: 'h', text: '5. Se aparecer restrição' },
    { t: 'steps', items: [
      { title: 'Aviso', body: 'por WhatsApp, e-mail ou carta' },
      { title: '30 dias', body: 'para limpar o nome' },
      { title: '+30 dias', body: 'último prazo, com reunião' },
      { title: 'Solução', body: 'outro comprador, unidade menor, mais entrada/FGTS ou cessão' },
    ] },
    { t: 'small', text: 'Faltando menos de 120 dias para as chaves, os prazos caem pela metade. Avisos para os contatos deste Termo são válidos: devo mantê-los atualizados.' },

    { t: 'h', text: '6. Se eu não cumprir' },
    { t: 'callout', color: 'red', text: 'Se eu descumprir este Termo e isso impedir o financiamento, **a culpa é minha (inadimplemento do comprador)** e o contrato pode ser desfeito conforme o **quadro-resumo** e a **Lei 13.786/2018** (Lei do Distrato). Se a vendedora tolerar algum atraso, isso não é renúncia aos seus direitos.' },

    { t: 'p', text: '**Li este Termo, tirei minhas dúvidas, recebi uma via e rubriquei todas as páginas.**' },
    { t: 'p', text: 'Local e data: ______________________________, ___/___/______' },
    { t: 'sign', names: [['Comprador(a) 1', 'CPF'], ['Comprador(a) 2', 'CPF'], ['Vendedora', 'CNPJ'], ['', ''], ['Testemunha 1', 'CPF'], ['Testemunha 2', 'CPF']] },
  ],
};

module.exports = { C, E, docs: [politica, termo] };
