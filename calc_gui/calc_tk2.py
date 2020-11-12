#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Calculator app using tkinter for gui, another approach from scratch
# Version 0.1

""" TODO:
    - valid float handling -- DONE
    - leading minus sign -- DONE
    - dot, or coma handling to type in floats -- DONE
    - more operators
    - clear_all[CA] and clear_entry[CE] buttons
    - % operator handling
    - nicer looks -- partway
"""

from tkinter import *
from tkinter import ttk
import operator,copy

# the so called look-up table
operators = {"+" : operator.add,
             "-" : operator.sub,
             "*" : operator.mul,
             "/" : operator.truediv}


class Application(Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.display_var = StringVar()
        self.display_var.set("0")
        self.results = "0"
        self.temp = None
        self.last_operator = None
        self.clear_display = False
        self.turn_negative = False
        self.create_widgets()

    def create_widgets(self):
        """ Create buttons and text field """
        self.display = Label(self, textvariable = self.display_var, \
                anchor = "e", width =20, relief =SUNKEN
                ).grid(row = 0, column = 0, columnspan =4, sticky = N)

        Button(self, text=" ", width = 1, height = 1,
                command = lambda: self.button_action("%")
                ).grid(row = 1, column = 0,sticky = W)

        Button(self, text="/", width = 1, height = 1,
                command = lambda: self.button_action("/")
                ).grid(row = 1, column = 1,sticky = W)

        Button(self, text="*",  width = 1, height = 1,
                command = lambda: self.button_action("*")
                ).grid(row = 1, column = 2,sticky = W)

        Button(self, text="CE", width = 1, height = 1,
                command = self.clear_entry
                ).grid(row = 1, column = 3,sticky = W)

        Button(self, text="AC", width = 1, height = 1,
                command = self.all_clear
                ).grid(row = 2, column = 3,sticky = W)

        Button(self, text="-", width = 1, height = 1,
                command = lambda: self.button_action("-")
                ).grid(row = 3, column = 3,sticky = W)

        Button(self, text="7", width = 1, height = 1,
                command = lambda: self.button_action(7)
                ).grid(row = 2, column = 0,sticky = W)

        Button(self, text="8", width = 1, height = 1,
                command = lambda: self.button_action(8)
                ).grid(row = 2, column = 1,sticky = W)

        Button(self, text="9", width = 1, height = 1,
                command = lambda: self.button_action(9)
                ).grid(row = 2, column = 2,sticky = W)

        Button(self, text="+", width = 1, height = 1,
                command = lambda: self.button_action("+")
                ).grid(row = 4, column = 3, sticky = W)

        Button(self, text="4", width = 1, height = 1,
                command = lambda: self.button_action(4)
                ).grid(row = 3, column = 0,sticky = W)

        Button(self, text="5", width = 1, height = 1,
                command = lambda: self.button_action(5)
                ).grid(row = 3, column = 1,sticky = W)

        Button(self, text="6", width = 1, height = 1,
                command = lambda: self.button_action(6)
                ).grid(row = 3, column = 2,sticky = W)

        Button(self, text="1", width = 1, height = 1,
                command = lambda: self.button_action(1)
                ).grid(row = 4, column = 0,sticky = W)

        Button(self, text="2", width = 1, height = 1,
                command = lambda: self.button_action(2)
                ).grid(row = 4, column = 1,sticky = W)

        Button(self, text="3", width = 1, height = 1,
                command = lambda: self.button_action(3)
                ).grid(row = 4, column = 2,sticky = W)

        Button(self, text="=", width = 1, height = 1,
                command = lambda: self.button_action("=")
                ).grid(row = 5, column = 3, rowspan = 2, sticky = W)

        Button(self, text="0", width = 1, height = 1,
                command = lambda: self.button_action(0)
                ).grid(row = 5, column = 0, columnspan = 2, sticky = W)

        Button(self, text=".", width = 1, height = 1,
                command = lambda: self.button_action(".")
                ).grid(row = 5, column = 1, sticky = W)

    def button_action(self, token):
        if type(token) == type(0):
            self.join_digits(token)
        elif type(token) == type(","):
            if token == ".":
                """ if dot/coma, was pressed, contatenate dot/coma
                    to current number """
                self.make_float()
            elif token == "-" and self.results == "0" and not self.turn_negative:
                self.turn_negative = True
            elif token in operators.keys():
                self.last_operator = token
                self.clear_display = True
                self.temp = copy.copy(self.results)
                self.results = "0"
            elif token == "=":
                if self.last_operator:
                    if "." in self.temp or "." in self.results:
                        """ if either of parts of computation has "dot" sign/
                           is float, convert them into proper float numbers
                           for computation """
                        first_part = float(self.temp)
                        second_part = float(self.results)
                    else:
                        """ if both are integers, are dot-less, convert them
                            into proper integers """
                        first_part = int(self.temp)
                        second_part = int(self.results)
                    self.results = str(round(operators[self.last_operator](first_part, second_part), 4))
                self.last_operator = None
                self.temp = None
                self.update_display(self.results)

    def update_display(self, token):
        """ Simply display given token on the 'display' """
        self.display_var.set(str(token))

    def make_float(self):
        """ if there isnt one, concatenate "." sign to turn number into float """
        if "." not in self.results:
            new_float = self.results+"."
            self.results = copy.copy(new_float)
        self.update_display(self.results)

    def make_negative(self):
        """ if number is positive/has not leading minus sign, concatenate one """
        if "-" not in self.results:
            new_negative = "-" + self.results
            self.results = copy.copy(new_negative)
            self.turn_negative = False
        self.update_display(self.results)

    def join_digits(self, token):
        """ concatenate digits to create desired number """
        if self.clear_display:
            """ if there has been operator already chosen, clear display for new number """
            joined_digits = ""
            self.clear_display = False
        else:
            joined_digits = str(copy.copy(self.results))
        if self.results != "0":
            joined_digits += str(token)
            self.results = str(copy.copy(joined_digits))
            if self.turn_negative:
                self.make_negative()
            self.update_display(self.results)
        else:
            """ If the digit on display is just 0/zero """
            self.results = str(token)
            if self.turn_negative:
                self.make_negative()
            self.update_display(self.results)

    def clear_entry(self):
        pass

    def all_clear(self):
        self.display_var.set("0")
        self.results = "0"
        self.temp = None
        self.last_operator = None
        self.clear_display = False
        self.turn_negative = False



root = Tk()
ttk.Style().theme_use('alt')
root.title("Calc_tkinter")
root.eval('tk::PlaceWindow . center')
app = Application(root)
root.mainloop()
