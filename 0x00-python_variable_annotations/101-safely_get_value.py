#!/usr/bin/env python3
""" xddd dddd ddddd ddd"""
from typing import Sequence, List, Tuple, Any, Union, Mapping, TypeVar


T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """ xxddd dddd ddddd ddd """
    if key in dct:
        return dct[key]
    else:
        return default
