from collections.abc import MutableMapping
from typing import Any, Dict, List, Tuple


def flatten(obj: MutableMapping, sep: str, name: str = None) -> MutableMapping:
    """Flatten dictionary by combining nested keys with given separator."""
    items: List[Tuple[str, Any]] = []

    for k, v in obj.items():
        new_key = name + sep + k if name else k
        if isinstance(v, MutableMapping):
            items.extend(flatten(v, sep=sep, name=new_key).items())
        else:
            items.append((new_key, v))

    return dict(items)


def unflatten(obj: Dict[str, Any], sep: str) -> Dict[Any, Any]:
    """Construct a nested dictionary by splitting keys on given separator."""
    out: Dict[str, Any] = {}

    for key, value in obj.items():
        *init, last = key.split(sep)
        d = out

        for k in init:
            if k not in d:
                d[k] = {}

            d = d[k]

        d[last] = value

    return out
