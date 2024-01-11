#!/usr/bin/env python3
'''Basic annotations for variables.'''
from typing import List, Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''Returns the floor of a float.'''
    return (k, v**2)
