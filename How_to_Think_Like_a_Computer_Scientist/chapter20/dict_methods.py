#!/usr/bin/env python3

#Python dictionaries methods

eng2sp = { "one":"uno", "two":"dos", "three":"tres" }

#Itearate over the keys using .key() method
for k in eng2sp.keys():
    print("Got key", k, "which maps to value", eng2sp[k])

#Turn .keys() view into list
ks = list(eng2sp.keys())
print(ks)

#Iterate over keys
for k in eng2sp:
    print("Got key", k)

#Iterate over values using method
for v in eng2sp.values():
    print("Got value:", v)

#Turn values view into list
v = list(eng2sp.values())
print(v)

# Iterating over both keys and values using .items() method
for (k,v) in eng2sp.items():
    print("Got", k, "that maps to", v)

#Testing for keys in dictionary
print("one" in eng2sp)
print("six" in eng2sp)
# in tests for keys in dictionary, not values
print("tres" in eng2sp)

try:
    print(eng2sp["six"])
except:
    print("No key \"six\" in dictionary")
