import shutil
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import build

ROOT = Path(__file__).resolve().parent.parent
www = ROOT / "android/app/src/main/assets/www"


def main():
    if www.exists():
        shutil.rmtree(www)
    stage = ROOT / "dist/android-stage"
    if stage.exists():
        shutil.rmtree(stage)
    shutil.copytree(ROOT / "app/resources", stage / "resources", ignore=shutil.ignore_patterns("js"))
    build.build_page(stage)
    shutil.copytree(stage / "resources", www)
    print(f"{www.relative_to(ROOT)} ready")


if __name__ == "__main__":
    main()
