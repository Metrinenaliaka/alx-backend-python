#!/usr/bin/env python3
"""
Type-annotated function element_length
"""

from typing import Iterable, Tuple, Sequence, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Return a list of tuples, each tuple
    containing an element and its length
    """
    return [(i, len(i)) for i in lst]
