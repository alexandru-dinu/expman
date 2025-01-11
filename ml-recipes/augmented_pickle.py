"""
Suppose you have some input data sources `data_in`
on which you apply some process `F` parameterized by `args`:

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

    res = read_augmented_pickle("./data.apkl", get_body=True)

    # get metadata (body is not loaded)
    meta = next(res)

    # query the generator again to get body (data)
    data = next(res)
"""

from __future__ import annotations

import pickle
from os import PathLike
from typing import Any, Iterable


def write_augmented_pickle(
    metadata: Any,
    body: Any,
    path: str | PathLike,
) -> None:
    """Write an augmented pickle file containing `metadata` and `body`."""
    with open(path, "wb") as fp:
        pickle.dump(metadata, fp)
        pickle.dump(body, fp)


def read_augmented_pickle(
    path: str | PathLike,
    get_body: bool,
) -> Iterable[Any]:
    """Read an augmented pickle file containing `metadata` and `body`.
    Returns a generator that can be queried on-demand using `next`.
    If `get_body` is False, only `metadata` is yielded.
    """
    with open(path, "rb") as fp:
        metadata = pickle.load(fp)

        yield metadata

        if not get_body:
            return

        body = pickle.load(fp)

    yield body
