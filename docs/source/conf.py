# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.

import os
import sys
from pathlib import Path
import time

sys.path.insert(0, os.path.abspath("../.."))


# -- Project information -----------------------------------------------------

project = "expman"
copyright = time.strftime("%Y, Alexandru Dinu")
author = "Alexandru Dinu"


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.autodoc",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "furo"
html_title = "expman"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]


# -- Auto-generated code
module_root = Path(__file__).resolve().parents[2] / "expman"
ref_root = Path("./reference")
ref_root.mkdir(exist_ok=True)


def generate_references():
    def template(x: str) -> str:
        return "\n".join(
            [f"{x}", "=" * len(x), '', f".. automodule :: {x}", f"{' ' * 3}:members:"]
        )

    reference = [
        "Reference",
        "=========",
        "\n",
        ".. toctree ::" f"{' ' * 3}:maxdepth: 3",
        "\n",
    ]

    for py in module_root.glob("*.py"):
        module = py.stem
        ref = template(f"expman.{module}")
        with open(ref_root / f"{module}.rst", "wt") as fp:
            fp.write(ref)
        print(f"> wrote ref for {module}")

    with open("reference.rst", "wt") as fp:
        for rst in ref_root.glob("*.rst"):
            reference.append(f"\n{' ' * 3}{rst}")
        fp.write("\n".join(reference))
    print("> wrote reference.rst")


generate_references()
