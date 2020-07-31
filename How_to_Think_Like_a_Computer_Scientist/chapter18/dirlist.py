#!/usr/bin/env python3

import os

def get_dirlist(path):
    """
        Return a sorted list of all entries in path.
        This returns just the names, not the full path to the names.
    """
    dirlist = os.listdir(path)
    dirlist.sort()
    return dirlist

def print_files(path, prefix = ""):
    """ Print recursive listing of contents of path. """
    if prefix == "": # Detect outermost call, print a heading
        print("Folder listing for", path)
        prefix = "| "

    dirlist = get_dirlist(path)
    for f in dirlist:
        print(prefix+f)
        fullname = os.path.join(path, f)
        if os.path.isdir(fullname):
            print_files(fullname, prefix + "| ")

#print_files("/home/soda/python/python_learning")


def print_files2(path):
    """
        Return a list of files with full paths in given directory
        and subdirectories.
    """
    pathslist = []
    dirlist = get_dirlist(path)
    for f in dirlist:
        fullname = os.path.join(path, f)
        if os.path.isdir(fullname):
            pathslist.extend(print_files2(fullname))
        else:
            pathslist.append(fullname)

    return pathslist

for filepath in print_files2("/home/soda/Pobrane/"):
    print(filepath)


