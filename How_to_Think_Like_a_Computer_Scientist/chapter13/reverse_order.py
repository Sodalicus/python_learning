#!/usr/bin/env python3

def reverse_order(infile, outfile):
    f = open(infile)
    out = open(outfile, "w")
    new_words = []
    words = f.readlines()
    for line in words:
        new_words.insert(0, line)
    for line in new_words:
        out.write(line)
    f.close()
    out.close()

def reverse_order2(infile, outfile):
    f = open(infile)
    out = open(outfile, "w")
    words = f.readlines()
    new_words = []
    for i in range(len(words)-1,-1,-1):
        new_words.append(words[i])
    out.writelines(new_words)
    f.close()
    out.close()



