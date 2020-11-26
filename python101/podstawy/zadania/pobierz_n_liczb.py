#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 Paweł Krzemiński 
#
# Distributed under terms of the MIT license.

"""
Solution to excercise from python101 course.
Get n numbers from user. Print elements of the list and their indexes.
elements in backwards, sorted. Remove first occurence of the element given
by the user. Remove element of given index. Podaj number of occurences
and index number of the first occurence if the given element.
Pick elements from index i to j.
"""
i = 1
numbers = []
non = 0
non = int(input("How many number do you want to give: "))
while len(numbers) < non:
    try:
            numbers.append(int(input("Type in {} number: ".format(i))))
            i+=1
    except ValueError:
        continue

for i,v in enumerate(numbers):
    print("index {} - number {}".format(i,v))

for i in reversed(numbers):
    print(i, end=" ")
print()

for i in range(len(numbers)-1, -1, -1):
    print(numbers[i], end=" ")
print()

numbers.sort()
print(numbers)

if len(numbers):print("Before removing: ", numbers)
while len(numbers):
    try:
        toberemoved = int(input("Give number on the list to be removed: "))
        numbers.remove(toberemoved)
        break
    except ValueError:
        print("Given number is not on the list.")
        continue

if len(numbers):print("After removing: ", numbers)

while len(numbers):
    try:
        toberemoved = int(input("Give elements' index number to be removed: "))
        if -len(numbers) <= toberemoved < len(numbers):
            numbers.pop(toberemoved)
            break
        print("Given index number is not on the list.")
    except ValueError:
        print("Given index number is not on the list.")
        continue

if len(numbers):print("After removing: ", numbers)
while len(numbers):
    try:
        tocount = int(input("Give number on the list to count its occurences: "))
        print("Given number {} count is {} and the its first occurence index number is {}.".\
                format(tocount,numbers.count(tocount),numbers.index(tocount)))
        break
    except ValueError:
        print("Given number is not on the list.")


while len(numbers):
        try:
            i = int(input("Give first index: "))
            j = int(input("Give second index: "))
            if -len(numbers) <= i < len(numbers) and\
                    -len(numbers) <= i < len(numbers):
                print(numbers[i:j])
                break
        except ValueError:
            print("Given index number is not valid.")


if len(numbers)==0: print("The list is empty, nothing to do here!")


