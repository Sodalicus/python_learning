#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 Paweł Krzemiński 
#
# Distributed under terms of the MIT license.

"""
Solution excercise from python101 course.
"""
import math

def average(scores):
    """
    Return average
    """
    ave = 0
    if scores:
        for score in scores:
            ave+=score
    return round(ave/len(scores), 2)
    #return sum(scores)/len(scores)
    #return 


def med(scores):
    """Return median"""
    scores_copy = scores.copy()
    scores_copy.sort()
    print("len: ", len(scores))
    if scores:
        if len(scores)%2:
            return scores[round(len(scores)/2)]
        else:
            middle = len(scores_copy)/2
            print(middle)
            print(int(middle))
            middle = int(middle)
            median = (scores_copy[middle-1]+scores_copy[middle])/2
            return median


def std_dev(scores):
    """Return standard deviation"""
    if scores:
        ave = average(scores)
        dev = 0
        for i in scores:
            dev += (i-ave)**2
    return round(math.sqrt(dev/len(scores)), 2)








