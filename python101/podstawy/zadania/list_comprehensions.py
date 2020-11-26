#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#

"""
Example from python101 course
"""
# lista kwadratów liczb od 0 do 9
print([x**2 for x in range(10)])

# lista dwuwymiarowa [20,40] o wartosciach a

# lista krotek (x, y), przy czym x != y
print([(x, y) for x in [1,2,3] for y in [3,1,4] if x != y])

# utworzenie listy 3-literowych imion i ich pierwszych liter
wyrazy = ['anna', 'ala', 'ela', 'wiola', 'ola']
print([[imie, imie[0]] for imie in wyrazy if len(imie)==3])


# zagnieżdzone wyrażenie listowe tworzące listę współrzędnych
# lista kwadratów z zakresu {5;50}
print([y for y in [x**2 for x in range(10)] if y > 5 and y < 50])
