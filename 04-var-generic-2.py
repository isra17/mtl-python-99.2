#!/usr/bin/env -S ./py311 -m mypy --enable-incomplete-feature=Unpack --enable-incomplete-feature=TypeVarTuple
from typing import TypeVarTuple, Generic, Unpack, Literal

Shape = TypeVarTuple('Shape')

class Array(Generic[Unpack[Shape]]):
    pass


def pointwise_multiply(
    x: Array[Unpack[Shape]],
    y: Array[Unpack[Shape]]
) -> Array[Unpack[Shape]]: return x or y

x: Array[Literal[100]] = Array()
y: Array[Literal[42]] = Array()
z: Array[Literal[100], Literal[42]] = Array()

pointwise_multiply(x, x)  # Valid
pointwise_multiply(z, z)  # Error
pointwise_multiply(x, y)  # Error
pointwise_multiply(x, z)  # Error
