#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Calculator app using tkinter for gui
# Version 0.1
from tkinter import *
from tkinter import ttk

""" TODO:
    - valid float handling
    - leading minus sign
    - dot, or coma handling to type in floats
    - % operator handling
    - nicer looks
"""


class Application(Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.temp = None
        self.operator = None
        self.clear_display = False
        self.display_var = StringVar()
        self.display_var.set("0")
        self.create_widgets()

    def create_widgets(self):
        self.display = Label(self, textvariable = self.display_var, \
                anchor = "e", width =20
                ).grid(row = 0, column = 0, columnspan =4, sticky = E)

        Button(self, text="%", command = lambda: self.button_action("%")
                ).grid(row = 1, column = 0,sticky = W)

        Button(self, text="/", command = lambda: self.button_action("/")
                ).grid(row = 1, column = 1,sticky = W)

        Button(self, text="x", command = lambda: self.button_action("*")
                ).grid(row = 1, column = 2,sticky = W)

        Button(self, text="-", command = lambda: self.button_action("-")
                ).grid(row = 1, column = 3,sticky = W)

        Button(self, text="7", command = lambda: self.button_action(7)
                ).grid(row = 2, column = 0,sticky = W)

        Button(self, text="8", command = lambda: self.button_action(8)
                ).grid(row = 2, column = 1,sticky = W)

        Button(self, text="9", command = lambda: self.button_action(9)
                ).grid(row = 2, column = 2,sticky = W)

        Button(self, text="+", command = lambda: self.button_action("+")
                ).grid(row = 2, column = 3, rowspan = 2, sticky = W)

        Button(self, text="4", command = lambda: self.button_action(4)
                ).grid(row = 3, column = 0,sticky = W)

        Button(self, text="5", command = lambda: self.button_action(5)
                ).grid(row = 3, column = 1,sticky = W)

        Button(self, text="6", command = lambda: self.button_action(6)
                ).grid(row = 3, column = 2,sticky = W)

        Button(self, text="1", command = lambda: self.button_action(1)
                ).grid(row = 4, column = 0,sticky = W)

        Button(self, text="2", command = lambda: self.button_action(2)
                ).grid(row = 4, column = 1,sticky = W)

        Button(self, text="3", command = lambda: self.button_action(3)
                ).grid(row = 4, column = 2,sticky = W)

        Button(self, text="=", command = lambda: self.button_action("=")
                ).grid(row = 4, column = 3, rowspan = 2, sticky = W)

        Button(self, text="0", command = lambda: self.button_action(0)
                ).grid(row = 5, column = 0, columnspan = 2, sticky = W)

        Button(self, text=",", command = lambda: self.button_action(",")
                ).grid(row = 5, column = 1, sticky = W)

    def button_action(self, button_id):
        """ Take action according to a button pressed """
        token = button_id
        #print("Pressed button: ", button_id)
        if type(token) == type(0):
            self.conc_digits(token)
        elif type(token) ==type(","):
            if token in ["+", "-", "*", "/", "%"]:
                self.operator = token
                self.temp = int(float(self.display_var.get()))
                self.clear_display = True
            if token == ",":
                pass
            if token == "=":
                if self.operator != None:
                    if self.operator == "+":
                        result = self.temp + int(self.display_var.get())
                    elif self.operator == "-":
                        result = self.temp - int(self.display_var.get())
                    elif self.operator == "*":
                        result = self.temp * int(self.display_var.get())
                    elif self.operator == "/":
                        result = self.temp / int(self.display_var.get())
                    elif self.operator == "%":
                        pass

                    self.show_on_display(result)
                    self.temp = None
                    self.operator = None


    def show_on_display(self, token):
        """ update display """
        self.display_var.set(str(token))

    def conc_digits(self, digit):
        """ concatenate numerals of digits and display result """
        if self.clear_display:
            result = ""
            self.clear_display = False
        else:
            result = str(self.display_var.get())
        if result == "0":
            result = ""
        result += str(digit)
        print(result)
        self.show_on_display(result)

root = Tk()
ttk.Style().theme_use('alt')
root.title("Calc_tkinter")
root.eval('tk::PlaceWindow . center')
app = Application(root)
root.mainloop()
