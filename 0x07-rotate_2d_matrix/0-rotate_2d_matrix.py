#!/usr/bin/python3
"""Rotates matrix"""


def rotate_2d_matrix(matrix):
    """
       Rotates 2 dimensional matrix 
       args:
          matrix
    """
    l, r = 0, len(matrix) - 1

    while l < r:
        for i in range(r - l):
            top, bottom = l, r
            topl = matrix[top][l + i]
            matrix[top][l + i] = matrix[bottom - i][l]
            matrix[bottom - i][l] = matrix[bottom][r - i]
            matrix[bottom][r - i] = matrix[top + i][r]
            matrix[top + i][r] = topl
        r -= 1
        l += 1
