#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = matrix.copy()
    t = len(matrix)
    for i in range(t):
        new_matrix[i]=list(map(lambda x: x**2, matrix[i]))
    return (new_matrix)

        