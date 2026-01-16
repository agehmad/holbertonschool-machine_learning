#!/usr/bin/env python3
"""
Docstring for math.calculus.17-integrate
"""


def poly_integral(poly, C=0):
    """
    Docstring for poly_integral

    :param poly: Description
    :param C: Description
    """
    if (type(poly) is not list) or (len(poly) == 0) or (type(C) is not int):
        return None
    result = all(type(item) is int for item in poly)
    if result is False:
        return None
    else:
        y = [0]
        for i in range(1, len(poly)):
            y.append(poly[i] / (i+4))
        return y
