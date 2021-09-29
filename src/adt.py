from dataclasses import dataclass
from typing import Union


@dataclass(frozen=True)  # OK Int
class OK:
    result: int


@dataclass(frozen=True)  # Failure String
class Failure:
    msg: str


# data Result = OK Int | Failure String
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
