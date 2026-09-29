"""Bairro de BH -> regional administrativa (aproximado, para agregacao).
Bairros ausentes ficam como "BH (sem regional)". Fonte: divisao das 9
regionais da PBH, montada a mao para os bairros que aparecem na base."""
import re
import unicodedata

_R = {
    "Centro-Sul": """savassi santa lucia lourdes centro santa efigenia funcionarios belvedere santo agostinho
        santo antonio sion serra barro preto cruzeiro luxemburgo sao pedro anchieta cidade jardim carmo sao bento
        mangabeiras coracao de jesus comiteco vila paris boa viagem sao lucas novo sao lucas carmo sion
        serra do curral vila da serra bairro de lourdes bairro savassi funcionario sto agostinho do carmo bairro carmo
        secao urbana quarta - boa viagem bairro praca 12 becentro""",
    "Oeste": """buritis dos buritis burutis estoril gutierrez prado calafate nova suissa nova suica grajau alpes palmeiras
        havai salgado filho barroca alto barroca nova granada jardim america betania cinquentenario madre gertrudes
        gameleira nova gameleira vista alegre cabana leonina marajo estrela dalva jardinopolis vila oeste oeste
        parque sao jose nova cintra santa sofia""",
    "Noroeste": """padre eustaquio padre eustauqio caicaras alto caicaras carlos prates ex colonia carlos prates
        coracao eucaristico dom bosco gloria novo gloria jardim montanhes jardim montanhez minas brasil monsenhor messias
        pedro ii santo andre sao salvador coqueiros california conjunto california conjunto california i ermelinda
        joao pinheiro dom cabral bonfim lagoinha aparecida aparecida setima secao pindorama nova cachoeirinha
        senhor dos passos sao cristovao bom jesus caicara adelaide caicara-adelaide caicara""",
    "Pampulha": """castelo ouro preto santa amelia itapoa itapua santa branca sta. branca sao luiz sao luiz (pampulha)
        sao jose (pampulha) liberdade jaragua santa rosa bandeirantes bandeirantes (pampulha) dona clara garcas braunas
        trevo vila trevo aeroporto paqueta jardim paqueta santa terezinha manacas engenho nogueira alipio de melo serrano
        urca enseada das garcas itatiaia sao francisco novo sao francisco jardim atlantico universitario suzana indaia
        pampulha jardim alvorada mineirao""",
    "Venda Nova": """venda nova santa monica novo santa monica ceu azul candelaria candelaria v nova
        sao joao batista (venda nova) sao joao batista parque sao joao batista piratininga piratininga (venda nova)
        piratininga venda nova jardim dos comerciarios jardim dos comerciarios (venda nova) j. comerciarios rio branco
        leticia mantiqueira europa minascaixa serra verde serra verde (venda nova) jardim leblon parque jardim leblon
        lagoinha leblon lagoinha leblon (venda nova) parque sao pedro maria helena cenaculo lagoa canaa""",
    "Norte": """planalto heliopolis sao bernardo vila cloris floramar jardim guanabara tupi tupi a tupi b novo tupi
        juliana primeiro de maio vila primeiro de maio minaslandia minaslandia (p maio) aarao reis novo aarao reis
        etelvina carneiro guarani jaqueline solimoes monte azul campo alegre lajedo providencia frei leopoldo
        jardim felicidade sao goncalo xodo marize""",
    "Nordeste": """cidade nova uniao sao paulo ipiranga silveira palmares sao gabriel cachoeirinha goiania nazare
        concordia fernao dias santa cruz dom joaquim nova floresta renascenca graca bairro da graca da graca
        jardim vitoria paulo vi conjunto paulo vi capitao eduardo ribeiro de abreu maria goretti vitoria ouro minas
        sao marcos eymard beira linha piraja""",
    "Leste": """floresta santa tereza santa teresa sta tereza sagrada familia esplanada pompeia saudade horto
        horto florestal paraiso alto vera cruz taquaril conjunto taquaril vera cruz sao geraldo boa vista casa branca
        santa ines nova vista pirineus mariano de abreu granja de freitas vila da paz colegio batista
        alto coleg. batista""",
    "Barreiro": """barreiro bairro do barreiro barreiro de baixo barrreiro de baixo barreiro de cima milionarios
        milionarios (barreiro) diamante diamante (barreiro) santa helena (barreiro) lindeia lindeia (barreiro) tirol
        tirol (barreiro) cardoso cardoso (barreiro) jatoba cdi jatoba cdi jatoba (barreiro) distrito industrial do jatoba
        vale do jatoba vale do jatoba (barreiro) conjunto habitacional vale do jatoba (barreiro) brasil industrial
        brasil industrial (barreiro) miramar miramar (barreiro) das industrias das industrias i (barreiro)
        bairro das industrias i bairro das industrias ii industrias i (barreiro) novo das industrias (barreiro)
        bairro novo das industrias teixeira dias teixeira dias (barreiro) santa margarida santa margarida (barreiro)
        bonsucesso bonsucesso (barreiro) castanheira castanheira (barreiro) olhos d'agua olhos dagua mangueiras
        mangueiras (barreiro) petropolis petropolis (barreiro) solar do barreiro solar do barreiro (barreiro) itaipu
        itaipu (barreiro) flavio marques lisboa flavio marques lisboa (barreiro) independencia santa rita (barreiro)
        conjunto tunel ibirite (barreiro) tunel de ibirite ademar maldonado conjunto ademar maldonado (barreiro) regina
        atila de paiva marilandia vila pinho vila pinho (vale do jatoba) santa cecilia novo santa cecilia pilar
        jardim do vale""",
}

def norm(s):
    s = unicodedata.normalize("NFKD", s or "").encode("ascii", "ignore").decode().lower()
    return re.sub(r"\s+", " ", s).strip()

# Casos ambiguos resolvidos a mao (o nome curto tambem aparece dentro de outro bairro).
_FIXOS = {"sao jose": "Pampulha", "santa helena": "Barreiro", "santa monica": "Venda Nova"}
_MAPA = {}

def preparar(bairros):
    """Classifica de uma vez todos os bairros da base (nomes normalizados).
    O nome precisa aparecer inteiro, entre espacos, no texto da regional."""
    _MAPA.clear()
    textos = {reg: " " + norm(txt) + " " for reg, txt in _R.items()}
    for b in {norm(x) for x in bairros}:
        if b in _FIXOS:
            _MAPA[b] = _FIXOS[b]
            continue
        for reg, txt in textos.items():
            if f" {b} " in txt:
                _MAPA[b] = reg
                break

def regional(bairro):
    return _MAPA.get(norm(bairro), "BH (sem regional)")
