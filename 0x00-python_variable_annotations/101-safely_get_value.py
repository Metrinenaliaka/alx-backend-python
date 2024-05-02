#!/usr/bin/env python3
"""
Type-annotated function safely_get_value
"""


from typing import Dict, Any, TypeVar, Optional

# Define a type variable for the value type of the dictionary
V = TypeVar('V')


def safely_get_value(
    dct: Dict[str, V],
    key: str,
    default: Optional[V] = None
) -> Optional[V]:
    """
    Return the value of a key in a dictionary
    """
    if key in dct:
        return dct[key]
    else:
        return default
