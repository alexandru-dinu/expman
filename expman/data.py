from typing import *

import numpy as np
from toolz.itertoolz import take


def seed_everything(seed: Optional[int]) -> None:
    if seed is None:
        return

    random.seed(seed)
    np.random.seed(seed)
    T.manual_seed(seed)


def split_data(
    data: List[Any], train_f: float, test_f: float, shuffle: bool = False
) -> Dict[str, List[Any]]:
    """Get train / test / valid splits from `data`.
    If `shuffle` is True, then use a random permutation of `data`."""
    n = len(data)

    # use a generator to keep offset internally when taking elements
    if shuffle:
        rand_idx = np.random.permutation(n)
        gen = (data[i] for i in rand_idx)
    else:
        gen = (x for x in data)

    return {
        "train": list(take(int(n * train_f), gen)),  # take first
        "test": list(take(int(n * test_f), gen)),  # take next
        "valid": list(gen),  # take remaining
    }


def batchify(xs: np.ndarray, bs: int, func: callable = None):
    """
    Batchify `xs`. If `func` is not None, then the emitted item is `func(batch)`.
    """
    if not isinstance(bs, int) or not (1 <= bs <= len(xs)):
        raise ValueError(f"Batch size must be an int in [1, {xs.shape[0]}].")

    if not isinstance(xs, np.ndarray):
        xs = np.array(xs)

    if func is None:
        func = lambda x: x

    l = len(xs)
    for ndx in range(0, l, bs):
        yield func(xs[ndx : min(ndx + bs, l)])
