#!/usr/bin/env python
import random, sys

def test(did_pass):
    """ Print the result of a test. """
    linenum = sys._getframe(1).f_lineno # Get the caller’s line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)

numbers = []
for i in range(-10,20):
    numbers.append(i)


def count_odd(numbers):
    count = 0 
    for i in numbers:
        if i%2 == 1:count +=1
    return count

def count_even(numbers):
    count = 0
    for i in numbers:
        if i%2 == 0:count +=1
    return count

def sum_neg(numbers):
    sum = 0
    for number in numbers:
        if number < 0: sum+= number
    return sum

def count_5_words(words):
    count = 0
    for word in words:
        if len(word)==5: count+=1
    return count

def sum_up_to_even(numbers):
    sum = 0
    for number in numbers:
        if number%2 == 0: break
        sum +=number
    return sum

def count_no_sam_words(words):
    count = 0
    for word in words:
        if "sam" in word:
            break
        count += 1
    return count

def sqrt(n):
    approx = n//2.0
    while True:
        better = (approx + n/approx)/2.0
        if abs(approx - better) < 0.001:
            return better
        print(better)
        approx = better

def print_multiples(n, high):
    for i in range(1, high+1):
        print(n * i, end=" ")
    print()

def print_mult_table(high):
    for i in range(1, high+1):
        print_multiples(i, high)

def print_triangular_numbers(n):
    sum = 0
    for i in range(1, n+1):
        sum+=i
        print(i,"\t",sum)

def is_prime(n):
    for i in range(2,n):
        if n%i == 0: return False
    return True

def num_digits(n):
    count = 0
    n = abs(n)
    if n == 0:return 1
    while n != 0:
        n = n // 10
        count += 1
    return count

def num_even_digits(n):
    count = 0
    if n == 0: return 1
    while n != 0:
        if n%2 == 0: count += 1
        n = n//10
    return count

def sum_of_squares(xs):
    sum = 0
    for s in xs:
        sum += s**2
    return sum

sam_list = ["white", "red", "sam", "green"]
sam1_list = ["sam", "green", "orange"]
no_sam = ["yellow", "purple", "black"]

def test_suite():
    test(sum_up_to_even([2,4,2,5]) == 0 )
    test(sum_up_to_even([1,1,7,9,4]) == 18)
    test(sum_up_to_even([]) == 0)
    test(count_no_sam_words(sam_list) == 2)
    test(count_no_sam_words(sam1_list) == 0)
    test(count_no_sam_words(no_sam) == 3)
    test(is_prime(11))
    test(not is_prime(35))
    #test(is_prime(19911121))
    test(num_digits(0) == 1)
    test(num_digits(-12345) == 5)
    test(num_digits(500) == 3)
    test(num_even_digits(123456) == 3)
    test(num_even_digits(2468) == 4)
    test(num_even_digits(1357) == 0)
    test(num_even_digits(0) == 1)
    test(sum_of_squares([2, 3, 4]) == 29)
    test(sum_of_squares([ ]) == 0)
    test(sum_of_squares([2, -3, 4]) == 29)
test_suite()
