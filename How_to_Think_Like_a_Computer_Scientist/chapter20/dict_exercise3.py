#!/usr/bin/env python3

import string

infilename = "AliceInWonderland.txt"

def text_to_lines(the_text):
    """ return a list of lines with all punctuation removed,
        and all in lowercase.
    """

    my_substitutions = the_text.maketrans(
      # If you find any of these
      "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&()*+,-./:;<=>?@[]^_`{|}~'\\",
      # Replace them by these
      "abcdefghijklmnopqrstuvwxyz                                          ")

    # Translate the text now.
    cleaned_text = the_text.translate(my_substitutions)
    wds = cleaned_text.split()
    return wds


def lines_occ(infile):
    try:
        infile = open(infilename, "r")
    except:
        print("No such file as", infilename)


    new_intext = []
    longest = ""
    j = " "
    for line in infile:
        line = line.replace("?", j).replace("!", j).replace(".", j)
        line = line.replace(",", j).replace("(", j).replace(")", j)
        line = line.replace("_", j).replace("-", j)
        line = line.replace(":", j).replace("\"", j).replace("\'", j)
        line = line.lower()
        line = line.split()
        for word in line:
            if word.isalpha():
                if len(word) > len(longest):
                    longest = word 
                new_intext.append(word)
    infile.close()
    in_dict = {}
    for k in new_intext:
        in_dict[str(k)] = in_dict.get(k, 0)+1
    alice_cnt = in_dict["alice"]

    in_dict = list(in_dict.items())
    in_dict.sort()

    outfile = open("alice_lines.txt", "w")
    outfile.writelines("Write"+12*" "+"Count"+"\n")
    outfile.writelines(22*"="+"\n")

    for key, val in in_dict:
        outfile.writelines("{:<12}{:>10}".format(key, val)+"\n")
    outfile.close()

    print("Word 'alice' occurs {} times in the book".format(alice_cnt))
    print("The longest line in the book is {}, which is {} chaaracters long".format(longest, len(longest)))

def test_file(infile):
    try:
        test_file = open(infile, "r")
    except:
        print("No such file as", infile)

    for i in range(10):
        print(test_file.readline(), end="")


lines_occ(infilename)
test_file("alice_lines.txt")
