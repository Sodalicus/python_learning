# Blackjack
# Od 1 do 7 graczy współzawodniczy z rozdającym

import karty, gry     

class BJ_Card(karty.Card):
    """ Karta do blackjacka. """
    ACE_VALUE = 1

    @property
    def value(self):
        if self.is_face_up:
            v = BJ_Card.RANKS.index(self.rank) + 1
            if v > 10:
                v = 10
        else:
            v = None
        return v

class BJ_Deck(karty.Deck):
    """ Talia kart do blackjacka. """
    def populate(self):
        for suit in BJ_Card.SUITS: 
            for rank in BJ_Card.RANKS: 
                self.cards.append(BJ_Card(rank, suit))


class BJ_Hand(karty.Hand):
    """ Ręka w blackjacku. """
    def __init__(self, name):
        super(BJ_Hand, self).__init__()
        self.name = name
        self._money = 2000
        self._bet = 0
        self.won = False
        self.draw = False

    def __str__(self):
        rep = self.name + ":\t" + super(BJ_Hand, self).__str__()  
        if self.total:
            rep += "(" + str(self.total) + ")"        
        return rep

    @property     
    def total(self):
        # jeśli karta w ręce ma wartość None, to i wartość sumy wynosi None
        for card in self.cards:
            if not card.value:
                return None
        
        # zsumuj wartości kart, traktuj każdego asa jako 1
        t = 0
        for card in self.cards:
              t += card.value

        # ustal, czy ręka zawiera asa
        contains_ace = False
        for card in self.cards:
            if card.value == BJ_Card.ACE_VALUE:
                contains_ace = True
                
        # jeśli ręka zawiera asa, a suma jest wystarczająco niska,
        # potraktuj asa jako 11
        if contains_ace and t <= 11:
            # dodaj tylko 10, ponieważ już dodaliśmy 1 za asa
            t += 10   
                
        return t

    def is_busted(self):
        return self.total > 21

    def no_money(self):
        return self._money <= 0

    def balance(self, action='check', amount=0):
        if action == 'check':
            return self._money
        elif action == 'add':
            self._money += amount
        elif action == 'substract':
            if amount <= self._money:
                self._money -= amount
        else:
            print('Nieznana opcja')

    def bet(self, action='check', amount=0):
        if action == 'check':
            return self._bet
        elif action == 'set':
            self._bet = amount
        elif action == 'clear':
            self._bet = 0
        else:
            print('Nieznana opcja')

class BJ_Player(BJ_Hand):
    """ Gracz w blackjacku. """
    def is_hitting(self):
        response = gry.ask_yes_no("\n" + self.name + ", chcesz dobrać kartę? (T/N): ")
        return response == "t"

    def bust(self):
        print(self.name, "ma furę.")
        self.lose()

    def lose(self):
        print(self.name, "przegrywa.")
        self.won = False

    def win(self):
        print(self.name, "wygrywa.")
        self.won = True

    def push(self):
        print(self.name, "remisuje.")
        self.draw = True

    def bankrupt(self):
        print(self.name, "bankrutuje.")

        
class BJ_Dealer(BJ_Hand):
    """ Rozdający w blackjacku. """
    def is_hitting(self):
        return self.total < 17

    def bust(self):
        print(self.name, "ma furę.")

    def flip_first_card(self):
        first_card = self.cards[0]
        first_card.flip()


class BJ_Game(object):
    """ Gra w blackjacka. """
    def __init__(self, names):      
        self.players = []
        for name in names:
            player = BJ_Player(name)
            self.players.append(player)

        self.dealer = BJ_Dealer("Rozdający")

        self.deck = BJ_Deck()
        self.deck.populate()
        self.deck.shuffle()

    @property
    def still_playing(self):
        sp = []
        for player in self.players:
            if not player.is_busted():
                sp.append(player)
        return sp

    def __additional_cards(self, player):
        while not player.is_busted() and player.is_hitting():
            self.deck.deal([player])
            print(player)
            if player.is_busted():
                player.bust()
    
    def make_bet(self, player):
        if not player.bet():
           to_bet = gry.ask_number("{} ile chcesz postawić(Posiadasz {} żetonów): ".format(player.name, player.balance()), 1, player.balance()+1)
           player.bet(action='set', amount=to_bet)

    def pay_bet(self, player, result):
        if result == 'lost':
            player.balance(action='substract', amount=player.bet())
            print('{} płaci {} krupierowi'.format(player.name, player.bet()))
            player.bet(action='clear')
        elif result == 'won':
            player.balance(action='add', amount=player.bet()*2)
            print('Krupier płaci {} graczowi {}'.format(player.bet()*2, player.name))
            player.bet(action='clear')
        elif result == 'draw':
            player.balance(action='substract', amount=int(player.bet()/2))
            print('{} płaci {} krupierowi'.format(player.name, int(player.bet()/2)))
            player.bet(action='clear')
        
    def play(self):
        # sprawdź czy w talii znajduje się dość kart, jeżeli nie, to wydaj nową talię.
        if self.deck.card_count() < 52:
            print("W talli znajduje się {} kart.\n".format(self.deck.card_count()))
            self.deck.clear()
            self.deck.populate()
            self.deck.shuffle()
            print("W talli znajduje się {} kart.\n".format(self.deck.card_count()))
            
        # rozdaj każdemu początkowe dwie karty
        self.deck.deal(self.players + [self.dealer], per_hand = 2)
        self.dealer.flip_first_card()    # ukryj pierwszą kartę rozdającego
        for player in self.players:
            print(player)
        print(self.dealer)
        # spytaj kazdego gracza, ile chce postawic
        for player in self.players:
            self.make_bet(player)

        # rozdaj graczom dodatkowe karty
        for player in self.players:
            self.__additional_cards(player)

        self.dealer.flip_first_card()    # odsłoń pierwszą kartę rozdającego 

        if not self.still_playing:
            # ponieważ wszyscy gracze dostali furę, pokaż tylko rękę rozdającego
            print(self.dealer)
        else:
            # daj dodatkowe karty rozdającemu
            print(self.dealer)
            self.__additional_cards(self.dealer)

            if self.dealer.is_busted():
                # wygrywa każdy, kto jeszcze pozostaje w grze
                for player in self.still_playing:
                    player.win()                    
            else:
                # porównaj punkty każdego gracza pozostającego w grze z punktami rozdającego
                for player in self.still_playing:
                    if player.total > self.dealer.total:
                        player.win()
                    elif player.total < self.dealer.total:
                        player.lose()
                    else:
                        player.push()

        for player in self.players:
            if player.won == True:
                self.pay_bet(player, 'won')
                player.won = False
            elif player.won == False and player.draw == False:
                self.pay_bet(player, 'lost')
            elif player.won == False and player.draw == True:
                self.pay_bet(player, 'draw')
                player.draw = False

        # usuń karty wszystkich graczy
        for player in self.players:
            player.clear()
        self.dealer.clear()

    def is_bankrupt(self):
        for player in self.players:
            if player.no_money():
                self.players.remove(player)
                print(player.name, 'zbankrutował i opuszcza stolik.')
                player.bankrupt()


        

def main():
    print("\t\tWitaj w grze 'Blackjack'!\n")
    
    names = []
    number = gry.ask_number("Podaj liczbę graczy (1 - 7): ", low = 1, high = 8)
    for i in range(number):
        name = input("Wprowadź nazwę gracza: ")
        names.append(name)
    print()
        
    game = BJ_Game(names)

    again = None
    while again != "n":
        game.is_bankrupt()
        game.play()
        again = gry.ask_yes_no("\nCzy chcesz zagrać ponownie?: ")


main()
input("\n\nAby zakończyć program, naciśnij klawisz Enter.")



