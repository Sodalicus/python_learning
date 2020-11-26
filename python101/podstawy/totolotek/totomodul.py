#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
import os
import json

def ustawienia():
    """Funkcja pbiera nick użytkownika, ilość losowanych liczb, maksymalną wartość
    oraz ilość prób. Pozwala określić stopień trudności gry. """

    nick = input("Podaj nick: ")
    nazwapliku = nick + ".ini"
    gracz = czytaj_ust(nazwapliku)
    odp = None
    if gracz:
        print("Twoje ustawenia:\nLiczb: %s\nZ Maks: %s\nLosowań: %s" %
                (gracz[1], gracz[2], gracz[3]))
        odp = input("Zmieniasz (t/n)? ")

    if not gracz or odp.lower() == "t":
        while True:
            try:
                ile = int(input("Podaj ilość typowanych liczb: "))
                maks = int(input("Podaj maksymalną losowaną liczbę: "))
                if ile > maks:
                    print("Błędne dane!")
                    continue
                ilelos = int(input("Ile losowań: "))
                break
            except ValueError:
                print("Błędne dane!")
                continue
        gracz = [nick, str(ile), str(maks), str(ilelos)]
        zapisz_ust(nazwapliku, gracz)

    return gracz[0:1] + [int(x) for x in gracz[1:4]]


def czytaj_ust(nazwapliku):
    if os.path.isfile(nazwapliku):
        plik = open(nazwapliku, "r")
        linia = plik.readline()
        plik.close()
        if linia:
            return linia.split(";")
    return False


def zapisz_ust(nazwapliku, gracz):
    plik = open(nazwapliku, "w")
    plik.write(";".join(gracz))
    plik.close()


def losujliczby(ile, maks):
    """Funcja losuje ile unikalnych liczb całkowitych od 1 do maks"""
    liczby = []
    i = 0
    while i < ile:
        liczba = random.randint(1, maks)
        if liczby.count(liczba) == 0:
            liczby.append(liczba)
            i += 1
    return liczby


def pobierztypy(ile, maks):
    """Funkcja pobiera od użytkownika jego typy wylosowanych liczb"""
    print("Wytypuj %s z %s liczb: " % (ile, maks))
    typy = set()
    i = 0
    while i < ile:
        try:
            typ = int(input("Podaj liczbę %s: " % (i+1)))
        except ValueError:
            print("Błędne dane!")
            continue

        if 0 < typ <= maks and typ not in typy:
            typy.add(typ)
            i += 1
    return typy


def wyniki(liczby, typy):
    """Funkcja porównuje wylosowane i wytypowane liczby,
    zwraca ilość trafień"""
    trafione = set(liczby) & typy
    if trafione:
        print("\nIlość trafień: %s" % len(trafione))
        trafione = ", ".join(map(str, trafione))
        print("Trafione liczby: %s" % trafione)
    else:
        print("Brak trafień. Spróbuj jeszcze raz!")

    print("\n" + "x" * 40 + "\n")  # wydrukuj 40 znaków x

    return len(trafione)


def czytaj_json(nazwapliku):
    """Funkcja odczytuje dane w formacie json z pliku"""
    dane = []
    if os.path.isfile(nazwapliku):
        with open(nazwapliku, "r") as plik:
            dane = json.load(plik)
    return dane


def zapisz_json(nazwapliku, dane):
    """Funkcja zapisuje dane w formacie json do pliku"""
    with open(nazwapliku, "w") as plik:
        json.dump(dane, plik)


def zapisz_str(nazwapliku, dane):
    """Funkcja zapisuje dane w formacie txt do pliku"""
    with open(nazwapliku, "w") as plik:
        for slownik in dane:
            linia = [k + ":" + str(w) for k, w in slownik.items()]
            linia = ";".join(linia)
            plik.write(linia+"\n")
            # print >> plik, linia

#toto = "wylosowane:[1];dane:(5, 45);ile:1;czas:1605800551.2767868"

def czytaj_str(nazwapliku):
    """Funkcja odczytuje dane z pliku i zwraca listę słowników"""
    dane = []
    with open(nazwapliku, "r") as plik:
        for line in plik:
            slownik = {}
            for para in line.split(";"):
                para = para.split(":")
                slownik[para[0]] = para[1]
            dane.append(slownik)
    return dane

czytaj_str("soda.str")
