#!/usr/bin/env python3
"""
Type-annotated function safe_first_element
"""

from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Return the first element of a sequence
    """
    return lst[0] if lst else None