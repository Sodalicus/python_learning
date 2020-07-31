#!/usr/bin/env python3
import turtle

def koch(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in (60, -120, 60, 0):
            koch(t, order-1, size/4)
            t.left(angle)


wn = turtle.Screen()
tess = turtle.Turtle()

koch(tess, 2, 200)
tess.left(240)
koch(tess, 2, 200)
tess.left(240)
koch(tess, 2, 200)

wn.mainloop()
