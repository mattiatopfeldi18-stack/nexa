#!/usr/bin/env python3
"""Ricava l'asset del logo dall'immagine incorporata nel preventivo originale.

L'immagine nel PDF è opaca su un fondo off-white (254, 251, 244) e non sul
crema del documento: appoggiata così com'è lascerebbe un riquadro chiaro.
Qui il punto di bianco viene rimappato sul fondo pagina, che su un artwork
scuro equivale a un PNG trasparente composto sul crema.
"""
import base64, pathlib, re, struct, sys, zlib

CREMA = (0xF4, 0xEF, 0xE5)
MARGINE = 0.06          # aria attorno all'inchiostro, in frazione del lato
TOLLERANZA = 14         # scarto entro cui un pixel conta come fondo, non come inchiostro
LATO_USCITA = 720       # px: a 22 mm di stampa sono oltre 800 dpi


def estrai(pdf):
    d = pathlib.Path(pdf).read_bytes()
    m = re.search(rb'/BitsPerComponent 8.*?/Height (\d+).*?/Width (\d+).*?stream\r?\n', d, re.S)
    h, w = int(m.group(1)), int(m.group(2))
    s = m.end()
    raw = zlib.decompress(base64.a85decode(d[s:d.find(b"endstream", s)].strip(), adobe=True))
    return w, h, raw


def png(path, w, h, rgb):
    def chunk(tipo, dati):
        c = tipo + dati
        return struct.pack(">I", len(dati)) + c + struct.pack(">I", zlib.crc32(c))
    scan = b"".join(b"\x00" + rgb[y * w * 3:(y + 1) * w * 3] for y in range(h))
    path.write_bytes(b"\x89PNG\r\n\x1a\n"
                     + chunk(b"IHDR", struct.pack(">IIBBBBB", w, h, 8, 2, 0, 0, 0))
                     + chunk(b"IDAT", zlib.compress(scan, 9)) + chunk(b"IEND", b""))


def main(pdf, dest):
    w, h, px = estrai(pdf)

    # fondo = colore dominante, campionato sul bordo
    bordo = [tuple(px[(y * w + x) * 3:(y * w + x) * 3 + 3])
             for y in (0, h - 1) for x in range(0, w, 11)]
    fondo = max(set(bordo), key=bordo.count)

    # riquadro dell'inchiostro, con soglia relativa al fondo
    soglia = [c - 30 for c in fondo]
    x0, y0, x1, y1 = w, h, -1, -1
    for y in range(h):
        r = px[y * w * 3:(y + 1) * w * 3]
        for x in range(w):
            if r[x*3] < soglia[0] or r[x*3+1] < soglia[1] or r[x*3+2] < soglia[2]:
                x0, x1 = min(x0, x), max(x1, x)
                y0, y1 = min(y0, y), max(y1, y)

    # il fondo dell'originale non è uniforme: appiattirlo qui, prima della
    # riduzione, evita l'alone agli angoli e lascia sfumati i bordi dell'artwork
    piatto = bytearray(px)
    tol = [c - TOLLERANZA for c in fondo]
    for i in range(0, len(piatto), 3):
        if piatto[i] >= tol[0] and piatto[i+1] >= tol[1] and piatto[i+2] >= tol[2]:
            piatto[i:i+3] = bytes(fondo)
    px = bytes(piatto)

    lato = max(x1 - x0, y1 - y0) + 1
    aria = int(lato * MARGINE)
    cx, cy = (x0 + x1) // 2, (y0 + y1) // 2
    lato += 2 * aria
    sx, sy = cx - lato // 2, cy - lato // 2

    # rimappa il fondo sul crema e riduce con un filtro a scatola
    n = LATO_USCITA
    passo = lato / n
    out = bytearray(n * n * 3)
    for j in range(n):
        ya, yb = int(sy + j * passo), max(int(sy + j * passo) + 1, int(sy + (j + 1) * passo))
        for i in range(n):
            xa, xb = int(sx + i * passo), max(int(sx + i * passo) + 1, int(sx + (i + 1) * passo))
            acc, cnt = [0, 0, 0], 0
            for y in range(ya, yb):
                if not 0 <= y < h: continue
                base = y * w * 3
                for x in range(xa, xb):
                    if not 0 <= x < w: continue
                    for k in range(3):
                        acc[k] += px[base + x * 3 + k]
                    cnt += 1
            for k in range(3):
                v = (acc[k] // cnt if cnt else fondo[k]) * CREMA[k] / fondo[k]
                out[(j * n + i) * 3 + k] = min(255, max(0, round(v)))

    dest = pathlib.Path(dest)
    png(dest, n, n, bytes(out))
    print(f"fondo originale {fondo} -> crema {CREMA}")
    print(f"inchiostro {x1-x0+1}x{y1-y0+1} px  ->  {dest} {n}x{n}  ({dest.stat().st_size/1024:.0f} KB)")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
