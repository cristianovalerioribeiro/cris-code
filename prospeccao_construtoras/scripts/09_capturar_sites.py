#!/usr/bin/env python3
"""Tira um print da pagina inicial de cada construtora da lista para o relatorio.
Funciona em qualquer computador com internet:

    pip install playwright
    python -m playwright install chromium
    python 09_capturar_sites.py
    (na nuvem do Claude Code: CHROMIUM_PATH=/opt/pw-browsers/chromium python 09_capturar_sites.py)

As imagens vao para fichas_v3/img/<dominio>.jpg (ou para a pasta passada como
argumento). Depois, rode 08_relatorio_v3.py para colocar as imagens nos cartoes.
Sites fora do ar ficam registrados em status_sites.json."""
import json, os, sys
from datetime import datetime
from pathlib import Path
from playwright.sync_api import sync_playwright

SITES = {
    "rdrengenharia.com": "https://www.rdrengenharia.com/",
    "rlcostaengenharia.com.br": "https://rlcosta.com/",
    "engecomengenharia.com.br": "https://engecomengenharia.com.br/",
    "construtoraformula.com.br": "https://www.construtoraformula.com.br/",
    "meloprado.com.br": "https://meloprado.com.br/",
    "abiaengenharia.com.br": "https://abiaengenharia.com.br/",
    "sonharconstrutora.com.br": "https://sonharconstrutora.com.br/",
    "conup.com.br": "https://www.conup.com.br/",
    "f2construtora.com.br": "https://f2incorporadora.com.br/",
    "vivaquartzo.com.br": "https://vivaquartzo.com.br/",
    "casagrandeincorporacoes.com.br": "https://casagrandeincorporacoes.com.br/",
    "cobconstrutora.com.br": "https://cobconstrutora.com.br/",
    "sudoeste.com.br": "https://sudoeste.com.br/",
    "rveconstrucoes.com.br": "https://rveconstrucoes.com.br/",
    "orionempreendimentos.com": "https://orionempreendimentos.com/",
    "mpoconstrucoes.com.br": "https://www.mpoconstrucoes.com.br/",
    "tabinc.com.br": "https://www.tabinc.com.br/",
    "furtadoaraujo.com.br": "https://www.furtadoaraujo.com.br/",
    "becker.com.br": "https://becker.com.br/",
    "cimos.com.br": "https://www.cimos.com.br/",
    "sudesteengenharia.com.br": "https://sudesteengenharia.com.br/",
    "construtorammatos.com.br": "https://construtorammatos.com.br/",
    "capanemaempreendimentos.com.br": "https://capanemaempreendimentos.com.br/",
    "mcfconstrutora.com.br": "https://mcfconstrutora.com.br/",
    "tergosconstrutora.com.br": "https://tergosconstrutora.com.br/",
    "monterre.com.br": "https://www.monterre.com.br/",
    "meuzip.com.br": "https://meuzip.com.br/",
    "construtorahabit.com.br": "https://construtorahabit.com.br"
}

def main():
    pasta = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parent.parent / "fichas_v3" / "img"
    pasta.mkdir(parents=True, exist_ok=True)
    status = {}
    with sync_playwright() as pw:
        nav = pw.chromium.launch(executable_path=os.environ.get("CHROMIUM_PATH") or None)
        for dom, url in SITES.items():
            pag = nav.new_page(viewport={"width": 1366, "height": 854}, locale="pt-BR")
            try:
                r = pag.goto(url, timeout=30000, wait_until="domcontentloaded")
                pag.wait_for_timeout(3500)          # carrossel e imagens da home
                pag.screenshot(path=str(pasta / f"{dom}.jpg"), type="jpeg", quality=70)
                status[dom] = {"url": pag.url, "http": r.status if r else None, "no_ar": bool(r and r.status < 400)}
            except Exception as erro:
                status[dom] = {"url": url, "erro": str(erro).splitlines()[0], "no_ar": False}
            status[dom]["data"] = datetime.now().isoformat(timespec="minutes")
            print(dom, "ok" if status[dom]["no_ar"] else "FALHOU")
            pag.close()
        nav.close()
    (pasta / "status_sites.json").write_text(json.dumps(status, indent=1, ensure_ascii=False), encoding="utf-8")

if __name__ == "__main__":
    main()
