#!/usr/bin/env python3
'''Task 1's module.
'''
import asyncio
import time


wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    '''Computes the average runtime of wait_n.
    '''
    start_time = time.time()
    await asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
    elapsed_time = end_time - start_time
    return elapsed_time / n
