#!/usr/bin/env python3

def reverse_order(infile):
    f = open(infile)
    new_words = []
    words = f.readlines()
    for line in words:
        new_words.append(line)
    print(words)
    print()
    print()
    print(new_words)

def reverse_order2(infile):
    f = open(infile)
    words = f.readlines()
    new_words = []
    for i in range(len(words)-1,-1,-1):
        new_words.append(words[i])
    print(words)
    print()
    print()
    print(new_words)

reverse_order("lorem_nbr.txt")
