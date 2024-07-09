#!/usr/bin/env python3
'''Task 1's module.
'''
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    '''An asynchronous generator that yields numbers from 0 to 9.
    '''
    for i in range(10):
        await asyncio.sleep(1) 
        yield random.uniform(0, 10)
