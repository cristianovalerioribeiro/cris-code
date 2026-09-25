// Conteúdo dos dois documentos, num formato neutro que render.js transforma em
// Word (.docx) e em HTML (que vira PDF). Negrito: **texto**.

const C = { navy: '1F3864', green: 'E2EFDA', yellow: 'FFF2CC', orange: 'FCE4D6', red: 'F8CBAD', blue: 'DDEBF7', gray: 'F2F2F2' };
const E = { green: '548235', yellow: 'BF9000', orange: 'C55A11', red: 'C00000', blue: '2F5597', gray: '7F7F7F' };

const politica = {
  file: 'Politica_de_Credito_MCMV',
  footer: 'Política de Crédito MCMV · v3',
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
        { color: 'orange', cells: ['Alta', 'R$ 3.001 a R$ 6.000', 'até 2 rendas', '**Não assina.** Reserva por 60 dias (sinal devolvido se o crédito não sair); assina só depois de quitar e nova análise Caixa.'] },
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
      { big: '35%', label: 'Nas chaves: Caixa + entrada + acordos + empréstimos + cartão. Dívidas de banco acima de 6 rendas: só com comitê', color: 'blue' },
    ] },

    { t: 'h', text: '6. A rotina, do atendimento às chaves' },
    { t: 'table', widths: [22, 78], head: ['Quando', 'O que fazer'], boldFirst: true,
      rows: [
        { cells: ['Atendimento', 'Perguntar: renda e como comprova · já teve imóvel/financiamento · dívidas e com quem · algo com a Caixa. Cliente gera o **Registrato** (Banco Central) no celular pelo gov.br.'] },
        { cells: ['Até 5 dias', 'Consulta Serasa/SPC + Registrato + **SICAQ** no correspondente Caixa. Classificar pelas seções 1 a 5.'] },
        { cells: ['Assinatura', 'Contrato + **Termo de Responsabilidade** com as dívidas e o prazo de cada uma. Entregar ao cliente o resultado da análise prévia. Assinado em estande ou fora da sede: respeitar os **7 dias de arrependimento**.'] },
        { color: 'gray', cells: ['Durante a obra', 'Com restrição: consulta **todo mês** até limpar, depois a cada 3 meses. Sem restrição: a cada **6 meses**. Atraso de mais de 15 dias na entrada: consulta na hora.'] },
        { color: 'gray', cells: ['Restrição nova', 'Aviso por escrito → **30 dias** → mais **30 dias** e reunião → comitê decide. Para desfazer o contrato: **notificação judicial ou por cartório (RTD) com 15 dias** para regularizar.'] },
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
    { t: 'small', text: 'Teto da carteira: no máximo 20% das unidades vendidas com Termo em aberto. A classificação é apoio: a decisão é sempre de uma pessoa, e o cliente pode pedir revisão (LGPD, art. 20).' },

    { t: 'h', text: '8. Cuidados jurídicos' },
    { t: 'bullets', items: [
      'Valores em reais são ponto de partida: calibrar após 50 repasses.',
      'Retenção no distrato: 25% sem afetação; até 50% com afetação, **em julgamento no STJ** (Temas 1.464 a 1.466) — projetar com 25%.',
    ] },
  ],
};

const { termo, parecer } = require('./termo_parecer');

module.exports = { C, E, docs: [politica, termo, parecer] };
