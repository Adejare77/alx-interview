#!/usr/bin/python3
""" Rotate 2D Matrix """


def rotate_2d_matrix(matrix):
    """ Given an n x n 2D matrix, rotate it 90 degrees clockwise """
    # Reverse list to simplify it
    min_idx = 0
    max_idx = len(matrix) - 1
    while (min_idx < max_idx):
        matrix[min_idx], matrix[max_idx] = matrix[max_idx], matrix[min_idx]
        min_idx += 1
        max_idx -= 1

    # Zip the matrix
    zipped_list = list(zip(*matrix))

    # clear the matrix (This wouldn't affect the zipped_list)
    matrix.clear()
    for i in range(len(zipped_list)):
        matrix.append(list(zipped_list[i]))
