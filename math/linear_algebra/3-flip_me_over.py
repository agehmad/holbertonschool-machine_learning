# !/usr/bin/env python3
"""
Docstring for math.linear_algebra.3-flip_me_over
"""


def matrix_transpose(matrix):
    """
    Docstring for matrix_transpose

    :param matrix: Description
    """
    new_mat = []
    for column in range(len(matrix[0])):
        temp = []
        for row in range(len(matrix)):
            temp.append(matrix[row][column])
        new_mat.append(temp)
    return new_mat
