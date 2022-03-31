# -*- coding: utf-8 -*-
import asyncio


@asyncio.coroutine
def get_body(i):
    print(f"start{i}")
    yield from asyncio.sleep(1)
    print(f"end{i}")


loop = asyncio.get_event_loop()
tasks = [get_body(i) for i in range(5)]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
