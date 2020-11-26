#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 Paweł Krzemiński 
#
# Distributed under terms of the MIT license.

"""
Example from python101 course.
"""

import math


def drukuj(co, kom="Sekwencja zawiera: "):
    print(kom)
    for i in co:
        print(i, end=" ")


def srednia(oceny):
    suma = sum(oceny)
    return suma/float(len(oceny))


def mediana(oceny):
    """
    Jeżeli ilość ocen jest parzysta, medianą jest średnia arytmetyczna
    dwóch środkowych ocen. Jeśli ilość jest nieparzysta, mediana równa
    się elementowi środkowemu uporządkowanej rosnąco listy ocen.
    """
    oceny.sort()
    if len(oceny) %2 == 0:
        half = int(len(oceny)/2)
        #return float(oceny[half-1]+oceny[half]/2.0
        return float(sum(oceny[half-1:half+1]))/2.0
    else:
        return oceny[int(len(oceny)/2)]


def wariancja(oceny, srednia):
    """
    Wariancja to suma kwadratów różnicy każdej oceny i średniej
    podzielona przez ilość ocen:
    sigma = (o1-s)+(o2-s)+...+(on-s) / n, gdzie:
    o1, o2, ..., one - kolejne oceny,
    s - srednia ocen,
    n - liczba ocen.
    """
    sigma = 0.0 
    for ocena in oceny:
        sigma += (ocena-srednia)**2
    return sigma/len(oceny)


def odchylenie(oceny, srednia):
    w = wariancja(oceny, srednia)
    return math.sqrt(w)

def drukuj_plus(oceny, odchylenie):
    for ocena in oceny:
        print("{0} +/- {1:5.2f}".format(ocena, odchylenie))
