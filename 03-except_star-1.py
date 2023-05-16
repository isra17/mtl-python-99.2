#!/usr/bin/env python

import asyncio

async def do_work_1():
    raise ValueError("Nope")

async def do_work_2():
    raise ValueError("yes!")

async def do_work_3():
    return {}["Key"]

async def main():
    try:
        async with asyncio.TaskGroup() as tg:
            tg.create_task(do_work_1())
            tg.create_task(do_work_2())
            tg.create_task(do_work_3())
    except* ValueError as eg:
        print("Catched ValueError: ", eg.exceptions)
        print("---------------------------")
    except* KeyError as eg:
        print("Catched KeyError: ", eg.exceptions)
        print("---------------------------")


asyncio.run(main())
