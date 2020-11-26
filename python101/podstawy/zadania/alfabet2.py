#! /usr/bin/env python
# -*- coding: utf-8 -*-
n = int(input("Co którą literę wyświetlić?: "))
print("Alfabet w porządku naturalnym:")
x = 0
print(" ",end = "")
for i in range(65, 91, n):
    litera = chr(i)
    x+=1
    tmp = litera + " => " + litera.lower()
    if x == 5:
        x = 0
        tmp += "\n"
    print(tmp, end=" ")

x = -1
print("\nAlfabet w porządku odwróconym:")
print(" ",end = "")
for i in range(122, 96, -n):
    litera = chr(i)
    x +=1
    if x == 5:
        x = 0
        print("\n", end=" ")
    print(litera.upper(), " => ", litera, end = " ")
