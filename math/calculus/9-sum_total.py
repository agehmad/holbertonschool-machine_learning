#!/usr/bin/env python3
"""
Docstring for math.calculus.9-sum_total
"""


def summation_i_squared(n):
    """
    Docstring for summation_i_squared

    :param n: Description
    """
    if type(n) is not int or n <= 0:
        return None
    else:
        nums = list(range(1, n+1))
        nums = list(map(lambda x : x**2, nums))
        return  sum(nums)
