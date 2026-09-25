# Gerador dos documentos

O texto dos dois documentos fica em `conteudo.js`. Para regerar Word e PDF:

```bash
npm install docx            # uma vez
pip install playwright      # uma vez (usa o Chromium instalado)
node render.js ..           # gera os .docx e os .html
python3 pdf.py ..           # converte os .html em .pdf
rm ../*.html ../*.footer.txt
```
