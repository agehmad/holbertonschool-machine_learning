#!/usr/bin/env python3
"""documented"""


def determinant(matrix):
    """documented"""
    if (not isinstance(matrix, list) or
       any(not isinstance(row, list) for row in matrix)):
        raise TypeError("matrix must be a list of lists")
    if matrix == [[]]:
        return 1
    if any(len(row) != len(matrix) for row in matrix):
        raise ValueError("matrix must be a non-empty square matrix")
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


def minor(matrix):
    """Calculating minor matrix of a matrix"""
    if (not isinstance(matrix, list) or
       any(not isinstance(row, list) for row in matrix)):
        raise TypeError("matrix must be a list of lists")
    if any(len(row) != len(matrix) for row in matrix) or len(matrix) == 0:
        raise ValueError("matrix must be a non-empty square matrix")
    n = len(matrix)
    if n == 1:
        return [[1]]
    minor_mat = []
    for row in range(len(matrix)):
        temp = []
        for col in range(len(matrix[row])):
            minor = [[matrix[i][j] for i in range(len(matrix)) if i != row]
                     for j in range(len(matrix[row])) if j != col]
            temp.append(determinant(minor))
        minor_mat.append(temp)
    return minor_mat


def cofactor(matrix):
    """calculating cofactor matrix of a matrix"""
    if (not isinstance(matrix, list) or
       any(not isinstance(row, list) for row in matrix)):
        raise TypeError("matrix must be a list of lists")
    if any(len(row) != len(matrix) for row in matrix) or len(matrix) == 0:
        raise ValueError("matrix must be a non-empty square matrix")
    n = len(matrix)
    if n == 1:
        return [[1]]
    cofactor_mat = []
    for row in range(len(matrix)):
        temp = []
        for col in range(len(matrix[row])):
            minor = [[matrix[i][j] for i in range(len(matrix)) if i != row]
                     for j in range(len(matrix[row])) if j != col]
            temp.append(determinant(minor)*(-1)**(row + col))
        cofactor_mat.append(temp)
    return cofactor_mat


def adjugate(matrix):
    """adjugating a matrix"""
    new_mat = cofactor(matrix)
    adjugate_mat = zip(*new_mat)
    adjugate_mat = [list(item) for item in adjugate_mat]
    return adjugate_mat


def inverse(matrix):
    """calculating inverse of a matrix"""
    if len(matrix) == 1:
        return [[1/adjugate(matrix)[0][0]]]
    return (1/determinant(matrix))*(adjugate(matrix))
