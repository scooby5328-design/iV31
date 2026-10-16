import hashlib
import json
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
UPDATE_BASE = "https://raw.githubusercontent.com/scooby5328-design/iv31/main/updates/"


def compact(path):
    return json.dumps(json.loads(path.read_text(encoding="utf-8")), separators=(",", ":"), ensure_ascii=False)


def build_page(stage):
    page = (ROOT / "src/index.html").read_text(encoding="utf-8")
    for key, name in (("__LOC__", "locations.json"), ("__DEX__", "pokedex.json"), ("__SP__", "secret-power.json")):
        if page.count(key) != 1:
            sys.exit(f"src/index.html must contain {key} exactly once")
        page = page.replace(key, compact(ROOT / "src/data" / name))
    (stage / "resources/index.html").write_text(page, encoding="utf-8")


def main():
    config = json.loads((ROOT / "app/neutralino.config.json").read_text(encoding="utf-8"))
    version = config["version"]
    page = (ROOT / "src/index.html").read_text(encoding="utf-8")
    if f'const APP_VERSION = "{version}";' not in page:
        sys.exit(f"Set APP_VERSION in src/index.html to {version} to match app/neutralino.config.json")
    if not (ROOT / "release-notes" / f"{version}.md").exists():
        sys.exit(f"Write release-notes/{version}.md first")

    stage = ROOT / "dist/stage"
    if stage.parent.exists():
        shutil.rmtree(stage.parent)
    shutil.copytree(ROOT / "app/resources", stage / "resources")
    shutil.copy2(ROOT / "app/neutralino.config.json", stage / "neutralino.config.json")
    build_page(stage)

    neu = ROOT / "updates" / f"iv31-{version}.neu"
    subprocess.run(["node", str(ROOT / "tools/pack.mjs"), str(stage), str(neu)], check=True, cwd=ROOT)
    digest = hashlib.sha256(neu.read_bytes()).hexdigest()
    summary = json.loads((ROOT / "src/release.json").read_text(encoding="utf-8"))["summary"]
    manifest = {
        "applicationId": config["applicationId"],
        "version": version,
        "resourcesURL": f"{UPDATE_BASE}iv31-{version}.neu",
        "data": {
            "sha256": digest,
            "size": neu.stat().st_size,
            "notes": summary,
        },
    }
    (ROOT / "updates/manifest.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(f"updates/iv31-{version}.neu  {manifest['data']['size']} bytes  sha256 {digest}")


if __name__ == "__main__":
    main()
