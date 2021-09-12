from collections.abc import MutableMapping
from typing import Any, Dict


def flatten(obj: Dict[Any, Any], sep: str, name: str = None) -> Dict[str, Any]:
    """
    Flatten dictionary by combining nested keys with given separator.
    """
    # TODO: hide `name` arg.
    flat: Dict[str, Any] = {}

    if not isinstance(obj, MutableMapping):
        flat[name] = obj
    else:
        for key, value in obj.items():
            flat.update(
                flatten(
                    obj=value,
                    sep=sep,
                    name=(key if name is None else f"{name}{sep}{key}"),
                ),
            )

    return flat


def unflatten(obj: Dict[str, Any], sep: str) -> Dict[Any, Any]:
    """
    Construct a nested dictionary by splitting keys on given separator.
    """
    out = {}

    for key, value in obj.items():
        *init, last = key.split(sep)
        d = out

        for k in init:
            if k not in d:
                d[k] = {}
            d = d[k]

        d[last] = value

    return out
