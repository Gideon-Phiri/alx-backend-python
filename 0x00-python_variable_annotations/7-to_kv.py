#!/usr/bin/env python3
"""
This module provides a function to create a tuple from a string and an int/float.
"""

from typing import Union, Tuple

def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Creates a tuple from a string and the square of an int/float.

    Args:
        k (str): The string.
        v (Union[int, float]): The number to be squared.

    Returns:
        Tuple[str, float]: The string and the squared number as a float.
    """
    return (k, float(v ** 2))
