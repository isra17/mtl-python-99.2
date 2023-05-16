#!/usr/bin/env -S ./py311 -m mypy

from typing import TypedDict

class _MovieBase(TypedDict):  # implicitly total=True
    title: str

class Movie(_MovieBase, total=False):
    year: int

Movie(title="Star Wars")  # Works
Movie(year=1977)  # Error
