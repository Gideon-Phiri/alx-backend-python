import asyncio
from typing import List
from 0-basic_async_syntax import wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Run wait_random n times concurrently and return a list
    of delays in ascending order.
    Args:
        n (int): Number of coroutines to run.
        max_delay (int): Maximum delay for each coroutine.
    Returns:
        List[float]: List of delays in ascending order.
    """
    delays = await asyncio.gather(*(wait_random(max_delay) for _ in range(n)))
    return sorted(delays)
