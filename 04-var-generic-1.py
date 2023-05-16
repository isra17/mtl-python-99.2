#!/usr/bin/env -S ./py311 -m mypy --enable-incomplete-feature=Unpack --enable-incomplete-feature=TypeVarTuple
from typing import TypeVarTuple, Callable, Tuple, Unpack

Ts = TypeVarTuple('Ts')

class Process:
  def __init__(
    self,
    target: Callable[[Unpack[Ts]], None],
    args: Tuple[Unpack[Ts]],
  ) -> None: ...

def func(arg1: int, arg2: str) -> None: ...

Process(target=func, args=(0, 'foo'))  # Valid
Process(target=func, args=('foo', 0))  # Error
