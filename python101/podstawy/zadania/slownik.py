#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8

"""
Example from python101 course
"""
import os, csv

slownik = {}
sPlik = "slownik.csv"

"""
def otworz(sPlik):
    if os.path.isfile(sPlik):
        with open(sPlik, "r") as pliktxt:
            for line in pliktxt:
                t = line.split(":")
                wobcy = t[0]
                znaczenia = t[1].replace("\n", "")
                znaczenia = znaczenia.split(",")
                slownik[wobcy] = znaczenia
    return len(slownik)
"""
def otworz(sPlik):
    if os.path.isfile(sPlik):
        with open(sPlik, newline='') as plikcsv:
            tresc = csv.reader(plikcsv)
            for linia in tresc:
                slownik[linia[0]] = linia[1:]
    return len(slownik)
"""
def zapisz(slownik):
    pliktxt = open(sPlik, "w")
    for wobcy in slownik:
        znaczenia = ",".join(slownik[wobcy])
        linia = ":".join([wobcy, znaczenia])
        pliktxt.write(linia+"\n")
        #print(linia, file=pliktxt)
    pliktxt.close()
"""
def zapisz(slownik):
    with open(sPlik,"w", newline='') as plikcsv:
        tresc = csv.writer(plikcsv)
        for wobcy in slownik:
            lista = slownik[wobcy]
            lista.insert(0, wobcy)
            tresc.writerow(lista)

def oczysc(str):
    str = str.strip()  # usuń początkowe i końcowe białe znaki
    str = str.lower()  # zmień na małe litery
    return str


def drukuj(slownik):
    print("=" * 50)
    print("{0: <15}{1: <40}".format("Wyraz obcy", "Znaczenie"))
    print("=" * 50)
    for wobcy in slownik:
        ter = ".".join(slownik[wobcy])
        print("{0:<15}{1:<40}".format(wobcy, ter))


def nauka(slownik):
    """
    Wyświetla kolejne wyrazy obce z slownika.
    Pyta użytkownika o możliwe znaczenia.
    Wyświetla które znaczenia są poprawne.
    """
    for wobcy in slownik:
        znaczenia = input("Podaj znaczenia wyrazu {}, oddzielone przecinkami: ".format(wobcy))
        if znaczenia == "#koniec":return 0
        znaczenia = znaczenia.split(",")
        for znaczenie in znaczenia:
            if oczysc(znaczenie) in slownik[wobcy]:
                print(oczysc(znaczenie), "jest poprawnym tłumaczeniem słowa", wobcy)
            else:
                print(oczysc(znaczenie), "nie jest poprawnym tłumaczeniem słowa", wobcy)



def main(args):
    print("""Podaj dane w formacie:
    wyraz obcy: znaczenie1, znaczenie2
    Aby zakończyć wprowadzanie danych, podaj: #koniec.
    Aby usunąć wpis, podaj: #usun
    Aby rozpocząć naukę, podaj: #nauka
    """)

    # wobce = set() # pusty zbiór wyrazów obcych
    # zmienna oznaczająca, że użytkownik uzupełnił lub zmienił słownik
    nowy = False
    ileWyrazow = otworz(sPlik)
    print("Wpisów w bazie: ", ileWyrazow)

    while True:
        dane = input("Podaj dane: ")
        t = dane.split(":")
        wobcy = t[0].strip().lower()
        if wobcy == "#koniec":
            break
        elif wobcy =="#usun":
            dusunieca = input("Podaj wyraz do usunięcia: ")
            if dusunieca in slownik:
                del(slownik[dusunieca])
                continue
            else:
                print("Podanego wyrazu: {}, nie ma w słowniku".format(dusunieca))
                continue
        elif wobcy == "#nauka":
            nauka(slownik)
        elif dane.count(":") == 1:  # sprawdzamy poprawność danych
            if wobcy in slownik:
                print("Wyraz", wobcy, " i jego znaczenia są już w słowniku.")
                op = input("Zastąpić wpis (t/n)? ")
            if wobcy not in slownik or op == "t":
                znaczenia = t[1].split(",")
                znaczenia = list(map(oczysc, znaczenia))
                slownik[wobcy] = znaczenia
                nowy = True
        else:
            print("Błędny format.")
    if nowy:
        zapisz(slownik)

    drukuj(slownik)


    return 0


if __name__ == "__main__":
    import sys
    sys.exit(main(sys.argv))
