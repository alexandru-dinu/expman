"""
Modification of the https://github.com/JulienPalard/Pipe project
to support arbitrary objects as input.

See https://stackoverflow.com/a/69790644.
"""

from typing import Any

# A token to indicate the end of a pipe.
ExitPipe = None


class EnterPipe:
    """Processing using pipes.
    Wrap input value in `EnterPipe`, chain processing functions,
    then mark the end of the pipe using `ExitPipe`.

    Args:
        obj (Any): The wrapped pipe input object.

    Example:
    ```
    xs = np.array([1, 2, 3])
    ys = EnterPipe(xs) | (lambda x: 2 * x) | np.median | ExitPipe
    print(ys) # 4.0
    ```
    """

    def __init__(self, obj: Any):
        self._object = obj

    def __or__(self, other):
        if other is ExitPipe:
            return self._object

        if not callable(other):
            raise TypeError(f"pipe element '{other}' is not callable")

        return EnterPipe(other(self._object))


if __name__ == "__main__":
    import numpy as np

    xs = np.array([0, 22.5, 45, 90, 180])

    ys = (
        EnterPipe(xs)
        | (lambda x: 2 * x)
        | np.deg2rad
        | (lambda x: zip(x, np.cos(x)))
        | (lambda x: list(x))
        | (lambda x: np.round(x, 3))
        | (lambda x: dict(x))
        | ExitPipe
    )
    print(ys)
