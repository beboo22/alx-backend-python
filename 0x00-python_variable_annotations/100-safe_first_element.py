#!/usr/bin/env python3
""" xddd dddd ddddd ddd"""
from typing import Mapping, MutableMapping, Sequence, Iterable, List,
Tuple, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """ xxddd dddd ddddd ddd """
    if lst:
        return lst[0]
    else:
        return None
