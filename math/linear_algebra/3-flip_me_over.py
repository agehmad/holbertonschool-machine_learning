#!/usr/bin/env python3
"""
Docstring for math.linear_algebra.3-flip_me_over
"""


def matrix_transpose(matrix):
    """
    Docstring for matrix_transpose

    :param matrix: Description
    """
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if i == j:
                continue
            else:
                matrix[i][j] = matrix[j][i]
    new_mat = matrix
    return new_mat
