#!/usr/bin/env python3

test_string = "ThiS is String with Upper and lower case Letters"

def letter_count(in_string):
    in_string = in_string.lower()
    ltr_cnt = {}
    for k in in_string:
        ltr_cnt[k] = ltr_cnt.get(k, 0) + 1
    return ltr_cnt


def string_to_table(indata):
    count_dict = letter_count(indata)
    occ_table = list(count_dict.items())
    occ_table.sort()
    for k,v in occ_table:
        print(k, v)

string_to_table(test_string)
