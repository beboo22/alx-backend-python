#!/usr/bin/env python3
""" x"""
from typing import Mapping, MutableMapping, Sequence, Iterable, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ x """
    return [(i, len(i)) for i in lst]
