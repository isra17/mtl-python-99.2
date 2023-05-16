#!/usr/bin/env -S ./py311
import enum
import asyncio

async def elements(n):
    yield n
    yield n*2

async def async_comprehension():
    return { n: [x async for x in elements(n)] for n in range(3)}

print(asyncio.run(async_comprehension()))

class PythonVersions(enum.StrEnum):
    py39 = "3.9.12"
    py310 = "3.11.6"
    py311 = "3.11.3"

def major(s: str) -> str: return s.split(".")[0]

print(major(PythonVersions.py311))
