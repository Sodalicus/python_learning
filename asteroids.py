#!/usr/bin/env python3
# Simple asteroids like game, another step in my python learning.
# Using tkinter's canvas to draw the game.
# Author: Paweł Krzemiński

from tkinter import *
import time

WIDTH = 640
HEIGHT = 480

class Application(Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_canvas()
        self.myship = Ship(self.canvas, 1,1)
        self.create_widgets()
        self.master = master

    def create_canvas(self):
        self.canvas = Canvas(height = HEIGHT , width = WIDTH , background = "white")
        self.canvas.grid(row = 0, column = 0)


    def create_widgets(self):
        start_button = Button(text = "Start", command = self.move_sprite())
        start_button.grid(row = 1, column = 0, sticky=W)

    def move_sprite(self):
        self.myship.move()

    def main(self):
        while True:
            self.myship.move()
            self.master.update_idletasks()
            self.master.update()
            time.sleep(0.5)


class Sprite():
    def __init__(self, x, y, canvas, dx=0, dy=0):
        """ Create  shape with given center x, y"""
        pass
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.canvas = canvas

    def move(self):
        pass

    def destroy(self):
        pass

    def coords(self):
        pass

class AsteroidLarge(Sprite):
    def __init__(self, canvas, x, y):
        super(AsteroidLarge, self).__init__(self, canvas, x, y)
        self.id = kj 


class AsteroidMedium(Sprite):
    def __init__(self, canvas, x, y):
        super(AsteroidMedium, self).__init__(self, canvas, x, y)
        pass


class AsteroidSmall(Sprite):
    def __init__(self, canvas, x, y):
        super(AsteroidSmall, self).__init__(self, canvas, x, y)
        pass


class Ship(Sprite):
    def __init__(self, canvas, x, y):
        super(Ship, self).__init__(self, canvas, x, y)
        self.id = self.canvas.create_polygon(1,1,20,1,16,10, fill="", outline="black")
        self.canvas.move(self.id, 200,300)

    def move(self):
        self.canvas.move(self.id, 5,5)
root = Tk()
root.title("Asteroids")
app = Application(root)
app.main()
