#!/usr/bin/env python3
"""Mapa da base inteira (15.681 CNPJs de BH, Receita jul/2026).

1. Agrupa os CNPJs em grupos economicos: mesmo dominio de site (quando o
   dominio nao e de provedor ou de contador), mesma raiz de CNPJ, mesmo socio
   pessoa fisica ou holding da base. Socio PJ que e outra construtora vira
   "parceria", nao fusao (senao as SPEs em parceria juntam o mercado todo).
2. Para cada grupo: SPEs com bairro e regional (o endereco da SPE costuma ser
   o do terreno; quando coincide com a sede, a obra fica "local nao informado"),
   atividade por ano, todos os e-mails e telefones classificados, parceiros.
3. Pontua todos os grupos pelos criterios do grupo Hadron.

Saidas em dados/: grupos.json (todos), oportunidades.csv (ranking completo),
empreendimentos_base.csv (uma linha por SPE), contatos_base.csv."""
import csv, collections, json, math, re, sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import regionais_bh as RB
from regionais_bh import norm

AQUI = Path(__file__).resolve().parent.parent
BASE = Path("/home/user/construtoras-bh/data/input/construtoras_bh_2026-07_enriquecido.csv")
OUT = AQUI / "dados"

PROVEDORES = {"gmail.com", "hotmail.com", "yahoo.com.br", "yahoo.com", "uol.com.br", "terra.com.br",
              "bol.com.br", "outlook.com", "outlook.com.br", "uai.com.br", "veloxmail.com.br", "task.com.br",
              "appicenet.com.br", "csfonline.com.br", "ig.com.br", "globo.com", "live.com", "icloud.com",
              "msn.com", "hotmail.com.br", "oi.com.br", "superig.com.br", "globomail.com", "zipmail.com.br",
              "gamil.com", "terra.com", "portoegomes.com.br", "gmail.com.br", "yahoo.com.ar", "hotmai.com", "gmai.com", "outlook.com.pt"}
GENERICOS = {"construtora", "construcoes", "construcao", "engenharia", "eng", "grupo", "inc", "incorporadora",
             "empreendimentos", "imoveis", "imobiliaria", "realty", "urbanismo", "arquitetura", "br", "com", "mg", "bh"}
CAP_SOCIO = int(sys.argv[1]) if len(sys.argv) > 1 else 15   # socio PF presente em mais CNPJs que isso nao liga grupos
# Bairros da conversa do grupo (lista 1 = medio R$10-14 mil/m2; lista 2 = leste, economico)
ALVO_MEDIO = {"serra", "sion", "buritis", "dos buritis", "palmeiras", "estoril", "ouro preto", "paqueta",
              "jardim paqueta", "santa terezinha", "manacas", "engenho nogueira", "grajau", "nova suissa",
              "nova suica", "gameleira", "nova gameleira", "carmo sion"}
ALVO_LESTE = {"alto vera cruz", "boa vista", "pompeia", "sao geraldo", "esplanada", "taquaril", "saudade",
              "conjunto taquaril"}
ALTO_PADRAO = {"lourdes", "bairro de lourdes", "santo agostinho", "sto agostinho", "belvedere", "vila da serra",
               "funcionarios", "funcionario", "savassi", "bairro savassi", "mangabeiras", "vila paris",
               "sao bento", "santa lucia", "cidade jardim", "luxemburgo", "anchieta", "comiteco"}
PERIFERIA = {"Barreiro", "Venda Nova", "Norte", "Nordeste", "Leste"}
CNAE_SPE = {"4110700"}
GIGANTES = re.compile(r"\b(MRV|DIRECIONAL|CYRELA|PATRIMAR|EMCCAMP|TENDA|RIVA|VIC ENGENHARIA|CONATA|INFRACON|LCM)\b")

def raiz_dom(d):
    """'construtoraformula.com.br' -> 'formula'. Tira palavras genericas so no
    inicio/fim (tirar no meio estraga nomes: 'neocasaBRasil')."""
    r = re.sub(r"[^a-z0-9]", "", d.split(".")[0])
    mudou = True
    while mudou:
        mudou = False
        for w in sorted(GENERICOS, key=len, reverse=True):
            if len(r) > len(w) + 2 and r.startswith(w): r = r[len(w):]; mudou = True
            elif len(r) > len(w) + 2 and r.endswith(w): r = r[:-len(w)]; mudou = True
    return r

def dominio(site):
    return re.sub(r"^https?://(www\.)?", "", site or "").split("/")[0].lower()

def digitos(t):
    return re.sub(r"\D", "", t or "")

def tipo_fone(d):
    """d = so digitos com DDD. Movel: 9 digitos apos DDD, ou 8 comecando com 6-9."""
    local = d[2:]
    if len(local) == 9 or (len(local) == 8 and local[0] in "6789"):
        return "movel"
    return "fixo" if len(local) == 8 else "?"

def fmt_fone(d):
    return f"({d[:2]}) {d[2:-4]}-{d[-4:]}" if len(d) >= 10 else d

def socios_de(r):
    return [s.strip() for s in r["socios"].split("|") if s.strip()]

def eh_pj(nome):
    return bool(re.search(r"\b(LTDA|S/?A|S\.A\.?|EIRELI|PARTICIPA|EMPREEND|INCORPORA|ENGENHARIA|CONSTRU|HOLDING|"
                          r"INVESTIMENTOS|IMOBILIARI|SPE|ME|EPP|FUNDO|FII|CAPITAL)\b", nome))

def nome_empreendimento(razao):
    """'SPE OBRA 036 CONSTRUTORA SUDOESTE LTDA' -> nome limpo para listar."""
    n = re.sub(r"\b(LTDA\.?|S/?A|S\.A\.?|EIRELI|SPE|SCP|ME|EPP|EMPREENDIMENTOS?|IMOBILIARIOS?|IMOBILIARIAS?|"
               r"INCORPORACAO|INCORPORACOES|INCORPORADORA|PROPOSITO ESPECIFICO|SOCIEDADE DE|PARTICIPACOES|"
               r"CONSTRUCOES|CONSTRUTORA|ENGENHARIA|E\b|DE\b|DO\b|DA\b)", " ", razao)
    return re.sub(r"\s+", " ", n).strip(" -.") or razao

class UF:
    def __init__(s): s.p = {}
    def f(s, x):
        s.p.setdefault(x, x)
        while s.p[x] != x:
            s.p[x] = s.p[s.p[x]]; x = s.p[x]
        return x
    def u(s, a, b):
        a, b = s.f(a), s.f(b)
        if a != b: s.p[a] = b

def main():
    rows = list(csv.DictReader(open(BASE, encoding="utf-8-sig"), delimiter=";"))
    RB.preparar(r["bairro"] for r in rows)
    por_cnpj = {r["cnpj"]: r for r in rows}

    # ---- dominios validos: descarta provedor, contador (.cnt.br) e dominio "colcha de retalhos"
    dom_cnpjs = collections.defaultdict(list)
    for r in rows:
        d = dominio(r["site"])
        if d: dom_cnpjs[d].append(r)
    dom_invalido = {}
    for d, rs in dom_cnpjs.items():
        if (d in PROVEDORES or d.endswith((".cnt.br", ".adv.br", ".jus.br", ".gov.br"))
                or re.search(r"contab|contad|escritorio|assessoria|advog|imoveis|imobiliaria|corretor", d)):
            dom_invalido[d] = "provedor/contador"; continue
        if len(rs) >= 5:
            uf = UF()
            for r in rs:
                uf.f(r["cnpj"])
                for s in socios_de(r): uf.u(r["cnpj"], "S:" + s)
            maior = collections.Counter(uf.f(r["cnpj"]) for r in rs).most_common(1)[0][1]
            if maior / len(rs) < 0.5:
                dom_invalido[d] = f"socios sem relacao ({maior}/{len(rs)})"

    # ---- contatos repetidos em muitos "donos" diferentes = contador
    def dono(r):
        s = socios_de(r)
        return s[0] if s else r["cnpj"][:8]
    fone_donos, email_donos = collections.defaultdict(set), collections.defaultdict(set)
    for r in rows:
        f = digitos(r["telefone"])
        if len(f) >= 10: fone_donos[f].add(dono(r))
        if r["email"]: email_donos[r["email"].lower().strip()].add(dono(r))

    # ---- agrupamento em dois niveis (nao encadeia):
    # nivel 1: componentes por socio PF (ate CAP_SOCIO CNPJs) + raiz de CNPJ
    # nivel 2: cada CNPJ com site valido fica no grupo do site; os sem site vao para o
    #          site predominante do seu componente de socios (>=50% dos que tem site), senao
    #          o proprio componente vira o grupo. Dois sites nunca se fundem.
    razao_para_cnpj = {norm(r["razao_social"]): r["cnpj"] for r in rows if r["razao_social"]}
    grau = collections.Counter(s for r in rows for s in set(socios_de(r)))
    uf = UF()
    for r in rows:
        c = r["cnpj"]; uf.f(c); uf.u(c, "R:" + c[:8])
        for s in socios_de(r):
            if not eh_pj(s) and grau[s] <= CAP_SOCIO: uf.u(c, "S:" + s)
    comp_soc = collections.defaultdict(list)
    for r in rows: comp_soc[uf.f(r["cnpj"])].append(r)
    dom_ok = lambda r: (dominio(r["site"]) if dominio(r["site"]) and dominio(r["site"]) not in dom_invalido else "")
    dom_do_comp = {}
    for k, rs in comp_soc.items():
        ds = collections.Counter(dom_ok(r) for r in rs if dom_ok(r))
        if ds:
            d, n = ds.most_common(1)[0]
            if n / sum(ds.values()) >= 0.5: dom_do_comp[k] = d
    cnpj_grupo = {}
    for r in rows:
        d = dom_ok(r)
        k = uf.f(r["cnpj"])
        cnpj_grupo[r["cnpj"]] = "D:" + d if d else ("D:" + dom_do_comp[k] if k in dom_do_comp else "C:" + k)
    # SPE isolada cujo socio PJ e uma empresa da base: vai para o grupo dessa empresa
    tam = collections.Counter(cnpj_grupo.values())
    for r in rows:
        if tam[cnpj_grupo[r["cnpj"]]] > 1: continue
        alvos = {cnpj_grupo[razao_para_cnpj[norm(s)]] for s in socios_de(r) if eh_pj(s) and norm(s) in razao_para_cnpj}
        alvos.discard(cnpj_grupo[r["cnpj"]])
        if len(alvos) == 1: cnpj_grupo[r["cnpj"]] = next(iter(alvos))
    comp = collections.defaultdict(list)
    for r in rows: comp[cnpj_grupo[r["cnpj"]]].append(r)

    grupos = []
    for gid, rs in comp.items():
        g = resumir(rs, dom_invalido, fone_donos, email_donos, razao_para_cnpj, cnpj_grupo, por_cnpj)
        if g: grupos.append(g)
    # nome dos parceiros
    nome_grupo = {g["gid"]: g["nome"] for g in grupos}
    for g in grupos:
        g["parceiros"] = sorted({nome_grupo.get(p, "") for p in g.pop("_parc_gids")} - {""})[:8]
    grupos.sort(key=lambda g: -g["score"])
    for i, g in enumerate(grupos, 1): g["rank"] = i
    salvar(grupos)

def resumir(rs, dom_invalido, fone_donos, email_donos, razao_para_cnpj, cnpj_grupo, por_cnpj):
    gid = cnpj_grupo[rs[0]["cnpj"]]
    spes = [r for r in rs if r["cnae"] in CNAE_SPE or re.search(r"\bSPE\b|EMPREENDIMENTO|INCORPORA|RESIDENCIAL|EDIFICIO|CONDOMINIO", r["razao_social"])]
    if not spes and len(rs) < 3:
        return None
    # sede: CNPJ mais antigo que nao e SPE (ou o mais antigo de todos)
    nao_spe = [r for r in rs if r not in spes] or rs
    sede = min(nao_spe, key=lambda r: r["inicio_atividade"] or "9")
    doms = collections.Counter(dominio(r["site"]) for r in rs if r["site"] and dominio(r["site"]) not in dom_invalido)
    pj = collections.Counter(s for r in rs for s in socios_de(r) if eh_pj(s))
    pf = collections.Counter(s for r in rs for s in set(socios_de(r)) if not eh_pj(s))
    # o dominio so vale como "site da construtora" se o nome dele aparece nas razoes/fantasias do grupo
    compacto = re.sub(r"[^a-z0-9]", "", " ".join(norm(r["razao_social"] + r["nome_fantasia"]) for r in rs))
    def bate(d):
        r_ = raiz_dom(d)
        if len(r_) >= 3 and r_ in compacto:
            return True
        # site usado por 3+ CNPJs do mesmo grupo de socios tambem vale
        return sum(1 for r in rs if dominio(r["site"]) == d) >= 3
    doms_ok = [d for d, _ in doms.most_common() if bate(d)]
    dom_terceiro = [d for d, _ in doms.most_common() if d not in doms_ok]
    dom = doms_ok[0] if doms_ok else ""
    titulo = next((r["titulo_site"] for r in rs if dominio(r["site"]) == dom and r["titulo_site"]), "")
    # nome: a empresa cujo nome contem a raiz do site; senao a operacional mais antiga
    def operacional(r):
        return re.search(r"CONSTRU|ENGENHARIA|INCORPORA|EMPREENDIMENTOS|URBANISMO|EDIFICA", r["razao_social"]) and not re.search(r"\bSPE\b|\bSCP\b", r["razao_social"])
    cand = []
    if dom:
        raiz = raiz_dom(dom)
        cand = [r for r in rs if raiz and raiz in re.sub(r"[^a-z0-9]", "", norm(r["razao_social"] + r["nome_fantasia"]))]
    cand = cand or [r for r in rs if operacional(r)] or nao_spe
    ref = min(cand, key=lambda r: (not operacional(r), r["inicio_atividade"] or "9"))
    nome = ref["nome_fantasia"] or ref["razao_social"]

    # empreendimentos inferidos (SPEs)
    bairro_sede = norm(sede["bairro"])
    emps = []
    for r in sorted(spes, key=lambda r: r["inicio_atividade"], reverse=True):
        b = norm(r["bairro"])
        emps.append(dict(cnpj=r["cnpj"], nome=nome_empreendimento(r["razao_social"]), razao=r["razao_social"],
                         bairro=r["bairro"], regional=RB.regional(r["bairro"]), ano=r["inicio_atividade"][:4],
                         capital=float(r["capital_social"] or 0), mesmo_bairro_da_sede=(b == bairro_sede and len(spes) > 2)))
    locais = [e for e in emps if not e["mesmo_bairro_da_sede"]]
    reg = collections.Counter(e["regional"] for e in locais)
    bairros = collections.Counter(norm(e["bairro"]) for e in locais)
    anos = collections.Counter(e["ano"] for e in emps)
    recentes = sum(v for a, v in anos.items() if a >= "2023")
    n_loc = max(1, len(locais))
    sh_medio = sum(v for b, v in bairros.items() if b in ALVO_MEDIO) / n_loc
    sh_leste = sum(v for b, v in bairros.items() if b in ALVO_LESTE) / n_loc
    sh_alto = sum(v for b, v in bairros.items() if b in ALTO_PADRAO) / n_loc
    sh_perif = sum(v for r_, v in reg.items() if r_ in PERIFERIA) / n_loc

    # contatos
    emails, fones = {}, {}
    for r in rs:
        e = r["email"].lower().strip()
        if e:
            d = e.split("@")[-1]
            cls = ("contador" if len(email_donos[e]) >= 5 else
                   "provedor_generico" if d in PROVEDORES else
                   "dominio_proprio" if d in doms_ok else "outro_dominio")
            x = emails.setdefault(e, dict(email=e, classe=cls, n_cnpjs=0)); x["n_cnpjs"] += 1
        f = digitos(r["telefone"])
        if len(f) >= 10:
            x = fones.setdefault(f, dict(numero=fmt_fone(f), tipo=tipo_fone(f),
                                          classe="contador" if len(fone_donos[f]) >= 5 else "proprio_receita", n_cnpjs=0))
            x["n_cnpjs"] += 1
    emails = sorted(emails.values(), key=lambda x: (x["classe"] != "dominio_proprio", -x["n_cnpjs"]))
    fones = sorted(fones.values(), key=lambda x: (x["classe"] != "proprio_receita", x["tipo"] != "fixo", -x["n_cnpjs"]))

    # sinais do site (robo da base)
    padroes = collections.Counter(r["padrao"] for r in rs if r["padrao"])
    mcmv_site = any(r["usa_mcmv"] == "sim" for r in rs)
    insta = next((r["instagram"] for r in rs if r["instagram"]), "")
    parc = set()
    for r in rs:
        for s in socios_de(r):
            c = razao_para_cnpj.get(norm(s))
            if c and cnpj_grupo.get(c) != gid: parc.add(cnpj_grupo[c])
    gigante = len(spes) > 80 or bool(GIGANTES.search(" ".join(pj) + " " + nome))

    # segmento
    if mcmv_site or sh_perif >= 0.5 or "economico" in padroes: seg = "MCMV/econômico"
    elif sh_alto >= 0.6: seg = "Alto padrão"
    else: seg = "Médio"
    if (mcmv_site or sh_perif >= 0.3) and (sh_medio > 0 or {"medio", "medio_alto"} & set(padroes)): seg = "Misto"

    # pontuacao 0-100
    p = min(22, 5 * math.sqrt(len(spes)))
    p += min(14, 2.5 * recentes)
    p += 18 * min(1, sh_medio * 2) + 10 * min(1, sh_leste * 3)
    p += 10 if seg in ("MCMV/econômico", "Misto") else 0
    p += 6 if {"medio", "medio_alto"} & set(padroes) else 0
    p -= 14 * sh_alto
    p += 8 if dom else 0
    p += 3 if insta else 0
    p += 4 if any(e["classe"] == "dominio_proprio" for e in emails) else 0
    p += 4 if any(f["classe"] == "proprio_receita" and f["tipo"] == "fixo" for f in fones) else 0
    if gigante: p -= 20
    ativo = recentes > 0 or any(e["ano"] >= "2021" for e in emps)
    if not ativo: p -= 15

    return dict(gid=gid, nome=nome.strip(), razao_sede=sede["razao_social"], cnpj_sede=sede["cnpj"],
                bairro_sede=sede["bairro"], dominio=dom, titulo_site=titulo, instagram=insta,
                dominios_descartados=sorted({dominio(r["site"]) for r in rs if dominio(r["site"]) in dom_invalido} | set(dom_terceiro)),
                n_cnpj=len(rs), n_spe=len(spes), spe_desde_2023=recentes,
                spe_por_ano={a: anos[a] for a in sorted(anos) if a >= "2015"},
                regionais=dict(reg.most_common()), bairros_top=[b for b, _ in bairros.most_common(12)],
                bairros_alvo_medio=sorted(b for b in bairros if b in ALVO_MEDIO),
                bairros_alvo_leste=sorted(b for b in bairros if b in ALVO_LESTE),
                share_alvo_medio=round(sh_medio, 2), share_alto=round(sh_alto, 2), share_periferia=round(sh_perif, 2),
                padrao_site=";".join(padroes), mcmv_site=mcmv_site, segmento=seg, gigante=gigante, ativo=ativo,
                capital_total=round(sum(float(r["capital_social"] or 0) for r in rs)),
                socios_pf=[s for s, _ in pf.most_common(10)], socios_pj=[s for s, _ in pj.most_common(8)],
                emails=emails, fones=fones, empreendimentos=emps, _parc_gids=parc, score=round(p, 1))

def salvar(grupos):
    OUT.mkdir(exist_ok=True)
    json.dump(grupos, open(OUT / "grupos.json", "w"), ensure_ascii=False)
    cols = ["rank", "score", "nome", "segmento", "dominio", "n_spe", "spe_desde_2023", "share_alvo_medio",
            "share_alto", "share_periferia", "gigante", "ativo", "bairro_sede", "cnpj_sede"]
    with open(OUT / "oportunidades.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f, delimiter=";"); w.writerow(cols + ["regionais", "bairros_top", "emails_dominio", "fones_fixos_proprios", "socios_pf"])
        for g in grupos:
            w.writerow([g[c] for c in cols] + [
                " | ".join(f"{k}:{v}" for k, v in g["regionais"].items()), " | ".join(g["bairros_top"]),
                " | ".join(e["email"] for e in g["emails"] if e["classe"] == "dominio_proprio"),
                " | ".join(x["numero"] for x in g["fones"] if x["classe"] == "proprio_receita" and x["tipo"] == "fixo"),
                " | ".join(g["socios_pf"][:5])])
    with open(OUT / "empreendimentos_base.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f, delimiter=";"); w.writerow(["grupo", "rank", "cnpj", "empreendimento", "razao_social", "bairro", "regional", "ano", "capital", "bairro_igual_sede"])
        for g in grupos:
            for e in g["empreendimentos"]:
                w.writerow([g["nome"], g["rank"], e["cnpj"], e["nome"], e["razao"], e["bairro"], e["regional"], e["ano"], e["capital"], e["mesmo_bairro_da_sede"]])
    n = len(grupos)
    print(f"grupos com incorporacao: {n} | ativos: {sum(g['ativo'] for g in grupos)} | com site: {sum(bool(g['dominio']) for g in grupos)} "
          f"| gigantes: {sum(g['gigante'] for g in grupos)} | SPEs: {sum(g['n_spe'] for g in grupos)}")
    tam = sorted((g["n_cnpj"] for g in grupos), reverse=True)[:10]
    print("maiores grupos (n CNPJ):", tam)
    print(collections.Counter(g["segmento"] for g in grupos))
    for g in grupos[:60]:
        print(f"{g['rank']:3} {g['score']:5} {g['nome'][:34]:34} {g['segmento'][:6]:6} spe={g['n_spe']:3} rec={g['spe_desde_2023']:2} "
              f"medio={g['share_alvo_medio']:.2f} alto={g['share_alto']:.2f} per={g['share_periferia']:.2f} {g['dominio'][:24]}")

if __name__ == "__main__":
    main()
