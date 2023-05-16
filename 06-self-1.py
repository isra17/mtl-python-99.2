#!/usr/bin/env -S ./py311 -m mypy

class Parent:
    def copy(self) -> "Parent":
        return self

class Child(Parent):
    def copy(self) -> "Child":
        return self

child: Child = Child().copy()
