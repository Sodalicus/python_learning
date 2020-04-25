#!/usr/bin/env python
# Chapter 9, Excercise 2. Simple card war game, each player recives one card, the one with the highet card wins.
# When both cards rank match, we check for the higher suit. Diamonds > Clubs > Hearts > Spades.

class Card():
    RANKS = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A')
    SUITS = ('s', 'h', 'c', 'd')

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        rep = self.rank + self.suit
        return rep

    def value(self):
        if self.rank and self.suit:
            r = Card.RANKS.index(self.rank)+2
            s = Card.SUITS.index(self.suit)+1
        return (r, s)

class Hand(): 
    def __init__(self):
        self.cards = []

    def __str__(self):
        rep = ''
        if self.cards:
            for card in self.cards:
                rep +=str(card)+'\t'
            rep += '\n'
            rep += 'Number of cards: '+str(len(self.cards))+'\n'
        return rep

    def add_card(self, card):
        self.cards.append(card)

    def give_card(self, hand):
        if self.cards:
            topCard = self.cards[0]
            hand.add_card(topCard)
            self.cards.remove(topCard)

    def top_card_value(self):
        if self.cards:
            v = self.cards[0].value()
        else:
            v = (0,0)
        return v

class Deck(Hand):
    def populate(self):
        for rank in Card.RANKS:
            for suit in Card.SUITS:
                self.cards.append(Card(rank, suit))

    def shuffle(self):
        import random
        random.shuffle(self.cards)

    def deal(self, hands, numberOfCards=1):
        for rounds in range(numberOfCards):
            if self.cards:
                for hand in hands:
                    self.give_card(hand)
            else:
                print("Out of cards to deal,")

class Player(Hand):
    def __init__(self, name):
        super(Player, self).__init__()
        self.name = name
        self.score = 0

    def player_name(self):
        if self.name:
            return self.name
        else:
            return str('<No name given>')

class WarGame():
    def __init__(self):
        self.players = []

    def create_deck(self):
        self.deck = Deck()
        self.deck.populate()
        self.deck.shuffle()
        
    def create_players(self):
        warplayer = ''
        playersNumber = 2
        while playersNumber not in range(1, 4):
            playersNumber = int(input('Podaj liczbę graczy(1-4): '))
        print(playersNumber)

        for i in range(playersNumber): 
            warplayer = input("Enter player {} name: ".format(i+1))
            if warplayer:
                self.players.append(Player(warplayer))

    def winner_check(self):
        self.win_player_index = None
        self.uttermost_card_val = (0,0)

        for player in self.players:
            if player.top_card_value()[0] > self.uttermost_card_val[0]: #if current player's card's rank is higher than the uttermost card's rank
                self.uttermost_card_val = player.top_card_value()
                self.win_player_index = self.players.index(player)
            elif player.top_card_value()[0] == self.uttermost_card_val[0]: # if current player's card rank is the same as the highest card, check for highest suit
                if player.top_card_value()[1] > self.players[self.win_player_index].top_card_value()[1]:
                    self.uttermost_card_val = player.top_card_value()
                    self.win_player_index = self.players.index(player)
        return self.win_player_index



    def show_players(self):
        for player in self.players:
            print()
            print("Player: "+player.player_name()+" has: "+str(player))

    def game(self):
        self.deck.deal(self.players)
        self.show_players()
        self.winner = self.players[self.winner_check()].player_name()
        print("Player {} has won".format(self.winner))
        for player in self.players:
            player.give_card(self.deck)

    def main(self):
        self.create_deck()
        self.create_players()
        i = 0
        while i < 11:
            print(20*'*')
            print("Game", i)
            self.game()
            i+=1


wg = WarGame()
wg.main()
