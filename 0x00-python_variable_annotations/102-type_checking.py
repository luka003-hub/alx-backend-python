#!/usr/bin/env python3
"""
Type Checking
"""
from typing import Union, Any, Mapping, Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
    zoom
    """
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in

