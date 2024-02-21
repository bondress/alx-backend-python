#!/usr/bin/env python3
'''This measure_runtime coroutine executes async_comprehension
                four times in parallel using asyncio.gather.

                measure_runtime measures the total runtime and returns it.
'''

from asyncio import gather
from time import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    '''Measures the runtime of async_comprehension executed 4 times in
        parallel. '''
    start_time = time()
    await gather(async_comprehension(), async_comprehension(),
                 async_comprehension(), async_comprehension())
    next_time = time()

    return next_time - start_time
