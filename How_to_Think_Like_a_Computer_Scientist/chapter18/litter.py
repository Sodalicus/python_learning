#!/usr/bin/env python3

import os

def create_file(path, name):
    if type(path) != type(str()):
        print("Path must be a string.")
    elif type(name) != type(str()):
        print("Name must be a string.")
    else:
        os.chdir(path)
        f = open(name, "w")
        f.close

def get_dirlist(path):
    dirlist = os.listdir(path)
    dirlist.sort()
    return dirlist

def litter(path=None):
    if path == None:
        path = "."
    path = os.path.abspath(path)

    dirlist = get_dirlist(path)
    for f in dirlist:
        current_path = os.path.join(path, f)
        if os.path.isdir(current_path):
            print("creating {}/trash.txt".format(current_path))
            create_file(current_path, "trash.txt")
            litter(current_path)


def cleanup(path=None):
    if path == None:
        path = "."
    path = os.path.abspath(path)
    dirlist = get_dirlist(path)

    for f in dirlist:
        fullname = os.path.join(path, f)

        if f == "trash.txt" and\
                os.path.isfile(fullname):
            print("deleting {}.".format(fullname))
            os.remove(fullname)

        if os.path.isdir(fullname):
            cleanup(fullname)

litter("/home/soda/Pobrane")
cleanup("/home/soda/Pobrane")
