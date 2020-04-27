#!/usr/bin/env python3
# Simple asteroids like game, another step in my python learning.
# Using tkinter's canvas to draw the game.
# Author: Paweł Krzemiński

from tkinter import *
import time, random

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
        self.sprites = []

    def create_canvas(self):
        self.canvas = Canvas(height = HEIGHT , width = WIDTH , background = "white")
        self.canvas.grid(row = 0, column = 0, columnspan = 3)


    def create_widgets(self):
        up_button = Button(text = "Up", command = self.myship.move_up)
        up_button.grid(row = 1, column = 1, sticky = N)
        left_button = Button(text = "Left", command = self.myship.move_left)
        left_button.grid(row = 2, column = 0, sticky = E)
        down_button = Button(text = "Down", command = self.myship.move_down)
        down_button.grid(row = 2, column = 1, sticky = N)
        right_button = Button(text = "Right", command = self.myship.move_right)
        right_button.grid(row = 2, column = 2, sticky = W)
        self.canvas.bind_all('<KeyPress-Up>', self.myship.move)
        self.canvas.bind_all('<KeyPress-Down>', self.myship.move)
        self.canvas.bind_all('<KeyPress-Left>', self.myship.move)
        self.canvas.bind_all('<KeyPress-Right>', self.myship.move)

    def add_sprite(self, sprite):
        self.sprites.append(sprite)



    def main(self):
        for i in range(10):
            i = AsteroidLarge(self.canvas, 1, 1)
            self.add_sprite(i)
        self.add_sprite(self.myship)
        while True:
            for sprite in self.sprites:
                sprite.update()
            self.master.update_idletasks()
            self.master.update()
            time.sleep(0.01)


class Sprite():
    def __init__(self, canvas, x, y, dx=0, dy=0):
        """ Create  shape with given center x, y"""
        pass
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.canvas = canvas

    def update(self):
        self.coords = self.canvas.coords(self.id)
        if self.coords[0] < 0 or self.coords[2] > WIDTH:
            self.dx = -self.dx
        if self.coords[1] < 0 or self.coords[3] > HEIGHT:
            self.dy = -self.dy
        self.canvas.move(self.id, self.dx, self.dy)

    def move(self):
        pass

    def destroy(self):
        pass

    def coords(self):
        self.coords = self.canvas.coords(self.id)
        self.x1 = self.coords[0]
        self.y1 = self.coords[1]
        self.x2 = self.coords[2]
        self.y2 = self.coords[3]

    def within_y(self, sprite):
        for sprite in self.sprites:
            if sprite==


class Ship(Sprite):
    def __init__(self, canvas, x, y):
        super(Ship, self).__init__(canvas, x, y)
        self.id = self.canvas.create_oval(100,100,125,125)

    def move_up(self):
        self.dy = -5

    def move_down(self):
        self.dy = 5

    def move_left(self):
        self.dx = -5

    def move_right(self):
        self.dx = 5

    def move(self, event):
        if event.keysym == "Up": self.dy = -5
        elif event.keysym == "Down": self.dy = 5
        elif event.keysym == "Left": self.dx = -5
        elif event.keysym == "Right": self.dx = 5


    def update(self):
        self.canvas.move(self.id, self.dx, self.dy)
        if self.dx > 0: self.dx -= 1
        elif self.dx < 0: self.dx += 1

        if self.dy > 0: self.dy -= 1
        elif self.dy < 0: self.dy += 1

class AsteroidLarge(Sprite):
    def __init__(self, canvas, x, y):
        super(AsteroidLarge, self).__init__(canvas, x, y)
        self.id = self.canvas.create_oval(0, 0, 50, 50, fill="", outline="black")
        x1 = random.randrange(WIDTH/2)
        y1 = random.randrange(HEIGHT/2)
        self.canvas.coords(self.id, x1, y1, x1+50, y1+50)
        self.dx = 1 #random.randrange(1, 4)
        self.dy = 1 #random.randrange(1, 4)

class AsteroidMedium(Sprite):
    def __init__(self, canvas, x, y):
        super(AsteroidMedium, self).__init__(canvas, x, y)
        pass


class AsteroidSmall(Sprite):
    def __init__(self, canvas, x, y):
        super(AsteroidSmall, self).__init__(canvas, x, y)
        pass


root = Tk()
root.title("Asteroids")
app = Application(root)
app.main()
