#!/usr/bin/python3
"""Divide the ellements of matrix"""


def matrix_divided(matrix, div):
    """Divide the contens of the matrix by integer

    Args:
        matrix (list of list): a list of list
        div (int): divider number

    Rerturn:
        the divided matrix
    """
    res = []
    if not matrix:
         raise TypeError('matrix must be a matrix (list of lists) of integers/floats')

    for i in range(len(matrix)):
        row = []

        if not all(isinstance(row, list) for row in matrix):
            raise TypeError('matrix must be a matrix (list of lists) of integers/floats')

        if i < len(matrix) - 1 and len(matrix[i]) != len(matrix[i + 1]):
            raise TypeError('Each row of the matrix must have the same size')

        for j in range(len(matrix[i])):
            if not isinstance(matrix[i][j], (int, float)):
                raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
            if not isinstance(div, (int, float)):
                raise TypeError('div must be a number')
            if div == 0:
                raise ZeroDivisionError('division by zero')

            temp = round((matrix[i][j] / div), 2)
            row.append(temp)

        res.append(row)

    return res
