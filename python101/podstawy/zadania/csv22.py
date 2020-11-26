#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8

"""

"""
import csv

dane = ([1, 'jan', 'kowalski'], [2, 'anna', 'nowak'])
plik = 'test.csv'

with open(plik, 'w', newline='') as plikcsv:
    tresc = csv.writer(plikcsv, delimiter=';')
    for lista in dane:
        tresc.writerow(lista)


with open(plik, newline='') as plikcsv:
    tresc = csv.reader(plikcsv, delimiter=';')
    for linia in tresc:
        print(linia)
