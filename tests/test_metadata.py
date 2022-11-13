from collections.abc import Iterable

import pytest
from hypothesis import given
from hypothesis import strategies as st
from omegaconf import OmegaConf
from omegaconf.errors import ConfigAttributeError, ConfigKeyError


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


@given(
    st.recursive(
        base=st.dictionaries(
            keys=st.text(min_size=1),
            values=st.booleans() | st.floats() | st.integers() | st.text(),
            min_size=1,
        ),
        extend=lambda children: st.dictionaries(
            keys=st.text(min_size=1),
            values=children,
            min_size=1,
        ),
        max_leaves=10,
    )
)
def test_random(d):
    meta = OmegaConf.create(d)

    assert d == OmegaConf.to_container(meta, resolve=True)
