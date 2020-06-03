#!/usr/bin/env python

def fill_table(n):
    table = []
    for i in range(n):
        val = []
        print("{} porcja wartosści".format(i+1))
        for j in range(3):
            val.append(input("Podaj {} wartość: ".format(j+1)))
        table.append(val)
    print("Koniec wpisywania wartości.")
    return table

table = fill_table(int(input("Podaj ilość rzędów: ")))
print(table)


def truth(table):
    for i in range(len(table)):
        row = table[i]
        p = row[0]
        q = row[1]
        r = row[2]
        print(p,q,r)
        if ((not(p and q)) or r) == True:
            print("{} rząd jest prawdziwy".format(i+1))
        else:
            print("{} rząd jest fałszywy".format(i+1))

truth(table)

