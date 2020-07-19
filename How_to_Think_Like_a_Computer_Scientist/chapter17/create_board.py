#!/usr/bin/env python3

import random
# a Module with a purpose of providing a function (n_queens()), that return a solution to n queens puzzle.

def share_diagonal(x0, y0, x1, y1):
    """ Is (x0, y0) on shared diagonal with (x1, y1)? """
    dy = abs(y1 - y0)       # Calc the absolute y distance
    dx = abs(x1 - x0)       # Calc the absolute x distance
    return dx == dy         # They clash if dx == dy

def col_clashes(bs, c):
    """ Return True if the queen at column c clashes
        with any queen to its left. 
    """
    for i in range(c):  # Look at all columns to the left of c
        if share_diagonal(i, bs[i], c, bs[c]):
            return True

    return False        # No clashes - col c has a safe placement.

def has_clashes(the_board):
    """ Determine whether we have any queens clashing on the diagonals.
        We're assuming here that the board is a permutation of column
        numbers, so we're not explicitly checking row or column clashes.
    """
    for col in range(1, len(the_board)):
        if col_clashes(the_board, col):
            return True
    return False

def n_queens(n=8):
    """ Returns a valid eight queens puzzle solution. """
    bd = list(range(n))
    while True:
        random.shuffle(bd)
        if not has_clashes(bd):
            return bd

if __name__ == '__main__':
    print("This is a module.")
    print(n_queens(12))
    print(n_queens())
    print(n_queens())


