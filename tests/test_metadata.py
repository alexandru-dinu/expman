from unittest import TestCase

import pytest
from hypothesis import given
from hypothesis import strategies as st

from expman.metadata import Metadata


class TestLoader(TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_simple(self):
        meta = Metadata(foo="123", bar=[1, 2, 3])

        self.assertEqual(2, len(meta))
        self.assertIsInstance(meta.foo, str)
        self.assertIsInstance(meta.bar, list)

        self.assertEqual("123", meta["foo"])
        self.assertListEqual([1, 2, 3], meta["bar"])

        with pytest.raises(KeyError):
            _ = meta["nope"]

        with pytest.raises(AttributeError):
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
        meta = Metadata(**d)

        self.assertDictEqual(meta.to_dict(), d)
