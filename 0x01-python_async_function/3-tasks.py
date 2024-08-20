import asyncio
from 0-basic_async_syntax import wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Create an asyncio.Task from the wait_random coroutine.
    Args:
        max_delay (int): Maximum delay for the coroutine.
    Returns:
        asyncio.Task: An asyncio task wrapping wait_random.
    """
    return asyncio.create_task(wait_random(max_delay))
