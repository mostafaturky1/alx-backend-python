#!/usr/bin/env python3
'''Task 0's module.
'''
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''Calculates the length of each element in a list.
    '''
    return [(i, len(i)) for i in lst]
