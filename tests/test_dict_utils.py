from unittest import TestCase

from hypothesis import given, settings
from hypothesis import strategies as st

import expman.dict_utils as du


class TestLoader(TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    @given(
        st.recursive(
            base=st.dictionaries(
                keys=st.text(min_size=1).filter(lambda k: "/" not in k),
                values=st.booleans() | st.floats() | st.integers() | st.text(),
                min_size=1,
            ),
            extend=lambda children: st.dictionaries(
                keys=st.text(min_size=1).filter(lambda k: "/" not in k),
                values=children,
                min_size=1,
            ),
            max_leaves=10,
        )
    )
    def test_flatten_unflatten(self, obj: dict):
        sep = "/"
        self.assertDictEqual(obj, du.unflatten(du.flatten(obj, sep), sep))
