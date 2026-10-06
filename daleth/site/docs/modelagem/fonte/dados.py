# -*- coding: utf-8 -*-
import re, json
JS = open('/home/user/cris-code/daleth/site/assets/js/modelagem.js', encoding='utf-8').read()
FRENTES = []
for m in re.finditer(r'\{ id: "(\w+)", num: "(\d+)", nome: "([^"]+)", curto: "([^"]+)",\s*frase: "([^"]+)",\s*sub: \[(.*?)\],\s*move: \[(.*?)\]', JS, re.S):
    FRENTES.append(dict(id=m.group(1), num=m.group(2), nome=m.group(3), curto=m.group(4), frase=m.group(5),
                        sub=json.loads('['+m.group(6)+']'), move=json.loads('['+m.group(7)+']')))
POR_ID = {f['id']: f for f in FRENTES}
TUDO = FRENTES[0]; DEZ = FRENTES[1:]

# Texto de apoio por frente: o que está em jogo e a pergunta que a modelagem responde.
APOIO = {
 "terreno": ("A forma de acesso ao terreno define quem corre o risco e quando o caixa sai. Comprar à vista, permutar por unidades ou montar uma parceria são negócios diferentes sobre o mesmo lote.",
             "Qual forma de acesso ao terreno preserva caixa sem comprometer a segurança jurídica?"),
 "produto": ("O produto é a primeira decisão que muda todas as outras. Tipologia, mix e ticket definem o VGV, o custo e a velocidade de vendas.",
             "Que produto este terreno e este mercado absorvem no preço e no prazo que o negócio precisa?"),
 "tecnica": ("A solução técnica transforma o produto em custo e prazo. Implantação, sistema construtivo e fases determinam o orçamento e o cronograma que o caixa terá de suportar.",
             "Qual solução técnica entrega o produto com o custo e o prazo que o fluxo de caixa comporta?"),
 "juridico": ("Sem base jurídica, nenhuma frente se sustenta. Matrícula, licenças, memorial e contratos são o que permite registrar, financiar e vender.",
              "O empreendimento pode ser registrado, financiado e comercializado com segurança em cada etapa?"),
 "societario": ("A sociedade define quem decide, quem aporta e quem recebe. A escolha entre SPE, SCP e holding muda o risco, o tributo e o acesso ao capital.",
                "Que estrutura societária isola riscos, organiza aportes e distribui resultados com clareza?"),
 "tributario": ("O regime tributário acompanha a estrutura, não o contrário. RET, presumido ou real dependem do que foi decidido no societário, no comercial e no financeiro.",
                "Qual regime é mais eficiente e coerente com a forma como o negócio foi montado?"),
 "financeiro": ("Aqui todas as frentes aparecem em números. Fluxo de caixa, exposição e sensibilidade mostram se o empreendimento cria valor e aguenta seus riscos.",
                "Quanto capital o negócio exige, em que momento, e o que acontece se as premissas mudarem?"),
 "capital": ("Capital é meio, não fim. Capital próprio, sócios, investidor, banco e recebíveis entram em momentos diferentes, com custo e garantias diferentes.",
             "Que combinação de fontes financia a exposição do caixa com custo e risco compatíveis?"),
 "comercial": ("A comercialização transforma produto em receita e receita em caixa. Preço, tabela e velocidade de vendas decidem quanto capital externo o negócio pedirá.",
               "Que estratégia de vendas equilibra preço, velocidade e geração de caixa ao longo da obra?"),
 "risco": ("Toda estrutura distribui risco e retorno entre as partes. Garantias, covenants, preferências e waterfall dizem quem protege quem e em que ordem.",
           "Como proteção, exposição e remuneração ficam equilibradas entre empreendedor, investidores e financiadores?"),
}

CAMINHOS = [
 ("Vender", "Recebe à vista e sai no primeiro dia.", "Menor risco. Menor captura de valor."),
 ("Permutar", "Recebe unidades no lugar do preço.", "Assume risco de obra e de vendas. Caixa preservado."),
 ("Incorporar", "Assume o empreendimento inteiro.", "Maior captura de valor. Maior exposição."),
]
CADEIA = ["Produto", "Orçamento", "Caixa", "Capital", "Cronograma", "Vendas"]
MOVIMENTOS = [("01", "Mapear", "para compreender"), ("02", "Modelar", "para enxergar"),
              ("03", "Estruturar", "para tornar executável"), ("04", "Conduzir", "para funcionar")]
ENTREGA = [
 ("Premissas escritas", "Cada número do modelo tem origem declarada: mercado, custo, prazo, tributo e capital."),
 ("Caminhos lado a lado", "Dois ou três cenários comparados pelos mesmos critérios, não uma recomendação isolada."),
 ("Efeito no caixa", "Para cada caminho, a exposição máxima, o momento em que ela acontece e quem a financia."),
 ("Decisão registrada", "O caminho escolhido, o porquê e o que precisa estar pronto para a estruturação começar."),
]
SITE = "cristianovalerioribeiro.github.io/cris-code"
SLOGAN = "Ao seu lado na construção da sua história."
