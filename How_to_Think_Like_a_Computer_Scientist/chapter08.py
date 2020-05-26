from testing import test
import string

#"How to Think Like a Computer Scientist"
#Excercises from chapter 8 - "Strings"

#Excercise 1
"""What is the result of each of the following:"""
"""
>>> "Python"[1]
'y'
>>> "Strings are sequences of characters."[5]
'g'
>>> len("wonderful")
9
>>> "Mystery"[:4]
'Myst'
>>> "p" in "Pineapple"
True
>>> "apple" in "Pineapple"
True
>>> "pear" not in "Pineapple"
False
>>> "apple" > "pineapple"
False
>>> "pineapple" < "Peach"
False
"""

#Excercise 2
"""Modify:
prefixes = "JKLMNOPQ"
suffix = "ack"

for letter in prefixes:
    print(letter + suffix)

so that Ouack and Quack are spelled correctly.
"""

def ducklings():
    prefixes = "JKLMNOPQ"
    suffix = "ack"
    for letter in prefixes:
        if letter in ("Q","O"):
            letter +="u"
        print(letter+suffix)

#Excercise 3
"""Encapsulate:

fruit = "banana"
count = 0
for char in fruit:
    if char == "a":
        count += 1
print(count)

in a function named count_letters, and generalize it so that it accepts the string and the letter as arguments. Make the function return the number of characters, rather than print the answer. The caller should do the printing."""

def count_letters(strgiv, letter):
    count = 0
    for char in strgiv:
        if char == letter:
            count +=1
    return count

aaa = "banana is a fruit."

test(count_letters(aaa, "a")== 4)

#Excercise 4
"""Now rewrite the count_letters function so that instead of traversing the string, it repeatedly calls the find method, with the optional third parameter to locate new occurrences of the letter being counted."""

def count_letter2(strgiv, letter):
    count = 0
    result = strgiv.find(letter, 0)
    while result != -1:
        result = strgiv.find(letter, result+1)
        count +=1
    return count
test(count_letter2(aaa, "a") == 4)

#Excercise 5
"""Assign to a variable in your program a triple-quoted string that contains your favourite paragraph of text — perhaps a poem, a speech, instructions to bake a cake, some inspirational verses, etc.

Write a function which removes all punctuation from the string, breaks the string into a list of words, and counts the number of words in your text that contain the letter “e”. Your program should print an analysis of the text like this:

Your text contains 243 words, of which 109 (44.8%) contain an "e".
"""

quote = """After a long moment I closed the freezer door. I wanted to lie down and press my cheek against the cool linoleum. Instead I reached out with my little finger and flipped the Barbie's head. It went thack thack against the door. I flipped it again. Thack thack. Whee. I had a new hobby."""

def count_e(sx):
    new_string = ""
    for char in sx:
        if char not in string.punctuation:
            new_string += char
    print(new_string)
    words = len(new_string.split())
    ewords = 0
    for ew in new_string:
        if ew.find("e") != -1:
            ewords += 1
    print('Your text contains {} words, of which {} ({:.1f}%) contain an "e".'.format(words, ewords, ewords/words*100))

#Excerice 6
"""Print a neat looking multiplication table like this:

        1   2   3   4   5   6   7   8   9  10  11  12
  :--------------------------------------------------
 1:     1   2   3   4   5   6   7   8   9  10  11  12
 2:     2   4   6   8  10  12  14  16  18  20  22  24
 3:     3   6   9  12  15  18  21  24  27  30  33  36
 4:     4   8  12  16  20  24  28  32  36  40  44  48
 5:     5  10  15  20  25  30  35  40  45  50  55  60
 6:     6  12  18  24  30  36  42  48  54  60  66  72
 7:     7  14  21  28  35  42  49  56  63  70  77  84
 8:     8  16  24  32  40  48  56  64  72  80  88  96
 9:     9  18  27  36  45  54  63  72  81  90  99 108
10:    10  20  30  40  50  60  70  80  90 100 110 120
11:    11  22  33  44  55  66  77  88  99 110 121 132
12:    12  24  36  48  60  72  84  96 108 120 132 144
"""

def multi_mult():
    layout2 = "{:>4}"
    print(" "*4, end="")
    for i in range(1,13):
        print("{:>4}".format(i), end="")
    print()
    print("  :"+50*"-")
    for i in range(1,13):
        print("{:>2}:  ".format(i), end="")
        for j in range(1,13):
            print(layout2.format(i*j), end="")
        print()

#Excercise 7
"""Write a function that reverses its string argument, and satisfies these tests:"""

def reverse(sx):
    new_string = ""
    for i in range(1,len(sx)+1):
        new_string += sx[-i]
    return new_string

test(reverse("happy") == "yppah")
test(reverse("Python") == "nohtyP")
test(reverse("") == "")
test(reverse("a") == "a")

#Excercise 8
"""Write a function that mirrors its argument:"""

def mirror(sx):
    new_string = sx[:]
    for i in range(1,len(sx)+1):
        new_string += sx[-i]
    return new_string

test(mirror("good") == "gooddoog")
test(mirror("Python") == "PythonnohtyP")
test(mirror("") == "")
test(mirror("a") == "aa")

#Excerice 9
"""Write a function that removes all occurrences of a given letter from a string:"""

def remove_letter(letter, xs):
    new_string = ""
    for char in xs:
        if char != letter:
            new_string += char
    return new_string


test(remove_letter("a", "apple") == "pple")
test(remove_letter("a", "banana") == "bnn")
test(remove_letter("z", "banana") == "banana")
test(remove_letter("i", "Mississippi") == "Msssspp")
test(remove_letter("b", "") == "")
test(remove_letter("b", "c") == "c")

#Excercise 10
"""Write a function that recognizes palindromes. (Hint: use your reverse function to make this easy!):"""

def is_palindrome(sx):
    if sx == reverse(sx):
        return True
    else:
        return False

test(is_palindrome("abba"))
test(not is_palindrome("abab"))
test(is_palindrome("tenet"))
test(not is_palindrome("banana"))
test(is_palindrome("straw warts"))
test(is_palindrome("a"))

#Excercise 11
"""Write a function that counts how many times a substring occurs in a string:"""

def count(spat, strx):
    if spat not in strx or len(spat)>len(strx):
        return 0
    count = 0
    in_down = 0
    in_up = len(spat)
    while in_up <= len(strx):
        if spat == strx[in_down:in_up]:
            count += 1
        in_up += 1
        in_down += 1
    return count

test(count("is", "Mississippi") == 2)
test(count("an", "banana") == 2)
test(count("ana", "banana") == 2)
test(count("nana", "banana") == 1)
test(count("nanan", "banana") == 0)
test(count("aaa", "aaaaaa") == 4)
test(count("aaaaaaaaaaaa", "aa") == 0)

#Excercise 12
"""Write a function that removes the first occurrence of a string from another string:"""

def remove(spat, strx):
    if spat not in strx or len(spat)>len(strx):
        return strx
    else:
        inx = [] 
        new_string = ""
        for i in range(len(strx)):
            if spat == strx[i:i+len(spat)]:
                inx = list(range(i,i+len(spat)))
                break
        for i,ch in enumerate(strx):
            if i not in inx:
                new_string += ch
    return new_string


test(remove("an", "banana") == "bana")
test(remove("cyc", "bicycle") == "bile")
test(remove("iss", "Mississippi") == "Missippi")
test(remove("eggs", "bicycle") == "bicycle")

#Excercise 13
"""Write a function that removes all occurrences of a string from another string:"""

def remove_all(spat, strx):
    if spat not in strx or len(spat)>len(strx):
        return strx
    else:
        inx = [] 
        new_string = ""
        for i in range(len(strx)):
            if spat == strx[i:i+len(spat)]:
                inx.extend(range(i,i+len(spat)))
        for i,ch in enumerate(strx):
            if i not in inx:
                new_string += ch
    return new_string


test(remove_all("an", "banana") == "ba")
test(remove_all("cyc", "bicycle") == "bile")
test(remove_all("iss", "Mississippi") == "Mippi")
test(remove_all("eggs", "bicycle") == "bicycle")

