import json
from typing import Any


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

    def _get_nested(self, ds: dict) -> dict:
        out = {}

        for k, v in ds.items():
            # nested
            if isinstance(v, Metadata):
                out[k] = "<self>" if v is self else self._get_nested(v.__dict__)

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
        return self._get_nested(self.__dict__)
