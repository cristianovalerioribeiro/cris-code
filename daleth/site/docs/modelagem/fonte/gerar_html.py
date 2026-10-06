# -*- coding: utf-8 -*-
import dados as D, html
e = html.escape
def chips(lst, cls=""): return '<div class="chips %s">%s</div>' % (cls, ''.join('<span>%s</span>' % e(s) for s in lst))
def nome(id_): return D.POR_ID[id_]['nome']

paginas = []
# 1 · Capa
paginas.append(f'''
<section class="pagina capa">
  <img class="fundo" src="img/capa.jpg" alt="">
  <div class="veu"></div>
  <img class="marca" src="horizontal-negative.svg" alt="DALETH">
  <div class="capa-texto">
    <p class="rotulo">Método DALETH · 02 · Modelar</p>
    <h1>Modelagem do<br>empreendimento</h1>
    <p class="lead">Dez frentes, uma decisão. Mudar uma muda as outras.<br>Por isso modelamos antes de escolher.</p>
  </div>
  <p class="capa-pe">Estruturação de Negócios Imobiliários · Belo Horizonte · atuação nacional</p>
</section>''')

# 2 · O que é modelar
mov = ''.join(f'<div class="mov {"ativo" if n=="02" else ""}"><span class="n">{n}</span><strong>{v}</strong><span class="p">{p}</span></div>' for n,v,p in D.MOVIMENTOS)
cam = ''.join(f'<div class="cam"><strong>{e(t)}</strong><p>{e(a)}</p><p class="apoio">{e(b)}</p></div>' for t,a,b in D.CAMINHOS)
cad = '<span class="seta">→</span>'.join(f'<span>{e(c)}</span>' for c in D.CADEIA)
paginas.append(f'''
<section class="pagina clara">
  <header class="topo"><span>Modelagem do empreendimento</span><span>O que é modelar</span></header>
  <p class="rotulo">O segundo movimento do método</p>
  <h2>Modelar é colocar os caminhos lado a lado, com premissas escritas, antes de comprometer capital.</h2>
  <div class="movimentos">{mov}</div>
  <p class="lead">Mapeamos para compreender, modelamos para enxergar, estruturamos para tornar executável, sustentamos para funcionar. Modelar é o movimento que muda o resultado: é quando o empreendimento ainda cabe inteiro numa planilha e qualquer decisão custa pouco para ser revista.</p>
  <h3>O mesmo terreno gera negócios diferentes</h3>
  <p>Vender, permutar ou incorporar. Uma torre ou duas fases. SPE ou SCP. Crédito de obra ou investidor. Cada escolha move as outras, e todas aparecem no caixa. Comparamos os caminhos pelos mesmos critérios antes de escolher um.</p>
  <div class="caminhos">{cam}</div>
  <h3>Cada decisão muda a seguinte</h3>
  <div class="cadeia">{cad}</div>
  <p class="apoio">O produto define o orçamento. O orçamento define o caixa. O caixa define o capital necessário, que define o cronograma, que define as vendas. Modelar é enxergar essa cadeia antes que ela aconteça.</p>
  <footer class="pe"><span>DALETH</span><span class="num">02</span></footer>
</section>''')

# 3 · Tudo conectado
legenda = ''.join(f'<li class="vt"><b>{e(v)}</b><small>{e(d)}</small></li>' + ''.join(f'<li><span class="n">{D.POR_ID[i]["num"]}</span>{e(D.POR_ID[i]["nome"])}</li>' for i in ids) for v,d,ids in D.VERTENTES)
paginas.append(f'''
<section class="pagina clara">
  <header class="topo"><span>Modelagem do empreendimento</span><span>O conceito visual</span></header>
  <p class="rotulo">Tudo conectado</p>
  <h2>Um empreendimento se decide em dez frentes ao mesmo tempo.</h2>
  <figure class="prancha"><img src="img/tudo.jpg" alt="Rede tridimensional com dez frentes ligadas ao empreendimento"></figure>
  <div class="duas">
    <div>
      <h3>Como ler a imagem</h3>
      <p>No centro, o empreendimento. Em volta, uma rede: cada ponto é uma decisão, cada linha é uma consequência. Nenhuma frente está isolada. Puxar uma delas desloca as vizinhas, e o efeito chega ao caixa.</p>
      <p>As dez frentes se agrupam em três vertentes: empreendimento, empresa e capital. O projeto costuma ficar com o arquiteto, a empresa com o contador, o capital com o banco. Estruturar é decidir as três de uma vez.</p>
      <p>Nas páginas seguintes, a rede troca de palavras a cada frente: as decisões que ela carrega e as outras frentes que ela move.</p>
    </div>
    <ol class="legenda-frentes">{legenda}</ol>
  </div>
  <footer class="pe"><span>DALETH</span><span class="num">03</span></footer>
</section>''')

# 4–13 · Frentes
for i, f in enumerate(D.DEZ):
    apoio, pergunta = D.APOIO[f['id']]
    move = ' · '.join(e(nome(m)) for m in f['move'])
    trilho = ''.join('<span class="%s"><b>%s</b>%s</span>' % ('ativo' if g['id']==f['id'] else ('move' if g['id'] in f['move'] else ''), g['num'], e(g['curto'])) for g in D.DEZ)
    paginas.append(f'''
<section class="pagina frente">
  <div class="banda"><img src="img/{f['id']}.jpg" alt=""><div class="banda-veu"></div>
    <p class="banda-rotulo">Frente {f['num']} de 10</p>
  </div>
  <div class="corpo">
    <div class="titulo"><span class="num-grande">{f['num']}</span><div><p class="rotulo">Frente</p><h2>{e(f['nome'])}</h2></div></div>
    <p class="frase">{e(f['frase'])}</p>
    <div class="duas">
      <div>
        <h4>O que está em jogo</h4>
        <p>{e(apoio)}</p>
        <h4>A pergunta que a modelagem responde</h4>
        <p class="pergunta">{e(pergunta)}</p>
      </div>
      <div>
        <h4>Decisões desta frente</h4>
        {chips(f['sub'])}
        <h4>Também move</h4>
        <p class="move">{move}</p>
      </div>
    </div>
  </div>
  <div class="trilho">{trilho}</div>
  <footer class="pe"><span>DALETH</span><span class="num">{i+4:02d}</span></footer>
</section>''')

# 14 · Mapa de conexões
linhas = ''
for f in D.DEZ:
    cels = ''.join('<td class="%s">%s</td>' % ('eu' if g['id']==f['id'] else ('sim' if g['id'] in f['move'] else ''), '●' if g['id'] in f['move'] else '') for g in D.DEZ)
    linhas += f'<tr><th><span class="n">{f["num"]}</span>{e(f["nome"])}</th>{cels}</tr>'
cab = ''.join(f'<th><span>{e(g["curto"])}</span></th>' for g in D.DEZ)
paginas.append(f'''
<section class="pagina clara">
  <header class="topo"><span>Modelagem do empreendimento</span><span>Mapa de conexões</span></header>
  <p class="rotulo">Quem move quem</p>
  <h2>Nenhuma frente se decide sozinha.</h2>
  <p class="lead">Cada linha mostra as frentes que uma decisão move primeiro. Terreno puxa produto, jurídico e capital. Societário puxa tributário, risco e capital. O financeiro recebe quase todas.</p>
  <table class="mapa"><thead><tr><th></th>{cab}</tr></thead><tbody>{linhas}</tbody></table>
  <p class="legenda">Leitura: a frente da linha move as frentes marcadas na coluna. As conexões indicadas são as primeiras, não as únicas: na modelagem, todas chegam ao caixa.</p>
  <div class="leituras">
    <div><strong>O financeiro recebe quase tudo</strong><p>Produto, técnica, tributário, funding e comercialização desembocam no fluxo de caixa. É onde as frentes viram números comparáveis.</p></div>
    <div><strong>Um triângulo de estrutura</strong><p>Jurídico, societário e capital se movem juntos. A forma da sociedade define o que pode ser contratado, financiado e garantido.</p></div>
    <div><strong>O terreno é o ponto de partida</strong><p>A forma de acesso ao terreno já escolhe produto, base jurídica e necessidade de capital. Modelar começa ali.</p></div>
  </div>
  <footer class="pe"><span>DALETH</span><span class="num">14</span></footer>
</section>''')

# 15 · O que entrega + convite
ent = ''.join(f'<div class="ent"><strong>{e(t)}</strong><p>{e(d)}</p></div>' for t,d in D.ENTREGA)
paginas.append(f'''
<section class="pagina escura">
  <header class="topo"><span>Modelagem do empreendimento</span><span>O que a modelagem entrega</span></header>
  <p class="rotulo">Do mapa ao seu caso</p>
  <h2>Modelar é o que separa uma oportunidade de uma decisão.</h2>
  <div class="entregas">{ent}</div>
  <div class="papeis"><p>{e(D.PAPEIS)}</p></div>
  <div class="convite">
    <h3>Modelar o seu empreendimento começa com uma conversa</h3>
    <p>Conte o terreno, o produto ou a empresa. A primeira conversa é de enquadramento, sem custo, e já mostra por quais frentes o seu caso pede para começar.</p>
    <p class="site">{D.SITE}/metodo/modelagem/</p>
  </div>
  <div class="assinatura"><img src="horizontal-negative.svg" alt="DALETH"><p>{e(D.SLOGAN)}</p></div>
  <footer class="pe"><span>DALETH</span><span class="num">15</span></footer>
</section>''')

CSS = open('doc.css', encoding='utf-8').read()
open('doc.html','w',encoding='utf-8').write(f'''<!doctype html><html lang="pt-BR"><head><meta charset="utf-8">
<title>DALETH · Modelagem do empreendimento</title><style>{CSS}</style></head><body>{''.join(paginas)}</body></html>''')
print('ok', len(paginas), 'páginas')
