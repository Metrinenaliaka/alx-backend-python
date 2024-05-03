#!/usr/bin/env python3
"""
Type-annotated function safely_get_value
"""

from typing import Mapping, TypeVar, Any, Union, Optional

V = TypeVar('V')
T = TypeVar('T')

def safely_get_value(
    dct: Mapping[str, V],
    key: Any,
    default: Optional[T] = None
) -> Union[Any, T]:
    """
    Return the value of a key in a dictionary
    """
    if key in dct:
        return dct[key]
    else:
        return default
