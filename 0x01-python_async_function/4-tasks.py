#!/usr/bin/env python3
"""This function takes the code from wait_n and alters it into a new function
task_wait_n. The code is nearly identical to wait_n except
task_wait_random is being called.
"""


import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Spawn wait_random n times"""
    jobs = []
    waits = []

    for i in range(n):
        job = task_wait_random(max_delay)
        jobs.append(job)

    for job in asyncio.as_completed((jobs)):
        delay = await job
        waits.append(delay)

    return waits
