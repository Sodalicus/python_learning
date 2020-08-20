#!/usr/bin/env python3
import turtle, math


def sierp0(point, size):
    print(point)
    x,y = point
    tess = turtle.Turtle()
    tess.speed(0)
    tess.hideturtle()
    tess.penup()
    tess.goto(x,y)
    tess.pendown()

    for i in range(3):
        tess.forward(size)
        tess.left(120)

def sierp1(point, size):
    x,y = point
    points = ((x,y), (x+size/2, y), (x+size/4, y+(size/2)*math.sqrt(3)/2))
    for st_point in points:
        print("drawing level 1 triangle")
        sierp0(st_point, size/2)

def sierp2(point, size):
    x,y = point
    points = ((x,y), (x+size/2, y), (x+size/4, y+(size/2)*math.sqrt(3)/2))
    for st_point in points:
        sierp1(st_point, size/2)

def sierp3(point, size):
    x,y = point
    points = ((x,y), (x+size/2, y), (x+size/4, y+(size/2)*math.sqrt(3)/2))
    for st_point in points:
        sierp2(st_point, size/2)

def exit_turtle():
    wn.bye()

wn = turtle.Screen()
sierp3((50,50), 100)

wn.onkey(exit_turtle, key="Escape")
wn.listen()
wn.mainloop()
