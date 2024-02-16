#!/usr/bin/env python3
"""This type-annotated function takes a list
of integers and floats and returns their sum as a float.
"""

import typing


def sum_mixed_list(mxd_lst: typing.List[typing.Union[int, float]]) -> float:
    return float(sum(mxd_lst))
