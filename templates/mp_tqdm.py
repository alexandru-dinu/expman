"""
Use `tqdm` in a `multiprocessing` environment.
Each worker has its own progress bar whose position is given by the worker idx.
"""

import functools
import multiprocessing as mp
import pickle
import time

import numpy as np
from tqdm import tqdm


def process(idx, **kwargs):
    data = kwargs.get("data")

    i, j = idx

    # n-th worker process in the pool
    worker_idx = mp.current_process()._identity[0] - 1

    with tqdm(
        total=data.shape[0],
        position=worker_idx,
        desc=f"{worker_idx:2d}",
        ascii=True,
        leave=False,
    ) as pbar:
        # simulate work...
        out = 0
        for k in range(data.shape[0]):
            out += data[k, i, j] / data.shape[0]

            time.sleep(np.random.uniform(0, 0.5))

            pbar.update(1)

    return out


def main():
    out = []

    data = np.random.uniform(size=(32, 100, 100))

    work_fn = functools.partial(process, data=data)
    work_args = zip(*np.random.randint(100, size=16).reshape(2, -1))

    with mp.Pool(
        processes=4, initializer=tqdm.set_lock, initargs=(tqdm.get_lock(),)
    ) as pool:
        for x in pool.imap_unordered(work_fn, work_args):
            out.append(x)

    with open("out.pkl", "wb") as fp:
        pickle.dump(out, fp)


if __name__ == "__main__":
    main()
