from toolz.itertoolz import take
from typing import *


def seed_everything(seed: Optional[int]) -> None:
    # logger.info(f"Using {seed=}")
    if seed is None:
        return

    random.seed(seed)
    np.random.seed(seed)
    T.manual_seed(seed)


def split_data(data: List[Any], train_f: float, test_f: float) -> Dict[str, List[Any]]:
    n = len(data)
    gen = (x for x in data)  # to keep offset internally

    return {
        "train": list(take(int(n * train_f), gen)),  # take first
        "test": list(take(int(n * test_f), gen)),  # take next
        "valid": list(gen),  # take remaining
    }
