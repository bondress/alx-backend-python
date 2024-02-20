#!/usr/bin/env python3
"""This measure_time function with integers n and max_delay as
arguments, measures the total execution time for wait_n(n, max_delay),
and returns total_time / n.
"""


import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Return total execution time"""
    begin_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()

    total_time = end_time - begin_time
    return (total_time/n)
