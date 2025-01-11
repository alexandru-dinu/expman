import hypothesis.extra.numpy as hnp
import hypothesis.strategies as st
import numpy as np
from hypothesis import given

from ml_recipes.pipe import EnterPipe, ExitPipe


@given(
    hnp.arrays(
        dtype=float,
        shape=hnp.array_shapes(min_dims=1, max_dims=5, min_side=1, max_side=10),
        elements=st.floats(min_value=-10, max_value=10),
    )
)
def test_simple(xs: np.ndarray):
    f1 = lambda x: x * np.pi
    f2 = lambda x: x[x >= 0.5]
    f3 = lambda x: np.nan if x.size == 0 else np.median(x)

    ys1 = f3(f2(f1(xs)))
    ys2 = EnterPipe(xs) | f1 | f2 | f3 | ExitPipe

    assert np.allclose(ys1, ys2, equal_nan=True)
