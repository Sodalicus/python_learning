#!/usr/bin/env python
# 

from tkinter import *

class Application(Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        Label(self,
                text = "Składak opowiadania."
                ).grid(row = 0 , column = 0, sticky = W)
        
        Label(self,
                text = "Imię bohatera: "
                ).grid(row = 1, column = 0, sticky = W)
        self.name_ent = Entry(self)
        self.name_ent.grid(row = 1, column = 1, sticky = W)

        Label(self,
                text = "Rasa: "
                ).grid(row = 2, column = 0, sticky = W)
        self.race = StringVar()
        self.race.set(None)
        column = 0
        self.races = ["Elf", "Krasnolud", "Człowiek", "Niziołek"]
        for race in self.races:
            Radiobutton(self,
                    text = race,
                    variable = self.race,
                    value = race
                    ).grid(row = 3, column = column, sticky = W)
            column += 1

        Label(self,
                text = "Wyposażenie: "
                ).grid(row = 4 , column = 0, sticky = W)
        """
        self.equipment = ["Miecz", "Topór", "Łuk", "Sztylet"]
        self.is_equipment = []
        for i in range(len(self.equipment)):
            self.is_equipment.append(BooleanVar())
        column = 0
        for weapon in self.equipment:
            Checkbutton(self,
                    text = weapon,
                    variable = self.is_equipment[i]
                    ).grid(row = 5, column = column, sticky = W)
            column += 1 """
        self.is_sword = BooleanVar()
        Checkbutton(self,
                text = "Miecz",
                variable = self.is_sword
                ).grid(row = 5, column = 0, sticky = W)
        self.is_axe = BooleanVar()
        Checkbutton(self,
                text = "Topór",
                variable = self.is_axe
                ).grid(row = 5, column = 1, sticky = W)
        self.is_bow = BooleanVar()
        Checkbutton(self,
                text = "Łuk",
                variable = self.is_bow
                ).grid(row = 5, column = 2, sticky = W)
        self.is_dagger = BooleanVar()
        Checkbutton(self,
                text = "Sztylet",
                variable = self.is_dagger
                ).grid(row = 5, column = 3, sticky = W)

        Label(self,
                text = "Przeciwnicy(rzeczownik w liczbie mnogiej: "
                ).grid(row = 6, column = 0, sticky = W)
        self.noun_ent = Entry(self)
        self.noun_ent.grid(row = 6, column = 1, sticky = W)
        
        Label(self,
                text = "Działanie(czasownik): "
                ).grid(row = 7, column = 0, sticky = W)
        self.verb_ent = Entry(self)
        self.verb_ent.grid(row = 7, column = 1, sticky = W) 

        Button(self,
                text = "Składaj!",
                command = self.update_txt
                ).grid(row = 15, column = 0, sticky = W)

        self.result_txt = Text(self, width = 80, height = 20, wrap = WORD)
        self.result_txt.grid(row = 14, column = 0, columnspan = 3, sticky = W)

    def update_txt(self):
        name = self.name_ent.get()
        noun = self.noun_ent.get()
        verb = self.verb_ent.get()
        if self.race.get():
            race = self.race.get()
        """
        weapon = ""
        for i in range(len(self.is_equipment)):
            if self.is_equipment[i].get():
                print(self.is_equipment[i].get())
                weapon += self.equipment[i]+" "
        weapon +="."
        """
        weapon = ""
        if self.is_sword.get():
            weapon+="Miecz, "
        if self.is_axe.get():
            weapon+="Topór, "
        if self.is_bow.get():
            weapon+="Łuk, "
        if self.is_dagger.get():
            weapon+="Sztylet, "

        result = "W świecie, gdzie butelki walają się pod każdym drzewem. "
        result += "Pojawił się bohater, jego imię to "
        result += name+"."
        result += "Był to dumny "
        result += race+". "
        result += "Przy swoim pasku nosił swóje wyposażenie "
        result += weapon
        result += "wykąpane w Dębowym Mocnym, przez lokalnych żuli. "
        result += "Przechadzajəc się przez śmietnik, w pobliżu upadłej twierdzy Lidl. "
        result += "Na swej drodze spotkał upadłe "
        result += noun+". "
        result += "Odważny wojownik, herbu 'Kupa na podeszwie', postanowił te wrogie hordy "
        result += verb+". "
        self.result_txt.delete(0.0, END)
        self.result_txt.insert(0.0, result)


root = Tk()
root.title("Składak")
app = Application(root)
root.mainloop()

