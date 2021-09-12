import os
from datetime import datetime

import numpy as np
from omegaconf import OmegaConf

from augmented_pickle import read_augmented_pickle, write_augmented_pickle


def dump():
    meta = OmegaConf.create()

    meta.params = {"margin": 1.0, "distance": "euclidean", "shape": (8, 128)}
    meta.input_path = "/foo/bar/baz.pkl"
    meta.generated_on = int(datetime.now().timestamp())

    b, n = meta.params.shape

    data = {
        "train": np.random.uniform(0, 1, size=(b, n)),
        "test": np.random.uniform(0, 1, size=(b, n)),
        "valid": np.random.uniform(0, 1, size=(b, n)),
    }

    write_augmented_pickle(
        metadata=OmegaConf.to_container(meta, resolve=True),
        body=data,
        path="./data.pkl",
    )


def load():
    # generator containing (metadata, body)
    res = read_augmented_pickle("./data.pkl", get_metadata=True, get_body=True)

    # get metadata (body is not loaded)
    meta = next(res)
    print(meta)

    # if body is needed, query the generator again
    data = next(res)
    for k, v in data.items():
        print(k, v.shape)


def main():
    dump()
    print("Dumped augmented pickle to ./data.pkl.")

    load()
    print("Loaded augmented pickle from ./data.pkl.")

    os.unlink("data.pkl")


if __name__ == "__main__":
    main()
