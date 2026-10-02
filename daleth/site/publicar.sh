#!/usr/bin/env bash
# Publica o site no GitHub Pages: gera o site e envia o resultado para a branch gh-pages.
# Endereço: https://cristianovalerioribeiro.github.io/cris-code/
# Quando houver domínio próprio apontado para o Pages, rode com RAIZ=/ (e crie dist/CNAME).
set -euo pipefail
cd "$(dirname "$0")"
RAIZ="${RAIZ:-/cris-code/}"
python3 build.py --raiz="$RAIZ"

REPO=$(git rev-parse --show-toplevel)
ALVO=$(mktemp -d)
trap 'git -C "$REPO" worktree remove --force "$ALVO" >/dev/null 2>&1 || true' EXIT

if git -C "$REPO" fetch -q origin gh-pages 2>/dev/null; then
  git -C "$REPO" worktree add -q -B gh-pages "$ALVO" origin/gh-pages
else
  git -C "$REPO" worktree add -q --orphan -b gh-pages "$ALVO"
fi

find "$ALVO" -mindepth 1 -maxdepth 1 ! -name .git -exec rm -rf {} +
cp -a dist/. "$ALVO"/
cd "$ALVO"
git add -A
if git diff --cached --quiet; then
  echo "Nada mudou desde a última publicação."
  exit 0
fi
ORIGEM=$(git -C "$REPO" rev-parse --short HEAD)
git commit -q -m "Publica o site DALETH ($ORIGEM)"
for espera in 0 2 4 8 16; do
  sleep "$espera"
  if git push -q -u origin gh-pages; then
    echo "Publicado: https://cristianovalerioribeiro.github.io${RAIZ}"
    exit 0
  fi
done
echo "Falha ao enviar para gh-pages." >&2
exit 1
