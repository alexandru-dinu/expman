import argparse
import errno
import os
from pathlib import Path
from typing import Union


def args_path_ensure_exists(file_path: str) -> Path:
    """Returns a `Path` object containing the resolved `file_path`.
    Raises `FileNotFoundError` if the path does not exist.
    """
    path = Path(file_path).resolve()

    if not path.exists():
        raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), str(path))

    return path


def _args_list_example(x: str) -> Union[str, int]:
    """When applied to an arg with `nargs="+"`, this function is called for each value in arg."""
    return int(x) if ord(x) % 2 else str(x)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--foo", type=args_path_ensure_exists, required=False)
    parser.add_argument("--bar", type=_args_list_example, nargs="+", required=False)
    args = parser.parse_args()

    print(args.bar)
