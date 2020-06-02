from testing import test
import string
#Chapter 12 Exercise 8

def cleanword(word):
    new_word = ""
    for ch in word:
        if ch not in string.punctuation:
            new_word += ch
    return new_word


test(cleanword("what?") == "what")
test(cleanword("'now!'") == "now")
test(cleanword("?+='w-o-r-d!,@$()'") ==  "word")

def has_dashdash(word):
    if "-" in word:
        return True
    else:
        return False

test(has_dashdash("distance--but"))
test(not has_dashdash("several"))
test(has_dashdash("spoke--"))
test(has_dashdash("distance--but"))
test(not has_dashdash("-yo-yo-"))

def extract_words(words):
    new_words = ""
    for ch in words:
        if ch not in string.punctuation:
            new_words += ch
        else:
            new_words += " "
    return new_words.lower().split()

test(extract_words("Now is the time!  'Now', is the time? Yes, now.") ==
      ['now','is','the','time','now','is','the','time','yes','now'])
test(extract_words("she tried to curtsey as she spoke--fancy") ==
      ['she','tried','to','curtsey','as','she','spoke','fancy'])

def wordcount(pattern, words):
    count = 0
    for word in words:
        if word == pattern:
            count += 1
    return count


test(wordcount("now", ["now","is","time","is","now","is","is"]) == 2)
test(wordcount("is", ["now","is","time","is","now","the","is"]) == 3)
test(wordcount("time", ["now","is","time","is","now","is","is"]) == 1)
test(wordcount("frog", ["now","is","time","is","now","is","is"]) == 0)

def wordset(words):
    new_words = []
    temp = words[:]
    temp.sort()
    for word in temp:
        if word not in new_words:
            new_words.append(word)
    return new_words

test(wordset(["now", "is", "time", "is", "now", "is", "is"]) ==
      ["is", "now", "time"])
test(wordset(["I", "a", "a", "is", "a", "is", "I", "am"]) ==
      ["I", "a", "am", "is"])
test(wordset(["or", "a", "am", "is", "are", "be", "but", "am"]) ==
      ["a", "am", "are", "be", "but", "is", "or"])

def longestword(words):
    longest = 0
    for word in words:
        if len(word) > longest:
            longest = len(word)
    return longest


test(longestword(["a", "apple", "pear", "grape"]) == 5)
test(longestword(["a", "am", "I", "be"]) == 2)
test(longestword(["this","supercalifragilisticexpialidocious"]) == 34)
test(longestword([ ]) == 0)
