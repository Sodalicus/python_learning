#!/usr/bin/env python3

def read_snake(infile):
    f = open(infile)
    words = f.readlines()
    for line in words:
        if "snake" in line:
            print(line)

read_snake("lorem_nbr.txt")

