#!/usr/bin/env python3
'''Task 8's module.
'''
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''Creates a function that multiplies its input by a given multiplier.
    '''
    return lambda x: x * multiplier
