#!/usr/bin/env python3

# Counting letters using dictionaries

# if letter is already in dict, values +=1. If it is not in dictionary yet, 
# ensure it appears there with values 0+1, using .get() methon, ommiting Key error
letter_counts = {}
for letter in "Mississippi":
    letter_counts[letter] = letter_counts.get(letter, 0) +1

letter_counts = list(letter_counts.items())
letter_counts.sort()
print(letter_counts)
