#!/usr/bin/env python3

import turtle

def cesaro(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in (-85, -190, -85, 0):
            cesaro(t, order-1, size/2)
            t.left(angle)

wn = turtle.Screen()
wn.screensize(1024,768)
tess = turtle.Turtle()
tess.penup()
tess.goto(-200, 0)
tess.pendown()
print(tess.pos())
tess.speed(0)

for order in range(4):
    for i in range(4):
        cesaro(tess, order, 100)
        tess.left(-90)
    tess.penup()
    tess.forward(150)
    tess.pendown()

wn.mainloop()


