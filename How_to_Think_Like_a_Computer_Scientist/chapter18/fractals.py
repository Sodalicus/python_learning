#!/usr/bin/env python3
#-*-coding:utf-8-*-

import turtle

def koch(t, order, size):
    """
        Make turtle t draw a Koch fractal of 'order' and 'size'.
        Leave the turtle facing the direction.
    """
    print("order: ", order)

    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch(t, order-1, size/3)
            t.left(angle)











wn = turtle.Screen()

tess = turtle.Turtle()

koch(tess, 3, 200)

def exit_turtle():
    wn.bye()

turtle.onkey(exit_turtle, key="Escape")
turtle.listen()
wn.mainloop()
