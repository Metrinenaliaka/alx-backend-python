#!/usr/bin/env python3
"""
Type-annotated function element_length
"""

from typing import Iterable, Tuple


def element_length(lst: Iterable[str]) -> Iterable[Tuple[str, int]]:
    return [(i, len(i)) for i in lst]
