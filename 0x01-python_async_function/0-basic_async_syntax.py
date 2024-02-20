#!/usr/bin/env python3
"""This is an asynchronous coroutine that takes in an integer argument
(max_delay, with a default value of 10) named wait_random that waits
for a random delay between 0 and max_delay (included and float value)
seconds and eventually returns it.
"""


import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """Wait for max_delay seconds and return waiting time."""
    waiting_time = random.random() * max_delay
    await asyncio.sleep(waiting_time)
    return waiting_time
