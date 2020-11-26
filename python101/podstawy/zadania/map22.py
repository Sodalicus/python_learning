#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#

"""

"""
def kwadrat(x):
    return x**2

kwadraty = map(kwadrat, range(10))
print(list(kwadraty))
print([x**2 for x in range(10)])
kwadraty = map(lambda x: x**2, range(10))
print(list(kwadraty))
