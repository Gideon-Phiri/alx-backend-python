#!/usr/bin/env python3
"""
Module 100-safe_first_element
Contains a function safe_first_element
"""

from typing import Sequence, Any, Union

def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Returns the first element of a sequence or None if the sequence is empty.

    Args:
        lst (Sequence[Any]): The input sequence.

    Returns:
        Union[Any, None]: The first element or None.
    """
    if lst:
        return lst[0]
    else:
        return None
