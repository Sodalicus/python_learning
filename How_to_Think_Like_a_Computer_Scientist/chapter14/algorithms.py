#!/usr/bin/env python3
import pickle,time,random
from testing import test
import draw_queens

def search_linear(xs, target):
    """ Find and return the index of target in sequence xs """
    for (i, v) in enumerate(xs):
        if v == target:
            return i
    return -1

def search_binary(xs, target):
    """ Find and return the index of key in sequence xs """
    lb = 0
    ub = len(xs)
    while True:
        if lb == ub:   # If region of interest (ROI) becomes empty
           return -1

        # Next probe should be in the middle of the ROI
        mid_index = (lb + ub) // 2

        # Fetch the item at that position
        item_at_mid = xs[mid_index]

        #print("ROI[{0}:{1}](size={2}), probed='{3}', target='{4}'"
        #       .format(lb, ub, ub-lb, item_at_mid, target))

        # How does the probed item compare to the target?
        if item_at_mid == target:
            return mid_index      # Found it!
        if item_at_mid < target:
            lb = mid_index + 1    # Use upper half of ROI next time
        else:
            ub = mid_index        # Use lower half of ROI next time

f = open("lorem_list.pickle", "rb")
words = pickle.load(f)
print(search_linear(words, "ipsum"))

vocab = ["apple", "boy", "dog", "down",
                          "fell", "girl", "grass", "the", "tree"]
book_words = "the apple fell from the tree to the grass".split()

def find_unknown_words(vocab, wds):
    """ Return a list of words in wds that do not occur in vocab """
    result = []
    for w in wds:
        if (search_binary(vocab, w) < 0):
            result.append(w)
    return result

test(find_unknown_words(vocab, book_words) == ["from", "to"])
test(find_unknown_words([], book_words) == book_words)
test(find_unknown_words(vocab, ["the", "boy", "fell"]) == [])

def load_words_from_file(filename):
    """ Read words from filename, return list of words. """
    f = open(filename, "r")
    file_content = f.read()
    f.close()
    wds = file_content.split()
    return wds

bigger_vocab = load_words_from_file("vocab.txt")
print("There are {0} words in the vocab, starting with\n {1} "
              .format(len(bigger_vocab), bigger_vocab[:6]))

def text_to_words(the_text):
    """ return a list of words with all punctuation removed,
        and all in lowercase.
    """

    my_substitutions = the_text.maketrans(
      # If you find any of these
      "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&()*+,-./:;<=>?@[]^_`{|}~'\\",
      # Replace them by these
      "abcdefghijklmnopqrstuvwxyz                                          ")

    # Translate the text now.
    cleaned_text = the_text.translate(my_substitutions)
    wds = cleaned_text.split()
    return wds

test(text_to_words("My name is Earl!") == ["my", "name", "is", "earl"])
test(text_to_words('"Well, I never!", said Alice.') ==
                             ["well", "i", "never", "said", "alice"])

def get_words_in_book(filename):
    """ Read a book from filename, and return a list of its words. """
    f = open(filename, "r")
    content = f.read()
    f.close()
    wds = text_to_words(content)
    return wds

book_words = get_words_in_book("AliceInWonderland.txt")
print("There are {0} words in the book, the first 100 are\n{1}".
           format(len(book_words), book_words[:100]))

t0 = time.clock()
missing_words = find_unknown_words(bigger_vocab, book_words)
t1 = time.clock()
print("There are {0} unknown words.".format(len(missing_words)))
print("That took {0:.4f} seconds.".format(t1-t0))




xs = [2,3,5,7,11,13,17,23,29,31,37,43,47,53]
test(search_binary(xs, 20) == -1)
test(search_binary(xs, 99) == -1)
test(search_binary(xs, 1) == -1)
for (i, v) in enumerate(xs):
    test(search_binary(xs, v) == i)

def remove_adjacent_dups(xs):
    """ Return a list with adjecent duplicates removed,
        from a given sorted list. """
    new_list = []
    last_added = None
    for element in xs:
        if element != last_added:
            new_list.append(element)
            last_added = element 
    return new_list


test(remove_adjacent_dups([1,2,3,3,3,3,5,6,9,9]) == [1,2,3,5,6,9])
test(remove_adjacent_dups([]) == [])
test(remove_adjacent_dups(["a", "big", "big", "bite", "dog"]) ==
                                   ["a", "big", "bite", "dog"])

all_words = get_words_in_book("AliceInWonderland.txt")
all_words.sort()
book_words = remove_adjacent_dups(all_words)
#print("There are {0} words in the book. Only {1} are unique.".\
#        format(len(all_words), len(book_words)))
#print("The first 100 words are\n{0}".format(book_words[:100]))

def merge(xxs, yyx):
    pass

xs = [1,3,5,7,9,11,13,15,17,19]
ys = [4,8,12,16,20,24]
zs = xs+ys
zs.sort()

def merge(xs, ys):
    """merge sorted lists xs and ys. Return a sorted result """
    result = []
    xi = 0
    yi = 0

    while True:
        if xi >= len(xs):
            result.extend(ys[yi:])
            return result

        if yi >= len(ys):
            result.extend(xs[xi:])
            return result

        if xs[xi] <= ys[yi]:
            result.append(xs[xi])
            xi += 1
        else:
            result.append(ys[yi])
            yi += 1

test(merge(xs, []) == xs)
test(merge([], ys) == ys)
test(merge([], []) == [])
test(merge(xs, ys) == zs)
test(merge([1,2,3], [3,4,5]) == [1,2,3,3,4,5])
test(merge(["a", "big", "cat"], ["big", "bite", "dog"]) ==\
        ["a", "big", "big", "bite", "cat", "dog"])

def merge_present_both(xs,ys):
    """merge sorted lists xs and ys. Return only those that are present in both lists. """
    result = []
    xi = 0
    yi = 0
    while True:
        if xi >= len(xs):
            return result
        if yi >= len(ys):
            return result

        if xs[xi] == ys[yi]:    # both smallest items are eqaul, which means they exist on both lists.
            result.append(xs[xi])
            xi += 1
        elif xs[xi] < ys[yi]:   # keep increasing smallets item on either list, `till items are equal.
            xi += 1
        elif ys[yi] < xs[xi]:
            yi += 1

test(merge_present_both([1,2,3,5],[1,2,4,6]) == [1,2])
test(merge_present_both([1,2,3,5,6,7,8,9], [1,2,4,7,9]) == [1,2,7,9])
test(merge_present_both([xs], []) == [])
test(merge_present_both([], ys) == [])
test(merge_present_both(["a", "big", "cat"], ["big", "bite", "dog"]) ==\
        ["big"])

def merge_present_first(xs, ys):
    """Return only those items that are present in the first list, but not in the second."""
    result = []
    xi = 0
    yi = 0

    while True:
        if xi >= len(xs):
            return result   # firts list has finished, the are no more items to add to results.

        if yi >= len(ys):
            result.extend(xs[xi:])  # second list has finished, all reamaing items on the first list exist only on first list.
            return result

        if xs[xi] < ys[yi]:     # if 1st smallest item from the 1st list is smaller than the smallest item from the 2nd list.
            result.append(xs[xi])   # That means it exists only on the first list.
            xi += 1
        elif xs[xi] == ys[yi]:  # both items are eqaul, keep going
            xi += 1
            yi += 1
        else:   # xs[xi] > ys[yi]
            yi += 1

test(merge_present_first([1,2,3,5,6],[1,2,7,8,9]) == [3,5,6])
test(merge_present_first(xs, []) == xs)
test(merge_present_first([],ys) == [])
test(merge_present_first(["a", "big", "cat"], ["big", "bite", "dog"]) ==\
        ["a", "cat"])

def merge_present_second(xs,ys):
    """Return only those items that are present only in the second list, but not in the first."""
    result = []
    xi = 0
    yi = 0

    while True:
        if xi >= len(xs):   # 1st list has finished, all remaining items from the 2nd list exist only on the 2nd list.
            result.extend(ys[yi:])
            return result

        if yi >= len(ys):   # 2nd list has finished, there are no more items to add to the result.
            return result

        if xs[xi] > ys[yi]:     # The smallest item from the 2nd list is smaller than the smallest item from the 1st list
            result.append(ys[yi])   # That means in exist only on the 2nd list.
            yi += 1
        elif xs[xi] == ys[yi]:  # both iteams are equalt, they are on both lists, keep going.
            xi += 1
            yi += 1
        else:   # xs[xi] < ys[yi]
            xi += 1

    test(merge_present_second([1,2,3,5,6],[1,2,7,8,9]) == [7,8,9])
test(merge_present_second(xs, []) == [])
test(merge_present_second([],ys) == ys)
test(merge_present_second(["a", "big", "cat"], ["big", "bite", "dog"]) ==\
        ["bite", "dog"])

def merge_present_either(xs, ys):
    """Return items that are present in either the first or the second list."""
    result = []
    xi = 0
    yi = 0

    while True:
        if xi >= len(xs):
            result.extend(ys[yi:])
            return result
        if yi >= len(ys):
            result.extend(xs[xi:])
            return result
        # Any non equality means that items are on either lists.
        if xs[xi] < ys[yi]:
            result.append(xs[xi])
            xi += 1
        elif xs[xi] > ys[yi]:
            result.append(ys[yi])
            yi += 1
        else:   # xs[xi] == ys[yi] - both items are on both list
            yi += 1
            xi += 1


test(merge_present_either([1,2,3],[2,3,4]) == [1,4])
test(merge_present_either([1,2,3,4,5],[3,4,5,6,7,8,9]) == [1,2,6,7,8,9])
test(merge_present_either(xs,[]) == xs)
test(merge_present_either([], ys) == ys)
test(merge_present_either(["a", "big", "cat"], ["big", "bite", "dog"]) ==\
        ["a", "bite", "cat", "dog"])

def bagdiff(xs, ys):
    """Return items from the first list, that are not eliminated by a matching items in the second list."""
    result = []
    xi = 0
    yi = 0

    while True:
        if xi >= len(xs):
            return result
        if yi >= len(ys):
            result.extend(xs[xi:])
            return result

        if xs[xi] == ys[yi]:    # Bypass/eliminate every occurence of items existing on both lists.
            xi += 1
            yi += 1
        elif xs[xi] < ys[yi]:
            result.append(xs[xi])
            xi += 1
        else:   # xs[xi] > ys[yi]
            yi += 1


test(bagdiff([5,7,11,11,11,12,13], [7,8,11]) == [5,11,11,12,13])

def find_unknowns_merge_pattern(vocab, wds):
    """ Both the vocab and wds must be sorted. Return a new
        list of words from wds that do not occur in vocab.
    """

    result = []
    xi = 0 
    yi = 0

    while True:
        if xi >= len(vocab):
            result.extend(wds[yi:])
            return result

        if yi >= len(wds):
            return result

        if vocab[xi] == wds[yi]:
            yi += 1

        elif vocab[xi] < wds[yi]:
            xi += 1

        else: # vocab[xi] > wds[yi]
            result.append(wds[yi])
            yi += 1

all_words = get_words_in_book("AliceInWonderland.txt")
t0 = time.clock()
all_words.sort()
book_words = remove_adjacent_dups(all_words)
missing_words = find_unknowns_merge_pattern(bigger_vocab, book_words)
t1 = time.clock()
print("There are {0} unknown words.".format(len(missing_words)))
print("That took {0:.4f} seconds.".format(t1-t0))

def share_diagonal(x0, y0, x1, y1):
    """ Is (x0, y0) on shared diagonal with (x1, y1)? """
    dy = abs(y1 - y0)       # Calc the absolute y distance
    dx = abs(x1 - x0)       # Calc the absolute x distance
    return dx == dy         # They clash if dx == dy


test(not share_diagonal(5,2,2,0))
test(share_diagonal(5,2,3,0))
test(share_diagonal(5,2,4,3))
test(share_diagonal(5,2,4,1))
test(not share_diagonal(2,7,4,6))
test(share_diagonal(2,7,3,6))


def col_clashes(bs, c):
    """ Return True if the queen at column c clashes
        with any queen to its left. 
    """
    for i in range(c):  # Look at all columns to the left of c
        if share_diagonal(i, bs[i], c, bs[c]):
            return True

    return False        # No clashes - col c has a safe placement.

# Solutions cases that should not have any clashes
test(not col_clashes([6,4,2,0,5], 4))
test(not col_clashes([6,4,2,0,5,7,1,3], 7))



# More test cases that should mostly clash
test(col_clashes([0,1], 1))
test(col_clashes([5,6], 1))
test(col_clashes([6,5], 1))
test(col_clashes([0,6,4,3], 3))
test(col_clashes([5,0,7], 2))
test(not col_clashes([2,0,1,3], 1))
test(col_clashes([2,0,1,3], 2))

def has_clashes(the_board):
    """ Determine whether we have any queens clashing on the diagonals.
        We're assuming here that the board is a permutation of column
        numbers, so we're not explicitly checking row or column clashes.
    """
    for col in range(1, len(the_board)):
        if col_clashes(the_board, col):
            return True
    return False

test(not has_clashes([6,4,2,0,5,7,1,3]))
test(has_clashes([4,6,2,0,5,7,1,3]))
test(has_clashes([0,1,2,3]))
test(not has_clashes([2,0,3,1]))


def eight_queens():
    rng = random.Random()

    bd = list(range(8))
    unique_boards = []
    sym_boards = []
    num_found = 0
    tries = 0
    t0 = time.clock()
    while num_found < 12:
        rng.shuffle(bd)
        tries += 1
        #if bd in good_boards:
            #print("Repetition")
        if not has_clashes(bd) and bd not in sym_boards:
            draw_queens.draw_board(bd)
            unique_boards.append(bd[:])
            sym_boards.extend(symetric_board(bd))
            print("Symytric boards: ")
            print(sym_boards)
            #t1 = time.clock()
            #print("Found solution {0} in {1} tries.".format(bd, tries))
            #print("It took {0} seconds.".format(t1-t0))
            print(bd)
            #t0 = time.clock()
            tries = 0
            num_found += 1
eight_queens()

def invert_board_x(bd):
    inv_bd = []
    max_col = len(bd)-1
    for col in range(len(bd)):
        inv_bd.append(max_col-bd[col])
    return inv_bd

test(invert_board_x([5,3,0,4,7,1,6,2]) == [2,4,7,3,0,6,1,5])
test(invert_board_x([2,4,7,3,0,6,1,5]) == [5,3,0,4,7,1,6,2])

def invert_board_y(bd):
    inv_bd = []
    for col in range(len(bd)-1,-1,-1):
        inv_bd.append(bd[col])

    return inv_bd

test(invert_board_y([5,3,0,4,7,1,6,2]) == [2,6,1,7,4,0,3,5])
test(invert_board_y([2,6,1,7,4,0,3,5]) == [5,3,0,4,7,1,6,2])


def invert_board_antcl(bd, n):
    """ Returns rotated board anticlockwise by 90 degree n times. """
    board = bd[:]
    rot_board = bd[:]
    max_col = len(board)-1
    rotates = 0
    while rotates < n:
        for indx,col in enumerate(board):
            rot_board[col] = max_col-indx
        rotates += 1
        board = rot_board[:]

    return rot_board

test(invert_board_antcl([5,3,0,4,7,1,6,2],0) == [5,3,0,4,7,1,6,2])
test(invert_board_antcl([5,3,0,4,7,1,6,2],1) == [5,2,0,6,4,7,1,3])

def symetric_board(bd):
    """ Return whole family of symetric boards for the given boards. """
    boards = []
    for i in range(4):
        rot_board = invert_board_antcl(bd,i)
        boards.append(rot_board)
        boards.append(invert_board_y(rot_board))

    return boards

#eight_queens()

my_tickets = [ [ 7, 17, 37, 19, 23, 43],
               [ 7,  2, 13, 41, 31, 43],
               [ 2,  5,  7, 11, 13, 17],
               [13, 17, 37, 19, 23, 43] ]

def lotto_draw():
    """ Return 6 random lotto numbers for range 1-49. """
    balls = list(range(1,50))
    random.shuffle(balls)
    draw = balls[:7]
    return draw

print(lotto_draw())

def lotto_match(draw_list, ticket_list):
    """ Return number of hits of numbers from lotto ticket against draft numbers. """
    tick_sorted = ticket_list[:]
    draw_sorted = draw_list[:]
    tick_sorted.sort()
    draw_sorted.sort()
    hits = 0
    di = 0
    ti = 0

    while True:
        if di >= len(draw_sorted) or ti >= len(tick_sorted):
            return hits

        if draw_sorted[di] == tick_sorted[ti]:
            hits += 1
            di += 1
            ti += 1

        elif draw_sorted[di] < tick_sorted[ti]:
            di += 1
        else: # draw_sorted[di] > tick_sorted[ti]
            ti += 1

def lotto_matches(draw, tickets):
    """ Return list of numbers of hits on each ticket on the given list of tickets. """
    hits_list = []
    for ticket in tickets:
        hits_list.append(lotto_match(draw, ticket))
    return hits_list

test(lotto_matches([42,4,7,11,1,13], my_tickets) == [1,2,3,1])
test(lotto_match([42,4,7,11,1,13], [2,5,7,11,13,17]) == 3)

def is_prime(n):
    """ Return True if given integer is prime. """
    if n == 1: return False
    for i in range(2,n):
        if n%i == 0:
            return False
    return True


def primes_in(numbers):
    """ Return number of primes in the given list. """
    primes = 0
    for n in numbers:
        if is_prime(n): primes += 1
    return primes

test(primes_in([42,4,7,11,1,13]) == 3)

def list_primes(n):
    """ Return list of prime numbers up to n(including). """
    primes = []
    for i in range(2,n+1):
        if is_prime(i): primes.append(i)
    return primes

def prime_misses(tickets):
    """ Return prime numbers not included in lotto tickets(range 1-49). """
    primes = list_primes(49)    # create a list of prime numbers 2-47
    primes_listed = []
    missed = []

    for ticket in tickets:
        primes_listed.extend(ticket)    # merge all tickets into one list

    primes_listed.sort()
    primes_listed = remove_adjacent_dups(primes_listed) # remove duplicates
    missed = merge_present_second(primes_listed, primes) # list all items from primes list missing in primes_listed
    return missed

test(prime_misses(my_tickets) == [3, 29, 47])

def multi_lotto(n):
    tries = 0
    while True:
        tries += 1
        hits = lotto_matches(lotto_draw(), my_tickets)
        if n in hits:
            return tries

def average_drafts(n):
    sum = 0
    print("Progres:")
    for i in range(20):
        print(".")
        sum += multi_lotto(n)
    print()
    return sum/20
#a = average_drafts(6)
#print("On average it takes {} drafts to get {} hits on any of four coupons.".format(a,5))
