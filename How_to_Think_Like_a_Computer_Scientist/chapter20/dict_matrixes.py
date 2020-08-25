#!/usr/bin/env python3

# Representation of matrixes using dictionaries

matrix = [[0, 0, 0, 1, 0],
          [0, 0, 0, 0, 0],
          [0, 2, 0, 0, 0],
          [0, 0, 0, 0, 0],
          [0, 0, 0, 3, 0]]

matrix2 = {(0, 3): 1, (2, 1): 2, (4, 3): 3}

print(matrix2[(2, 1)])

try:
    print(matrix2[(1, 2)])
except:
    print("Key error")

# Using .get() method you can ommit Key Error
# if key exist, the values gets printed as usual
print(matrix2.get((0, 3), 0))

# if key doesnt exist, 0 gets printed
print(matrix2.get((1, 2), 0))

#Memoization

alreadyknown = {0: 0, 1: 1}

def fib(n):
    if n not in alreadyknown:
        new_value = fib(n-1) + fib(n-1)
        alreadyknown[n] = new_value
    return alreadyknown[n]

print(fib(100))
