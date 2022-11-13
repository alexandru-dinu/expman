#!/usr/bin/env python3

from pathlib import Path

root = Path(__file__).resolve().parents[1]
src_root = root / "opskrift"
ref_root = root / "docs/sources/reference"
tpl_root = root / "docs/sources/template"

ref_root.mkdir(parents=True, exist_ok=False)
tpl_root.mkdir(parents=True, exist_ok=False)

def write(src, dst):
    assert src.is_dir()
    dirname = src.resolve().name

    for script in src.glob("*.py"):
        path = (dst / script.stem).with_suffix(".md")
        if '__init__' in str(path):
            continue

        with open(path, "wt") as fp:
            fp.write(f"::: {dirname}.{script.stem}\n")

        print(f"> generated ref to {path}.")


write(src=root / "opskrift", dst=ref_root)
write(src=root / "templates", dst=tpl_root)
