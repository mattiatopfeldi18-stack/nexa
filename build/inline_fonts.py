#!/usr/bin/env python3
"""Scarica i font e li incorpora nel CSS come data URI.

Le istanze statiche sono obbligatorie: sui font variabili Chromium ripiega
sui font Type3 in fase di export, che incorporano i glifi come procedure
vettoriali invece che come programma di font. Stampano, ma il testo non
resta selezionabile e diverse tipografie li rifiutano.
"""
import base64, pathlib, re, sys, urllib.request

# User-Agent di un browser senza supporto woff2: Google Fonts risponde con
# le istanze statiche in WOFF invece che con i font variabili in woff2.
UA = ("Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8) AppleWebKit/534.30 "
      "(KHTML, like Gecko) Version/5.1 Safari/534.30")

FACCE = [("EB Garamond", 400), ("EB Garamond", 600), ("Inter", 400), ("Inter", 600)]
ROOT = pathlib.Path(__file__).resolve().parent.parent


def scarica(url):
    return urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": UA})).read()


def main():
    blocchi = []
    for famiglia, peso in FACCE:
        css = scarica(f"https://fonts.googleapis.com/css?family="
                      f"{famiglia.replace(' ', '+')}:{peso}").decode()
        url = re.search(r"url\((https://[^)]+)\)", css).group(1)
        dati = scarica(url)
        if dati[:4] != b"wOFF":
            sys.exit(f"{famiglia} {peso}: atteso WOFF statico, ricevuto {dati[:4]!r}")
        b64 = base64.b64encode(dati).decode()
        blocchi.append(
            "@font-face{\n"
            f"  font-family:'{famiglia}';\n  font-style:normal;\n  font-weight:{peso};\n"
            "  font-display:block;\n"
            f"  src:url(data:font/woff;base64,{b64}) format('woff');\n}}"
        )
        print(f"  {famiglia} {peso}: {len(dati)/1024:.0f} KB", file=sys.stderr)

    dest = ROOT / "assets/fonts/fonts-inline.css"
    dest.write_text("\n".join(blocchi) + "\n")
    print(f"scritto {dest.relative_to(ROOT)} ({dest.stat().st_size/1024:.0f} KB)", file=sys.stderr)


if __name__ == "__main__":
    main()
