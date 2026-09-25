import glob, os, sys
from playwright.sync_api import sync_playwright

out = sys.argv[1]
exe = glob.glob('/opt/pw-browsers/chromium-*/chrome-linux/chrome')[0]
with sync_playwright() as p:
    b = p.chromium.launch(executable_path=exe)
    for html in glob.glob(os.path.join(out, '*.html')):
        base = html[:-5]
        footer = open(base + '.footer.txt').read()
        pg = b.new_page()
        pg.goto('file://' + html)
        pg.pdf(path=base + '.pdf', format='A4', print_background=True, prefer_css_page_size=True,
               display_header_footer=True, header_template='<span></span>',
               footer_template=f'<div style="font-family:Arial;font-size:7pt;color:#808080;width:100%;text-align:center">{footer} · página <span class="pageNumber"></span> de <span class="totalPages"></span></div>')
        print(base + '.pdf')
    b.close()
