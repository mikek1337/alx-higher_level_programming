#!/usr/bin/python3

"""Module for dividing all values in a matrix"""


def matrix_divided(matrix, div):
    """
    Returns martix of the divided elements
    """
    div_matrix = []
    if not isinstance(matrix, list):
        raise TypeError(
            "matrix must be a matrix(list of lists) of integers/floats")
    matrix_len = len(matrix)
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    for i in matrix:
        div_list = []
        if len(matrix[0]) != len(i):
            raise TypeError("Each row of the matrix must be the same size")
        for j in i:
            if not isinstance(j, int) and not isinstance(j, float):
                raise TypeError(
                    "matrix must be a matrix(list of lists) of integers/floats")
            div_list.append(float("{:.2f}".format(j/div)))
        div_matrix.append(div_list)
    return div_matrix
