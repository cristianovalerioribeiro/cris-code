#!/usr/bin/env python3
"""Agrupa os CNPJs da base por dominio do site (= grupo economico), detecta
contatos de contador/provedor e pontua cada grupo pelos criterios do grupo
Hadron. Saida: dados/candidatas.csv (todas) e dados/top100.json."""
import csv, collections, json, re, sys, unicodedata
from pathlib import Path

BASE = Path(sys.argv[1] if len(sys.argv) > 1 else
            "/home/user/construtoras-bh/data/input/construtoras_bh_2026-07_enriquecido.csv")
OUT = Path(__file__).resolve().parent.parent / "dados"

BAIRROS_ALVO = {"serra", "sion", "buritis", "palmeiras", "estoril", "ouro preto", "paqueta",
                "santa terezinha", "manacas", "engenho nogueira", "grajau", "nova suica",
                "gameleira", "alto vera cruz", "boa vista", "pompeia", "sao geraldo",
                "esplanada", "taquaril", "saudade", "cidade nova"}
# "sion" e "prado" ficam de fora: o extrator da base casa substring
# ("profisSIONal", "comPRADO"), entao a citacao desses dois nao e confiavel.
BAIRROS_ALVO -= {"sion"}
CIDADES_MCMV = {"contagem", "betim", "ribeirao das neves", "belo horizonte"}
PROVEDORES = {"gmail.com", "hotmail.com", "yahoo.com.br", "uol.com.br", "terra.com.br",
              "bol.com.br", "outlook.com", "uai.com.br", "veloxmail.com.br", "task.com.br",
              "appicenet.com.br", "csfonline.com.br", "ig.com.br", "globo.com", "live.com"}
CNAE_OBRA = {"4110700", "4120400", "4211101", "4292802", "4299599", "4321500", "4330499"}

def norm(s):
    s = unicodedata.normalize("NFKD", s or "").encode("ascii", "ignore").decode().lower()
    return re.sub(r"\s+", " ", s).strip()

def dominio(site):
    return re.sub(r"^https?://(www\.)?", "", site or "").split("/")[0].lower()

def fone(t):
    d = re.sub(r"\D", "", t or "")
    return d if len(d) >= 10 else ""

rows = list(csv.DictReader(open(BASE, encoding="utf-8-sig"), delimiter=";"))

# 1) contatos repetidos na base inteira: quantos grupos (dominios/raizes) distintos usam cada fone/e-mail
fone_grupos = collections.defaultdict(set)
email_grupos = collections.defaultdict(set)
for r in rows:
    g = dominio(r["site"]) or r["cnpj"][:8]
    if fone(r["telefone"]): fone_grupos[fone(r["telefone"])].add(g)
    if r["email"]: email_grupos[r["email"].lower()].add(g)

grupos = collections.defaultdict(list)
for r in rows:
    d = dominio(r["site"])
    if d and d not in PROVEDORES and not d.endswith(".cnt.br"):
        grupos[d].append(r)

saida = []
for d, rs in grupos.items():
    socios = collections.Counter()
    for r in rs:
        for s in {x.strip() for x in r["socios"].split("|") if x.strip()}:
            socios[s] += 1
    top_socio, top_n = (socios.most_common(1)[0] if socios else ("", 0))
    coesao = top_n / len(rs)          # fracao de CNPJs com o socio mais comum
    nomes = " ".join(norm(r["razao_social"] + " " + r["nome_fantasia"]) for r in rs)
    titulo = norm(next((r["titulo_site"] for r in rs if r["titulo_site"]), ""))
    raiz = norm(d.split(".")[0])
    site_bate = bool(raiz) and (raiz[:5] in nomes.replace(" ", "") or
                                any(t in raiz for t in titulo.split() if len(t) > 3))
    regioes = collections.Counter(x for r in rs for x in r["regioes_citadas"].split(";") if x)
    padroes = collections.Counter(r["padrao"] for r in rs if r["padrao"])
    tip = collections.Counter(x for r in rs for x in r["tipologias"].split(";") if x)
    mcmv = any(r["usa_mcmv"] == "sim" for r in rs)
    n_spe = sum(1 for r in rs if "SPE" in r["razao_social"] or r["cnae"] == "4110700")
    obra = sum(1 for r in rs if r["cnae"] in CNAE_OBRA)
    recentes = sum(1 for r in rs if r["inicio_atividade"][:4] >= "2023")
    qtd_emp = max((int(r["qtd_empreendimentos"]) for r in rs if r["qtd_empreendimentos"].isdigit()), default=0)
    insta = next((r["instagram"] for r in rs if r["instagram"]), "")
    matriz = min(rs, key=lambda r: r["inicio_atividade"] or "9")
    fones = collections.Counter(fone(r["telefone"]) for r in rs if fone(r["telefone"]))
    fones_ok = [f for f, _ in fones.most_common() if len(fone_grupos[f]) <= 2]
    fones_contador = [f for f in fones if len(fone_grupos[f]) >= 5]
    emails = collections.Counter(r["email"].lower() for r in rs if r["email"])
    emails_dom = [e for e, _ in emails.most_common() if e.endswith("@" + d)]
    emails_contador = [e for e in emails if len(email_grupos[e]) >= 5]
    capital = sum(float(r["capital_social"] or 0) for r in rs)
    alvo = sorted(set(regioes) & BAIRROS_ALVO)
    cidades = sorted(set(regioes) & CIDADES_MCMV)

    # --- pontuacao (0-100) ---
    p = 0
    p += min(25, 6 * (n_spe ** 0.5))                    # volume de SPEs = lancamentos
    p += min(10, recentes * 2)                          # abriu SPE desde 2023 = lancando agora
    so_alto = padroes and set(padroes) == {"alto"}
    if mcmv or "economico" in padroes: p += 12
    if {"medio", "medio_alto"} & set(padroes): p += 12
    if so_alto: p -= 4                                  # "nenhum dos nossos projetos e de alto padrao"
    p += min(12, 4 * len(alvo)) + (6 if cidades and mcmv else 0)
    if site_bate: p += 10
    if insta: p += 5
    if tip.get("apartamento"): p += 5
    p += min(8, qtd_emp / 3)
    if coesao >= 0.5: p += 5
    if fones_ok: p += 3
    if emails_dom: p += 3
    gigante = n_spe > 80
    if gigante: p -= 15                                 # tem projeto interno; nao e o alvo
    saida.append(dict(
        dominio=d, nome=(matriz["nome_fantasia"] or matriz["razao_social"]), titulo_site=titulo,
        cnpj_matriz=matriz["cnpj"], razao_matriz=matriz["razao_social"], n_cnpj=len(rs),
        n_spe=n_spe, spe_desde_2023=recentes, coesao_socios=round(coesao, 2), site_bate_nome=site_bate,
        padrao=";".join(padroes), mcmv=mcmv, tipologias=";".join(t for t, _ in tip.most_common(4)),
        bairros_alvo=";".join(alvo), cidades=";".join(cidades),
        regioes=";".join(x for x, _ in regioes.most_common(8)), qtd_empreendimentos_site=qtd_emp,
        instagram=insta, capital_total=round(capital), socios_top=" | ".join(s for s, _ in socios.most_common(6)),
        fones_proprios=";".join(fones_ok[:3]), fones_contador=";".join(fones_contador[:3]),
        emails_dominio=";".join(emails_dom[:3]), emails_contador=";".join(emails_contador[:3]),
        gigante=gigante, score=round(p, 1)))

# grupos que parecem contador/provedor: muitos CNPJs, socios sem relacao, site nao bate
for s in saida:
    s["suspeita_contador"] = s["n_cnpj"] >= 8 and s["coesao_socios"] < 0.2 and not s["site_bate_nome"]
saida.sort(key=lambda s: -s["score"])
OUT.mkdir(exist_ok=True)
with open(OUT / "candidatas.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=list(saida[0]), delimiter=";")
    w.writeheader(); w.writerows(saida)
top = [s for s in saida if not s["suspeita_contador"] and s["site_bate_nome"]][:100]
json.dump(top, open(OUT / "top100.json", "w"), ensure_ascii=False, indent=1)
print(f"grupos={len(saida)} suspeita_contador={sum(s['suspeita_contador'] for s in saida)} "
      f"site_bate={sum(s['site_bate_nome'] for s in saida)} top100={len(top)}")
print(f"fones da base usados por >=5 grupos (contador provavel): {sum(1 for v in fone_grupos.values() if len(v)>=5)}")
print(f"e-mails da base usados por >=5 grupos: {sum(1 for v in email_grupos.values() if len(v)>=5)}")
for s in top[:100]:
    print(f"{s['score']:5} {s['dominio'][:28]:28} {s['nome'][:30]:30} spe={s['n_spe']:3} rec={s['spe_desde_2023']:2} {s['padrao'][:22]:22} mcmv={int(s['mcmv'])} alvo={s['bairros_alvo'][:30]} ig={'s' if s['instagram'] else '-'}")
