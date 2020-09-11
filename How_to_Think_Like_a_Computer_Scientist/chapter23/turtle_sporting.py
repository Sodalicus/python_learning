#!/usr/bin/env python3 import turtle, random

class TurtleGTX(turtle.Turtle):
    def __init__(self):
        super(TurtleGTX, self).__init__()
        self.distance = 0
        self.flat_tire = False

    def odometer(self, dist=0):
        self.distance += abs(dist)
        return self.distance

    def forward(self, distance):
        if self.flat_tire:
            tire_is_flat = ValueError("You can't drive, your turtle has flat tyre.")
            raise tire_is_flat
        else:
            self.fd(distance)
            self.damage_tire()
            #super(TurtleGTX, self).forward(distance)
            self.odometer(distance)

    def change_tire(self):
        if self.flat_tire:
            self.flat_tire = False
            print("Changing tire.")

    def damage_tire(self):
        if random.randrange(200)%3 == 2:
            self.flat_tire = True
            print("Your tire has punctured!")

def exit_turtle():
    wn.bye()

wn = turtle.Screen()
tess = TurtleGTX()
for i in range(100):
    try:
        tess.forward(50)
    except:
        tess.change_tire()
        print(tess.odometer())

wn.onkey(exit_turtle, key="Escape")
wn.listen()
wn.mainloop()
