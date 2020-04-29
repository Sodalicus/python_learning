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
        rep += '\nLocation type: '+self.typeOfTerrain
        rep += '\nLocated at: '+str(self.xy)
        return rep

    def add_entity(self, entity):
        if not entity in self.surface:
            entity.set_coords(self.xy)
            self.surface.append(entity)

    def remove_entity(self, entity):
        if entity in self.surface:
            self.surface.remove(entity)

    def return_symbol(self):
        rep = self.typeOfTerrain[0:1]
        return rep

    def coords(self):
        return self.xy

    def is_empty(self):
        return not self.surface

class Player():

    def __init__(self, name, x, y):
        self.name = name
        self.xy = (x, y)

    def __str__(self):
        return 'X'

    def set_coords(self, xy):
        self.xy = xy

    def location(self, where):
        loca = where.find_loc(self.xy)
        return loca

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

    def find_loc(self, xy):
        for loc in self.locs:
            if loc.coords() == xy:
                return self.locs.index(loc)

    def show_map(self):
        for y in range(self.size):
            for x in range(self.size):
                index = self.find_loc((x,y))
                loc = self.locs[index]
                if not loc.is_empty():
                    print('X', end=' ')
                else:
                    print(loc.return_symbol(), end=' ')
            print()
        print()



    def show_map2(self):
        for x in range(self.size):
            for y in range(self.size):
                print(self.find_loc((x,y)), end=' ')
            print()
        print()

class Game():
    def __init__(self):
        self.world = WorldMap("Westeros", 9)
        self.world.generate()

        
    def create_player(self):
        self.gamer = Player("Soda", 0,0)
        self.world.locs[0].add_entity(self.gamer)

    def move_player(self, entity, where):
        current_coords = entity.xy
        current_loc = self.world.find_loc(current_coords)
        x = current_coords[0]
        y = current_coords[1]
        new_coords=()
        if where == 'n':
            if y-1 < 0:
                print("You cannot go north.")
            else:
                new_coords = (x, y-1)
                new_loc = self.world.find_loc(new_coords)
                self.world.locs[current_loc].remove_entity(entity)
                self.world.locs[new_loc].add_entity(entity)

        elif where == 's':
            if y+1 > self.world.size-1:
                print("You cannot got south.")
            else:
                new_coords = (x, y+1)
                new_loc = self.world.find_loc(new_coords)
                self.world.locs[current_loc].remove_entity(entity)
                self.world.locs[new_loc].add_entity(entity)

        elif where == 'w':
            if x-1 < 0:
                print("You cannot got west.")
            else:
                new_coords = (x-1, y)
                new_loc = self.world.find_loc(new_coords)
                self.world.locs[current_loc].remove_entity(entity)
                self.world.locs[new_loc].add_entity(entity)

        elif where == 'e':
            if x+1 > self.world.size-1:
                print("You cannot go east.")
            else:
                new_coords = (x+1, y)
                new_loc = self.world.find_loc(new_coords)
                self.world.locs[current_loc].remove_entity(entity)
                self.world.locs[new_loc].add_entity(entity)

        print(new_coords)
        
    def main(self):
        choice = None
        print("Welcome to world of {}.".format(self.world.name))
        print("Your name is {}.".format(self.gamer.name))
        print("You are located at: {} ".format(self.gamer.xy))
        while choice != 'n':
            print("""
    Choices:
    1 - Move
    2 - Where are You
    3 - Show map
    n - Quit
                """)
            choice = input("choice:")
            if choice == '1':
                print("Where do you want to move?")
                direction = None
                while direction not in ('n', 'e', 's', 'w'):
                    direction = input("""
                    Pick direction:
                        (n)orth
                    (w)est  (e)ast
                        (s)outh
                    """)
                    game.move_player(self.gamer,direction)

            elif choice == '2':
                print(self.world.locs[self.gamer.location(self.world)])
            elif choice == '3':
                self.world.show_map()





game=Game()
game.create_player()
game.main()
