#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = [[row * row for row in matrix[i]] for i in range(3)]
    return new_matrix
