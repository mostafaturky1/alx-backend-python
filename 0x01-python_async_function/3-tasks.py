#!/usr/bin/env python3
'''Task 1's module.
'''
import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int):
    '''Creates a coroutine that waits for a random amount of time between 0
    and `max_delay` seconds and returns the time in seconds.
    '''
    return asyncio.create_task(wait_random(max_delay))
