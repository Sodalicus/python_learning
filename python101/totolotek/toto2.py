#/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
"""
maksliczb = int(input("Podaj maksymalną wylosowaną liczbę: "))
ileliczb = maksliczb+1
while ileliczb>maksliczb:
    ileliczb = int(input("Ile liczb chcesz wytypować: "))
    if ileliczb>maksliczb:
        print("Błędne dane")
"""
try:
    ileliczb = int(input("Podaj ilość typowanych liczb: "))
    maksliczb = int(input("Podaj maksymalną losowaną liczbę: "))
    if ileliczb > maksliczb:
        print("Błędne dane!")
        exit()
except ValueError:
    print("Błędne dane!")
    exit()

#print("Wytypuj {} z {} liczb.".format(ileliczb, maksliczb))

"""
wylosowane = []

for i in range(ileliczb):
    wylosowane.append(random.randint(0, maksliczb))

wylosowane.sort()
print("Wylosowane liczby: ", wylosowane)
"""
wylosowane = []
i = 0
while i < ileliczb:
    liczba = random.randint(0, maksliczb)
    if liczba not in wylosowane:
    #if wylosowane.count(liczba) == 0:
        wylosowane.append(liczba)
        i += 1

for i in range(3):
    print("Wytypuj %s z %s liczb: " % (ileliczb, maksliczb))
    typy = set()
    i = 0
    while i < ileliczb:
        try:
            typ = int(input("Podaj liczbę %s: " %(i + 1)))
        except ValueError:
            print("Błędne dane!")
            continue
        if 0 < typ <= maksliczb and typ not in typy:
            typy.add(typ)
            i += 1

    trafione = set(wylosowane) & typy
    if trafione:
        print("\nIlość trafień: %s" % len(trafione))
        print("Trafione liczby: ", trafione)
    else:
        print("Brak trafień. Spróbuj jeszcze raz!")
print(wylosowane)
