#!/usr/bin/env python3
"""
Docstring for math.calculus.10-matisse
"""


def poly_derivative(poly):
    """
    Docstring for poly_derivative

    :param poly: Description
    """
    result = all(type(item) is int for item in poly)
    if result == False:
        return None
    else:
        y = []
        for i in range(len(poly)):
            if poly[i] != 0:
                y.append(i * poly[i])
        return y
