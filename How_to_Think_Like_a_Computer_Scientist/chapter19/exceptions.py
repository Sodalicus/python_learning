#!/bin/usr/env python3

def open_file():
    """ Catch no such file exception """
    filename = input("Enter a file name: ")
    try:
        f = open(filename, "r")
    except:
        print("There is no file named", filename)

def exists(filename):
    """ Check if file exists - bad way.
    import os
    os.path.isfile("path")
    is more like it
    """
    try:
        f = open(filename)
        f.close()
        return True
    except:
        return False

def get_age():
    """ Raise an exception when age value is below 0"""
    age = int(input("Please enter your age: "))
    if age <0:
        # Create a new instance of an exception
        my_error = ValueError("{0} is not a valid age".format(age))
        raise my_error
    return age

def recursion_depth(number):
    """ Don't crash when reached maximum recursion level,
        just print info. """
    print("Recursion depth number", number)
    try:
        recursion_depth(number+1)
    except:
        print("I cannot go any deeper into this wormhole.")

