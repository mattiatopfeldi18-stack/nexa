#!/usr/bin/env python3
"""Compone il preventivo Nexa Atelier in un HTML A4 autonomo, print-ready."""
import base64, json, html, mimetypes, pathlib, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
E = lambda s: html.escape(str(s), quote=False)


def euro(v):
    """Importo in formato italiano. Le stringhe passano intatte (intervalli, 'da €')."""
    if isinstance(v, str):
        return E(v)
    intero, dec = f"{v:,.2f}".split(".")
    return "\u20ac\u00a0" + intero.replace(",", ".") + "," + dec   # \u20ac\u00a0 = euro + spazio unificatore


def data_uri(path):
    p = pathlib.Path(path)
    if not p.is_absolute():
        p = ROOT / p
    mime = mimetypes.guess_type(p.name)[0] or "application/octet-stream"
    return f"data:{mime};base64,{base64.b64encode(p.read_bytes()).decode()}"


def righe(voci):
    out = []
    for v in voci:
        det = f'<span class="dettaglio">{E(v["dettaglio"])}</span>' if v.get("dettaglio") else ""
        out.append(
            "<tr>"
            f'<td><span class="voce">{E(v["voce"])}</span>{det}</td>'
            f'<td class="cifra">{euro(v["importo"])}</td>'
            "</tr>"
        )
    return "\n".join(out)


def tabella(titolo, voci, intestazione_importo="Importo"):
    return f"""
      <section class="sezione">
        <div class="titolo">
          <span class="etichetta">{E(titolo)}</span>
          <span class="etichetta">{E(intestazione_importo)}</span>
        </div>
        <table>
          <colgroup><col><col class="c-importo"></colgroup>
          <tbody>
{righe(voci)}
          </tbody>
        </table>
      </section>"""


def campo(etichetta, valore):
    if isinstance(valore, (list, tuple)):
        valore = "".join(f"<span>{E(x)}</span>" for x in valore)
    else:
        valore = E(valore)
    return f'<div class="campo"><span class="etichetta">{E(etichetta)}</span>' \
           f'<div class="valore">{valore}</div></div>'


def blocco(etichetta, testo):
    return f'<div class="blocco"><span class="etichetta">{E(etichetta)}</span>' \
           f'<p>{E(testo)}</p></div>'


def main():
    src = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "data/preventivo.json"
    d = json.loads(src.read_text(encoding="utf-8"))
    css = (ROOT / "assets/fonts/fonts-inline.css").read_text() + "\n" + (ROOT / "src/style.css").read_text()

    ev, cli, rie, az = d["evento"], d["cliente"], d["riepilogo"], d["azienda"]

    # riepilogo economico
    rows = [f'<tr><td class="et">{E(r["voce"])}</td><td class="cifra">{euro(r["importo"])}</td></tr>'
            for r in rie["voci"]]
    rows.append(f'<tr class="totale"><td class="et">{E(rie["etichetta_totale"])}</td>'
                f'<td class="cifra">{euro(rie["totale"])}</td></tr>')

    condizioni = "\n".join(blocco(c["etichetta"], c["testo"]) for c in d["condizioni"])

    doc = f"""<!doctype html>
<html lang="it">
<head>
<meta charset="utf-8">
<title>Preventivo {E(d['numero'])} — Nexa Atelier</title>
<style>
{css}
</style>
</head>
<body>
<div class="foglio">

  <img class="logo" src="{data_uri(d['logo'])}" alt="Nexa Atelier">

  <div class="riga-testata">
    <span class="etichetta">Preventivo n. {E(d['numero'])}</span>
    <span class="etichetta">{E(d['data_emissione'])}</span>
  </div>

  <header class="evento">
    <h1>{E(ev['titolo'])}</h1>
    <div class="coordinate">{E(ev['coordinate'])}</div>
  </header>

  <div class="dati">
    {campo('Cliente', cli['nome'])}
    {campo('Contatto', cli['contatto'])}
    {campo('Riferimento evento', cli['riferimento'])}
  </div>

{tabella('Servizi inclusi', d['servizi_inclusi'])}
{tabella('Servizi opzionali', d['servizi_opzionali'])}

  <div class="riepilogo">
    <table><tbody>
{chr(10).join(rows)}
    </tbody></table>
  </div>
  <p class="nota-iva">{E(d['nota_iva'])}</p>

  <section class="condizioni">
    <div class="titolo"><span class="etichetta">{E(d['titolo_condizioni'])}</span></div>
    <div class="griglia">
{condizioni}
    </div>
  </section>

  <section class="accettazione">
    <div class="riga"><div class="linea"></div><span class="etichetta">Luogo</span></div>
    <div class="riga"><div class="linea"></div><span class="etichetta">Data</span></div>
    <div class="riga"><div class="linea"></div><span class="etichetta">Firma del cliente per accettazione</span></div>
  </section>

  <footer class="pie">
    <span class="ragione">{E(az['ragione_sociale'])}</span>
    <div><span>P. IVA {E(az['piva'])}</span><span>{E(az['email'])}</span><span>{E(az['telefono'])}</span><span>{E(az['sito'])}</span></div>
  </footer>

</div>
</body>
</html>
"""
    out = pathlib.Path(sys.argv[2]) if len(sys.argv) > 2 else ROOT / "preventivo-nexa-atelier.html"
    out.write_text(doc, encoding="utf-8")
    print(f"scritto {out}  ({len(doc)/1024:.0f} KB)")


if __name__ == "__main__":
    main()
