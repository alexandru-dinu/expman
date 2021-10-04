"""
Simple example of Abstract Data Types in Python.

In Haskell we would write:

    data Result = OK Int | Failure String

In Python we can do:

    Result = Union[OK, Failure]

where `OK` and `Failure` are frozen dataclasses.
"""

from dataclasses import dataclass
from typing import Union


# OK Int
@dataclass(frozen=True)
class OK:
    result: int


# Failure String
@dataclass(frozen=True)
class Failure:
    msg: str


Result = Union[OK, Failure]


def show_result(r: Result) -> str:
    if isinstance(r, OK):
        return str(r.result)

    if isinstance(r, Failure):
        return "Failure: " + r.msg

    raise AssertionError(f"Unhandled type: {type(r).__name__}")


if __name__ == "__main__":
    print(show_result(OK(42)))
    print(show_result(Failure("Nope.")))
