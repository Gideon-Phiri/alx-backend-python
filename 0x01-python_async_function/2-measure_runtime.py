import time
import asyncio
from 1-concurrent_coroutines import wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure total runtime of wait_n and return the average time per coroutine.
    Args:
        n (int): Number of coroutines to run.
        max_delay (int): Maximum delay for each coroutine.
    Returns:
        float: Average time per coroutine.
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    elapsed_time = time.time() - start_time
    return elapsed_time / n
