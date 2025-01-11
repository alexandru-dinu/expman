from __future__ import annotations

from typing import *

"""
Maybe Monad
https://stackoverflow.com/questions/28607666/maybe-monad-in-python-with-method-chaining
"""


a = TypeVar("a")
b = TypeVar("b")


class Maybe:
    def __init__(self, value: Optional[a], err: Optional[Exception] = None):
        self.value = value
        self.err = err

    @classmethod
    def unit(cls, *args, **kwargs) -> "Maybe":
        return cls(*args, **kwargs)

    def unwrap(self) -> a | Exception:
        if self.value is not None:
            assert self.err is None
            return self.value
        else:
            assert self.err is not None
            return self.err

    def bind(self, func: Callable) -> "Maybe":
        """
        Call `func` on the wrapped value, storing and propagating the exception if any.
        This has the effect of "fail-on-first-error".

        Similar to Haskell's `(>>=) :: Monad m => m a -> (a -> m b) -> m b`
        """
        if self.value is None:
            return self

        try:
            return Maybe(func(self.value), err=None)
        except Exception as e:
            return Maybe(value=None, err=e)

    def __str__(self):
        if self.value is None:
            if self.err is not None:
                return f"Except ({self.err})"
            else:
                return "Nothing"
        return f"Just ({self.value})"

    __repr__ = __str__


if __name__ == "__main__":
    import numpy as np

    out = (
        Maybe.unit(np.array([1, 2, 3])).bind(lambda x: x * 0.5).bind(lambda x: x.median())
    ).unwrap()
    print(f"{type(out)}: {out}")

    out = (
        Maybe.unit(np.array([1, 2, 3]))
        .bind(lambda x: x * 0.5)
        .bind(lambda x: (np.median(x), np.mean(x)))
    ).unwrap()
    print(f"{type(out)}: {out}")
