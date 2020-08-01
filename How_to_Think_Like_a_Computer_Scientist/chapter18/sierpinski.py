#!/usr/bin/env python3
import turtle,math

def sierpinski(point, depth, size):
    turtles = []
    angles_lists = [(120, 120, 120), (-120, -120, -120), (-120, -120, -120)]
    x,y = point
    if depth == 0 or depth == 1:
        tops = [(x,y,0), (size,y,180), (size/2, size*math.sqrt(3)/2, -60)]
    else:
        tops = [(x,y,0), (size/2**(depth-1),y,180), (size/2**(depth), (size/2**(depth-1))*math.sqrt(3)/2,-60)]

    for x,y,angle in tops:
        print(x,y,angle)
        tess = turtle.Turtle()
        tess.hideturtle()
        tess.penup()
        tess.goto(x,y)
        tess.pendown()
        tess.setheading(angle)
        turtles.append(tess)

        for i,tess in enumerate(turtles):
            angles = angles_lists[i]
            for angle in angles:
                if depth == 0:
                    tess.forward(size)
                    tess.left(angle)
                else:
                    tess.forward(size/2**depth)
                    tess.left(angle)







def exit_turtle():
    wn.bye()

wn = turtle.Screen()

sierpinski((0,0), 3, 100)

wn.onkey(exit_turtle, key="Escape")
wn.listen()
wn.mainloop()
