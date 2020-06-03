#!/usr/bin/env python

import turtle, random

root = turtle.Screen()
root.bgcolor("lightgreen")
tess = turtle.Turtle()
tess.speed(8)
tess.color("blue")
tess.pensize(3)
colours = ['red', 'green', 'pink', 'purple', 'yellow', 'blue', 'navy']

def draw_star():
    for i in range(5):
        for i in range(5):
            tess.fd(100)
            tess.left(144)
        tess.penup()
        tess.forward(350)
        tess.left(144)
        tess.pendown()
draw_star()

def spiral():
    side = 5
    for i in range(100):
        colour = random.choice(colours)
        colour2 = random.choice(colours)
        root.bgcolor(colour2)
        tess.color(colour)
        tess.fd(side)
        side+=4
        tess.right(115)


def draw_poly(turt, n, sz):
    for i in range(n):
        turt.fd(sz)
        turt.left(360/n)

def draw_triangle(t, sz):
    draw_poly(t, 3, sz)

def square2(side):
    for i in range(4):
        tess.fd(side)
        tess.left(90)

def rot_squares():
    for i in range(5):
        for i in range(4):
            square2(100)
            tess.left(90)
        tess.left(36)

def squares():
    side = 20
    for i in range(1, 6):
        square2(side*i)
        tess.penup()
        tess.left(180)
        tess.fd(side/2)
        tess.left(90)
        tess.fd(side/2)
        tess.left(90)
        tess.pendown()


def square():
    for i in range(4):
        tess.fd(20)
        tess.left(90)
    tess.penup()
    tess.fd(40)
    tess.pendown()

def clock():
    tess.speed(1)
    tess.hideturtle()
    tess.color("Blue")
    tess.stamp()
    for i in range(12):
        tess.penup()
        tess.fd(100)
        tess.pendown()
        tess.fd(10)
        tess.penup()
        tess.fd(20)
        tess.stamp()
        tess.fd(-130)
        tess.left(30)

input()
