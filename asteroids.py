#!/usr/bin/env python3
# Simple asteroids like game, another step in my python learning.
# Using tkinter's canvas to draw the game.
# Author: Paweł Krzemiński

from tkinter import *

class Application(Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_canvas()
        self.myship = Ship(self.canvas, 1,1)
        self.create_widgets()

    def create_canvas(self):
        self.canvas_width = 640
        self.canvas_height = 480
        self.canvas = Canvas(height = 480, width = 640, background = "white")
        self.canvas.grid(row = 0, column = 0)


    def create_widgets(self):
        start_button = Button(text = "Start", command = self.move_sprite())
        start_button.grid(row = 1, column = 0, sticky=W)

    def move_sprite(self):
        self.myship.move()
        root.update()


class Sprite():
    def __init__(self, x, y, dx=0, dy=0):
        """ Create  shape with given center x, y"""
        pass
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy

    def move(self):
        pass

    def destroy(self):
        pass

    def coords(self):
        pass

class AsteroidLarge(Sprite):
    def __init__(self):
        super(AsteroidLarge, self).__init__(self)
        pass


class AsteroidMedium(Sprite):
    def __init__(self):
        super(AsteroidMedium, self).__init__(self)
        pass


class AsteroidSmall(Sprite):
    def __init__(self):
        super(AsteroidSmall, self).__init__(self)
        pass


class Ship(Sprite):
    def __init__(self, canvas, x, y):
        super(Ship, self).__init__(self, x, y)
        self.canvas = canvas
        self.id = self.canvas.create_polygon(1,1,10,1,8,5, fill="", outline="black")
        self.canvas.move(self.id, 200,300)

    def move(self):
        self.canvas.move(self.id, 5,5)
root = Tk()
root.title("Asteroids")
app = Application(root)
root.mainloop()
