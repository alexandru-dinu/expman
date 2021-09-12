"""
Suppose you have some input data sources `data_in` on which you apply some process `F` parameterized by `args`:

    data_out = F(data_in, args)

You want to serialize `data_out`, but also don't want to lose `args`,
to preserve the exact setup that generated the output data.

Now suppose you want to inspect `args` for a particular `data_out`:
- Saving both `{"data": data_out, "args": args}` may not be a viable solution,
as `data_out` needs to be fully loaded into memory without actually needing it.
- Saving `data_out` and `args` separately necessitates extra care to keep them tied together.

Solution: define a simple data format -- *augmented pickle*

    <metadata>
    <body (actual data)>

Pickle both objects, but read body on-demand:

    res = read_augmented_pickle("./data.apkl", get_metadata=True, get_body=True)

    # get metadata (body is not loaded)
    meta = next(res)

    # query the generator again to get body (data)
    data = next(res)
"""

from datetime import datetime
from unittest import TestCase

import numpy as np
from omegaconf import OmegaConf

from src.augmented_pickle import read_augmented_pickle, write_augmented_pickle


class TestLoader(TestCase):
    @staticmethod
    def dump(path: str):
        meta = OmegaConf.create()

        meta.params = {"margin": 1.0, "distance": "euclidean", "shape": (8, 128)}
        meta.input_path = "/foo/bar/baz.apkl"
        meta.generated_on = int(datetime.now().timestamp())

        b, n = meta.params.shape

        data = {
            "train": np.random.uniform(0, 1, size=(b, n)),
            "test": np.random.uniform(0, 1, size=(b, n)),
            "valid": np.random.uniform(0, 1, size=(b, n)),
        }

        meta = OmegaConf.to_container(meta, resolve=True)

        write_augmented_pickle(
            metadata=meta,
            body=data,
            path=path,
        )
        return meta, data

    @staticmethod
    def load(path):
        # generator containing (metadata, body)
        res = read_augmented_pickle(path, get_metadata=True, get_body=True)

        # get metadata (body is not loaded)
        meta = next(res)

        # if body is needed, query the generator again
        data = next(res)

        return meta, data

    def test_dump_and_load(self):
        path = "/tmp/foo.apkl"
        meta1, data1 = self.dump(path)
        meta2, data2 = self.load(path)

        self.assertDictEqual(meta1, meta2)

        for k in data1.keys():
            self.assertTrue(np.allclose(data1[k], data2[k]))
