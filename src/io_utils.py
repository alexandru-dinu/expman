import json
import pickle
from os import PathLike
from typing import Any, Iterable, Union


class Metadata:
    """
    Represent meta-information about experiments and files.
    """

    def __init__(self, **kwargs):
        self.__dict__.update({k: self._traverse(v) for k, v in kwargs.items()})

    def __str__(self):
        return json.dumps(self._get_nested(), indent=4)

    def __repr__(self):
        return str(self)

    def __len__(self):
        return len(self.__dict__)

    def __getitem__(self, key: str) -> Any:
        return self.__dict__[key]

    def _traverse(self, xs):
        if isinstance(xs, dict):
            return Metadata(**xs)

        if isinstance(xs, (list, tuple)):
            return [self._traverse(x) for x in xs]

        return xs

    def _get_nested(self) -> dict:
        out = {}

        for k, v in self.__dict__.items():
            # nested
            if isinstance(v, Metadata):
                out[k] = "<self>" if v is self else self._get_nested(v)

            # non-primitive type, call its str method
            elif hasattr(v, "__dict__"):
                out[k] = str(v)

            # primitives
            else:
                out[k] = v

        return out

    def is_empty(self):
        return len(self) == 0

    def to_dict(self) -> dict:
        return self._get_nested()


def write_pickle(
    metadata: Metadata,
    body: Any,
    path: Union[str, PathLike],
) -> None:
    """
    Write an augmented pickle file containing both <metadata|body>.
    """
    with open(path, "wb") as fp:
        pickle.dump(metadata, fp)
        pickle.dump(body, fp)


def read_pickle(
    path: Union[str, PathLike],
    get_metadata: bool,
    get_body: bool,
) -> Iterable[Union[Metadata, Any]]:
    """
    Read an augmented pickle file containing both <metadata|body>.
    Returns a generator that can be queried on-demand using "next".
    """
    with open(path, "rb") as fp:
        metadata = pickle.load(fp)
        if get_metadata:
            yield metadata

        if not get_body:
            return

        body = pickle.load(fp)

    yield body
