#!/usr/bin/env python3
'''Task 100's module.
'''
from typing import Mapping, Any, Union, TypeVar
T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any, default:
                     Union[T, None] = None) -> Union[Any, T]:
    '''Returns the value associated with a key in a dictionary.
    '''
    if key in dct:
        return dct[key]
    else:
        return default
