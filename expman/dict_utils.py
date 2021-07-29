from functools import reduce
from typing import *


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


def get_by_path(data: Dict[Union[str, float], Any], key_path: List[str]) -> Any:
    """Traverse dict using `key_path`."""
    return reduce(lambda d, k: d[try_num(k)], key_path, data)


def set_by_path(
    data: Dict[Union[str, float], Any],
    key_path: List[str],
    value: str,
    create_non_existent: bool,
) -> bool:
    """Set value in sub dict given by `key_path`.
    If `create_non_existent` is True, then creates key, assuming it does not exist.
    Returns True / False depending on whether set was successful.
    """
    *init, last = map(try_num, key_path)

    sub_dict = data

    for k in init:
        if k not in sub_dict:
            # k is the first key that does not exist in dict;
            # if there's no intention to create it, don't do anything,
            # otherwise continue to create sub dicts
            if not create_non_existent:
                return False
            sub_dict[k] = {}

        sub_dict = sub_dict[k]

    # here we are at the final nesting level
    # only update the key if required
    if last not in sub_dict and not create_non_existent:
        return False

    sub_dict[last] = try_num(value)
    return True
