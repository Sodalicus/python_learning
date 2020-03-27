#!/usr/bin/env python
#Author: Paweł Krzemiński
#Simple 'game'. An adventurer can travel from one place to another.
# Excercise in OOP in Python, 
# Solution to Exc 4 from chapter 9 from "Python Programming for the Absolute Beginner" by Michael Dowson.
import random

class Place():
    TYPES = ( "forest", "plains", "lake", "hills", "river")
    def __init__(self, x,y):
        self.typeOfTerrain = Place.TYPES[random.randrange(len(Place.TYPES))]
        self.xy = (x,y)
        self.surface = []

    def __str__(self):
        rep = ''
        rep += '\nLocation type:'+self.typeOfTerrain
        rep += '\nLocated at:'+str(self.xy)
        return rep

    def add_entity(self, entity):
        if not entity in self.surface:
            self.surface.append(entity)

    def remove_entity(self, entity):
        if entity in self.surface:
            self.surface.remove(entity)

    def return_symbol(self):
        rep = self.typeOfTerrain[0:1]
        return rep

class Player():
    def __init__(self, name, xy=[0,0]):
        self.name = name
        self.location = xy

    def move(self, where):
        pass

    def coords(self):
        return self.location


class WorldMap():
    def __init__(self, name, size):
        self.name = name
        self.size = size
        self.locs = []
    def __str__(self):
        rep = ''
        for loc in self.locs:
            rep +=str(loc)
        return rep

    def generate(self):
        for x in range(self.size):
            for y in range(self.size):
                self.locs.append(Place(x,y))

    def show_map(self):
        print(self.size*'* * * \n')
        for loc in self.locs:
            symbol = loc.return_symbol()
            print('* {} *'.format(symbol), end=' ')

"""
* * * * * * *
* f * f * f *
* * * * * * *
* f * f * f *
* * * * * * *
* f * f * f *
* * * * * * *
"""

world = WorldMap("Westeros", 3)
world.generate()
print(world)

gamer = Player("Soda")
world.locs[0].add_entity(gamer)
print(gamer.coords())
world.show_map()
