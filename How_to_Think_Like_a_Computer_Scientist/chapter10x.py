import turtle, time
#Excercises from 2 to 5 from chapter 10.
state_num = 0

def bye():
    wn.bye()

def draw_housing(t, coords):
    """ Draw a nice housing to hold the traffic lights """
    t.penup()
    t.goto(coords)
    t.pendown()
    t.pensize(3)
    t.color("black", "darkgrey")
    t.begin_fill()
    t.forward(80)
    t.left(90)
    t.forward(200)
    t.circle(40, 180)
    t.forward(200)
    t.left(90)
    t.end_fill()

def position_light(t):
    t.penup()
    # Position t onto the place where the green light should be
    t.forward(40)
    t.left(90)
    t.forward(50)
    # Turn t into a big green circle
    t.shape("circle")
    t.shapesize(3)
    t.fillcolor("green")

def advance_state_machine():
    global state_num
    if state_num == 0:       # Orange/Yellow
        orange.fillcolor("yellow")
        green.fillcolor("darkgreen")
        wait = 1000
        state_num = 1
    elif state_num == 1:     #Red light 
        red.fillcolor("red")
        orange.fillcolor("darkorange")
        wait = 2000
        state_num = 2
    elif state_num == 2:                   #Green light 
        green.fillcolor("green")
        red.fillcolor("darkred")
        wait = 3000
        state_num = 3 
    else:                   # Green and Orange/Yellow
        orange.fillcolor("yellow")
        wait = 1000
        state_num = 0

    wn.ontimer(advance_state_machine, wait)

turtle.setup(800,600)
wn = turtle.Screen()
wn.title("Traffic lights!")
wn.bgcolor("lightgreen")

red = turtle.Turtle()
green = turtle.Turtle()
orange = turtle.Turtle()
turtles = [red, green, orange]

for t in turtles:
    t.speed(0)

draw_housing(red, (0,0))
position_light(red)

for t in (green,orange):
    t.penup()
    t.goto(0,0)
    t.forward(40)
    t.left(90)
    t.forward(50)
    # Turn t into a big green circle
    t.shape("circle")
    t.shapesize(3)


green.fillcolor("darkgreen")
orange.fillcolor("darkorange")
orange.forward(70)
red.fillcolor("darkred")
red.forward(140)

advance_state_machine()

wn.listen()                      # Listen for events
wn.onkey(bye, "q")
wn.mainloop()
