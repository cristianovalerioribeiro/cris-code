#!/usr/bin/env python3
"""Escolhe as 30 construtoras com os dados de contato mais consistentes (nao
as maiores). Le dados/grupos.json (05_mapa_base.py) e, quando existe, a
pesquisa web (dados/v2/pesquisa, dados/pesquisa).

Consistente = site proprio que bate com o nome da empresa; e-mail no dominio do
site que nao e de contabilidade, juridico, fiscal ou DP, de preferencia usado
em mais de um CNPJ do grupo; telefone fixo proprio (nao se repete em outras
empresas) e usado em mais de um CNPJ; SPE aberta desde 2023 (esta ativa).
Saida: dados/v3/selecao30.json e dados/v3/candidatas.csv."""
import csv, json, re, sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from regionais_bh import norm

R = Path(__file__).resolve().parent.parent
G = json.load(open(R / "dados/grupos.json"))
OUT = R / "dados/v3"; OUT.mkdir(parents=True, exist_ok=True)

# dominios que a pesquisa mostrou nao serem da construtora
DOM_ERRADO = {"textobh.com.br", "legalizatec.com.br", "portoegomes.com.br", "workmaster.com.br", "nexpe.com.br",
              "btsproperties.com.br", "lafaete.com.br", "grupomunizrabelo.com.br", "sandropimenta.com.br"}
RUIM = re.compile(r"contab|contador|contabil|fiscal|jurid|advog|escritorio|\bdp\b|pessoal|folha|nfe?\b|notafiscal|"
                  r"cobranca|tributa|imposto|societario|legaliza|assessoria")
BOM = re.compile(r"contato|comercial|vendas|atendimento|novosnegocios|novos\.negocios|terreno|incorpora|diretoria|"
                 r"relacionamento|sac|faleconosco|marketing|projetos|engenharia|obras")
MEIO = re.compile(r"financeiro|adm|administrativo|compras|suprimentos|rh")

def carregar_web(g):
    for p in (R / "dados/v2/pesquisa", R / "dados/pesquisa"):
        for nome in (g["dominio"],):
            f = p / f"{nome}.json"
            if nome and f.exists():
                try: return json.load(open(f)), p.name
                except json.JSONDecodeError: pass
    return {}, ""

def parecido(a, b):
    """Erro de digitacao: mesmo tamanho +-1 e no maximo 1 letra diferente."""
    if a == b or abs(len(a) - len(b)) > 1: return False
    i = 0
    while i < min(len(a), len(b)) and a[i] == b[i]: i += 1
    return a[i + 1:] == b[i + 1:] or a[i + 1:] == b[i:] or a[i:] == b[i + 1:]

def classe_email(email):
    local = email.split("@")[0]
    if RUIM.search(local) or RUIM.search(email.split("@")[-1]): return "ruim"
    if BOM.search(local): return "bom"
    if MEIO.search(local): return "meio"
    return "nominal"

linhas = []
for g in G:
    if not g["ativo"] or g["gigante"] or not (3 <= g["n_spe"] <= 60): continue
    if not g["dominio"] or g["dominio"] in DOM_ERRADO: continue
    web, origem = carregar_web(g)
    site_web_errado = bool(web) and (web.get("site") or {}).get("confirmado") is False
    emails = [x for x in g["emails"] if x["classe"] == "dominio_proprio"]
    emails = [x for x in emails if not any(y is not x and y["n_cnpjs"] >= x["n_cnpjs"] and parecido(x["email"], y["email"]) for y in emails)]
    for x in emails: x["q"] = classe_email(x["email"])
    bons = [x for x in emails if x["q"] in ("bom", "nominal", "meio")]
    otimos = [x for x in emails if x["q"] == "bom"]
    fixos = [x for x in g["fones"] if x["classe"] == "proprio_receita" and x["tipo"] == "fixo"]
    # pesquisa web: contatos confirmados em publicacao da empresa
    em_web = [x for x in (web.get("emails") or []) if (x.get("confirmado_publicacao") or x.get("validado") == "confirmado")
              and not RUIM.search(str(x.get("email", "")))]
    fo_web = [x for x in (web.get("telefones") or []) if (x.get("confirmado_publicacao") or x.get("validado") == "confirmado")]
    enc = (web.get("aderencia") or web.get("aderencia_hadron") or {}).get("encaixe", "")

    p = 0.0
    p += 25                                                    # tem site proprio que bate com o nome
    p += 12 * min(1, len(bons) / 2) + 8 * bool(otimos)
    p += 6 * bool(any(x["n_cnpjs"] >= 2 for x in bons))        # mesmo e-mail em varios CNPJs = cadastro consistente
    p += 15 * bool(fixos) + 6 * bool(any(x["n_cnpjs"] >= 2 for x in fixos))
    p += 8 * min(1, g["spe_desde_2023"] / 3)
    p += 6 if g["segmento"] in ("Médio", "MCMV/econômico", "Misto") else 0
    p += 4 if (g["bairros_alvo_medio"] or g["bairros_alvo_leste"]) else 0
    p += 10 * bool(em_web) + 6 * bool(fo_web)
    p -= 6 * sum(1 for x in emails if x["q"] == "ruim") / max(1, len(emails))
    if enc in ("alto", "fora"): p -= 12
    if site_web_errado: p -= 30
    linhas.append(dict(gid=g["gid"], rank_base=g["rank"], nome=g["nome"], dominio=g["dominio"], segmento=g["segmento"],
                       n_spe=g["n_spe"], spe_desde_2023=g["spe_desde_2023"], emails_bons=[x["email"] for x in bons],
                       emails_otimos=[x["email"] for x in otimos], emails_descartados=[x["email"] for x in emails if x["q"] == "ruim"],
                       fixos=[x["numero"] for x in fixos], fixo_multi=any(x["n_cnpjs"] >= 2 for x in fixos),
                       web=origem, encaixe_web=enc, bairros_alvo=g["bairros_alvo_medio"] + g["bairros_alvo_leste"],
                       regionais=g["regionais"], score=round(p, 1)))

linhas.sort(key=lambda x: -x["score"])
# exige o minimo: e-mail utilizavel no dominio E telefone fixo proprio (Receita ou web)
aptas = [x for x in linhas if x["emails_bons"] and (x["fixos"] or x["web"])
         and x["spe_desde_2023"] >= 1 and x["encaixe_web"] not in ("alto", "fora")]
sel = aptas[:30]
json.dump(sel, open(OUT / "selecao30.json", "w"), ensure_ascii=False, indent=1)
with open(OUT / "candidatas.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f, delimiter=";"); w.writerow(["score", "nome", "dominio", "segmento", "n_spe", "spe_desde_2023", "emails_bons", "fixos", "web"])
    for x in linhas: w.writerow([x["score"], x["nome"], x["dominio"], x["segmento"], x["n_spe"], x["spe_desde_2023"],
                                 " | ".join(x["emails_bons"]), " | ".join(x["fixos"]), x["web"]])
print(f"avaliadas {len(linhas)} · aptas {len(aptas)} · selecionadas {len(sel)}")
for i, x in enumerate(sel, 1):
    print(f"{i:2} {x['score']:5} {x['nome'][:32]:32} {x['dominio'][:28]:28} {x['segmento'][:6]:6} spe={x['n_spe']:2} rec={x['spe_desde_2023']:2} "
          f"em={len(x['emails_bons'])} fx={len(x['fixos'])} web={x['web'] or '-':8} {x['encaixe_web']}")
