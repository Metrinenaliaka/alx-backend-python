#!/usr/bin/env python3
"""
Type-annotated function element_length
"""

from typing import Sequence, Union, List, Tuple


def element_length(
    lst: Union[Sequence[Union[List[int], Tuple[int, int]]]]
) -> List[Tuple[Union[List[int], Tuple[int, int]], int]]:
    """
    Return list of tuples where each tuple contains a sequence and its length
    """
    return [(i, len(i)) for i in lst]
