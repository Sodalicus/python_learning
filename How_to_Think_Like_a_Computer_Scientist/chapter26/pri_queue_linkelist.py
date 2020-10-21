#!/usr/bin/env python3
import time, random

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

class PrioQueueLL:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def insert(self, cargo):
        node = Node(cargo)
        if self.is_empty():     # if list is empty, add first node
            self.head = node
        else:
            if node.cargo >= self.head.cargo:   # if new node.cargo is the highest, add it on the top
                node.next = self.head
                self.head = node
            else:
                """
                Keep the reference to the current pair, check the second.cargo, if the node.cargo is greater
                insert node between first and second.
                If it's not, move down the list by one, and compare the new second cargo.
                """
                first = self.head
                second = first.next
                while second is not None:
                    if node.cargo >= second.cargo:
                        node.next = second
                        first.next = node
                        break
                    else:
                        if first.next is not None: # if we didnt get to the end of the list
                            first = first.next
                        else: # We got to the end of the list, node.cargo is the lowest, put it at the end
                            first.next = node
                            break


    def remove(self):
        if self.is_empty():
            pass
        else:
            self.head = self.head.next

def print_list(node):
    while node is not None:
        print(node, end=" ")
        node = node.next
    print()

def test_prioqueuell():
    pqll = PrioQueueLL()
    t0 = time.time()
    for i in range(10000):
        pqll.insert(i)

    while not pqll.is_empty():
        pqll.remove()
    print(pqll.is_empty())
    t1 = time.time()
    print("Priority_queue_LL")
    print("It took {:f} seconds to run.".format(t1-t0))


rand_ints = []
for i in range(10000):
    rand_ints.append(random.randrange(10000))

for i in range(5):
    print(rand_ints[i])

test_prioqueuell()
