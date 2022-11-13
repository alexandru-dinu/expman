from datetime import datetime

import numpy as np
from omegaconf import OmegaConf

from opskrift.augmented_pickle import read_augmented_pickle, write_augmented_pickle


def dump(path: str):
    meta = OmegaConf.create()

    meta.params = {"margin": 1.0, "distance": "euclidean", "shape": (8, 128)}
    meta.input_path = "/foo/bar/baz.apkl"
    meta.generated_on = int(datetime.now().timestamp())

    b, n = meta.params["shape"]

    data = {
        "train": np.random.uniform(0, 1, size=(b, n)),
        "test": np.random.uniform(0, 1, size=(b, n)),
        "valid": np.random.uniform(0, 1, size=(b, n)),
    }

    meta_dict = OmegaConf.to_container(meta, resolve=True)

    write_augmented_pickle(
        metadata=meta_dict,
        body=data,
        path=path,
    )
    return meta_dict, data


def load(path):
    # generator containing (metadata, body)
    res = read_augmented_pickle(path, get_body=True)

    # get metadata (body is not loaded)
    meta = next(res)

    # if body is needed, query the generator again
    data = next(res)

    return meta, data


def test_dump_and_load():
    path = "/tmp/foo.apkl"
    meta1, data1 = dump(path)
    meta2, data2 = load(path)

    assert meta1 == meta2

    for k in data1.keys():
        assert np.allclose(data1[k], data2[k])
