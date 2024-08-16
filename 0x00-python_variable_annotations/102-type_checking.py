#!/usr/bin/env python3
"""
Module 102-type_checking
Contains a function zoom_array
"""

from typing import Tuple, List

def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
    Returns a zoomed-in version of the input array by repeating its elements.

    Args:
        lst (Tuple): The input tuple to be zoomed.
        factor (int, optional): The zoom factor. Defaults to 2.

    Returns:
        List: A list containing the zoomed-in elements.
    """
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
