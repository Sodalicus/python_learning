#!/usr/bin/env python3
# Chapter 16 - Classes and Objects - Digging a little deeper.
from oop import Point
from testing import test
import copy

class Rectangle:
    """ A class to manufacture rectangle objects. """

    def __init__(self, posn, w, h):
        """ Initialize rectangle at posn, with width w, height h. """
        self.corner = posn
        self.width = w
        self.height = h

    def __str__(self):
        return "{0}, {1}, {2}".format\
                (self.corner, self.width, self.height)

    def grow(self, delta_width, delta_height):
        """ Grow (or shrink) this object by the deltas. """
        self.width += delta_width
        self.height += delta_height

    def move(self, dx, dy):
        """ Move this object by the deltas. """
        self.corner.x += dx
        self.corner.y += dy

    def area(self):
        return self.width*self.height

    def perimeter(self):
        return 2*self.width+2*self.height

    def flip(self):
        self.height, self.width = self.width, self.height

    def contains(self, p):
        if p.x >= 0 and p.x < self.width\
            and p.y >= 0 and p.y < self.height:
            return True
        else:
            return False

def rectangles_collision(r1, r2):
    """ Return True if two given rectangles collide with eachother. """
    # r1.x, r1.y, r1.x1 = r1.x+r1.width, r1.y1 = r1.y+r1.height
    # r2.x, r2.y, r2.x1 = r2.x+r2.width, r2.y1 = r2.y+r2.height
    r1c1 = copy.copy(r1.corner)
    r1c2 = Point(r1.corner.x + r1.width, r1.corner.y + r1.height)

    r2c1 = copy.copy(r2.corner)
    r2c2 = Point(r2.corner.x + r2.width, r2.corner.y + r2.height)
    #print(r1c1.x, r1c1.y)
    #print(r1c2.x, r1c2.y)
    #print(r2c1.x, r2c1.y)
    #print(r2c2.x, r2c2.y)

    if r2c1.x >= r1c1.x and r2c1.x < r1c2.x:
        """ Lower left corner x coord within the other rectangle. """

        if r2c1.y >= r1c1.y and r2c1.y < r1c2.y:
            """ Lower left corner y coords within the other rectangle. """
            return True

        elif r2c2.y <= r1c2.y and r2c2.y > r1c1.y:
            """ Upper right corner y coord within the other rectangle. """
            return True

        else:
            return False

    elif r2c2.x > r1c1.x and r2c2.x <= r1c2.x:
        """ Upper right corner x coord within the other rectangle. """

        if r2c2.y <= r1c2.y and r2c2.y > r1c1.y:
            """ Upper right corner y coord within the other rectangle. """
            return True

        elif r2c1.y >= r1c1.y and r2c1.y < r1c2.y:
            """ Lower left corner y coord within the other rectangle. """
            return True
        else:
            return False

    else:
        return False





box = Rectangle(Point(0,0), 100, 200)
bomb = Rectangle(Point(100, 80), 5, 10)
print("box: ", box)
print("bomb: ", bomb)

def same_coordinates(p1, p2):
    return (p1.x == p2.x) and (p1.y == p2.y)


r = Rectangle(Point(0, 0), 10, 5)
test(r.area() == 50)

test(r.perimeter() == 30)

test(r.width == 10 and r.height == 5)
r.flip()
test(r.width == 5 and r.height == 10)

r = Rectangle(Point(0, 0), 10, 5)
test(r.contains(Point(0,0)))
test(r.contains(Point(3,3)))
test(not r.contains(Point(3,7)))
test(not r.contains(Point(3,5)))
test(r.contains(Point(3, 4.99999)))
test(not r.contains(Point(-3,-3)))

r1 = Rectangle(Point(0,0), 6, 8)
r2 = Rectangle(Point(7,2), 7, 10)
r3 = Rectangle(Point(3,6), 6, 8)

test(not rectangles_collision(r1, r2))
test(rectangles_collision(r1, r3))
test(rectangles_collision(r2, r3))


