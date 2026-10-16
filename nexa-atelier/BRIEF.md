# NEXA ATELIER — Brief sito v1 (Home one-page)

> Testi definitivi: vanno usati **alla lettera**. Le parti tra [QUADRE] sono da completare dall'utente.
> Design: vedi `DESIGN.md`. Dati torte e contatti: `data/torte.js`.

## Obiettivo
Una home one-page che porta il visitatore a scrivere su **WhatsApp**. Tre linee di servizio (lauree, privati, aziende): ognuna ha il proprio messaggio WhatsApp precompilato, così dalla chat si capisce subito da quale linea arriva il contatto.

## Struttura (in quest'ordine)
1. Nav
2. Hero
3. Manifesto
4. Cosa facciamo (3 servizi)
5. Metodo (4 passaggi)
6. Torte d'atelier (catalogo)
7. Fascia CTA
8. Domande frequenti
9. Footer

---

## 1. Nav
Wordmark NEXA / ATELIER · Link: Servizi · Metodo · Torte · Contatti · CTA secondaria: **Scrivici**

## 2. Hero
- Eyebrow: EVENTI SU MISURA · MILANO E SICILIA
- H1: Eventi cuciti *su misura*.
- Lead: Feste di laurea, ricevimenti privati ed eventi aziendali, progettati come un abito d'atelier: dalla prima idea all'ultimo brindisi.
- CTA primaria: **Prenota una consulenza** → WhatsApp (messaggio "generale")
- CTA secondaria: **Scopri le torte** → #torte
- Visual: immagine hero a tutta altezza (`assets/img/hero.webp`) con velo ink al 55%. Se manca: sfondo ink con monogramma N grande in hairline.

## 3. Manifesto
- Eyebrow: L'ATELIER
- Testo (Bodoni, grande, max 3 righe desktop): Ogni evento parte da una domanda: *come deve sentirsi chi entra?*
- Sotto (Jost, mute): Da lì disegniamo luce, musica, tavola e ritmo della serata. Un solo referente, nessun dettaglio lasciato al caso.

## 4. Cosa facciamo — id `servizi`
- Eyebrow: COSA FACCIAMO
- H2: Tre occasioni, *una firma*.

| # | Titolo | Testo | CTA | Messaggio WhatsApp |
|---|---|---|---|---|
| I | Feste di laurea | Il traguardo merita una regia. Location, allestimento, musica, torta e foto: voi pensate agli ospiti, al resto pensiamo noi. | Organizza la tua laurea | Ciao Nexa, vorrei organizzare una festa di laurea. Data indicativa: … Ospiti: … |
| II | Eventi privati | Compleanni, anniversari, cene riservate. Atmosfere intime o grandi serate, sempre con la stessa cura. | Racconta la tua idea | Ciao Nexa, vorrei organizzare un evento privato (tipo: …). Data indicativa: … Ospiti: … |
| III | Eventi aziendali | Lanci, cene di gala, team event e feste di fine anno. Un evento che rappresenta l'azienda, con tempi e budget chiari. | Richiedi una proposta | Buongiorno Nexa, scrivo per conto di [azienda]. Vorremmo organizzare un evento aziendale. Periodo: … Partecipanti: … |

## 5. Metodo — id `metodo`
- Eyebrow: IL METODO
- H2: Dalla prima chiamata *all'ultimo ospite*.
1. **Ascolto** — Una chiamata di venti minuti per capire occasione, ospiti e budget.
2. **Progetto** — Concept, moodboard e preventivo chiaro, voce per voce.
3. **Regia** — Coordiniamo location, fornitori e tempi. Un solo referente per tutto.
4. **La serata** — Siamo presenti dall'allestimento fino all'ultimo ospite.

## 6. Torte d'atelier — id `torte`
- Eyebrow: LA PASTICCERIA
- H2: Torte *d'atelier*.
- Lead: Una selezione creata con una pasticceria artigianale partner. Ogni torta si personalizza in gusto, dimensione e dettagli.
- Griglia card generata da `data/torte.js` (3 col desktop, 2 tablet, 1 mobile).
- CTA su ogni card: **Richiedi** → WhatsApp con messaggio: `Ciao Nexa, sono interessato alla torta "{nome}". Data: … Persone: …`
- Prezzo: se `prezzoDa` è null → mostra "Su richiesta".
- Nota sotto la griglia (small, mute): Ordini con almeno [7] giorni di anticipo. Immagini indicative: ogni torta viene realizzata a mano e può variare nei dettagli.

## 7. Fascia CTA (bordeaux) — id `contatti`
- H2 (ivory): Raccontateci la vostra *occasione*.
- Testo: Rispondiamo entro 24 ore, con una prima idea già sul tavolo.
- CTA primaria: **Scrivici su WhatsApp** (messaggio generale)
- Link secondario: oppure scrivici a [email]

## 8. Domande frequenti
Accordion accessibile (`<details>`), max 4:
1. **In quali zone lavorate?** — Milano e provincia, Sicilia orientale. Per altre zone, scriveteci.
2. **Con quanto anticipo devo contattarvi?** — Per una festa privata bastano tre o quattro settimane; per eventi aziendali consigliamo almeno due mesi.
3. **Posso ordinare solo la torta?** — Sì, le torte del catalogo si possono richiedere anche senza organizzare l'evento con noi. [verificare con la pasticceria partner]
4. **Come funziona il preventivo?** — Dopo la prima chiamata ricevete una proposta scritta con ogni voce indicata. Nessun costo nascosto.

## 9. Footer
Wordmark · Contatti (WhatsApp, email, Instagram) · "Nexa Atelier di Mattia Di Donato · P.IVA [numero]" · © anno corrente · link Privacy.

## Messaggio WhatsApp "generale"
Ciao Nexa, vorrei informazioni per un evento. Tipo: … Data indicativa: … Ospiti: …

## SEO
- Title: Nexa Atelier — Eventi su misura a Milano e in Sicilia
- Description: Feste di laurea, eventi privati e aziendali progettati su misura, con torte d'atelier da pasticceria artigianale. Scrivici su WhatsApp.
- JSON-LD `EventPlanner` (nome, area servita, contatti da config).
- Open Graph con `assets/img/og.jpg` (1200×630).
