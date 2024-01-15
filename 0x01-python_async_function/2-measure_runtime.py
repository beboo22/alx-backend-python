#!/usr/bin/env python3
"""dsffdsfsdddsdsdsf"""
from asyncio import run
import time
from typing import List
from random import uniform
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int = 10) -> float:
    """dsffdsfsdddsdsdsf"""
    starT = time.time()
    run(wait_n(n, max_delay))
    endT = time.time()
    return (endT - starT) / n
