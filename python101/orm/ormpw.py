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

if os.path.exists('test_peewee.db'):
    os.remove('test_peewee.db')
# tworzymy instancję bazy używanej przez modele
baza = SqliteDatabase('test_peewee.db')

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
print(uczniowie)

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
        hello = "\n"
        hello += "1. Create \n"
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
                hello = "\n"
                hello += "What do you want to create? \n"
                hello += "1. Class \n"
                hello += "2. Student \n"
                hello += "0. Get back \n"
                hello += "Choice: "
                choice = input(hello)
                if choice == "1":
                    """ Create Class """
                    hello = "\n"
                    hello += "Type in name and profile seperated by coma: "
                    data = input(hello).split(sep=",")
                    if len(data) == 2:
                        inst_klasa = Klasa(nazwa=data[0].upper(), profil=data[1])
                        inst_klasa.save()
                elif choice == "2":
                    """ Create Student """
                    hello = "\n"
                    hello += "Type in class name, name and surname seperated by coma: "
                    data = ""
                    while data.count(",") != 2:
                        data = input(hello)
                    data = data.split(",")
                    try:
                        inst_klasa = Klasa.select().where(Klasa.nazwa == data[0].upper()).get()
                        uczen = Uczen(imie = data[1].capitalize(), nazwisko = data[2].capitalize(), klasa = inst_klasa)
                        uczen.save()
                    except DoesNotExist:
                        print("No class with the name {}.".format(data[0].upper()))


        elif choice == "2":
            """ Read """
            while choice !="0":
                hello = "\n"
                hello += "What do you want to read? \n"
                hello += "1. Classes \n"
                hello += "2. Student \n"
                hello += "3. All students \n"
                hello += "0. Get back \n"
                hello += "Choice: "
                choice = input(hello)
                if choice == "1":
                    """ Read Classes """
                    classes = Klasa.select()
                    for klasa in classes:
                        print(klasa.id, klasa.profil, klasa.nazwa)
                elif choice == "2":
                    """ Read Student """
                    hello = "\n"
                    hello += "What's the surname of the student: "
                    student_surname = input(hello)
                    query = (Uczen
                            .select().where(Uczen.nazwisko == student_surname.capitalize()))
                    if len(query):
                        for uczen in query:
                            print(uczen.id, uczen.imie, uczen.nazwisko)
                    else:
                        print("No student with such surname.")
                elif choice == "3":
                    """ Read All Students """
                    query = Uczen.select().join(Klasa)
                    if len(query):
                        for uczen in query:
                            print(uczen.id, uczen.imie, uczen.nazwisko, uczen.klasa.nazwa)

        elif choice == "3":
            """ Update """
            while choice != "0":
                hello = "\n"
                hello += "What do you want to update? \n"
                hello += "1. Class` profile \n"
                hello += "2. Student's data \n"
                hello += "0. Get back \n"
                hello += "Choice: "
                choice = input(hello)
                if choice == "1":
                    """ Update Class' Profile """
                    hello = "\n"
                    hello += "Type in class name and new profile, seperated by coma: "
                    data = ""
                    while "," not in data:
                        data = input(hello)
                    data = data.split(",")
                    try:
                        klasa_inst = Klasa.select().where(Klasa.nazwa == data[0].upper()).get()
                        klasa_inst.profil = data[1]
                        klasa_inst.save()
                    except DoesNotExist:
                        print("No class with given name: ", data[0].upper())
                elif choice == "2":
                    """ Update Student's Data """
                    hello = "\n"
                    hello += "What's the student id: "
                    data = input(hello)
                    try:
                        uczen = Uczen.select().join(Klasa).where(Uczen.id == data).get()
                        print(uczen.id, uczen.imie, uczen.nazwisko, uczen.klasa.nazwa)
                        hello = "\n"
                        hello += "Type in new name, surname and class name, separated by comas: "
                        new_data = ""
                        while new_data.count(",") != 2:
                            new_data = input(hello)
                        print(new_data)
                        new_data = new_data.split(",")
                        print(new_data)
                        try:
                            klasa_inst = Klasa.select().where(Klasa.nazwa == new_data[2].upper()).get()
                            uczen.imie = new_data[0].capitalize()
                            uczen.nazwisko = new_data[1].capitalize()
                            uczen.klasa = klasa_inst
                            uczen.save()

                        except DoesNotExist:
                            print("No class with given name: ",new_data[2].upper())
                    except DoesNotExist:
                        print("No student with given id: ", data)

        elif choice == "4":
            """ Delete """
            while choice !="0":
                hello = "\n"
                hello += "What do you want to delete? \n"
                hello += "1. Empty Class \n"
                hello += "2. Student \n"
                hello += "0. Get back \n"
                hello += "Choice: "
                choice = input(hello)
                if choice == "1":
                    """Delete Empty Class """
                    hello = "\n"
                    hello += "What is the class name: "
                    data = input(hello)
                    try:
                        klasa_inst = Klasa.select().where(Klasa.nazwa == data.upper()).get()
                        uczniowie =  Uczen.select().join(Klasa).where(Uczen.klasa.id == klasa_inst).count()
                        if uczniowie <= 0:
                            klasa_inst.delete_instance()
                        else:
                            print("Class {} in not empty, it has {} student(s)".format(data.upper(), uczniowie))
                    except DoesNotExist:
                        print("No class with given name: ",data.upper())
                elif choice == "2":
                    """ Delete Student by id"""
                    hello = "\n"
                    hello += "What is the student's id: "
                    data = input(hello)
                    try:
                        uczen = Uczen.select().join(Klasa).where(Uczen.id == data).get()
                        print(uczen.id, uczen.imie, uczen.nazwisko, uczen.klasa.nazwa)
                        uczen.delete_instance()
                    except DoesNotExist:
                        print("No student with given id: ", data)

main()



