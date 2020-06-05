#!/usr/bin/env python3

def nmbr_lns(infile, outfile):
    f = open(infile)
    o = open(outfile, "w")
    in_lines = f.readlines()
    out_lines = []
    count = 1
    for line in in_lines:
        out_lines.append("{:>4} ".format(count)+line)
        count +=1
    o.writelines(out_lines)
    f.close()
    o.close()

def denmbr_lns(infile, outfile):
    f = open(infile)
    o = open(outfile, "w")
    in_lines = f.readlines()
    out_lines = []
    for line in in_lines:
        o.write(line[5:])
    f.close()
    o.close()


nmbr_lns("lorem.txt", "loremX.txt")


