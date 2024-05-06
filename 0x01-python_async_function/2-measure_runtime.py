#!/usr/bin/env python3
"""
measure_time function with ints n and max_delay as args
measures the total execution time for wait_n(n, max_delay)
returns total_time / n
"""

import asyncio
import random
import time
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Returns the average time of the n calls to wait_random
    """
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    end = time.time()
    return (end - start) / n
