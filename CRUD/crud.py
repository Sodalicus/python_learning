#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 Paweł Krzemiński 
#
# Distributed under terms of the MIT license.

"""
My first CRUD approach
"""

import sqlite3, os
from create_base import *
from crud_mod import *


def main():
    sql_pragma = ('PRAGMA foreign_keys = ON;')
    # Set foreign keys constraint on
    exe_query(sql_pragma)

    while True:
        hello = "What do you want to do?\n"
        hello += "1) Create\n"
        hello += "2) Read\n"
        hello += "3) Update\n"
        hello += "4) Delete\n"
        hello += "5) Reset database\n"
        hello += "0) Exit\n"
        hello += "Choice: "
        choice = ""
        print()


        choice = input(hello).lower()
        if choice == "0":
            """Exit program"""
            print("Over")
            break


        elif choice == "1":
            """Create"""
            while True:
                print()
                mm = input("Create: 1) Student, 2) Class; 0) Back: ")
                if mm == "1":
                    """Create student"""
                    student = input("Type in: name,surname,class_name: ")
                    add_student(student)
                elif mm == "2":
                    """Create class"""
                    class_name = input("Type in: class_name,profile: ")
                    add_class(class_name)
                elif mm == '0':
                    """Go back"""
                    print("Going back.")
                    break


        elif choice == "2":
            """Read"""
            while True:
                print()
                hello = "What do you want read?:\n"
                hello += "1) Classes,\n"
                hello += "2) All students,\n"
                hello += "3) Student\n"
                hello += "0) Back\n"
                hello += "Choice: "
                print()
                mm = input(hello)

                if mm == "1":
                    """Read classes"""
                    sql_query = ('SELECT * FROM class;')
                    classes = read_all_rows(sql_query)
                    print()
                    print_multi_row(classes)

                elif mm == "2":
                    """Read all students"""
                    sql_query = ('SELECT * FROM student;')
                    students = read_all_rows(sql_query)
                    print()
                    print_multi_row(students)

                elif mm == "3":
                    """Read student"""
                    surname = input("Type in student's surname: ").strip()
                    surname = surname.capitalize()
                    sql_query = 'SELECT * FROM student WHERE surname=?'
                    student = read_single_row(sql_query, surname)
                    print()
                    print_single_row(student)

                elif mm == "0":
                    """Go back"""
                    print("Going back")
                    break


        elif choice == "3":
            """Update"""
            while True:
                hello = "What do you want to update?\n"
                hello += "1) Student's name\n"
                hello += "2) Student's surname\n"
                hello += "3) Student's class\n"
                hello += "4) Class' profile\n"
                hello += "0) Back\n"
                hello += "Choice: "
                print()
                choice = ""
                choice = input(hello)
                if choice == "1":
                    """Update student's name"""
                    students_id = get_integer("What's student id: ")
                    print("Student's details: ")
                    print("id,   name,   surname,  class")
                    print_single_row(return_student(students_id))
                    print()
                    name = input("What's new name: ").capitalize()
                    update_name(name,students_id)
                elif choice == "2":
                    """Update student's surename"""
                    students_id = get_integer("What's student id: ")
                    print("Student's details: ")
                    print_single_row(return_student(students_id))
                    print()
                    surname = input("What's new surname: ").capitalize()
                    update_surname(surname,students_id)
                elif choice == "3":
                    """Update student's class"""
                    students_id = get_integer("What's student id: ")
                    print("Student's details: ")
                    print_single_row(return_student(students_id))
                    print()
                    class_name = None
                    while class_name not in get_classes():
                        print("Available classes: ", get_classes())
                        class_name = input("What's new student's class: ").upper()
                    update_students_class(class_name,students_id)
                elif choice == "4":
                    """Update class' profile"""
                    class_name = None
                    while class_name not in get_classes():
                        print("Available classes: ", get_classes())
                        class_name = input("What's the class name which profile you want to update: ")
                    new_profile = input("What the new class' profile: ")
                    update_class_profile(new_profile, class_name)
                elif choice == "0":
                    """Go back"""
                    print("Going back")
                    break


        elif choice == "4":
            """Delete"""
            while True:
                print()
                mm = input("What do you want delete? 1) Student, 2) Class; 0) Back: ").lower()
                if mm == "1":
                    """Delete student"""
                    student_id = input("What's the student's id?: ")
                    delete_student(student_id)
                elif mm== "2":
                    """Delete class"""
                    class_id = input("Whats's the class id?: ")
                    delete_class(class_id)
                elif mm == "0":
                    """Go back"""
                    print("Going back")
                    break


        elif choice == '5':
            """Reset"""
            create_db()
            sql = ('INSERT INTO student VALUES (NULL, ?, ?, ?);')
            fill_db('students.csv',sql)
            sql = ('INSERT INTO class VALUES (NULL, ?, ?);')
            fill_db('classes.csv', sql)


main()
