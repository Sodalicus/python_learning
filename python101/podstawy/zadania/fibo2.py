#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
"""
Example from the python101 course
"""


def fib_iter1(n):
    """
    Funkcja drukuje kolejne wyrazy ciągu Fibonacciego
    aż do wyrazu n-tego, który zwraca.
    Werjsa iteracyjna z pętlą while.
    """
    pwyrazy = (1,1)
    a, b = pwyrazy
    print(a, end=' ')
    while n > 1:
        print(b, end=' ')
        a, b = b, a+b
        n -= 1

    print()
    return b

def fib_iter2(n):
    """
    Funkcja drukuje kolejne wyrazy ciągu Fibonacciego
    aż do wyrazu n-tego, który zwraca.
    Wersja iteracyjna z pętlą for.
    """

    a, b = 1, 1
    print("wyraz", 1, a)
    print("wyraz", 2, b)
    for i in range(1, n - 1):
        a, b = b, a + b
        print("wyraz", i + 2, b)

    print()
    return b

def fib_rek(n):
    """
    Funkcja zwraca n-ty wyraz ciągu Fibonacciego.
    Wersja rekurencyjna.
    """
    if n < 1:
        return 1
    if n < 2:
        return 1
    return fib_rek(n-1)+fib_rek(n-2)

def main(args):
    n = int(input("Podaj numer wyrazu: "))
    fib_iter1(n)
    print()
    print("=" * 40)
    fib_iter2(n)
    print("="*40)
    print(fib_rek(n-1))
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
