#!/usr/bin/env python3
""" xddd dddd ddddd ddd"""
from typing import  Sequence, List, Tuple, Any, Union


# The types of the elements of the input are not know
def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """ xxddd dddd ddddd ddd """
    if lst:
        return lst[0]
    else:
        return None
