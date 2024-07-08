#!/usr/bin/env python3
'''Task 0's module.
'''
import asyncio
import random


async def wait_random(max_delay: float = 10):
    """
    Asynchronously waits for a random amount of time between 0
    and `max_delay` seconds.

    Parameters:
    max_delay (float, optional): The maximum delay in seconds. Defaults to 10.

    Returns:
    float: The actual delay time in seconds.
    """
    rendtime: float = random.uniform(0, max_delay)
    await asyncio.sleep(rendtime)
    return float(rendtime)
