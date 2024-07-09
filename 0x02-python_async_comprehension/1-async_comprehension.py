#!/usr/bin/env python3
'''Task 1's module.
'''
import asyncio
import random
from typing import List


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    '''An asynchronous comprehension that generates a list of
    numbers from 0 to 9.
    '''
    return [num async for num in async_generator()]
