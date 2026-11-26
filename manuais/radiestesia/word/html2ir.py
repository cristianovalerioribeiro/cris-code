# -*- coding: utf-8 -*-
"""HTML final do manual (pages/livro_final.html) → estrutura intermediária (word/ir.json) para o gerador Word.
Falha em voz alta diante de qualquer construção não mapeada."""
import re, json, os, sys
from bs4 import BeautifulSoup, NavigableString, Tag
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
src = sys.argv[1] if len(sys.argv) > 1 else os.path.join(ROOT, "pages", "livro_final.html")
html = open(src, encoding="utf-8").read()
soup = BeautifulSoup(html, "html.parser")
body = soup.body

def cls(el): return el.get("class", []) if isinstance(el, Tag) else []
def has(el, c): return c in cls(el)
def anchor(id_): return re.sub(r"[^A-Za-z0-9_]", "_", id_)[:40] if id_ else None
WARN = set()

# ---------- inline ----------
def runs_of(el, base=None):
    """Lista de runs a partir dos filhos inline de el. base: dict de atributos herdados."""
    base = dict(base or {}); out = []
    def add(text, **kw):
        if text == "": return
        r = dict(base); r.update(kw); r["text"] = text; out.append(r)
    for ch in el.children:
        if isinstance(ch, NavigableString):
            t = str(ch).replace("\n", " ")
            if t: add(t)
            continue
        if not isinstance(ch, Tag): continue
        n = ch.name; c = cls(ch)
        if n == "br": out.append(dict(base, br=True, text="")); continue
        if n == "b" or n == "strong": out += runs_of(ch, dict(base, b=True)); continue
        if n == "i" or n == "em": out += runs_of(ch, dict(base, i=True)); continue
        if n == "a":
            href = ch.get("href", ""); go = "go" in c
            sub = runs_of(ch, dict(base, link=anchor(href[1:]) if href.startswith("#") else None, b=base.get("b", False) or go, color="1F4E8C"))
            out += sub
            if go and href.startswith("#"): out.append(dict(base, text="", pageref=anchor(href[1:])))
            continue
        if n == "span" or n == "div":
            if "q" in c or "pergunta" in c: out += runs_of(ch, dict(base, i=True, color="17407A", shade=("EEF2F8" if "pergunta" in c else None))); continue
            if "vai" in c: out += runs_of(ch, dict(base, b=True, color="1F4E8C")); continue
            if "sym" in c: out += runs_of(ch, dict(base, b=True, color="1F4E8C")); continue
            if "pi-id" in c: out += runs_of(ch, dict(base, b=True, color="1F4E8C", size=9)); continue
            if "dot" in c: add("○ ", color="777777"); continue
            if "arrow" in c: out += runs_of(ch, dict(base, b=True, color="1F4E8C", size=9)); continue
            if n == "span" and not c: out += runs_of(ch, base); continue
        if n == "sup": out += runs_of(ch, dict(base, sup=True)); continue
        if n == "img": continue
        raise ValueError(f"inline não mapeado: <{n} class={c}> em {str(el)[:160]}")
    return out

def is_block(ch):
    return isinstance(ch, Tag) and ch.name in ("p", "div", "table", "ul", "ol", "h1", "h2", "h3", "h4", "figure", "section", "nav", "img") and not (ch.name == "div" and has(ch, "pergunta") and not only_child(ch)) and not (ch.name == "img" and False)

def only_child(ch):
    p = ch.parent
    sib = [x for x in p.children if (isinstance(x, Tag)) or (isinstance(x, NavigableString) and str(x).strip())]
    return len(sib) == 1

# ---------- blocos ----------
def blocks_of(el, ctx=None):
    """Converte os filhos de el em blocos. Texto solto e inlines viram parágrafos."""
    ctx = ctx or {}; out = []; pend = []   # pend: inlines acumulados para um <p>
    def flush():
        nonlocal pend
        if pend:
            tmp = soup.new_tag("p")
            r = []
            for x in pend: r += runs_of(x) if isinstance(x, Tag) else [{"text": str(x).replace("\n", " ")}]
            if any(x["text"].strip() or x.get("pageref") for x in r): out.append({"t": "p", "runs": r})
            pend = []
    for ch in el.children:
        if isinstance(ch, NavigableString):
            if str(ch).strip(): pend.append(ch)
            continue
        if not isinstance(ch, Tag): continue
        if not is_block(ch): pend.append(ch); continue
        flush(); out += block(ch, ctx)
    flush(); return out

def block(ch, ctx):
    n = ch.name; c = cls(ch); id_ = ch.get("id")
    if n == "p":
        kind = next((k for k in ("rota", "base", "res1", "intro") if k in c), None)
        return [{"t": "p", "runs": runs_of(ch), "cls": kind, "id": anchor(id_)}]
    if n in ("h2", "h3", "h4"):
        return [{"t": n, "runs": runs_of(ch), "id": anchor(id_)}]
    if n == "h1":
        return [{"t": "h1", "text": ch.get_text(" ", strip=True), "short": ch.get("data-short"), "id": anchor(id_)}]
    if n in ("ul", "ol"):
        items = []
        for li in ch.find_all("li", recursive=False):
            items.append({"runs": runs_of(li), "cls": [x for x in cls(li) if x in ("l1", "l2")]})
        st = re.search(r"list-item (\d+)", ch.get("style", "")); start = int(st.group(1)) + 1 if st else int(ch.get("start", 1))
        return [{"t": "list", "ordered": n == "ol", "start": start, "cls": c, "items": items}]
    if n == "img":
        return [image(ch, ctx)]
    if n == "figure":
        img = ch.find("img"); cap = ch.find("figcaption")
        return [{"t": "pic", "src": img["src"], "caption": runs_of(cap) if cap else [], "full": "flow" in c}]
    if n == "table":
        return [table(ch, ctx)]
    if n == "nav":
        items = [{"level": 1 if has(li, "l1") else 2, "text": li.get_text(" ", strip=True), "anchor": anchor(li.a["href"][1:])} for li in ch.find_all("li")]
        return [{"t": "toc", "title": ch.h1.get_text(strip=True), "items": items}]
    if n == "section":
        if "cover" in c: return [{"t": "cover"}]
        out = [{"t": "chapter", "id": anchor(id_), "flow": "flow" in c}]
        return out + blocks_of(ch, ctx)
    if n == "div":
        if "tab" in c: return []
        if "kicker" in c: return [{"t": "p", "runs": runs_of(ch), "cls": "kicker"}]
        if "trilha" in c:
            chips = []
            for a in ch.find_all("a", class_="chip"):
                b = a.find("b"); lab = a.get_text(" ", strip=True)
                chips.append({"id": b.get_text(strip=True) if b else "", "label": lab[len(b.get_text(strip=True)):].strip() if b else lab, "anchor": anchor(a["href"][1:])})
            return [{"t": "trilha", "chips": chips}]
        if "chapstart" in c or "keep" in c or "h2wide" in c or "wide" in c or "nextrun" in c or "interp" in c or "lb" in c or "chart" in c and "grp" not in c and "tf" not in c and "k-lista" not in c and ch.find("table", class_="cb") is None:
            blk = blocks_of(ch, ctx)
            if "lb" in c and id_: blk = [{"t": "anchor", "id": anchor(id_)}] + blk
            if "intro" in c: pass
            if "interp" in c: blk = [dict(b, interp=True) if b.get("t") in ("p", "list") else b for b in blk]
            if "chapstart" in c:  # o intro ocupa 64 %
                blk = [dict(b, narrow=64) if b.get("t") == "p" and b.get("cls") == "intro" else b for b in blk]
            return blk
        if "intro" in c:
            return [dict(b, cls="intro") for b in blocks_of(ch, ctx)]
        if "pi-id" in c: return [{"t": "p", "runs": runs_of(ch, {"b": True, "color": "1F4E8C", "size": 9}), "cls": "pi-id"}]
        if "cellhead" in c: return [{"t": "p", "runs": runs_of(ch), "cls": "cellhead", "id": anchor(id_)}]
        if "chart-head" in c:
            cid = ch.find(class_="chart-id").get_text(" ", strip=True); tt = ch.find(class_="chart-title")
            return [{"t": "chart-head", "cid": cid, "title": tt.get_text(" ", strip=True) if tt else "", "long": bool(tt and has(tt, "long")), "id": anchor(ctx.get("pending_id"))}]
        if "chart" in c:   # div.chart (simples), .tf, .grp, .k-lista
            sub = {"pending_id": id_} if id_ else {}
            blk = blocks_of(ch, dict(ctx, **sub))
            if id_ and not any(b.get("t") == "chart-head" for b in blk): blk = [{"t": "anchor", "id": anchor(id_)}] + blk
            if "tf" in c or "grp" in c: blk = [dict(b, keep_with_next=True) if b.get("t") == "chart-head" else b for b in blk]
            return blk
        if "cols" in c:
            ncol = 4 if "cards" in c else (3 if "three" in c else 2)
            if "one" in c: ncol = 1
            return [{"t": "cols", "n": ncol, "grpflow": "grpflow" in c, "blocks": blocks_of(ch, ctx)}]
        if "one" in c: return [{"t": "one", "blocks": blocks_of(ch, ctx)}]
        if "box" in c:
            kind = "variacao" if "variacao" in c else ("alerta" if "alerta" in c else "")
            inner = []
            for x in ch.children:
                if isinstance(x, Tag) and has(x, "box-title"): inner.append({"t": "p", "runs": runs_of(x), "cls": "box-title"})
                elif isinstance(x, Tag) and x.name == "div" and not cls(x): inner += blocks_of(x, ctx) if any(is_block(y) for y in x.children) else [{"t": "p", "runs": runs_of(x)}]
                elif isinstance(x, Tag): inner += block(x, ctx) if is_block(x) else [{"t": "p", "runs": runs_of(x)}]
                elif str(x).strip(): inner.append({"t": "p", "runs": [{"text": str(x).strip()}]})
            return [{"t": "box", "cls": kind, "blocks": inner}]
        if "dcard" in c:
            img = ch.find("img"); did = ch.find(class_="did"); q = ch.find(class_="q"); tb = ch.find("table")
            return [{"t": "dcard", "id": anchor(id_), "thumb": img["src"] if img else None, "thumb_anchor": anchor(img.parent["href"][1:]) if img and img.parent.name == "a" else None,
                     "did": did.get_text(" ", strip=True), "q": runs_of(q) if q else [], "table": table(tb, ctx) if tb else None}]
        if "beside" in c: return [{"t": "beside", "rule": "tfb" not in c, "blocks": blocks_of(ch, ctx)}]
        if "gloss" in c: return [{"t": "gloss", "blocks": blocks_of(ch, ctx)}]
        if "tec" in c: return [{"t": "tec", "id": anchor(id_), "blocks": blocks_of(ch, ctx)}]
        if "pb" in c: return [{"t": "pb"}] + blocks_of(ch, ctx)
        if "pergunta" in c:   # bloco: pergunta destacada com filete à esquerda
            return [{"t": "p", "runs": runs_of(ch, {"i": True, "color": "17407A"}), "cls": "pergunta-block"}]
        if "dhead" in c or "dtxt" in c or "did" in c or "q" in c:
            raise ValueError("dcard fora de contexto")
        if "box-title" in c: return [{"t": "p", "runs": runs_of(ch), "cls": "box-title"}]
        if not c:   # div sem classe: contêiner
            if any(is_block(y) for y in ch.children): return blocks_of(ch, ctx)
            return [{"t": "p", "runs": runs_of(ch)}]
        raise ValueError(f"div não mapeado: class={c} id={id_} :: {str(ch)[:200]}")
    raise ValueError(f"bloco não mapeado: <{n} class={c}> :: {str(ch)[:200]}")

PNG = {}
def png_info(src):
    name = os.path.basename(src)[:-4]
    fn = ("mini_" + name) if src.startswith("charts_mini") else name
    path = os.path.join(HERE, "png", fn + ".png")
    if path not in PNG:
        import pymupdf
        pix = pymupdf.Pixmap(path); PNG[path] = (pix.width, pix.height)
    return path, PNG[path]

def image(img, ctx):
    path, (w, h) = png_info(img["src"])
    return {"t": "image", "path": os.path.relpath(path, ROOT), "wpx": w, "hpx": h, "thumb": has(img, "thumb"), "src": img["src"]}

def pct(style):
    m = re.search(r"width:\s*([\d.]+)%", style or ""); return float(m.group(1)) if m else None

def table(tb, ctx):
    c = cls(tb); kind = "plain"
    for k in ("legend", "small", "lista", "two", "cb", "gi"): 
        if k in c: kind = k; break
    rows = []
    for tr in tb.find_all("tr"):
        if tr.find_parent("table") is not tb: continue
        header = tr.parent.name == "thead" or (tr.find("th") is not None and tr.find("td") is None)
        cells = []
        for td in tr.find_all(["td", "th"], recursive=False):
            tc = cls(td); st = td.get("style", "")
            cell = {"w": pct(st), "cls": tc, "colspan": int(td.get("colspan", 1))}
            if "lh" in tc:
                m = re.search(r"background:\s*(#[0-9a-fA-F]{6})", st); cell["shade"] = m.group(1)[1:] if m else None
            if "li" in tc:
                m = re.search(r"border-left-color:\s*(#[0-9a-fA-F]{6})", st); cell["lborder"] = m.group(1)[1:] if m else "9A9A9A"
            if "cap" in tc: cell["cap"] = True
            if td.get("id"): cell["id"] = anchor(td["id"])
            sub = {"pending_id": td.get("id")} if td.get("id") else {}
            if any(is_block(y) for y in td.children): cell["blocks"] = blocks_of(td, dict(ctx, **sub))
            else: cell["blocks"] = [{"t": "p", "runs": runs_of(td)}] if td.get_text(strip=True) or td.find("img") else []
            if td.find("img") and not any(is_block(y) for y in td.children): cell["blocks"] = [image(td.find("img"), ctx)]
            cells.append(cell)
        rows.append({"header": header, "cells": cells})
    return {"t": "table", "cls": kind, "classes": c, "rows": rows, "grp": "grp" in c, "side": "side" in c}

# ---------- documento ----------
doc = []
for ch in body.children:
    if isinstance(ch, NavigableString):
        if str(ch).strip(): raise ValueError("texto solto no body")
        continue
    doc += block(ch, {})
json.dump({"blocks": doc}, open(os.path.join(HERE, "ir.json"), "w", encoding="utf-8"), ensure_ascii=False)
from collections import Counter
cnt = Counter()
def walk(bl):
    for b in bl:
        cnt[b["t"]] += 1
        for k in ("blocks",):
            if k in b: walk(b[k])
        if b["t"] == "table":
            for r in b["rows"]:
                for cl in r["cells"]: walk(cl["blocks"])
        if b["t"] == "dcard" and b.get("table"): walk([b["table"]])
walk(doc)
print("IR:", dict(cnt))
