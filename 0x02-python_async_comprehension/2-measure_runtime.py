#!/usr/bin/env python3
'''Task 1's module.
'''
import asyncio
import time


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Asynchronously measures the runtime of multiple instances of
    the async_comprehension function.
    """
    startime = time.time()
    task = (async_comprehension(), async_comprehension(),
            async_comprehension(), async_comprehension())
    await asyncio.gather(*task)
    endtime = time.time()
    return endtime - startime
