from testing import test
import string
def myreplace(old, new, s):
    """ Replace all occurrences of old with new in s. """
    if old in string.whitespace:
        return new.join(s.split())
    else:
        return new.join(s.split(old))


test(myreplace(",", ";", "this, that, and some other thing") ==
                         "this; that; and some other thing")
test(myreplace(" ", "**",
                 "Words will now      be  separated by stars.") ==
                 "Words**will**now**be**separated**by**stars.")
