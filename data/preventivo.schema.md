# Campi del preventivo

Il documento si compone da un solo file `data/preventivo.json`. Nessun campo
ammette segnaposto: una voce senza dato va rimossa, non riempita a caso.

| Campo | Tipo | Note |
|---|---|---|
| `logo` | percorso | PNG con sfondo trasparente, incorporato in base64 |
| `numero` | stringa | progressivo del preventivo |
| `data_emissione` | stringa | data per esteso, es. `12 marzo 2026` |
| `evento.titolo` | stringa | titolo dell'evento |
| `evento.coordinate` | stringa | data e location, separate da `·` |
| `cliente.nome` | stringa | ragione sociale o nome del referente |
| `cliente.contatto` | stringa | email e telefono |
| `cliente.riferimento` | stringa | orario e numero di ospiti stimati |
| `servizi_inclusi[]` | `voce`, `dettaglio?`, `importo` | solo le voci base |
| `servizi_opzionali[]` | `voce`, `dettaglio?`, `importo` | tabella separata, senza colonna di stato |
| `riepilogo.voci[]` | `voce`, `importo` | imponibile e coordinamento |
| `riepilogo.etichetta_totale` | stringa | `Totale` oppure `Totale dovuto` |
| `riepilogo.totale` | numero | |
| `nota_iva` | stringa | regime esplicitato per esteso |
| `titolo_condizioni` | stringa | |
| `condizioni[]` | `etichetta`, `testo` | massimo tre righe per blocco |
| `azienda` | `ragione_sociale`, `piva`, `email`, `telefono`, `sito` | |

## Importi

`importo` accetta un numero (formattato `€ 1.234,56`) oppure una stringa, che
passa intatta. Le stringhe servono per gli importi non ancora definiti, dove
la parola «circa» non è ammessa:

- `"€ 180 – 220"` — intervallo esplicito
- `"da € 200, definito a conferma quantità"` — soglia minima
