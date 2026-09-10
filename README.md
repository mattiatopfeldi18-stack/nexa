# Preventivo — Nexa Atelier

Documento commerciale A4, una pagina, print-ready.

```
build/genera.sh                 # da data/preventivo.json
build/genera.sh altri-dati.json
```

Produce `preventivo-nexa-atelier.html` (autonomo: font e logo incorporati in
base64, nessuna risorsa esterna) e `preventivo-nexa-atelier.pdf`.

## Sistema visivo

Fondo `#F4EFE5` a pieno formato. Bordeaux `#701017` riservato a logo, filetti
di sezione e totale. Testo `#0F0F0E` per i titoli, `#4A4540` per corpo e
didascalie. EB Garamond per titoli e cifre, Inter per tabelle e note: due pesi
per famiglia, subset latino incorporato nel PDF. Gerarchia costruita con lo
spazio bianco e filetti da 0,5 pt — nessun riquadro, ombra, gradiente o icona.
Tutti gli importi in cifre tabulari allineate a destra, due decimali.

## Densità

Il ritmo verticale è governato dalle variabili in cima a `src/style.css`
(`--h-logo`, `--gap-sezione`, `--pad-riga`, scala tipografica). `build/render.js`
misura l'altezza naturale del contenuto e segnala se il documento deborda.

Rientrano in pagina circa otto voci di servizio con note di tre righe. Oltre
quel volume si accorciano le note: il corpo del testo non scende sotto i 9 pt.

## Font

`assets/fonts/fonts-inline.css` è generato da `build/inline_fonts.py`, che
scarica EB Garamond e Inter e li incorpora come data URI. Va rigenerato solo
per cambiare famiglia o peso.

Servono le **istanze statiche**, non i font variabili. Con i variabili
Chromium ripiega in export sui font Type3, che incorporano i glifi come
procedure vettoriali anziché come programma di font: stampano, ma il testo
non resta selezionabile e diverse tipografie li rifiutano. Lo script chiede
perciò a Google Fonts le versioni WOFF statiche e si ferma se riceve altro.
Nel PDF prodotto i font compaiono come `CIDFontType2` con `FontFile2`.

## Logo

`build/logo.py` ricava l'asset dall'immagine incorporata nel preventivo
originale, che è opaca su un fondo off-white e non sul crema del documento.
Lo script appiattisce quel fondo e ne rimappa il punto di bianco sul colore
pagina: su un artwork scuro il risultato equivale a un PNG trasparente
composto sul crema. Se è disponibile il PNG originale con trasparenza,
sostituirlo in `assets/` è preferibile — l'immagine del PDF porta con sé
gli artefatti JPEG della sorgente.
