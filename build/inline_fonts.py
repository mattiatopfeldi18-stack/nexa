import re, base64, urllib.request, pathlib, sys

CSS = pathlib.Path("assets/fonts/gf.css").read_text()
KEEP = {"latin", "latin-ext"}
out = []
blocks = re.split(r"/\*\s*([a-z\-]+)\s*\*/", CSS)
# blocks: ['', 'cyrillic-ext', '@font-face{...}', 'cyrillic', '...', ...]
cache = {}
for i in range(1, len(blocks), 2):
    subset, body = blocks[i], blocks[i+1]
    if subset not in KEEP:
        continue
    url = re.search(r"url\((https://[^)]+)\)", body).group(1)
    if url not in cache:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        cache[url] = base64.b64encode(urllib.request.urlopen(req).read()).decode()
        print(f"  fetched {subset:10s} {url.rsplit('/',1)[-1]}", file=sys.stderr)
    body = body.replace(url, f"data:font/woff2;base64,{cache[url]}")
    body = body.replace("font-display: swap;", "font-display: block;")
    out.append(body.strip())

pathlib.Path("assets/fonts/fonts-inline.css").write_text("\n".join(out) + "\n")
print(f"blocks: {len(out)}  unique files: {len(cache)}", file=sys.stderr)
