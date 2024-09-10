#!/usr/bin/python3
"""
rotating a give `n x n` 2D matrix by 90 degrees clockwise, in place
"""


def transpose_in_place(matrix):
    """ transpose matrix
    """
    for i in range(len(matrix)):
        for j in range(i + 1, len(matrix[0])):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


def reverse_matrix_rows_in_place(matrix):
    """
    reverse elements of each row of matrix in place
    """
    for i in range(len(matrix)):
        start, end = 0, len(matrix[0]) - 1
        while start < end:
            matrix[i][start], matrix[i][end] = matrix[i][end], matrix[i][start]
            start += 1
            end -= 1


def rotate_2d_matrix(matrix):
    """
    rotates a 2d matrix by 90 degrees clockwise in place
    """
    transpose_in_place(matrix)
    reverse_matrix_rows_in_place(matrix)
