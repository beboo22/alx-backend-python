#!/usr/bin/env python3
'''Basic annotations for variables.'''
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    '''Returns the floor of a float.'''
    return float(sum(mxd_lst))
