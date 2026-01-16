#!/usr/bin/env python3
"""
Docstring for math.calculus.10-matisse
"""


def poly_derivative(poly):
    """
    Docstring for poly_derivative

    :param poly: Description
    """
    if type(poly) is not list:
        return None
    result = all(type(item) is int for item in poly)
    if result == False:
        return None
    else:
        if len(poly) == 1:
            return [0]
        y = []
        for i in range(1, len(poly)):
            y.append(i * poly[i])
        return y
