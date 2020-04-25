#!/usr/bin/env python

from tkinter import *
import random

class Application(Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()
        self.random_number = None
        self.reset()

    def create_widgets(self):
        Label(self,
                text = "Jaka to liczba?"
                ).grid(row = 0, column = 0, sticky = W)
        self.number_ent = Entry(self)
        self.number_ent.grid(row = 0, column = 1 , sticky = W)

        Button(self, text = "Ok",
                command = self.update_results
                ).grid(row = 1, column = 0, sticky = W)
        Button(self, text = "Reset",
                command = self.reset
                ).grid(row = 1, column = 1, sticky = W)

        self.tries_lbl = Label(self,
                text = "Pozostała liczba prób: "
                ).grid(row = 2, column = 0, sticky = W)
        self.tries_left_lbl_var = StringVar()
        self.tries_left_lbl_var.set("7")
        self.tries_left_lbl = Label(self, textvariable = self.tries_left_lbl_var)
        self.tries_left_lbl.grid(row = 2, column = 1, sticky = W)

        self.screen_txt = Text(self, width = 40, height = 6, wrap = WORD)
        self.screen_txt.grid(row = 3, column = 0, columnspan = 2)

    def update_results(self):
        number = 0
        if self.number_ent.get():
            number = int(self.number_ent.get()) self.tries -= 1
        if self.tries < 0: self.tries = 0
        if self.tries > 0 and number > self.random_number:
            self.info = "Szukana liczba jest mniejsza."
        elif self.tries > 0 and number < self.random_number:
            self.info = "Szukana liczba jest większa."
        elif number == self.random_number and self.tries > 0:
            self.info = "Brawo, odgadłeś szukaną liczbę."
        elif self.tries == 0:
            self.info = "Niestety skończyły Ci się próby."

        self.tries_left_lbl_var.set(self.tries)
        self.screen_txt.delete(0.0, END)
        self.screen_txt.insert(0.0, self.info)
        pass

    def reset(self):
        self.random_number = random.randint(1,100)
        self.tries = 7
        self.tries_left_lbl_var.set(self.tries)
        self.info = "Odgadnij liczbę z zakresu 1-100."

        self.screen_txt.delete(0.0, END)
        self.screen_txt.insert(0.0, self.info)

root = Tk()
root.title("Jaka to liczba?")
app = Application(root)
root.mainloop()
