#!/usr/bin/env python3
"""This type-annotated function takes
a float multiplier as argument and returns a function that
multiplies a float by multiplier.
"""


import typing


def make_multiplier(multiplier: float) -> typing.Callable[[float], float]:
    def float_multiply(x: float) -> float:
        return multiplier * x

    return float_multiply
