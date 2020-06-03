#!/usr/bin/env python

import turtle

root = turtle.Screen()
tess = turtle.Turtle()
root.bgcolor('lightgreen')

def draw_bar(t, height):
    barcolor =''
    if height >= 200: barcolor = 'red'
    elif 200 > height >= 100: barcolor = 'yellow'
    elif 100 > height: barcolor = 'green'
    t.color('blue',barcolor)
    t.left(90)
    t.begin_fill()
    t.fd(height)
    if height < 0:
        t.penup()
        t.fd(-20)
        t.write("   "+str(height))
        t.fd(20)
        t.pendown()
    else:
        t.write("   "+str(height))
    t.right(90)
    t.fd(30)
    t.right(90)
    t.fd(height)
    t.end_fill()
    t.left(90)
    t.penup()
    t.fd(10)
    t.pendown()
xs = [-50,48,117,200,240,160,260,220]
for s in xs:
    draw_bar(tess, s)
input()
