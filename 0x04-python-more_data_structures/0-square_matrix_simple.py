#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    rows = len(matrix)
    cols = len(matrix[0]) if matrix else 0

    # Create a new matrix filled with squares of elements
    sqrd_mtrx = [[matrix[i][j] ** 2 for j in range(cols)] for i in range(rows)]

    return sqrd_mtrx
