#!/usr/bin/env python3

import turtle

turtle.setup(400,500)                # Determine the window size
wn = turtle.Screen()                 # Get a reference to the window
wn.title("Handling keypresses!")     # Change the window title
wn.bgcolor("lightgreen")             # Set the background color
tess = turtle.Turtle()               # Create our favorite turtle
# The next four functions are our "event handlers".
def h1():
   tess.forward(30)

def h2():
   tess.left(45)

def h3():
   tess.right(45)

def h4():
    wn.bye()                        # Close down the turtle window

def h5():
    tess.color("red")

def h6():
    tess.color("green")

def h7():
    tess.color("blue")

def inc_pen():
    if tess.pensize() < 20:
        tess.pensize(tess.pensize()+1)
    print(tess.pensize())

def dec_pen():
    if tess.pensize() > 1:
        tess.pensize(tess.pensize()-1)
    print(tess.pensize())

def pen_up():
    tess.penup()

def pen_down():
    tess.pendown()



# These lines "wire up" keypresses to the handlers we've defined.
wn.onkey(h1, "Up")
wn.onkey(h2, "Left")
wn.onkey(h3, "Right")
wn.onkey(h4, "q")
wn.onkey(h5, "r")
wn.onkey(h6, "g")
wn.onkey(h7, "b")
wn.onkey(inc_pen, "plus")
wn.onkey(dec_pen, "minus")
wn.onkey(pen_up, "w")
wn.onkey(pen_down, "e")

# Now we need to tell the window to start listening for events,
# If any of the keys that we're monitoring is pressed, its
# handler will be called.
wn.listen()
wn.mainloop()
