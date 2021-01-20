#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2021 Paweł Krzemiński 
#
# Distributed under terms of the MIT license.

"""

"""
import os
from sqlalchemy import Column, ForeignKey, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

baza = create_engine('sqlite:///test_peewee.db')

BazaModel = declarative_base()
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
BazaModel.metadata.create_all(baza)
BDSesja = sessionmaker(bind=baza)
sesja = BDSesja()

def czytajdane():
    for uczen in sesja.query(Uczen).join(Klasa).all():
        print(uczen.id, uczen.imie, uczen.nazwisko, uczen.klasa.nazwa)
    print()

czytajdane()
