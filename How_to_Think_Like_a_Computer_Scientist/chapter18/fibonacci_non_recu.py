#!/usr/bin/env python3

def fibonacci(n):
    """ Return n number in fibonacci sequence. """
    fnm1 = 1
    fnm2 = 0
    fn = 0
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        for i in range(2, n+1):
            fn = fnm1 + fnm2
            fnm2 = fnm1
            fnm1 = fn

    return fn

print(fibonacci(20))
