#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
liczby = []
i = 1
while len(liczby) < 3:
    try:
        liczby.append(int(input("Podaj {} liczbę: ".format(i))))
        i+=1
    except ValueError:
        continue

smallest = liczby[0]
for i in liczby:
    if i < smallest: smallest = i

print(i)
"""

op = "t"
while op == "t":
    a, b, c = input("Podaj trzy liczby oddzielone spacjami: ").split(",")

    print("Wprowadzono liczby:", a, b, b)
    print("\nNajmniejsza:")

    if a < b:
        if a <c:
            najmniejsza = a
        else:
            najmniejsza = c
    elif b < c:
        najmniejsza = b
    else:
        najmniejsza = c

    print(najmniejsza)
    op = input("Jeszcze raz? (t/n)").lower()

