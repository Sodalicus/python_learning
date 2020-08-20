#!/usr/bin/env python3
import turtle, math, random

level = 2
lenght = 200
change = 1
point = 0,0
colors = ["red", "blue", "green"]


def draw_triangle(x,y,size, color):
    tess = turtle.Turtle()
    tess.color(color)
    tess.speed(0)
    tess.hideturtle()
    tess.penup()
    tess.goto(x,y)
    tess.pendown()

    for i in range(3):
        tess.forward(size)
        tess.left(120)

def sierpinski2(point, order, size, colorChangeDepth=-1):
    print(colorChangeDepth)
    x,y = point
    if colorChangeDepth == 0:
        print("Im here")
        print(order)
        color = random.choice(colors)
    else:
        color = "black"

    if order == 0:
        print(color)
        draw_triangle(x,y,size, color)
        print()

    if order > 0:
        starting_points = ((x,y), (x+size/2, y), (x+size/4, y+(size/2)*math.sqrt(3)/2))

        for st_point in starting_points:
            sierpinski2(st_point, order-1, size/2, colorChangeDepth-1)






def exit_turtle():
    wn.bye()

wn = turtle.Screen()

sierpinski2(point, level, lenght, change)

wn.onkey(exit_turtle, key="Escape")
wn.listen()
wn.mainloop()

