#!/usr/bin/env -S ./py311 -m mypy
from typing import LiteralString

def execute(s: LiteralString) -> None: ...

execute("my-safe-command")  # Ok

command: str = input()
execute(command)  # Error?
