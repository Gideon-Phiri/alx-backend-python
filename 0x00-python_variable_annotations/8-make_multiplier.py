#!/usr/bin/env python3
"""
This module provides a function to create a multiplier function.
"""

from typing import Callable

def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Creates a multiplier function.

    Args:
        multiplier (float): The multiplier.

    Returns:
        Callable[[float], float]: A function that multiplies a float by the multiplier.
    """
    def multiplier_func(x: float) -> float:
        return x * multiplier
    
    return multiplier_func
