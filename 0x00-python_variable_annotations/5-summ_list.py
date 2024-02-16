#!/usr/bin/env python3
"""This type-annotated function takes a list
of floats as argument and returns their sum as a float.
"""


from typing import List


def sum_list(input_list: List[float]) -> float:
    return float(sum(input_list))
