import hypothesis.strategies as st
import numpy as np
from hypothesis import given

from opskrift.pipe import EnterPipe, ExitPipe


@given(st.integers(min_value=0, max_value=2**10), st.floats(min_value=0, max_value=1))
def test_simple(n, thr):
    xs = np.random.uniform(0, 1, size=n)
    f1 = lambda x: 2 * x
    f2 = lambda x: x[x >= thr]
    f3 = np.median

    ys1 = f3(f2(f1(xs)))
    ys2 = EnterPipe(xs) | f1 | f2 | f3 | ExitPipe

    assert np.allclose(ys1, ys2, equal_nan=True)
