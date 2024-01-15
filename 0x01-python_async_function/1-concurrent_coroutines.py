#!/usr/bin/env python3
"""dsffdsfsdddsdsdsf"""
import asyncio
from typing import List
from random import uniform
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int = 10) -> List[float]:
    """dsffdsfsdddsdsdsf"""
    list_val = []
    data = []
    for x in range(n):
        task = asyncio.create_task(wait_random(max_delay))
        list_val.append(task)
        await task

    for res in list_val:
        data.append(await res)

    return data
