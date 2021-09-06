from dataclasses import dataclass
from functools import singledispatch
from typing import Union

# from https://stackoverflow.com/a/64578832

"""
-- Haskell

data Shape
    = Point Float Float -- x y
    | Circle Float Float Float -- x y r
    | Rectangle Float Float Float Float -- x y w h
"""


@dataclass
class Point:
    x: float
    y: float


@dataclass
class Circle:
    x: float
    y: float
    r: float


@dataclass
class Rectangle:
    x: float
    y: float
    w: float
    h: float


Shape = Union[Point, Circle, Rectangle]


"""
# naive if-else pattern matching

def print_shape(shape: Shape):
    if isinstance(shape, Point):
        print(f"Point {shape.x} {shape.y}")

    elif isinstance(shape, Circle):
        print(f"Circle {shape.x} {shape.y} {shape.r}")

    elif isinstance(shape, Rectangle):
        print(f"Rectangle {shape.x} {shape.y} {shape.w} {shape.h}")
"""

# 2) singledispatch
@singledispatch
def show_shape(shape: Shape):
    print(f"Shape: {shape}")


@show_shape.register
def _(shape: Point):
    print(f"Point {shape.x} {shape.y}")


@show_shape.register
def _(shape: Circle):
    print(f"Circle {shape.x} {shape.y} {shape.r}")


@show_shape.register
def _(shape: Rectangle):
    print(f"Rectangle {shape.x} {shape.y} {shape.w} {shape.h}")


# from http://blog.ezyang.com/2020/10/idiomatic-algebraic-data-types-in-python-with-dataclasses-and-union/


"""
-- Haskell

data Result = OK Int | Failure String

showResult :: Result -> String
showResult (OK result) = show result
showResult (Failure msg) = "Failure: " ++ msg
"""


@dataclass(frozen=True)  # OK Int
class OK:
    result: int


@dataclass(frozen=True)  # Failure String
class Failure:
    msg: str


Result = Union[OK, Failure]
# data Result = OK Int | Failure String


def assert_never(x: NoReturn) -> NoReturn:
    raise AssertionError("Unhandled type: {}".format(type(x).__name__))


def showResult(r: Result) -> str:
    if isinstance(r, OK):
        return str(r.result)

    if isinstance(r, Failure):
        return "Failure: " + r.msg

    assert_never(r)


if __name__ == "__main__":
    s1 = Point(x=1, y=-2)
    s2 = Circle(x=0, y=0, r=3.14)
    s3 = Rectangle(x=0, y=-2, w=10, h=11)

    for s in [s1, s2, s3]:
        show_shape(s)
