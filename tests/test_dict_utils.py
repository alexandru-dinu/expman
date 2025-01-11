from __future__ import annotations

from typing import Any

from hypothesis import given
from hypothesis import strategies as st

import ml_recipes.dict_utils as du
from tests.utils import build_tree


@given(st.lists(st.booleans() | st.floats() | st.integers() | st.text(), min_size=0, max_size=1024))
def test_flatten_unflatten(xs: list[Any]):
    tree = build_tree(xs)
    sep = "/"
    assert tree == du.unflatten(du.flatten(tree, sep), sep)
