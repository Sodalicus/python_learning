#!/usr/bin/env python3
import turtle

def sierpinski(t, order, size):
    if order == 0:
        for angle in (120, 120, 0):
            t.forward(size)
            t.left(angle)
    else:
        for i in range(3):
            sierpinski(t, order-1, size//2)


def exit_turtle():
    wn.bye()

wn = turtle.Screen()
tess = turtle.Turtle()

sierpinski(tess, 1, 100)

wn.onkey(exit_turtle, key="Escape")
wn.listen()
wn.mainloop()
