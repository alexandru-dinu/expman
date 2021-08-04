from typing import Any, Callable, Dict, Iterator, List

import numpy as np
from toolz import itertoolz


def split_data(
    data: List[Any], train_f: float, test_f: float, shuffle: bool = False
) -> Dict[str, List[Any]]:
    """Get `train / test / valid` splits from `data`.
    If `shuffle` is True, then use a random permutation of `data`.
    `valid` split size is given by `(1 - train_f - test_f) * len(data)`.

    Args:
        data (List[Any]): Any collection of items to be split.
        train_f (float): Train size factor from the entire length (must be between 0 and 1).
        test_f (float): Test size factor from the entire length (must be between 0 and 1).
        shuffle (bool): Whether to use a random permutation of `data`.

    Returns:
        Dict[str, List[Any]]: Keys are {train, test, valid}, and values are corresponding splits
    """
    n = len(data)

    # use a generator to keep offset internally when taking elements
    if shuffle:
        rand_idx = np.random.permutation(n)
        gen = (data[i] for i in rand_idx)
    else:
        gen = (x for x in data)

    return {
        "train": list(itertoolz.take(int(n * train_f), gen)),  # take first
        "test": list(itertoolz.take(int(n * test_f), gen)),  # take next
        "valid": list(gen),  # take remaining
    }


def batchify(
    data: np.ndarray, batch_size: int, func: Callable[[np.ndarray], np.ndarray] = None
) -> Iterator[np.ndarray]:
    """Batchify `data`. If `func` is not None, then the emitted item is `func(batch)`.

    Args:
        data (np.ndarray): NumPy array of items to batchify.
        batch_size (int): Batch size; must be between 1 and `len(data)`.
        func (Callable[[np.ndarray], np.ndarray], optional): Optional function to apply to each emitted batch.
            Defaults to identity function.

    Returns:
        Iterator[np.ndarray]: Generator object containing batches.
    """
    if not isinstance(batch_size, int) or not (1 <= batch_size <= len(data)):
        raise ValueError(f"Batch size must be an int in [1, {data.shape[0]}].")

    if not isinstance(data, np.ndarray):
        data = np.array(data)

    if func is None:
        func = lambda x: x

    n = len(data)
    for i in range(0, n, batch_size):
        yield func(data[i : min(i + batch_size, n)])
