#!/usr/bin/env python3
import pickle,os

class Tree:
    def __init__(self, cargo, left=None, right=None):
        self.cargo = cargo
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.cargo)

def create_tree(animal_list):
    """ Turn a list into a Tree """
    animal_tree = []
    if animal_list == None or len(animal_list)==0:
        return Tree("bird")
    for branch in animal_list:
        animal_tree.append(Tree(branch.splitlines()[0]))
    while len(animal_tree)>2:
        animal_tree[1].right = animal_tree[2]
        animal_tree[1].left = animal_tree[0]
        animal_tree[2] = animal_tree[1]
        del(animal_tree[0])
        del(animal_tree[1])
    return animal_tree[0]


def load_animal(infile):
    """ Loads file a file and return a content as a list """
    if os.path.isfile(infile):
        file = open(infile, "r")
        text_animal = file.readlines()
        return text_animal
    else:
        return None

def save_animal(tree_root):
    """ Saves given list to a file """
    text_animal = []
    infile = open("animal.txt", "w")
    create_list(tree_root, text_animal)
    print(len(text_animal))
    infile.writelines(text_animal)
    infile.close


def create_list(tree, lista):
    """ Creates a list of made of Tree's cargos """
    if tree is None: return
    create_list(tree.left, lista)
    lista.append(str(tree.cargo)+'\n')
    #print(level,str(tree.cargo))
    create_list(tree.right, lista)



def yes(ques):
    ans = input(ques).lower()
    return ans[0] == "y"

def animal():
    # Start with a singleton
    #root = Tree("bird")
    root = create_tree(load_animal("animal.txt"))

    # Loop until the user quits
    while True:
        print()
        if not yes("Are you thinking of an animal? "): break

        # Walk the tree
        tree = root
        while tree.left is not None:
            prompt = tree.cargo + "?"
            if yes(prompt):
                tree = tree.right
            else:
                tree = tree.left
        # Make a guess
        guess = tree.cargo
        prompt = "Is it a " + guess + "? "
        if yes(prompt):
            print("I rule!")
            continue

        # Get new information
        prompt = "What is the animal's name? "
        animal = input(prompt)
        prompt = "What question would distinguish a {0} from a {1}? "
        question = input(prompt.format(animal, guess))

        # Add new information to the tree
        tree.cargo = question 
        prompt = "If the animal were {0} the answer would be? "
        if yes(prompt.format(animal)):
            tree.left = Tree(guess)
            tree.right = Tree(animal)
        else:
            tree.left = Tree(animal)
            tree.right = Tree(guess)

    save_animal(root)
#global root
#root = Tree("Does it bark?", Tree("Does it moew?", Tree("bird"), Tree("cat")), Tree("dog"))
animal()
