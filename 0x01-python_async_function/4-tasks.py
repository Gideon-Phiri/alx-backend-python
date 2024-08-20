import asyncio
from typing import List
from 3-tasks import task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Run task_wait_random n times concurrently and return
    a list of delays in ascending order.
    Args:
        n (int): Number of coroutines to run.
        max_delay (int): Maximum delay for each coroutine.
    Returns:
        List[float]: List of delays in ascending order.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return sorted(delays)
