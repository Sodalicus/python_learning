#!/usr/bin/env python

from tkinter import *
from tkinter.ttk import * 
import random


class Application(Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.main_courses = ["stek z frytkami", "mielony z surówką", "spaghetti", "pierogi", "gołąbki"]
        self.soups = ["pomidorowa", "ogórkowa", "jarzynowa", "żurek", "barszcz"]
        self.deserts = ["lody", "ciastko z kremem", "czekoladowe gniazdko"]
        self.row = 0
        self.create_widgets()

    def create_widgets(self):
        self.row = 0
        for course in self.main_courses:
            Label(self,
                    text = course 
                   ).grid(row = self.row, column = 0, sticky = W)
            self.row += 1
        for soup in self.soups:
            Label(self, 
                    text = soup
                    ).grid(row = self.row, column = 0, sticky = W)
            self.row += 1
        for desert in self.deserts:
            Label(self,
                    text = desert
                    ).grid(row = self.row, column = 0, sticky = W)
            self.row += 1
        Button(self,
                text = "Rachunek",
                command = self.check_please
                ).grid()
        self.sum_lbl = Label(self,
                text = "Końcowy rachunek wynosi:   ")
        self.sum_lbl.grid()

        self.checklist = []
        self.checklist_prices = []
        for i in range(self.row):
            self.checklist_prices.append(random.randint(1,100)) 
            self.checklist.append(BooleanVar())
            Checkbutton(self,
                    text = self.checklist_prices[i],
                    variable = self.checklist[i]
                    ).grid (row = i, column = 1, sticky = W)

    def check_please(self):
        sum = 0
        info_sum = "Końcowy rachunek wynosi: "
        for i in range(self.row):
            if self.checklist[i].get():
                sum += self.checklist_prices[i]
        info_sum += str(sum)
        self.sum_lbl['text'] = info_sum 


root = Tk()
s = Style()
app = Application(root)
root.mainloop()
