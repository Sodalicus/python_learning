#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8

"""

"""
kwadraty = map(lambda x: x**2, range(10))
print(list(kwadraty))

uczniowie = [
        ('jan', 'Nowak', '1A', 15),
        ('ola', 'Kujawiak', '3B', 17),
        ('andrzej', 'bilski', '2F', 16),
        ('kamil', 'czuja', '1B', 14)]

wyrazy = ['anna', 'ala', 'ela', 'wiola', 'ola']
# sortowanie listy wg pierwszego elementu każdej tupli, czyli imienia
print(sorted(uczniowie))
# sortowanie po nazwisku
print(sorted(uczniowie, key=lambda x: x[1]))
# najstarszy uczeń
print(max(uczniowie, key=lambda x: x[3]))
# najmłodszy uczeń
print(min(uczniowie, key=lambda x: x[3]))
imiona = filter(lambda imie: len(imie) == 3, wyrazy)
print(list(imiona))
print([imie for imie in wyrazy if len(imie)==3])
