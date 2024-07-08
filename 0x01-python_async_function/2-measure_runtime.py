#!/usr/bin/env python3
'''Task 1's module.
'''
import asyncio
import time


wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the average time taken by 'wait_n' function to
    complete 'n' coroutines,
    each with a random delay between 0 and 'max_delay' seconds.

    Parameters:
    n (int): The number of coroutines to run.
    max_delay (int): The maximum delay in seconds for each coroutine.

    Returns:
    float: The average time taken by 'wait_n' function to complete
    all coroutines.
    """
    start_time = time.time()
    await asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
    elapsed_time = end_time - start_time
    return elapsed_time / n
