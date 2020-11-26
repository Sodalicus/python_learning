#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 Paweł Krzemiński 
#
# Distributed under terms of the MIT license.

"""
Python101 solution excercise.
f(n) = f(n-2)+f(n-1)
"""
def fibo(n):
    """Returns n fibonacci number """
    if n == 1:
        return 0
    elif n == 2:
        return 1
    elif n>2:
        return fibo(n-2)+fibo(n-1)

print(fibo(9))
