#!/usr/bin/env python3
"""
Type-annotated function safe_first_element
"""

from typing import Any, Optional


def safe_first_element(lst: list) -> Optional[Any]:
    return lst[0] if lst else None
