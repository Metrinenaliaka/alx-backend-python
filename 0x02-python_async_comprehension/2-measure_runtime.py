#!/usr/bin/env python3
"""
measure_runtime coroutine that will execute measure_time
4 times in parallel using asyncio.gather
"""

import asyncio
from typing import List
async_generator = __import__('0-async_generator').async_generator
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    A coroutine that executes async_comprehension
    """
    start_time = asyncio.get_event_loop().time()

    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )

    end_time = asyncio.get_event_loop().time()
    return end_time - start_time


if __name__ == "__main__":
    runtime = asyncio.run(measure_runtime())
    print(f"Total runtime: {runtime} seconds")
