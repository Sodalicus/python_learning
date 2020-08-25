#!/usr/bin/env python3

# Dictionaries are mutable!

opposites = {"up":"down", "right":"wrong", "yes":"no"}
alias = opposites
copy = opposites.copy() # Shallow copy

##################

copy["right"] = "privilege"
print("alias", alias["right"])
print("opposites", opposites["right"])
print("copy", copy["right"])

