#!/usr/bin/env python3
'''Task 0's module.
'''
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''Converts a key-value pair to a tuple with the value squared.
    '''
    return (k, float(v ** 2))
