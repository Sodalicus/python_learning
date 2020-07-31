#!/usr/bin/env 

from testing import test

def count(pattern, indata):
    cnt = 0

    for elem in indata:
        if type(elem) == type([]):
            cnt += count(pattern, elem)
        if elem == pattern:
            cnt += 1

    return cnt




test(count(2, []) ==  0)
test(count(3,[1,2,3,4,3,5,6,3]) == 3)
test(count(2, [2, 9, [2, 1, 13, 2], 8, [2, 6]]) == 4)
test(count(7, [[9, [7, 1, 13, 2], 8], [7, 6]]) == 2)
test(count(15, [[9, [7, 1, 13, 2], 8], [2, 6]]) == 0)
test(count(5, [[5, [5, [1, 5], 5], 5], [5, 6]]) == 6)
test(count("a",
     [["this",["a",["thing","a"],"a"],"is"], ["a","easy"]]) == 4)
