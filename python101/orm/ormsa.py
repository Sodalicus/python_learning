#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8

"""
Example from python101 course
"""

import os, random
from sqlalchemy import Column, ForeignKey, Integer, String, create_engine, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

if os.path.exists('test.db'):
    os.remove('test.db')

# tworzymy instancję klasy Engine do obsługi bazy
baza = create_engine('sqlite:///test.db', echo=False)

# klasa bazowa
BazaModel = declarative_base()

# klasy Klasa i Uczen opisują rekordy tabel "klasa" i "uczen"
# oraz relacje między nimi

class Klasa(BazaModel):
    __tablename__ = 'klasa'
    id = Column(Integer, primary_key = True)
    nazwa = Column(String(100), nullable=False)
    profil = Column(String(100), default='')
    uczniowie = relationship('Uczen', backref='klasa')

class Uczen(BazaModel):
    __tablename__ = 'uczen'
    id = Column(Integer, primary_key=True)
    imie = Column(String(100), nullable=False)
    nazwisko = Column(String(100), nullable=False)
    klasa_id = Column(Integer, ForeignKey('klasa.id'))

# tworzymy tabelę
BazaModel.metadata.create_all(baza)

# tworzymy sesję, która przechowuje obiekty i umozliwia "rozmowę" z bazą
BDSesja = sessionmaker(bind=baza)
sesja = BDSesja()

# dodajemy dwie klasy, jeżeli tabela jest pusta
if not sesja.query(Klasa).count():
    sesja.add(Klasa(nazwa='1A', profil='matematyczny'))
    sesja.add(Klasa(nazwa='1B', profil='humanistyczny'))

# tworzymy instancję klasy Klasa reprezentującą klasę '1A'
inst_klasa = sesja.query(Klasa).filter_by(nazwa='1A').one()

# dodajemy dane wielu uczniów
sesja.add_all([
    Uczen(imie='Tomasz', nazwisko='Nowak', klasa_id=inst_klasa.id),
    Uczen(imie='Jan', nazwisko='Kos', klasa_id=inst_klasa.id),
    Uczen(imie='Piotr', nazwisko='Kowalski', klasa_id=inst_klasa.id),
    Uczen(imie='Rak', nazwisko='Piotrowski', klasa_id="2")
    ])

names = "Ahmed Farid Jack Jesus Jahve Ewelina Julka Grażyna Janusz Seba Pioter Dick".split()
surnames = "Mohamed Black White Master Slave Goatfucker Rughead Pink Jude Ass Turd Bush".split()
random.shuffle(names)
random.shuffle(surnames)
for a in range(len(names)-1):
    a+=1
    i = random.randint(1,2)
    name=names[a]
    surname=surnames[a]
    sesja.add(Uczen(imie=name, nazwisko=surname, klasa_id = i))

def czytajdane():
    for uczen in sesja.query(Uczen).join(Klasa).all():
        print(uczen.id, uczen.imie, uczen.nazwisko, uczen.klasa.nazwa)
    print()

# zmiana klasy ucznia o identyfikatorze 2
inst_uczen = sesja.query(Uczen).filter(Uczen.id == 2).one()
inst_uczen.klasa_id = sesja.query(Klasa.id).filter(
        Klasa.nazwa == '1B').scalar()

# usunięcie ucznia o identyfikatorze 3
sesja.delete(sesja.query(Uczen).get(3))


# zapisanie zmian w bazie i zamknięcie sesji

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
            """ Create A"""
            while choice !="0":
                hello = "\n"
                hello += "What do you want to create? \n"
                hello += "1. Class \n"
                hello += "2. Student \n"
                hello += "0. Get back \n"
                hello += "Choice: "
                choice = input(hello)
                if choice == "1":
                    """ Create Class A"""
                    hello = "\n"
                    hello += "Type in name and profile seperated by coma: "
                    data = input(hello).split(sep=",")
                    if len(data) == 2:
                        sesja.add(Klasa(nazwa=data[0].upper(), profil=data[1]))
                elif choice == "2":
                    """ Create Student A"""
                    hello = "\n"
                    hello += "Type in class name, name and surname seperated by coma: "
                    data = ""
                    while data.count(",") != 2:
                        data = input(hello)
                    data = data.split(",")
                    try:
                        inst_klasa = sesja.query(Klasa).filter(Klasa.nazwa == data[0].upper()).one()
                        sesja.add(Uczen(imie=data[1].capitalize(), nazwisko = data[2].capitalize(), klasa = inst_klasa))
                    except:
                        print("No class with the name {}.".format(data[0].upper()))


        elif choice == "2":
            """ Read A"""
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
                    """ Read Classes A"""
                    classes = sesja.query(Klasa).all()
                    for klasa in classes:
                        print(klasa.id, klasa.profil, klasa.nazwa)
                elif choice == "2":
                    """ Read Student A"""
                    hello = "\n"
                    hello += "What's the surname of the student: "
                    student_surname = input(hello)
                    student = sesja.query(Uczen).filter(Uczen.nazwisko == student_surname.capitalize()).all()
                    if len(student):
                        for uczen in student:
                            print(uczen.id, uczen.imie, uczen.nazwisko)
                    else:
                        print("No student with such surname.")
                elif choice == "3":
                    """ Read All Students A"""
                    query = sesja.query(Uczen).join(Klasa).all()
                    if len(query):
                        print()
                        for uczen in query:
                            print(uczen.id, uczen.imie, uczen.nazwisko, uczen.klasa.nazwa)

        elif choice == "3":
            """ Update A"""
            while choice != "0":
                hello = "\n"
                hello += "What do you want to update? \n"
                hello += "1. Class` profile \n"
                hello += "2. Student's data \n"
                hello += "0. Get back \n"
                hello += "Choice: "
                choice = input(hello)
                if choice == "1":
                    """ Update Class' Profile A"""
                    hello = "\n"
                    hello += "Type in class name and new profile, seperated by coma: "
                    data = ""
                    while "," not in data:
                        data = input(hello)
                    data = data.split(",")
                    klasa = sesja.query(Klasa).filter(Klasa.nazwa == data[0].upper()).first()
                    if klasa:
                        klasa.profil = data[1]
                    else:
                        print("No class with name {}.".format(data[0].upper()))
                elif choice == "2":
                    """ Update Student's Data A"""
                    hello = "\n"
                    hello += "What's the student id: "
                    data = input(hello)
                    uczen = sesja.query(Uczen).filter(Uczen.id == data).first()
                    if uczen:
                        print(uczen.id, uczen.imie, uczen.nazwisko, uczen.klasa.nazwa)
                        hello = "\n"
                        hello += "Type in new name, surname and class name, separated by comas: "
                        new_data = ""
                        while new_data.count(",") != 2:
                            new_data = input(hello)
                        print(new_data)
                        new_data = new_data.split(",")
                        print(new_data)
                        klasa = sesja.query(Klasa).filter(Klasa.nazwa == new_data[2].upper()).first()
                        if klasa:
                            uczen.imie = new_data[0].capitalize()
                            uczen.nazwisko = new_data[1].capitalize()
                            uczen.klasa_id = klasa.id

                        else:
                            print("No class with given name: ",new_data[2].upper())
                    else:
                        print("No student with given id: ", data)

        elif choice == "4":
            """ Delete A"""
            while choice !="0":
                hello = "\n"
                hello += "What do you want to delete? \n"
                hello += "1. Empty Class \n"
                hello += "2. Student \n"
                hello += "0. Get back \n"
                hello += "Choice: "
                choice = input(hello)
                if choice == "1":
                    """Delete Empty Class A"""
                    hello = "\n"
                    hello += "What is the class name: "
                    data = input(hello).upper()
                    klasa_count = sesja.query(Klasa).filter(Klasa.nazwa == data).first()
                    if klasa_count:
                        klasa = sesja.query(Klasa).filter(Klasa.nazwa == data).first()
                        uczniowie_count= sesja.query(Uczen).filter(Uczen.klasa_id == klasa.id).count()
                        if uczniowie_count:
                            print("Class {} in not empty, it has {} student(s)".format(data.upper(), uczniowie_count))
                        else:
                            sesja.query(Klasa).filter(Klasa.nazwa == data).delete()
                            print("Class {} deleted".format(data))
                    else:
                        print("No class with given name: ",data.upper())
                elif choice == "2":
                    """ Delete Student by id A"""
                    hello = "\n"
                    hello += "What is the student's id: "
                    data = input(hello)
                    uczen = sesja.query(Uczen).filter(Uczen.id == data).first()
                    if uczen:
                        sesja.query(Uczen).filter(Uczen.id == data).delete()
                        print("Student with id {} deleted.".format(data))
                    else:
                        print("No student with id ", data)
main()
sesja.commit()
sesja.close()
