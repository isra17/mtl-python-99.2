#!/usr/bin/env -S ./py311 -m mypy
from typing import Self

class Parent:
    @classmethod
    def make(cls) -> Self:
        return cls()

class Child(Parent):
    @classmethod
    def make(cls) -> Self:
        return cls()

child: Child = Child.make()
