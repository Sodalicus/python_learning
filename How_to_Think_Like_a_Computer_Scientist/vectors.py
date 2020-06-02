#!/usr/bin/env python3
# Excercises from chapter 11 - Lists.

from testing import test

#Excercise 5
"""Lists can be used to represent mathematical vectors. In this exercise and several that follow you will write functions to perform standard operations on vectors. Create a script named vectors.py and write Python code to pass the tests in each case."""

def add_vectors(u, v):
    new_vector = []
    for i in range(len(u)):
        new_vector.append(u[i]+v[i])
    return new_vector

test(add_vectors([1, 1], [1, 1]) == [2, 2])
test(add_vectors([1, 2], [1, 4]) == [2, 6])
test(add_vectors([1, 2, 1], [1, 4, 3]) == [2, 6, 4])

#Excercise 6
"""Write a function scalar_mult(s, v) that takes a number, s, and a list, v and returns the scalar multiple of v by s. :"""

def scalar_mult(s, v):
    sm_list = []
    for item in v:
        sm_list.append(item*s)
    return sm_list
test(scalar_mult(5, [1, 2]) == [5, 10])
test(scalar_mult(3, [1, 0, -1]) == [3, 0, -3])
test(scalar_mult(7, [3, 0, 5, 11, 2]) == [21, 0, 35, 77, 14])

#Excercise 7
"""Write a function dot_product(u, v) that takes two lists of numbers of the same length, and returns the sum of the products of the corresponding elements of each (the dot_product)."""

def dot_product(u, v):
    sum = 0
    for i in range(len(u)):
        sum += u[i]*v[i]
    return sum

test(dot_product([1, 1], [1, 1]) ==  2)
test(dot_product([1, 2], [1, 4]) ==  9)
test(dot_product([1, 2, 1], [1, 4, 3]) == 12)

#Excercise 8
"""Extra challenge for the mathematically inclined: Write a function cross_product(u, v) that takes two lists of numbers of length 3 and returns their cross product. You should write your own tests."""

#Excercise 9
"""Describe the relationship between " ".join(song.split()) and song in the fragment of code below. Are they the same for all strings assigned to song? When would they be different?"""
song = "The rain in Spain..."
""".split(), removes all whitespaces, in this case spaces and return a list. S.join() takes iterable as an argument and return concatenation of items, whith the separator S.
If we change default split() delimiter, or if the was no given delimter in splitted string, or if we did change separator in join() methon, then the result depends on the changes we made."""

#Excercise 10
"""Write a function replace(s, old, new) that replaces all occurrences of old with new in a string s:"""

def replace(s, old, new):
    return new.join(s.split(old))

test(replace("Mississippi", "i", "I") == "MIssIssIppI")

s = "I love spom! Spom is my favorite food. Spom, spom, yum!"
test(replace(s, "om", "am") ==
    "I love spam! Spam is my favorite food. Spam, spam, yum!")

test(replace(s, "o", "a") ==
    "I lave spam! Spam is my favarite faad. Spam, spam, yum!")
#Excercise 11
"""Suppose you want to swap around the values in two variables. You decide to factor this out into a reusable function, and write this code:"""

def swap(x, y):      # Incorrect version
     print("before swap statement: x:", x, "y:", y)
     (x, y) = (y, x)
     print("after swap statement: x:", x, "y:", y)

a = ["This", "is", "fun"]
b = [2,3,4]
print("before swap function call: a:", a, "b:", b)
swap(a, b)
print("after swap function call: a:", a, "b:", b)
a, b = b, a
print("after manual swap call: a:", a, "b:", b)

"""Run this program and describe the results. Oops! So it didn’t do what you intended! Explain why not. Using a Python visualizer like the one at http://netserv.ict.ru.ac.za/python3_viz may help you build a good conceptual model of what is going on. What will be the values of a and b after the call to swap?"""
