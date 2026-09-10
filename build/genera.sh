#!/usr/bin/env bash
# Compone il preventivo e lo esporta in PDF. Uso: build/genera.sh [dati.json]
set -euo pipefail
cd "$(dirname "$0")/.."
DATI="${1:-data/preventivo.json}"
python3 build/build.py "$DATI" preventivo-nexa-atelier.html
NODE_PATH="${NODE_PATH:-/opt/node22/lib/node_modules}" node build/render.js \
  preventivo-nexa-atelier.html preventivo-nexa-atelier.pdf
