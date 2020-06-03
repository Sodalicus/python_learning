#!/usr/bin/env python

# Your friend will complete this function
human = 0
draw = 0
computer = 0
turn = None

def play_once(human_plays_first):
    """
    Must play one round of the game. If the parameter
    is True, the human gets to play first, else the
    computer gets to play first. When the round ends,
    the return value of the function is one of
    -1 (human wins), 0 (game drawn),
    1 (computer wins).
    """
    # This is all dummy scaffolding code right at the moment...
    import random
    # See Modules chapter ...
    rng = random.Random()
    # Pick a random result between -1 and 1.
    result = rng.randrange(-1,2)
    print("Human plays first={0}, winner={1} "
    .format(human_plays_first, result))
    return result

def yesno_question(question):
    result = None
    while result not in ("y","n"):
        result = input(question).lower()
    result=result.lower()
    if result == "y": return True
    elif result == "n": return False

def winner(result):
    global human
    global draw
    global computer
    if result == -1:
        human += 1
        print("You win")
    elif result == 0:
        draw += 1
        print("Draw")
    elif result == 1:
        computer += 1
        print("I win")
    print("Human won {} times, Computer won {} times, there was a draw {} times.".format(human, computer, draw))
    print("Human won: {}% of times".format(round((human/(human+draw+computer))*100)))

def turn():
    global turn
    if turn:
        turn = False
        return False
    elif not turn:
        turn = True
        return True


def main():
    winner(play_once(yesno_question("Do you want to play first?")))
    choice = None
    while choice != False:
        choice = yesno_question("Do you want to play again?")
        if choice:
            winner(play_once(yesno_question("Do you want to play first?")))
    print("Goodbue.")

main()
