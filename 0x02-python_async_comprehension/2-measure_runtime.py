#!/usr/bin/env python3
"""dsffdsfsdddsdsdsf"""
import asyncio
import random
import time
from typing import Generator, List
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """dsffdsfsdddsdsdsf"""
    startT = time.time()
    await asyncio.gather(async_comprehension())
    endT = time.time()
    return endT - startT
