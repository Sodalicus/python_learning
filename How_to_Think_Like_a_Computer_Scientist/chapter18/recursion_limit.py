#!/usr/bin/env python3

import sys

print("Current recursion limit is {}.".format(sys.getrecursionlimit()))

limit = 200

print("Setting recursion limit to {}.".format(limit))
sys.setrecursionlimit(limit)
def get_depth(n):
    """ print depth of current recursion. """
    print(n, end=" ")
    get_depth(n+1)

get_depth(1)
