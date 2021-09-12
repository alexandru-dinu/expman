from collections.abc import Iterable
from unittest import TestCase

import pytest
from hypothesis import given
from hypothesis import strategies as st
from omegaconf import OmegaConf
from omegaconf.errors import ConfigAttributeError, ConfigKeyError


class TestLoader(TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_simple(self):
        meta = OmegaConf.create({"foo": "123", "bar": [1, 2, 3]})

        self.assertEqual(2, len(meta))
        self.assertIsInstance(meta.foo, str)
        self.assertIsInstance(meta.bar, Iterable)

        self.assertTrue("123" == meta["foo"] == meta.foo)
        self.assertTrue([1, 2, 3] == meta.bar)

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
    def test_random(self, d):
        meta = OmegaConf.create(d)

        self.assertDictEqual(OmegaConf.to_container(meta, resolve=True), d)
