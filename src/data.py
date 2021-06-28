from toolz.itertoolz import take
from typing import *


def seed_everything(seed: Optional[int]) -> None:
    # logger.info(f"Using {seed=}")
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
