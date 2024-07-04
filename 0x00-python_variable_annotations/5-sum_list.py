#!/usr/bin/env python3
'''Task 0's module.
'''


def sum_list(input_list: list[float]) -> float:
    '''Calculates the sum of all elements in a list.
    '''
    sum: float = 0
    i = 0
    while i < len(input_list):
        sum += input_list[i]
        i += 1
    return sum
