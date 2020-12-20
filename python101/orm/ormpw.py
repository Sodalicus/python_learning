#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8

"""
Example from python101 course.
"""

import os
from sys import exit
from peewee import *
from ormpw_modul import *

if os.path.exists('test.db'):
    os.remove('test.db')
# tworzymy instancję bazy używanej przez modele
baza = SqliteDatabase('test.db')

class BazaModel(Model):     # klasa bazowa
    class Meta:
        database = baza

# klasy Klasa i Uczen opisują rekordy tabel "klasa" i "uczen"
# oraz relacje między nimi
class Klasa(BazaModel):
    nazwa = CharField(null=False)
    profil = CharField(default='')

class Uczen(BazaModel):
    imie = CharField(null=False)
    nazwisko = CharField(null=False)
    klasa = ForeignKeyField(Klasa, related_name = 'uczniowie')


baza.connect()  # nawiązujemy połączenie z bazą
baza.create_tables([Klasa, Uczen], safe=True)    # tworzymy tabele


# dodajemy dwie klasy, jeżeli tabela jest pusta
if Klasa().select().count() == 0:
    inst_klasa = Klasa(nazwa='1A', profil='matematyczny')
    inst_klasa.save()
    inst_klasa = Klasa(nazwa='1B', profil='humanistyczny')
    inst_klasa.save()

# tworzymy instancję klasy Klasa reprezentującą klasę "1A"
inst_klasa = Klasa.select().where(Klasa.nazwa == '1A').get()

# lista uczniów, których dane zapisane są w słownikach
uczniowie = [
        {'imie': 'Tomasz', 'nazwisko': 'Nowak', 'klasa': inst_klasa},
        {'imie': 'Jan', 'nazwisko': 'Kos', 'klasa': inst_klasa},
        {'imie': 'Piotr', 'nazwisko': 'Kowalski', 'klasa': inst_klasa}
]

# dodajemy dane wielu uczniów
Uczen.insert_many(uczniowie).execute()

# odczytujemy dane z bazy


def czytajdane():
    for uczen in Uczen.select().join(Klasa):
        print(uczen.id, uczen.imie, uczen.nazwisko, uczen.klasa.nazwa)
    print()


# zmiana klasy ucznia o identyfikatorze 2
inst_uczen = Uczen().select().join(Klasa).where(Uczen.id == 2).get()
inst_uczen.klasa = Klasa.select().where(Klasa.nazwa == '1B').get()
inst_uczen.save()

# usunięcei ucznia o identyfikatorze 3
Uczen.select().where(Uczen.id == 3).get().delete_instance()

baza.close()


inst_klasa = Klasa.select().where(Klasa.nazwa == '1B').get()
students = getdata('students.csv')
Uczen.insert_many(students).execute()

def main():
    while True:
        hello = "What is your choice?"
        hello = "1. Create \n"
        hello += "2. Read \n"
        hello += "3. Update \n"
        hello += "4. Delete \n"
        hello += "0. Quit \n"
        hello += "Pick one: "
        choice = input(hello)
        if choice == "0":
           exit()
        elif choice == "1":
            """ Create """
            while choice !="0":
                hello = "What do you want to create? \n"
                hello += "1. Class \n"
                hello += "2. Student \n"
                hello += "0. Get back \n"
                hello += "Choice: "
                choice = input(hello)
                if choice == "1":
        elif choice == "2":
            """ Read """
            while choice !="0":
                hello = "What do you want to read? \n"
                hello += "1. Class \n"
                hello += "2. Student \n"
                hello += "0. Get back \n"
                hello += "Choice: "
                choice = input(hello)
                if choice == "1":
                    classes = Klasa.select()
                    for klasa in classes:
                        print(klasa.id, klasa.profil, klasa.nazwa)
                elif choice == "2":
                    hello = "What's the surname of the student: "
                    student_surname = input(hello)
                    query = (Uczen
                            .select().where(Uczen.nazwisko == student_surname))
                    if len(query):
                        for uczen in query:
                            print(uczen.id, uczen.imie, uczen.nazwisko)
                    else:
                        print("No student with such surname.")

        elif choice == "3":
            pass
        elif choice == "4":
            pass

main()



