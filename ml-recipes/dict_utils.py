from __future__ import annotations

from typing import Any


def flatten(obj: dict[str, Any], sep: str, name: str | None = None) -> dict[str, Any]:
    """Flatten dictionary by combining nested keys with given separator."""
    items: list[tuple[str, Any]] = []

    for k, v in obj.items():
        new_key = f"{name}{sep}{k}" if name else k
        if not isinstance(v, dict) or len(v) == 0:
            items.append((new_key, v))
        else:
            items.extend(flatten(v, sep=sep, name=new_key).items())

    return dict(items)


def unflatten(obj: dict[str, Any], sep: str) -> dict[str, Any]:
    """Construct a nested dictionary by splitting keys on given separator."""
    out: dict[str, Any] = {}

    for key, value in obj.items():
        *init, last = key.split(sep)
        d = out

        for k in init:
            if k not in d:
                d[k] = {}

            d = d[k]

        d[last] = value

    return out
