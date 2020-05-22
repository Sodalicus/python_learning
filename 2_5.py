#!/usr/bin/env python3

def interest(p,r,n,t):
    a = p*(1+r/n)**(n*t)

    return a

principal = 10000.0
number = 12.0
rinterest = 0.08

tyears = float(input("How man years?"))

compound = interest(principal, rinterest, number, tyears)
print(compound)

print("Compound intersest: ", compound)

