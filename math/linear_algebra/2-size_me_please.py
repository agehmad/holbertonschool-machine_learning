#!/usr/bin/env python3
def matrix_shape(matrix):
    shap = []
    for i in matrix:
        if type(i) is list:
            shap.append(len(i))
    return shap
