#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from math import sqrt

slowka = {1:"pierwszego",2:"drugiego",3:"trzeciego"}

boki = []
i = 1
while len(boki) < 3:
    try:
        boki.append(int(input("Podaj dlugość {} boku: ".format(slowka[i]))))
        i+=1
    except ValueError:
        continue
boki.sort()
print(boki)
if abs(boki[1]-boki[2]) < boki[0] < boki[1] + boki[2]:
    print("Z podanych boków da się zbudować trójkąt")
else:
    print("Z podanych boków nie da się zbudować trójkąta")
if boki[0]**2 == boki[1]**2+boki[2]**2 or\
        boki[1]**2 == boki[2]**2+boki[0]**2 or\
        boki[2]**2 == boki[0]**2+boki[1]:
            print("Z podanych boków można zbudować trójkąt prostokątny.")
print("Obwód trójkąta wynosi: ", sum(boki))
p = sum(boki)/2
s = round(sqrt(abs(p*(p-boki[0])*(p-boki[1])*(p-boki[2]))),2)
print("Pole powierchni wynosi: ",s)
