#!/usr/bin/env python3

class LinkedList:
    def __init__(self):
        self.lenght = 0
        self.head = None

    def print_backward(self):
        print("[", end=" ")
        if self.head is not None:
            self.head.print_backward()
        print("]")

    def add_first(self, cargo):
        node = Node(cargo)
        node.next = self.head
        self.head = node
        self.lenght += 1

class Node:
    def __init__(self, cargo=None, next=None):
        self.cargo = cargo
        self.next = next

    def __str__(self):
        return str(self.cargo)

    def print_backward(self):
        if self.next is not None:
            tail = self.next
            tail.print_backward()
        print(self.cargo, end=", ")




def print_list(node):
    while node is not None:
        print(node, end=" ")
        node = node.next
    print()

def print_backward(list):
    if list is None: return
    head = list
    tail = list.next
    print_backward(tail)
    print(head, end=" ")

def print_backward2(list):
    if list is None: return
    print_backward2(list.next)
    print(list, end=" ")

def remove_second(list):
    if list is None: return
    if list.next == None:return
    first = list
    second = list.next
    # Make the first refer to the third
    first.next = second.next
    # Separate the second node from the rest of the list
    second.next = None
    return second

def print_backward_nicely(list):
    print("[", end=" ")
    print_backward(list)
    print("]")


node = Node("test")
print(node)

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node1.next = node2
node2.next = node3
list1 = LinkedList()
list1.add_first(1)
list1.add_first(2)
list1.add_first(3)
list1.print_backward()
list2 = LinkedList()
list2.print_backward()
"""
print_backward_nicely(node1)
print_list(node1)
print_backward(node1)
print_list(node1)
removed = remove_second(node1)
print_list(removed)
print_list(node1)
node4 = Node()
node5 = Node(5)
remove_second(node4)
remove_second(node5)
print_backward_nicely(node4)
print_backward_nicely(node5)
"""
