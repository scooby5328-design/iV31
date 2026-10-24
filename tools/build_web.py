import json
import shutil
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from build import ROOT, inline_data, old_engine_fallbacks

SITE = "https://scooby5328-design.github.io/iV31/"


def main():
    version = json.loads((ROOT / "app/neutralino.config.json").read_text(encoding="utf-8"))["version"]
    out = ROOT / "dist/web"
    if out.exists():
        shutil.rmtree(out)
    shutil.copytree(ROOT / "app/resources/fonts", out / "fonts")
    for name in ("icon-192.png", "icon-512.png", "apple-touch-icon.png", "manifest.webmanifest"):
        shutil.copy2(ROOT / "app/web" / name, out / name)
    shutil.copy2(ROOT / "app/resources/icon.png", out / "icon.png")

    page = inline_data(old_engine_fallbacks((ROOT / "src/index.html").read_text(encoding="utf-8")))
    tag = '<script src="js/neutralino.js"></script>'
    if page.count(tag) != 1:
        sys.exit("Expected one neutralino.js script tag")
    page = page.replace(tag, "<script>window.IV31_WEB=true</script>")
    csp_start = page.index('<meta http-equiv="Content-Security-Policy"')
    csp_end = page.index(">", csp_start) + 1
    desc = "Free offline Pokémon IV calculator: find hidden IVs, track EVs, plan natures and check type matchups, Hidden Power, Secret Power and Nature Power for every main game from Red to Scarlet."
    head = "\n".join([
        '<meta http-equiv="Content-Security-Policy" content="default-src \'self\'; style-src \'self\' \'unsafe-inline\'; script-src \'self\' \'unsafe-inline\'; font-src \'self\'; img-src \'self\' data:; connect-src \'self\'; manifest-src \'self\'; worker-src \'self\'">',
        f'<meta name="description" content="{desc}">',
        '<meta name="theme-color" content="#14171b">',
        '<link rel="manifest" href="manifest.webmanifest">',
        '<link rel="icon" type="image/png" href="icon-192.png">',
        '<link rel="apple-touch-icon" href="apple-touch-icon.png">',
        f'<link rel="canonical" href="{SITE}">',
        '<meta property="og:type" content="website">',
        '<meta property="og:title" content="iv31 · Pokémon IV Checker">',
        f'<meta property="og:description" content="{desc}">',
        f'<meta property="og:url" content="{SITE}">',
        f'<meta property="og:image" content="{SITE}icon-512.png">',
    ])
    page = page[:csp_start] + head + page[csp_end:]
    (out / "index.html").write_text(page, encoding="utf-8")

    files = ["./", "manifest.webmanifest", "icon-192.png", "icon-512.png"] + sorted(f"fonts/{p.name}" for p in (out / "fonts").iterdir())
    sw = (ROOT / "app/web/sw.js").read_text(encoding="utf-8").replace("__VERSION__", version).replace("__FILES__", json.dumps(files))
    (out / "sw.js").write_text(sw, encoding="utf-8")
    (out / ".nojekyll").write_text("", encoding="utf-8")
    (out / "robots.txt").write_text(f"User-agent: *\nAllow: /\n", encoding="utf-8")
    size = sum(p.stat().st_size for p in out.rglob("*") if p.is_file())
    print(f"dist/web  {version}  {size} bytes")


if __name__ == "__main__":
    main()
