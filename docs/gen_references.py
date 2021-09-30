import shutil
from pathlib import Path

root = Path(__file__).resolve().parents[1]
src_root = root / "src"
ref_root = root / "docs/sources/reference"

if ref_root.exists():
    shutil.rmtree(ref_root)

ref_root.mkdir(exist_ok=True)

for script in src_root.glob("*.py"):
    ref = (ref_root / script.stem).with_suffix(".md")

    with open(ref, "wt") as fp:
        fp.write(f"::: src.{script.stem}\n")

print(f"Generated references to {ref_root}.")
