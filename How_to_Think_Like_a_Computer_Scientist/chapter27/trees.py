#!/usr/bin/env python3

class Tree:
    def __init__(self, cargo, left=None, right=None):
        self.cargo = cargo
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.cargo)

def total(tree):
    if tree is None: return 0
    return total(tree.left) + total(tree.right) + tree.cargo

def print_tree(tree):
    if tree is None: return
    print(tree.cargo, end=" ")
    print_tree(tree.left)
    print_tree(tree.right)

def print_tree_postorder(tree):
    if tree is None: return
    print_tree_postorder(tree.left)
    print_tree_postorder(tree.right)
    print(tree.cargo, end=" ")

def print_tree_inorder(tree):
    if tree is None:
        return
    print_tree_inorder(tree.left)
    print(tree.cargo, end=" ")
    print_tree_inorder(tree.right)

def print_tree_indented(tree, level=0):
    if tree is None: return
    print_tree_indented(tree.right, level+1)
    print(" " * level + str(tree.cargo))
    print_tree_indented(tree.left, level+1)

def get_token(token_list, expected):
    if token_list[0] == expected:
        del token_list[0]
        return True
    return False

def get_number(token_list):
    if get_token(token_list, "("):
        x = get_sum(token_list)
        if not get_token(token_list, ")"):
            raise ValueError("Missing close parenthesis")
        return x
    else:
        x = token_list[0]
        if type(x) != type(0): return None
        del token_list[0]
        return Tree(x, None, None)

def get_product(token_list):
    a = get_number(token_list)
    if get_token(token_list, "*"):
        b = get_number(token_list)
        return Tree("*", a, b)
    return a

def get_product2(token_list):
    a = get_number(token_list)
    if get_token(token_list, "*"):
        b = get_product2(token_list)
        return Tree("*", a, b)
    return a

def get_sum(token_list):
    a = get_product2(token_list)
    if get_token(token_list, "+"):
        b = get_sum(token_list)
        return Tree("+", a, b)
    return a

token_list = [9, "*", "(", 11, "+", 5, ")", "*", 7, "end"]
tree = get_sum(token_list)
print_tree_postorder(tree)
print()

print("inorder")
token_list = [9, "*", 11, "+", 5, "*", 7, "end"]
tree = get_sum(token_list)
print_tree_inorder(tree)
print()
print("end")

token_list = [2, "*", 3, "*", 5, "*", 7, "end"]
tree = get_product2(token_list)
print_tree_postorder(tree)
print()


left = Tree(2)
right = Tree(3)
tree = Tree(1, left, right)
tree = Tree(1, Tree(2), Tree(3))
"""
print(total(tree))
tree = Tree("+", Tree(1), Tree("*", Tree(2), Tree(3)))
print_tree(tree)
print()
print_tree_postorder(tree)
print()

print("inorder")
print_tree_inorder(tree)
print()
print("-"*20)
print_tree_indented(tree)
"""
token_list = [9, 11, "end"]
x = get_number(token_list)
print_tree_postorder(x)
print(token_list)


