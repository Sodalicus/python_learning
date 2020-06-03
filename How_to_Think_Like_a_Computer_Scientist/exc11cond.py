#!/usr/bin/env python

def is_right_angled(a,b,c):
    sides = [a,b,c]
    print(sides)
    sides.sort()
    print(sides)
    a = sides[0]
    b = sides[1]
    c = sides[2]
    if abs((c**2)-(a**2+b**2))< 0.00001:
        return True
    else:
        return False

a = 6
b = 8
c = 3

print(is_right_angled(a,b,c))
