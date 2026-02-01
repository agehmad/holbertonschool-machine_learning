#!/usr/bin/env python3
"""
Docstring for math.linear_algebra.4-line_up
"""


def add_arrays(arr1, arr2):
    """
    Docstring for add_arrays

    :param arr1: Description
    :param arr2: Description
    """
    new = []
    if len(arr1) != len(arr2):
        return None
    else:
        for i in range(len(arr1)):
            new.append(arr1[i] + arr2[i])
    return new
