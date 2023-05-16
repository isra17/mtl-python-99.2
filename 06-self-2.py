#!/usr/bin/env -S ./py311 -m mypy
from typing import Self

class Parent:
    def copy(self) -> Self:
        return self

class Child(Parent):
    def copy(self) -> Self:
        return self

child: Child = Child().copy()
