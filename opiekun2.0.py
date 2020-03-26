#!/usr/bin/python
# -*- coding: utf-8 -*-

#Opiekun zwierzaka 2.0 - farma zwierzaków,
#Pytdk3 Rozdział 08, zadanie 4
import random

class Critter():
    def __init__(self, name):
        self.name = name
        self.hunger = random.randint(-10,10)
        self.boredom = random.randint(-10,10)

    def __mood(self):
        if self.hunger+self.boredom >= 15:
            print('Jestem szczęśliwy\n')
        elif 15 > self.hunger+self.boredom >= 10:
            print('Jestem zadowolony\n')
        elif 10 > self.hunger+self.boredom >= 7:
            print('Jest w porzadku...\n')
        else:
            print('Jestem zły!\n')

    def __passtime(self):
        self.hunger -= 2
        self.boredom -= 2

    def talk(self):
        self.boredom += 5
        print('Jestem zwierzątkiem, na imię mi {}.\n'.format(self.name))
        self.__mood()
        self.__passtime()

    def feed(self):
        self.hunger += 5
        print('{}: Mniam, mniam.'.format(self.name))
        self.__passtime()

    def play(self):
        self.boredom += 5
        print('{}: Zabawa!'.format(self.name))
        self.__passtime()

critterPack = []
crit1 = Critter('Romek')
crit2 = Critter('Tomek')
crit3 = Critter('Zgredek')
critterPack.append(crit1)
critterPack.append(crit2)
critterPack.append(crit3)

choice = None
while choice != "0":
    choice = input('''
    \n1 - Poroznawiaj
    \n2 - Nakarm
    \n3 - Pobaw się
    \n0 - Zakończ\n''')
    if choice == "1":
        for crit in critterPack:
            crit.talk()
    elif choice == "2":
        for crit in critterPack:
            crit.feed()
    elif choice == "3":
        for crit in critterPack:
            crit.play()
    elif choice == "0":
        print('Żegnaj\n')
    else:
        print('Wybierz opcje 0 - 4\n')

