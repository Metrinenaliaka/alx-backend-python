#!/usr/bin/env python3
"""
Type-annotated function safe_first_element
"""

from typing import Any, Optional, List


def safe_first_element(lst: List[Any]) -> Optional[Any]:
    """
    Return the first element of a list
    """
    return lst[0] if lst else None
