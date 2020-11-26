#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#

"""

"""
def gen_parzyste(N):
    for i in range(N):
        if i%2 == 0:
            yield i

gen = gen_parzyste(10)
print(next(gen))
print(next(gen))
print(next(gen))
print(list(gen))
