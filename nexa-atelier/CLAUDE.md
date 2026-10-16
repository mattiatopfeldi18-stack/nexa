# CLAUDE.md — Nexa Atelier (sito)

Leggi questo file a ogni sessione. Poi leggi `DESIGN.md` e `BRIEF.md` prima di toccare codice.

## Ruolo
Sviluppatore front-end senior con gusto editoriale. Obiettivo: sito elegante, veloce, facile da mantenere per una persona sola.

## Stack (non negoziabile)
- HTML5 + CSS + JavaScript vanilla. **Nessun framework, nessun build step, nessuna dipendenza npm.**
- Font da Google Fonts: Bodoni Moda (400, 500, 400 italic) e Jost (400, 500), con `display=swap` e preconnect.
- Il sito deve funzionare anche aprendo `index.html` con doppio clic (per questo i dati sono in `data/torte.js`, non in JSON con fetch).
- Hosting previsto: statico (Netlify / Vercel / GitHub Pages).

## Struttura file
```
index.html
privacy.html
assets/css/styles.css      ← token di DESIGN.md come variabili :root
assets/js/main.js          ← render catalogo, link WhatsApp, animazioni, nav
assets/img/                ← hero.webp, og.jpg, favicon.svg, torte/<id>.webp
data/torte.js              ← NEXA_CONFIG + NEXA_TORTE (unica fonte dati)
DESIGN.md · BRIEF.md · CLAUDE.md
```

## Regole di design
- Usa SOLO i token di `DESIGN.md`. Nessun colore, font, raggio od ombra fuori sistema.
- Testi: copiali da `BRIEF.md` **alla lettera**. Le parole in *corsivo* nel brief vanno rese in Bodoni italic.
- Immagine mancante → placeholder elegante (bg ink-3, monogramma N hairline, nome torta), mai un'icona rotta.
- Mobile first: verifica a 375, 768 e 1280 px. Nessuno scroll orizzontale.

## Regole tecniche
- Tutti i link WhatsApp sono generati in JS da `NEXA_CONFIG.whatsapp` + messaggio con `encodeURIComponent`. Formato: `https://wa.me/<numero>?text=<msg>`.
- HTML semantico, un solo `<h1>`, `alt` descrittivi, focus visibile, `prefers-reduced-motion` rispettato.
- Animazioni con IntersectionObserver, nessuna libreria.
- Immagini: `loading="lazy"` (tranne hero), `width`/`height` espliciti, formato webp.
- Obiettivo Lighthouse ≥ 95 su Performance, Accessibilità, Best Practices e SEO.

## Regole per risparmiare crediti
- Modifiche piccole = edit mirati. **Non riscrivere file interi** per cambiare poche righe.
- Non creare varianti, pagine o funzionalità non richieste.
- Non aggiungere dipendenze, tool di build o test framework.
- A fine task: elenco breve delle modifiche (file + cosa), senza ripetere il codice.

## Fuori perimetro (chiedere prima)
Pagamenti online, CMS, backend, cookie di tracciamento/analytics (richiedono banner cookie), nuove sezioni.
