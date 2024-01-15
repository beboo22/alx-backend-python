#!/usr/bin/env python3
"""dsffdsfsdddsdsdsf"""

from asyncio import Task, create_task
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int = 10) -> Task:
    """dsffdsfsdddsdsdsf"""
    tsk = create_task(wait_random(max_delay))
    return tsk
