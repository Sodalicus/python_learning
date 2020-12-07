#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 Paweł Krzemiński 
#
# Distributed under terms of the MIT license.

"""

"""
import os, sqlite3

basefile = "crud.db"



def get_integer(string_var):
    while True:
        try:
            integer = int(input(string_var))
            return str(integer)
        except ValueError:
            print(integer, "is not a valid integer")



def add_class(string_var):
    """ Adds new class to the table.
    accepts class_name,profile
    """
    data = string_var.split(",")
    data = [x.strip() for x in data]
    if len(data) == 2:
        class_name = (data[0].upper(), data[1])
        sql_query = ('INSERT INTO class VALUES(NULL, ?, ?);',class_name)
        add_row(basefile, sql_query)
    else:
        print("Invalid data.")


def add_student(string_var):
    """Accepts string in format name,surname,class,
    Then inserts data into student table.
    """
    data = string_var.split(",")
    data = [x.strip().capitalize() for x in data]
    if len(data) == 3:
        sql_query = ('SELECT id FROM class WHERE name = ?;', (data[2].upper(),))
        class_id = read_single_row(basefile,sql_query)
        if class_id is not None:
            student = (data[0], data[1], class_id[0])
            sql_query = ('INSERT INTO student VALUES(NULL, ?, ?, ?);',student)
            add_row(basefile, sql_query)
        else:
            print("no such class as {}".format(data[2]))
    else:
        print("Invalid data.")


def delete_student(string_var):
    try:
        data = int(string_var.strip())
        sql_query = ('DELETE FROM student WHERE id=?;',(data,))
        add_row(basefile, sql_query)
    except ValueError:
        print("It is not a number.")


def return_student(students_id):
    """Return student by id"""
    sql_query = ('SELECT * FROM student WHERE id=?;',students_id)
    student = read_single_row(basefile, sql_query)
    return student


def delete_class(string_var):
    try:
        data = int(string_var.strip())
        sql_query = ('DELETE FROM class WHERE id=?;',(data,))
        add_row(basefile, sql_query)
    except ValueError:
        print("It is not a number.")


def update_name(name,students_id):
    """Update student's name, given id and new name"""
    sql_query = ('UPDATE student SET name=? WHERE id=?;',(name,students_id))
    add_row(basefile, sql_query)


def update_surname(surname,students_id):
    """Update student's surname, given id and new surname"""
    sql_update_query = ('UPDATE student SET surname=? WHERE id=?;',(surname,students_id))
    add_row(basefile,sql_update_query)


def update_students_class(class_name,students_id):
    """Update student's class, given id and new class"""
    sql_update_query = ('UPDATE student SET class_id=? WHERE id=?;',(class_name,students_id))
    add_row(basefile,sql_update_query)


def get_classes():
    """Returns tuple of existing class names in class table"""
    class_names = []
    sql_query = ('SELECT DISTINCT name FROM class;')
    rows = read_all_rows(basefile,sql_query)
    for row in rows:
        class_names.append(row[0])
    return tuple(class_names)


def add_row(basefile, sql_query):
    try:
        connection = sqlite3.connect(basefile)
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()
        cursor.execute(*sql_query)
        connection.commit()
        cursor.close()
        return 0

    except sqlite3.Error as error:
        print("Failed to write data to the table", error)

    finally:
        if (connection):
            connection.close()


def read_single_row(basefile, sql_query):
    try:
        connection = sqlite3.connect(basefile)
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()
        cursor.execute(*sql_query)
        data = cursor.fetchone()
        cursor.close()
        return data

    except sqlite3.Error as error:
        print("Failed to read data from table", error)

    finally:
        if (connection):
            connection.close()


def read_all_rows(basefile, sql_query):
    try:
        connection = sqlite3.connect(basefile)
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()
        cursor.execute(sql_query)
        data = cursor.fetchall()
        cursor.close()
        return data

    except sqlite3.Error as error:
        print("Failed to read data from table", error)

    finally:
        if (connection):
            connection.close()


def print_single_row(row):
    if row == None:
        print("No data to print.")
    else:
        for cell in row:
            print(cell, end=" ")


def print_multi_row(table):
    if table == None:
        print("No data to print")
    else:
        for row in table:
            for i in range(len(row)):
                print(row[i], end= " ")
            print()

