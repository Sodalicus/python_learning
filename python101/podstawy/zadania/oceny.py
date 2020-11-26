#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 Paweł Krzemiński 
#
# Distributed under terms of the MIT license.

"""
Solution to excercise from python101 course
"""

from oceny_modul import average, med, std_dev

def school_diary(scores):
    """
    Get number of scores from the user,
    calculate average. med, standard deviation.
    """
    s = None
    while True:
        try:
            s = int(input("Type score 1-5(0 to end): "))
            if 6 > s > 0:
                scores.append(s)
                print("Scores: {}".format(scores))
            elif s==0:
                break
            else:
                print("Invalid score, has to be in range 1-5")
        except ValueError:
            print("Score has to be number")
            continue

    print(scores)

def main():
    scores = []
    school_diary(scores)
    print("Average score is: ", average(scores))
    print("Median is: ", med(scores))
    print("Standard deviation is: ", std_dev(scores))

main()

