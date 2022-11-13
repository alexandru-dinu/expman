from __future__ import annotations

from collections.abc import Iterable
from typing import Any

import pytest
from hypothesis import given
from hypothesis import strategies as st
from omegaconf import OmegaConf
from omegaconf.errors import ConfigAttributeError, ConfigKeyError

from tests.utils import build_tree


def test_simple():
    meta = OmegaConf.create({"foo": "123", "bar": [1, 2, 3]})

    assert len(meta) == 2
    assert isinstance(meta.foo, str)
    assert isinstance(meta.bar, Iterable)

    assert "123" == meta["foo"] == meta.foo
    assert [1, 2, 3] == meta.bar

    with pytest.raises(ConfigKeyError):
        _ = meta["nope"]

    with pytest.raises(ConfigAttributeError):
        _ = meta.nope


@given(st.lists(st.booleans() | st.floats() | st.integers() | st.text(), min_size=0, max_size=1024))
def test_random(xs: list[Any]):
    tree = build_tree(xs)
    meta = OmegaConf.create(tree)
    assert tree == OmegaConf.to_container(meta, resolve=True)
