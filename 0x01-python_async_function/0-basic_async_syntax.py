import asyncio
import random


async def wait_random(max_delay: float = 10.0) -> float:
    """
    Waits for a random delay between 0 and max_delay (inclusive) seconds
    and returns the delay.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
