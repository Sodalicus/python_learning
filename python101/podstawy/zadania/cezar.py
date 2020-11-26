#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 Paweł Krzemiński 
#
# Distributed under terms of the MIT license.

"""

"""
alphabet = "a b c d e f g h i j k l m n o p r s t u w v y z".split()
print(len(alphabet))
# 24
KEY = 13

def encode(phrase, key=13):
    new_phrase = ""
    for char in phrase.lower():
        if char not in alphabet:
            new_phrase += char
        else:
            new_index = (alphabet.index(char.lower())+key)%24
            new_phrase += alphabet[new_index]
    return new_phrase


def encode2(phrase, key=13):
    new_phrase = ""
    for char in phrase:
        new_char = ord(char)+key
        new_phrase+=chr(new_char)
    return new_phrase


def decode(phrase, key=13):
    new_phrase = ""
    for char in phrase.lower():
        if char not in alphabet:
            new_phrase += char
        else:
            new_index = (alphabet.index(char.lower())-key)%24
            new_phrase += alphabet[new_index]
    return new_phrase

def decode2(phrase, key=13):
    new_phrase = ""
    for char in phrase:
        new_char = ord(char)-key
        new_phrase+=chr(new_char)
    return new_phrase


enc = encode("To jest przykładowe zdanie.!@#$%", 13)
enc2 = encode2("To jest przykładowe zdanie.!@#$%", 13)
print(enc)
print(enc2)
print(decode(enc,13))
print(decode2(enc2, 13))
