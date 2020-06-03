#!/usr/bin/env python

import turtle

action = [(160, 20), (-43, 10), (270, 8), (-43, 12)]
house = [(0,100), (90,100), (90,100), (90,100), (135,142), (90,71), (90,71),(90,141)]

root = turtle.Screen()
tess = turtle.Turtle()
root.bgcolor("lightgreen")
tess.pensize(6)

for angle,steps in house:
    tess.left(angle)
    tess.fd(steps)

input()
