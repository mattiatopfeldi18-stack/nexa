# NEXA ATELIER — Design System v1 · "Notte couture"

> Unica fonte di verità visiva. Ogni pagina, prompt o grafica Nexa usa SOLO questi token.
> Se serve qualcosa che non c'è: si aggiunge qui prima, poi si usa.

## 1. Essenza
Atelier notturno: sartoria, champagne, luce bassa. Lusso silenzioso, mai ostentato.
Parole guida: **precisione · penombra · su misura · calma**.

## 2. Colori (token CSS)
```css
:root{
  --ink:        #0E0E10; /* sfondo pagina */
  --ink-2:      #16161A; /* sezioni alternate */
  --ink-3:      #1F1E23; /* card, input */
  --line:       rgba(217,198,165,.14); /* hairline */
  --line-strong:rgba(217,198,165,.32);
  --champagne:  #D9C6A5; /* titoli, accento primario, bottone primario */
  --ivory:      #EDE6DA; /* testo corrente */
  --mute:       #9C958A; /* testo secondario, didascalie */
  --rose:       #B58A93; /* eyebrow, piccole etichette */
  --bordeaux:   #5A1E2A; /* fasce CTA, hover, badge */
}
```
Regole: max 3 colori per vista oltre ai neutri ink. Bordeaux solo come superficie (mai testo su ink). Testo su bordeaux = ivory. Niente gradienti vistosi, niente neon, niente glow.

## 3. Tipografia
- **Display:** Bodoni Moda 400/500 (+ italic per una parola d'accento). Solo da 28px in su.
- **Testo/UI:** Jost 400/500.
- Scala (clamp mobile→desktop): H1 44→80 · H2 32→52 · H3 24→30 · body 16→17 · small 14 · eyebrow 12.
- Eyebrow: Jost 500, MAIUSCOLO, letter-spacing .32em, color --rose.
- Body: line-height 1.65, max 62 caratteri per riga.
- Titoli: line-height 1.05, letter-spacing -0.01em. Mai tutto maiuscolo in Bodoni tranne il wordmark.

## 4. Logo
Wordmark: **NEXA** (Bodoni Moda, letter-spacing .14em, champagne) sopra **ATELIER** (Jost 400, letter-spacing .45em, rose, ~40% della dimensione).
Monogramma: "N" in Bodoni dentro cornice rettangolare hairline (favicon, social, sigillo sulle box torte).

## 5. Spaziatura e layout
- Base 8px. Scala: 8 · 16 · 24 · 40 · 64 · 104 (padding verticale sezioni desktop) · 72 (mobile).
- Contenitore max 1200px, gutter 16px mobile / 32px desktop. Griglia 12 colonne.
- Molto vuoto: una sola idea per schermata.

## 6. Forme
- Angoli: **0** su bottoni, immagini, card (taglio sartoriale). Unica eccezione: input 2px.
- Bordi: 1px var(--line). Hover → var(--line-strong).
- Nessuna ombra. La profondità si fa con ink / ink-2 / ink-3.

## 7. Componenti
- **Nav:** wordmark a sinistra, 3–4 link Jost 14 mute→ivory hover, CTA secondaria a destra. Sticky, sfondo ink 85% + blur leggero.
- **Bottone primario:** bg champagne, testo ink, Jost 500 12px MAIUSCOLO, spacing .22em, padding 16×28. Max 1 per sezione.
- **Bottone secondario:** outline 1px champagne, testo champagne. Hover: bg champagne 8%.
- **Link testuale:** champagne + sottolineatura sottile che si allunga in hover.
- **Section header:** eyebrow rose → H2 Bodoni champagne (una parola in italic) → lead mute.
- **Card servizio:** bg ink-3, bordo line, numero romano Bodoni rose (I, II, III), titolo H3, 2 righe, link.
- **Card torta:** immagine 4:5 · nome Bodoni 24 · meta Jost 13 mute (porzioni · gusto) · "da € X" champagne · CTA "Richiedi". Hover: immagine scale 1.03, bordo line-strong.
- **Fascia CTA:** bg bordeaux, titolo Bodoni ivory, bottone primario.
- **Footer:** ink-2, wordmark, contatti, social, P.IVA.

## 8. Movimento
- Entrata: fade + translateY 16px, 700ms, cubic-bezier(.2,.7,.2,1), stagger 80ms.
- Hover: 250ms. Niente parallax pesanti, niente carousel automatici.
- Rispettare `prefers-reduced-motion`.

## 9. Fotografia
Luce bassa e calda, una sola fonte, sfondi scuri, grana leggera ammessa. Torte su fondo nero o pietra scura, inquadrature frontali o dall'alto pulite. Persone: mani, dettagli, momenti, mai pose da stock. Correzione colore coerente: neri profondi, alte luci champagne.

## 10. Voce
Italiano, frasi brevi, sicure. Nessun punto esclamativo, nessuna emoji, niente "unico/esclusivo/top". Mostrare, non dichiarare. Si dà del "voi" o forma impersonale elegante.

## 11. Divieti
Gradienti arcobaleno · angoli arrotondati a pillola · più di un bottone primario per sezione · Bodoni sotto 28px · testo centrato su paragrafi lunghi · icone colorate · foto stock riconoscibili.

## 12. Accessibilità
Contrasti verificati: ivory/ink e champagne/ink > 12:1, mute/ink ≈ 6.9:1 (AA). Focus visibile: outline 1px champagne + offset 3px. Target touch ≥ 44px.
