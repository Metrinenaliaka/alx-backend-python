#!/usr/bin/env python3
"""
measure_runtime coroutine that will execute measure_time
4 times in parallel using asyncio.gather
"""

import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    measure_runtime coroutine that will execute measure_time
    4 times in parallel using asyncio.gather
    """
    start_time = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end_time = time.time()
    return end_time - start_time
