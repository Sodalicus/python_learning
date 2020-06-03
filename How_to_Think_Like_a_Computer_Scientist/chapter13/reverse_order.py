#!/usr/bin/env python3

def reverse_order(infile):
    f = open(infile)
    words = f.readlines()
    for idx, lines in enumerate(words):
        lines = str(idx+1)+lines
    print(words)
    words.reverse()
    print()
    print()
    print(words)

reverse_order("lorem.txt") 
