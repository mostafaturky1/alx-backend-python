#!/usr/bin/env python3
'''Task 1's module.
'''
import asyncio
import random


async def async_generator():
    '''An asynchronous generator that yields numbers from 0 to 9.
    '''
    for i in range(10):
        await asyncio.sleep(1)
        rand = random.uniform(0, 10)
        yield rand
