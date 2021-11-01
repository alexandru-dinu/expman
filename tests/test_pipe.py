from unittest import TestCase

import hypothesis.strategies as st
import numpy as np
from hypothesis import given

from src.pipe import EnterPipe, ExitPipe


class TestLoader(TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    @given(
        st.integers(min_value=0, max_value=2 ** 10), st.floats(min_value=0, max_value=1)
    )
    def test_simple(self, n, thr):
        xs = np.random.uniform(0, 1, size=n)
        f1 = lambda x: 2 * x
        f2 = lambda x: x[x >= thr]
        f3 = np.median

        ys1 = f3(f2(f1(xs)))
        ys2 = EnterPipe(xs) | f1 | f2 | f3 | ExitPipe

        self.assertTrue(np.allclose(ys1, ys2, equal_nan=True))
