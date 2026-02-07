# !/usr/bin/env python3
"""calculating determinant"""


def determinant(matrix):
    """documented"""
    if (not isinstance(matrix, list) or
        any(not isinstance(row, list) for row in matrix)):
        raise TypeError("matrix must be a list of lists")
    if len(matrix) != len(matrix[0]):
        raise ValueError("matrix must be a square matrix")
    if matrix == [[]]:
        return 1
    n = len(matrix)
    if n == 1:
        return matrix[0][0]
    if n == 2:
        return (matrix[0][0]*matrix[1][1]-matrix[0][1]*matrix[1][0])
    if n > 2:
        sum = 0
        k = 2
        for colm in matrix[0]:
            minor = []
            for row in range(1, matrix):
                temp = []
                for col in range(matrix[row]):
                    if col != matrix[0].index(colm):
                        temp.append(matrix[row][col])
                minor.append(temp)
            det = determinant(minor)
            sum = sum + (-1)**k*(col*det)
            k += 1
        return sum
