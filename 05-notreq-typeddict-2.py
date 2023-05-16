#!/usr/bin/env -S ./py311 -m mypy
from typing import TypedDict, NotRequired

class Movie(TypedDict):
    title: str
    year: NotRequired[int]

movie = Movie(title="Star Wars")  # Works
Movie(year=1977)  # Error

# Caveas of "NotRequired":
print(movie["year"])  # Should fail.
