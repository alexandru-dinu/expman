import pickle
from os import PathLike
from typing import Any, Iterable, Union


def write_augmented_pickle(
    metadata: Any,
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
) -> Iterable[Union[Any, Any]]:
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
