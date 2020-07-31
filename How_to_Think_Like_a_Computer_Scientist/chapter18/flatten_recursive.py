#!/usr/bin/env python3

from testing import test

def flatten(indata):
    flt_list = []
    new_list = []

    for elem in indata:
        if type(elem) == type([]):
            flt_list.extend(flatten(elem))
        else:
            flt_list.append(elem)

    return flt_list


test(flatten([2,9,[2,1,13,2],8,[2,6]]) == [2,9,2,1,13,2,8,2,6])
test(flatten([[9,[7,1,13,2],8],[7,6]]) == [9,7,1,13,2,8,7,6])
test(flatten([[9,[7,1,13,2],8],[2,6]]) == [9,7,1,13,2,8,2,6])
test(flatten([["this",["a",["thing"],"a"],"is"],["a","easy"]]) ==
              ["this","a","thing","a","is","a","easy"])
test(flatten([]) == [])

