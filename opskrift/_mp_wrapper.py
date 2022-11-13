import argparse
import functools
from typing import Dict, List

# example
OutputType = Dict[str, List[int]]


def processing_func(x, data, foo, bar) -> OutputType:
    """
    This function does not know anything about CLI args.
    """

    out = {"foo": [1, 2, 3]}

    return out


def _wrapper(x, **kwargs):
    """
    This wrapper may use CLI args.
    """
    foo = kwargs.get("foo")
    bar = kwargs.get("bar")

    try:
        data = load(cli_args.input_file_path)
        out = processing_func(x, data, foo, bar)
    except:
        logger.warning(...)
        out = {}

    return x, out


def main():
    # work_fn :: type(x) -> (type(x), OutputType)
    work_fn = functools.partial(
        _wrapper,
        foo=foo,
        bar=bar,
    )
    work_args = [x for x in ...]

    with mp.Pool(num_processes) as pool:
        for x, out in pool.imap_unordered(work_fn, work_args):
            ...


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    ...
    cli_args = parser.parse_args()

    main()
