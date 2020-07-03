#!/usr/bin/env python3

""" Basics of Object Oriented Programming in Python. """

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

p = Point(3,4)

def print_point(pt):
    print("({0}, {1})".format(pt.x, pt.y))

print(p.distance_from_origin())
print_point(p)
print("xxxxxxxxxxxxxxxxxxxxxxxxx")
print(p)

def midpoint(p1, p2):
    """ Return the midpoint of points p1 and p2 """
    mx = (p1.x + p2.x)/2
    my = (p1.y + p2.y)/2
    return Point(mx, my)
q = Point(5, 12)
r = midpoint(p,q)
print(r)
x = p.halfway(q)
print(x)

def calc_distance(p1,p2):
    import math
    dist = math.sqrt((p1.x-p2.x)**2 +(p1.y-p2.y)**2)
    return dist

print(calc_distance(p,q))
print("yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy")
print(p)
print(p.reflect_x())
print(Point(4,10).slope_from_origin())
print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
print(Point(4, 11).get_line_to(Point(6, 15)))
