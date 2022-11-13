from hypothesis import HealthCheck, given, settings
from hypothesis import strategies as st

import opskrift.dict_utils as du


@settings(suppress_health_check=(HealthCheck.too_slow,))
@given(
    st.recursive(
        base=st.dictionaries(
            keys=st.text(min_size=1, max_size=1024).filter(lambda k: "/" not in k),
            values=st.booleans() | st.floats() | st.integers() | st.text(),
            min_size=1,
        ),
        extend=lambda children: st.dictionaries(
            keys=st.text(min_size=1, max_size=1024).filter(lambda k: "/" not in k),
            values=children,
            min_size=1,
        ),
        max_leaves=10,
    )
)
def test_flatten_unflatten(obj: dict):
    sep = "/"
    assert obj == du.unflatten(du.flatten(obj, sep), sep)
