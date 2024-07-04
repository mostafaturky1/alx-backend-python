#!/usr/bin/env python3
'''Task 100's module.
'''
from typing import Sequence, Any, Union

# The types of the elements of the input are not know
def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    '''Returns the first element of a sequence or None if the sequence is empty.
    '''
    if lst:
        return lst[0]
    else:
        return None
