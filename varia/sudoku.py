#!/usr/bin/env python3

def gen_empty():
    matrix = []
    for i in range(9):
        row = []
        for j in range(1,10):
            row.append(j)
        matrix.append(row)

    return matrix

def print_matrix(matrix):
    count = 0
    for row in matrix:
        i = 0
        for x in row:
            print


matrix = gen_empty()
print_matrix(matrix)
"""

 1 2 3 4 5 6 7 8 9
 2 3 4 5 6 7 8 9 1
 1:

"""
