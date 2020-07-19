#!/usr/bin/env python3
#-*-coding:utf-8-*-

# Create a list that represnts a deck of playing cards,
# shuffle them and deal 5 cards showing their graphical representation.

# cards[0:13] - 2 - 10, Jack, Queen, King, Ace (Hearths)
# cards[13:27] - 2 - 10, Jack, Queen, King, Ace (Diamonds)
# cards[27:40] - 2 - 10, Jack, Queen, King, Ace (Clubs)
# cards[40:52] - 2 - 10, Jack, Queen, King, Ace (Spades)

# Each card is 81x117.

import pygame, random

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
CARD_WIDTH = 81
CARD_HEIGHT = 117
cards_image = pygame.image.load("cards.gif")

class Card:
    def __init__(self, img, posn, card_number):
        self.image = img
        self.card_number = card_number
        self.posn = (posn * (CARD_WIDTH+30))+30, SCREEN_HEIGHT//2
        self.row = (card_number // 13)    # Card color
        self.column = (card_number % 13)  # Card rank
        self.order = posn

    def __str__(self):
        info = "Card number: {}\n".format(self.card_number)
        info += "Position: {}\n".format(self.order)
        info += "(x,y) : {}\n".format(self.posn)
        info += "Column/rank: {}; row/color: {}\n".format(self.column, self.row)
        info += "Slice: {}\n".format((self.column * CARD_WIDTH, self.row * CARD_HEIGHT, CARD_WIDTH, CARD_HEIGHT))
        return info


    def draw(self, target_surface):
        card_slice = (self.column * CARD_WIDTH, self.row * CARD_HEIGHT, CARD_WIDTH, CARD_HEIGHT)
        target_surface.blit(self.image, self.posn, card_slice)

def pick_five():
    """ Returns a list of five integeres from range 0-51. """
    deck = list(range(51))
    random.shuffle(deck)
    return deck[0:5]

def shuffle_cards():
    """ Shuffle cards and create new hand of five. """
    hand = []
    cards_list = pick_five()
    for inx,value in enumerate(cards_list):
        hand.append(Card(cards_image, inx, value))
    return hand

def main():
    pygame.init()
    my_clock = pygame.time.Clock()
    surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    background_color = (0,100,0)
    alive = True
    hand = shuffle_cards()


    for card in hand:
        print(card)

    while alive:
        ev = pygame.event.poll()
        if ev.type == pygame.QUIT:
            alive = False
        if ev.type == pygame.KEYDOWN:
            key = ev.dict["key"]
            if key == 27:
                alive = False
            if key == ord("s"):
                hand = shuffle_cards()

        background = (0,0, SCREEN_WIDTH, SCREEN_HEIGHT)
        surface.fill(background_color, background)

        for card in hand:
            card.draw(surface)

        my_clock.tick(30)
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
