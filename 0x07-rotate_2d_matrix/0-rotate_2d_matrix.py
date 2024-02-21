#!/usr/bin/python3
""" Module that implements rotate_2d_matrix """


def rotate_2d_matrix(matrix):
    """ Function that rotates a 2d matrix in place """
    # x = list(range(len(matrix)))
    # print(x)
    mat_len = len(matrix)
    for i in range(mat_len):
        for j in range(i + 1, mat_len):
            # print(f'i = {i}, j = {j}')
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for i in range(mat_len):
        matrix[i].reverse()
