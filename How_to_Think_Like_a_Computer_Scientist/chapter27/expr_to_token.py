#!/usr/bin/env python3

def expr2token(expr):
    token_list = []
    for item in expr:
        token_list.append(str(item))
    return token_list


expr = "2*2*3+3+7(8+9)"

print(expr2token(expr))
