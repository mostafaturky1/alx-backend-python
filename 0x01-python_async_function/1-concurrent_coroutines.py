#!/usr/bin/env python3
'''Task 0's module.
'''
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n, max_delay):
    '''
    This function waits for a random amount of
    time between 0 and max_delay (inclusive)
    for a specified number of times (n).
    It appends the wait times to a list and returns
    the list after all the waits are completed.

    Parameters:
    n (int): The number of times to wait for a random amount of time.
    max_delay (int): The maximum delay in seconds.

    Returns:
    list: A list containing the wait times for each iteration.
    '''
    list_wait_times = []
    for i in range(n):
        list_wait_times.append(* await asyncio.gather(wait_random(max_delay)))
    return sorted(list_wait_times)
