#!/usr/bin/env python3
"""dsffdsfsdddsdsdsf"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """dsffdsfsdddsdsdsf"""
    x = random.uniform(0, max_delay)
    await asyncio.sleep(x)
    return x
