#!/usr/bin/env python3

from testing import test

class MyTime:

    def __init__(self, hrs=0, mins=0, secs=0):
        """ Create a MyTime object initialized to hrs, mins, secs.
            The values of mins and secs may be outside the range 0-59,
            but the resulting MyTime object will be normalized.
        """
        # Calculate total seconds to represent
        totalsecs = hrs*3600 + mins*60 + secs
        self.hours = totalsecs// 3600
        leftoversecs = totalsecs % 3600
        self.minutes = leftoversecs// 60
        self.seconds = leftoversecs % 60

    def __str__(self):
        return "{}:{}:{}".format(self.hours, self.minutes, self.seconds)

    def increment(self, seconds):
        new_secs = self.to_seconds() + seconds
        if new_secs < 0:
            new_secs = 0

        self.hours = new_secs// 3600
        leftoversecs = new_secs % 3600
        self.minutes = leftoversecs// 60
        self.seconds = leftoversecs % 60

    def to_seconds(self):
        """ Return the number of seconds represented
            by this instance
        """
        return self.hours * 3600 + self.minutes * 60 + self.seconds

    def after(self, time2):
        """ Return True if I am strictly greater than time2 """
        return self.to_seconds() > time2.to_seconds()

    def __add__(self, other):
        return MyTime(0, 0, self.to_seconds() + other.to_seconds())

    def __sub__(self, other):
        return MyTime(0, 0, self.to_seconds() - other.to_seconds())

    def __gt__(self, other):
        return self.to_seconds() > other.to_seconds()

    def between(self, t1, t2):
        return t1.to_seconds() <= self.to_seconds() < t2.to_seconds()

class Point:
    """ Point class represents and manipulates x,y coords. """

    def __init__(self, x=0, y=0):
        """ Create a new point at the origin """
        self.x = x
        self.y = y

    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)


    def distance_from_origin(self):
        """ Compute my distance from the origin """
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def halfway(self, target):
        """ Return the halfway point between myself and the target """
        mx = (self.x + target.x)/2
        my = (self.y + target.y)/2
        return Point(mx, my)

    def reflect_x(self):
        return Point(-self.x, self.y)

    def slope_from_origin(self):
        m = self.y/self.x
        return m

    def get_line_to(self,point):
        a = (point.y - self.y)/(point.x - self.x)
        b = self.y - a*self.x
        return (a, b)

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __mul__(self, other):
        return self.x * other.x + self.y * other.y

    def __rmul__(self, other):
        return Point(other * self.x, other * self.y)

    def reverse(self):
        (self.x, self.y) = (self.y, self.x)




def multadd (x, y, z):
    return x * y + z

def front_and_back(front):
    import copy
    back = copy.copy(front)
    back.reverse()
    print(str(front) + str(back))



my_list = [1, 2, 3, 4]
front_and_back(my_list)
p = Point(3, 4)
front_and_back(p)


t1 = MyTime(5, 15, 42)
print("t1:", t1)
t2 = MyTime(2, 15, 42)
t6 = MyTime(5, 25, 0)
print("is t1: {} greater than t2: {}? => {}".format(t1, t2, t1 > t2))
print("is t6: {} between t1: {} and t2: {} =>: {}".format(t6, t1, t2, t6.between(t1,t2)))
print("t2", t2)
t3 = t1 + t2
print("t1+t2:", t3)
t4 = t1 - t2
print("t1-t2:", t4)

t20 = MyTime(1, 0, 0)
t20.increment(600)
test(t20.to_seconds() == MyTime(1, 10,0).to_seconds())
t20.increment(-600)
test(t20.to_seconds() == MyTime(1, 0, 0).to_seconds())
t20.increment(-500000)
test(t20.to_seconds() == MyTime(0, 0, 0).to_seconds())
