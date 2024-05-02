#!/usr/bin/env python3
"""
Type-annotated function element_length
"""

from typing import Sequence, Union, List, Tuple


def element_length(
    lst: Union[Sequence[Union[List[int], Tuple[int, int]]]]
) -> List[int]:
    """
    Return list of lengths of elements in lst
    """
    return [len(i) for i in lst]
