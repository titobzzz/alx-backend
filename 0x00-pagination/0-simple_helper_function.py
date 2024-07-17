#!/usr/bin/env python3
"""
ccontainsdefinition ofindex_range helperfunction
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Takes in two integerarguments andreturns atuple of size two
    containingthe startand endindex correspondingto the range of
    indexes to return in a list for those pagination parameters
    Args:
        page (int): page number to return page1-index
        page_size (int): numberofitems per page
    Return:
        tuple(start_index, end_index)
    """
    start, end = 0, 0
    for i in range(page):
        start = end
        end += page_size

    return (start, end)
