#!/usr/bin/env python3
"""dsffdsfsdddsdsdsf"""
import asyncio
from typing import List
from random import uniform
task_wait_random = __import__('3-tasks').task_wait_random

async def task_wait_n(n: int, max_delay: int = 10) -> List[float]:
    """dsffdsfsdddsdsdsf"""
    list_val = []
    data = []
    for x in range(n):
        # No need to use asyncio.create_task here
        task = task_wait_random(max_delay)
        list_val.append(task)
        await task
    
    for res in list_val:
        data.append(res.result())


    return sorted(data)
