#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 Paweł Krzemiński 
#
# Distributed under terms of the MIT license.

"""
Solution to excercise from python101 course.
Print alphabet from a to z, lower and upper case.
"""

# 97-122 a-z
# 65-90 A-Z
i = 0
for a in range(97, 123):
    print(chr(a) + " => " + chr(a).upper(), end=' ')
    i+=1
    if i%5 == 0:print()
print()
i = 0
for a in range(90, 64, -1):
    print(chr(a) + " => " + chr(a).lower(), end=' ')
    i +=1
    if i%5 == 0:print()
