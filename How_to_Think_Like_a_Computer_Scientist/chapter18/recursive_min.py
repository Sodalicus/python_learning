#!/usr/bin/env python4
from testing import test


def recursive_min(indata):
    smallest = None
    first_time = True


    for elem in indata:
        if type(elem) == type([]):
            elem = recursive_min(elem)

        if first_time and smallest == None:
            smallest = elem
            first_time = False

        if elem < smallest:
            smallest = elem

    return smallest


test(recursive_min([2, 9, [1, 13], 8, 6]) == 1)
test(recursive_min([2, [[100, 1], 90], [10, 13], 8, 6]) == 1)
test(recursive_min([2, [[13, -7], 90], [1, 100], 8, 6]) == -7)
test(recursive_min([[[-13, 7], 90], 2, [1, 100], 8, 6]) == -13)
