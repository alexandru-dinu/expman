from pathlib import Path

root = Path(__file__).resolve().parents[1]
src_root = root / "src"
ref_root = root / "docs/sources/reference"
tpl_root = root / "docs/sources/template"

ref_root.mkdir(parents=True, exist_ok=False)
tpl_root.mkdir(parents=True, exist_ok=False)

for script in src_root.glob("*.py"):
    if script.stem.startswith("_"):
        path = (tpl_root / script.stem).with_suffix(".md")
    else:
        path = (ref_root / script.stem).with_suffix(".md")

    with open(path, "wt") as fp:
        fp.write(f"::: src.{script.stem}\n")

    print(f"> generated ref to {path}.")
