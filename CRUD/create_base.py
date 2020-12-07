#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 Paweł Krzemiński 
#
# Distributed under terms of the MIT license.

"""

"""

import sqlite3
import os


def read_csv(csvfile):
    data = []
    if os.path.isfile(csvfile):
        with open(csvfile, "r") as file:
            for line in file:
                line = line.replace("\n", "")
                data.append(tuple(line.split(",")))
            return data
    else:
        print(csvfile, "doesn't exist")


def create_db():
    """Create empty database,
       if database exists, drop it,
       and create new empty"""
    connect = sqlite3.connect('crud.db')
    connect.row_factory = sqlite3.Row
    cursor = connect.cursor()

    cursor.execute("DROP TABLE IF EXISTS class;")
    cursor.execute("""
                    CREATE TABLE IF NOT EXISTS class (
                    id INTEGER PRIMARY KEY ASC,
                    name VARCHAR(250) NOT NULL,
                    profile VARCHAR(250) DEFAULT ''
                    )""")

    cursor.execute("DROP TABLE IF EXISTS student;")
    cursor.execute("""
                    CREATE TABLE IF NOT EXISTS student (
                    id INTEGER PRIMARY KEY ASC,
                    name varchar(250) NOT NULL,
                    surname VARCHAR(250) NOT NULL,
                    class_id INTEGER NOT NULL,
                    FOREIGN KEY(class_id) REFERENCES class(id))
                    """)


def fill_db(csvfile, sql):
    """Fill the existing database with content from file"""
    try:
        connect = sqlite3.connect('crud.db')
        connect.row_factory = sqlite3.Row
        cursor = connect.cursor()

        content = read_csv(csvfile)
        cursor.executemany(sql, content)
        connect.commit()
    except sqlite3.Error as error:
        print("sql error", error)


