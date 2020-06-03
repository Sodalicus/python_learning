#!/usr/bin/env python

import sys

def turn_clockwise(direction):
    if direction in ("N", "W", "S", "E"):
        if direction == "N": output = "E"
        elif direction == "E": output = "S"
        elif direction == "S": output = "W"
        elif direction == "W": output = "N"
        return output
    else:
        return None


def day_name(integer):
    days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    if integer in range(len(days)):
        return days[integer]
    else:
        return None

def day_num(day):
    days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    if day in days:
        return days.index(day)
    else:
        return None

def day_add(today, delta):
    td = day_num(today)
    after = (td+delta)%7
    return day_name(after)


def test(did_pass):
    """ Print the result of a test. """
    linenum = sys._getframe(1).f_lineno # Get the caller’s line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)


def compare(a,b):
    if a > b:
        return 1
    elif a < b:
        return -1
    else:
        return 0

def hypotenuse(a,b):
    c = (a**2+b**2)**0.5
    return c

def slope(x1,y1,x2,y2):
    m = (y2-y1)/(x2-x1)
    return m

def intercept(x1,y1,x2,y2):
    m = slope(x1,y1,x2,y2)
    y = y1 + m*(0-x1)
    return y

def is_even(x):
    if x%2 == 0:return True
    else: return False

def is_odd(x):
    if is_even(x): return False 
    else: return True 

def is_factor(f,n):
    if n%f == 0: return True

def is_multiple(a,b):
    if is_factor(b,a): return True

def f2c(f):
    c = round(5/9*(f-32))
    return c

def c2f(c): f = round((c/(5/9)+32))
    return f

def test_suite():
    test(turn_clockwise("N") == "E")
    test(turn_clockwise("W") == "N")
    test(turn_clockwise(42) == None)
    test(turn_clockwise("rubbish") == None)
    test(day_name(3) == "Wednesday")
    test(day_name(6) == "Saturday")
    test(day_name(42) == None)
    test(day_num("Friday") == 5)
    test(day_num("Sunday") == 0)
    test(day_num(day_name(3)) == 3)
    test(day_name(day_num("Thursday")) == "Thursday")
    test(day_num("Halloween") == None)
    test(day_add("Monday", 4) == "Friday")
    test(day_add("Tuesday", 0) == "Tuesday")
    test(day_add("Tuesday", 14) == "Tuesday")
    test(day_add("Sunday", 100) == "Tuesday")
    test(day_add("Sunday", -1) == "Saturday")
    test(day_add("Sunday", -7) == "Sunday")
    test(day_add("Tuesday", -100) == "Sunday")
    test(compare(5, 4) == 1)
    test(compare(7, 7) == 0)
    test(compare(2, 3) == -1)
    test(compare(42, 1) == 1)
    test(hypotenuse(3, 4) == 5.0)
    test(hypotenuse(12, 5) == 13.0)
    test(hypotenuse(24, 7) == 25.0)
    test(hypotenuse(9, 12) == 15.0)
    test(slope(5,3,4,2) == 1.0)
    test(slope(1,2,3,2) == 0.0)
    test(slope(1,2,3,3) == 0.5)
    test(slope(2,4,1,2) == 2.0)
    test(intercept(1, 6, 3, 12) == 3.0)
    test(intercept(6, 1, 1, 6) == 7.0)
    test(intercept(4, 6, 12, 8) == 5.0)
    test(is_even(0) == True)
    test(is_even(1) == False)
    test(is_even(2) == True)
    test(is_even(-6) == True)
    test(is_even(-9) == False)
    test(is_odd(0) == False)
    test(is_odd(9) == True)
    test(is_odd(-8) == False)
    test(is_odd(33) == True)
    test(is_factor(3, 12))
    test(not is_factor(5, 12))
    test(is_factor(7, 14))
    test(not is_factor(7, 15))
    test(is_factor(1, 15))
    test(is_factor(15, 15))
    test(not is_factor(25, 15))
    test(is_multiple(12, 3))
    test(is_multiple(12, 4))
    test(not is_multiple(12, 5))
    test(is_multiple(12, 6))
    test(not is_multiple(12, 7))
    test(f2c(212) == 100)
    test(f2c(32) == 0)
    test(f2c(-40) == -40)
    test(f2c(36) == 2)
    test(f2c(37) == 3)
    test(f2c(38) == 3)
    test(f2c(39) == 4)
    test(c2f(0) == 32)
    test(c2f(100) == 212)
    test(c2f(-40) == -40)
    test(c2f(12) == 54)
    test(c2f(18) == 64)
    test(c2f(-48) == -54)
test_suite()
