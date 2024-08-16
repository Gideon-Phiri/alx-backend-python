#!/usr/bin/env python3
"""
Module 101-safely_get_value
Contains a function safely_get_value
"""

from typing import Mapping, Any, Union, TypeVar

T = TypeVar('T')

def safely_get_value(dct: Mapping, key: Any, default: Union[T, None] = None) -> Union[Any, T]:
    """
    Safely retrieves a value from a dictionary.

    Args:
        dct (Mapping): The dictionary to search.
        key (Any): The key to look for.
        default (Union[T, None], optional): The default value if key is not found. Defaults to None.

    Returns:
        Union[Any, T]: The value from the dictionary or the default value.
    """
    if key in dct:
        return dct[key]
    else:
        return default
