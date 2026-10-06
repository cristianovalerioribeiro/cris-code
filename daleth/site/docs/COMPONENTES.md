# Componentes do site DALETH (para quem escreve páginas)

Cada página é `paginas/NN-nome.html`: um bloco `<!--meta {...} -->` em JSON no topo e, abaixo, só o
conteúdo do `<main>`. Cabeçalho, slogan, migalhas, fecho, rodapé, SEO e dados estruturados são
gerados pelo `build.py`. Não edite `build.py`, `assets/` nem páginas de outra pessoa.

Gerar e conferir: `python3 build.py --local && python3 qa/qa.py`.

## Metadados

```json
{
  "caminho": "/empreendimentos/estudo-de-viabilidade/",
  "titulo": "Estudo de viabilidade de incorporação",      // até ~50 caracteres; o build soma " · DALETH"
  "sem_sufixo": false,                                       // true se o título já tem DALETH
  "descricao": "até 155 caracteres, linguagem do cliente",
  "migalhas": [["Empreendimentos", "/empreendimentos/"], ["Estudo de viabilidade", "/empreendimentos/estudo-de-viabilidade/"]],
  "servico": "Nome do serviço para o schema (opcional)",
  "momento": "empresa|terreno|empreendimento|capital|investidor|obra-parada|estudando",  // pré-seleciona o contato
  "scripts": ["ferramentas.js"],                             // só se usar o simulador
  "noindex": false,
  "fecho": {"rotulo": "…", "titulo": "frase própria da página", "texto": "1–2 frases",
            "botao": "Falar sobre …", "secundario": ["/url/", "texto do link"], "garantias": false}
}
```

O fecho é o bloco marinho do fim. **Cada página tem título de fecho próprio.** A frase
"Devolvemos uma primeira leitura e, se fizer sentido, a proposta do diagnóstico" é reservada a
/como-comeca/ e /contato/.

## Blocos (copie a estrutura)

**Abertura** (sempre a primeira seção de página interna; o índice "Nesta página" é automático):
```html
<section class="abertura"><div class="wrap">
  <p class="rotulo">Vertente · Assunto</p>
  <h1>Título de consequência, até 2 linhas</h1>
  <p class="lead">Uma ou duas frases.</p>
  <div class="acoes">
    <a class="btn btn-primario" href="/contato/?momento=terreno&amp;origem=pagina-abertura">Falar sobre…</a>
    <a class="link" href="#ancora">Ação secundária</a>
  </div>
  <p class="microcopy">O primeiro passo é uma conversa de enquadramento, sem custo.</p>
</div></section>
```

**Seção padrão em duas colunas** (título à esquerda, conteúdo à direita). Use `class="secao"`
ou `class="secao papel"` (fundo claro) alternando. No máximo UMA `secao escura` por página.
Todo `h2` precisa de `id` (vira o índice da página).
```html
<section class="secao" aria-labelledby="x-t"><div class="wrap duas-colunas">
  <div><p class="rotulo">Rótulo curto</p><h2 id="x-t">Título</h2><p class="lead">opcional</p></div>
  <div> … conteúdo … </div>
</div></section>
```
`duas-colunas solto` = a coluna da esquerda não fica fixa (use quando ela tem botão).

**Seção de uma coluna:** `<div class="wrap"><div class="cabeca"><p class="rotulo">…</p><h2 id="…">…</h2><p class="lead">…</p></div> … </div>`

**Conteúdo disponível:**
- Lista com fio: `<ul class="itens"><li><strong>Termo.</strong> <span>explicação</span></li></ul>` (`itens duas` = 2 colunas)
- Lista com traço: `<ul class="lista-traco"><li>…</li></ul>`
- Linhas que levam a outra página: `<div class="linhas-link"><a href="/x/"><span class="t">Título</span><span class="d">detalhe</span></a></div>`
- Itens lado a lado sem caixa: `<div class="grade g2|g3|g4"><div class="cartao"><h3>…</h3><p>…</p></div></div>`
- Passos numerados: `<ol class="passos dois|quatro"><li class="passo"><span class="etiqueta">Sem custo</span><h3>…</h3><p>…</p></li></ol>`
- Método em lista: `<ol class="movimentos-lista"><li><b>Mapear</b> …</li><li class="central"><b>Modelar</b> …</li>…</ol>`
- Frase de destaque: `<p class="destaque-frase">…</p>` · Nota: `<p class="nota">…</p>` · Apoio: `<p class="apoio">…</p>`
- Perguntas frequentes (no máximo 4–5): `<div class="faqs"><details class="faq"><summary>Pergunta?</summary><p>Resposta.</p></details></div>`
- Gráfico de alternativas calculado (o MODELAR): escreva `{{QUADRO}}` sozinho numa coluna.
- Tabela comparativa: copie a estrutura de `paginas/21-terreno.html` (`tabela-rolagem` + `comparador`, com `data-rot` em cada `<td>`).
- "Para continuar": `<p class="continuar">Para continuar: <a href="…">…</a>, <a href="…">…</a>.</p>`

**Artigo de Inteligência:** abertura com `rotulo` "Inteligência · Tema", depois
`<section class="secao"><div class="wrap"><article class="artigo"> … h2/h3/p/ul … </article></div></section>`.
`.artigo` limita a medida de leitura. Termine com links para 1 serviço + 1 ferramenta.

**Cena 3D** (`assets/js/cena3d.js`): `<canvas data-cena="heroi|jornada|rede|modelagem" data-rotulos="A|B|C…">` dentro de um
contêiner com `<div class="cena-rotulos"></div>`. A cena `modelagem` aceita até 9 rótulos e troca-os em tempo real
com `canvas.cena3d.rotular([...])`; é a base da página /metodo/modelagem/ (`assets/js/modelagem.js`).

## Regras inegociáveis (o QA procura estes termos)

- Slogan "Ao seu lado na construção da sua história." já sai no topo; não repita no corpo.
- Nunca: preço, faixa, remuneração, mensalidade, êxito; prometer aprovação de crédito, captação ou
  retorno; "parecer assinado", laudo, veredito; "assumimos a execução" (a DALETH conduz, verifica,
  cobra o combinado e corrige a rota); "Setup de Estruturação"; "cobramos do cliente, nunca do banco";
  nada religioso ou esotérico; nunca inventar caso, número, depoimento, prazo ou cliente.
- Regra-mãe: partir da ambição do cliente, não da deficiência. Não diminuir o cliente.
- Evitar frases que colidem com concorrentes: "Ficamos até funcionar", "Potencial não basta",
  "Um empreendimento começa antes da obra".
- GERIC: não definir nem usar a sigla (a definição é do Cristiano). Use "análise de risco do banco".
- Termos técnicos (SPE, SCP, RET, SBPE, patrimônio de afetação) explicados na primeira vez; nada de
  número de alíquota, regra ou norma que você não possa sustentar. Na dúvida, descreva o efeito e diga
  que depende do caso.
- Tom: claro, sereno, próximo, "você". Sem exclamação, sem emoji. Frases curtas. Menos texto.
