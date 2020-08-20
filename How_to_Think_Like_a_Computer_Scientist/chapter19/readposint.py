#!/usr/bin/env python3

def readposint():
    """ prompt for positive integer, handle negative integers, values       that cannot be converted to ints, or empty values. """
    meets_req = False
    inint = None
    while meets_req == False:
        inint = input("Type positive intger: ")

        try:
            inint = int(inint)
            if inint <= 0 or inint == None:
                raise ValueError("Must be Positive.")
            meets_req = True

        except:
            print("Must be positive integer, not a string, or empty.")
    print()
    print(inint)


readposint()



