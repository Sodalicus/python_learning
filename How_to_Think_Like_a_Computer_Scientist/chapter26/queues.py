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

class Queue:
    def __init__(self):
        self.length = 0
        self.head = None

    def is_empty(self):
        return self.lenght == 0

    def insert(self, cargo):
        node = Node(cargo)
        if self.head is None:
            # If list is emoty the new node goes first
            self.head = node
        else:
            # Find the last node in the list
            last = self.head
            while last.next:
                last = last.next
            # Append the new node
            last.next = node
        self.length += 1

    def remove(self):
        cargo = self.head.cargo
        self.head = self.head.next
        self.length -= 1
        return cargo

class ImprovedQueue:
    def __init__(self):
        self.lenght = 0
        self.head = None
        self.last = None

    def is_empty(self):
        return self.lenght == 0

    def insert(self, cargo):
        node = Node(cargo)
        if self.lenght == 0:
            # If list is empty, the new node is head and last
            self.head = self.last = node
        else:
            # Find the last node
            last = self.last
            # Append the new node
            last.next = node
            self.last = node
        self.lenght += 1

    def remove(self):
        cargo = self.head.cargo
        self.head = self.head.next
        self.lenght -= 1
        if self.lenght == 0:
            self.last = None
        return cargo

class PriorityQueue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return not self.items

    def insert(self, item):
        self.items.append(item)

    def remove(self):
        maxi = 0
        for i in range(1, len(self.items)):
            if self.items[i] > self.items[maxi]:
                maxi = i
        item = self.items[maxi]
        del self.items[maxi]
        return item

class Golfer:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __str__(self):
        return "{0:16}: {1}".format(self.name, self.score)

    def __gt__(self, other):
        return self.score < other.score # Less is more

class QueueList:
    def __init__(self):
        self.items = []

    def insert(self, item):
        self.items.append(item)

    def remove(self):
        item = None
        if self.items:
            item = self.items[0]
            self.items.pop(0)
        return item

    def is_empty(self):
        return self.items == []

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


def test_queuelist():
    ql = QueueList()
    t0 = time.time()
    for i in rand_ints:
        ql.insert(i)

    while not ql.is_empty():
        ql.remove()
    t1 = time.time()
    print("Queue_list")
    print("It took {:f} seconds to run.".format(t1-t0))

def test_improved_queue():
    iq = ImprovedQueue()
    t0 = time.time()
    for i in rand_ints:
        iq.insert(i)

    while not iq.is_empty():
        iq.remove()
    t1 = time.time()
    print("Imprved_queue")
    print("It took {:f} seconds to run.".format(t1-t0))


rand_ints = []
for i in range(10000):
    rand_ints.append(random.randrange(10000))

for i in range(5):
    print(rand_ints[i])

tiger = Golfer("Tiger Woods", 61)
phil = Golfer("Phil Mickelson", 72)
hal = Golfer("Hal Sutton", 69)

pq = PriorityQueue()
for g in [tiger, phil, hal]:
    pq.insert(g)

while not pq.is_empty():
    print(pq.remove())


q = PriorityQueue()
for num in [11, 12, 14, 13]:
    q.insert(num)

while not q.is_empty():
    print(q.remove())

test_improved_queue()
test_queuelist()
