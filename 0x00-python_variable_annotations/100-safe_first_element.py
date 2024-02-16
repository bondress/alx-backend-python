!/usr/bin/env python3
"""Augment the given code with the correct duck-typed annotations:

# The types of the elements of the input are not known
def safe_first_element(lst):
    if lst:
        return lst[0]
    else:
        return None

{'lst': typing.Sequence[typing.Any], 'return': \
    typing.Union[typing.Any, NoneType]}
"""


import typing


def safe_first_element(lst: typing.Sequence[typing.Any]) -> \
        typing.Union[typing.Any, None]:
    """Correct Duck-typed annotation"""
    if lst:
        return lst[0]
    else:
        return None
