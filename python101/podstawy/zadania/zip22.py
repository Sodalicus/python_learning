#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#

"""
Example from python101 course
"""
panstwa = ['Polska', 'Niemcy', 'Francja']
stolice = ['Warszawa', 'Berlin', 'Paryż']
panstwa_stolice = zip(panstwa, stolice)
lista_tupli = list(panstwa_stolice)
print(lista_tupli)
slownik=dict(lista_tupli)
print(slownik)
args = "slownik.items() slownik.keys() slownik.values()".split()
for i in args:
    print(eval(i))

for klucz, wartosc in slownik.items():
    print(klucz, wartosc)
