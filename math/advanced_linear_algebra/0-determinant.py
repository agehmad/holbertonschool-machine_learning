#!/usr/bin/env python3
"""calculating determinant"""


def determinant(matrix):
    """documented"""
    if (not isinstance(matrix, list) or
       any(not isinstance(row, list) for row in matrix)):
        raise TypeError("matrix must be a list of lists")
    if matrix == [[]]:
        return 1
    if any(len(row) != len(matrix) for row in matrix):
        raise ValueError("matrix must be a square matrix")
    n = len(matrix)
    if n == 1:
        return matrix[0][0]
    if n == 2:
        return (matrix[0][0]*matrix[1][1]-matrix[0][1]*matrix[1][0])
    if n > 2:
        temp = []
        for ind, num in enumerate(matrix[0]):
            minor = [[matrix[i][j] for j in range(len(matrix[0])) if j != ind]
                     for i in range(len(matrix)) if i != 0]
            sign = 1 if ind % 2 == 0 else -1
            temp.append(sign*num*determinant(minor))
    return sum(temp)
