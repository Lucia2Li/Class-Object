import random

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    @property
    def suit(self):
        return self.__suit
    @suit.setter
    def suit(self, s):
        self.__suit = s
    
    @property
    def value(self):
        return self.__value
    @value.setter
    def value(self,v):
        self.__value = v
    
class Hand:
    def __init__(self):
        self.cards = []

    @property
    def cards(self):
        return self.__cards
    @cards.setter
    def cards(self,value):
        self.cards = value
    
    def recieve_card(self,card):
        self.cards.append(card)
    
    def discard_card(self,card):
        self.cards.remove(card)


class Deck:
    def __init__(self, suits, values):
        self.deck = []
        

    @property
    def deck(self):
        return self.__deck
    @deck.setter
    def deck(self, card):
        self.__deck = card
    
    def draw_card(self):
        self.deck.pop(0)

    def shuffle(self):
        random.shuffle(self.deck)
    
    def remove_cards(self, cards):
        for card in cards:
            if card in self.deck:
                self.deck.remove(card)
            else:
                raise ValueError("No card has been found")
    
    def deal(self, player,num):
        if len(self.deck) < num:
            return None
        else:
             card_deal = self.deck[:num]
             player.draw(card_deal)
             self.remove_cards(card_deal)
   
class Spanish_deck(Deck):
    suits = ["Oros","Copas","Bastos","Espadas"]
    values = ["A","2","3","4","5","6","7","8","9","10","11","12","13"]

    def __init__(self):
        super().__init__(Spanish_deck.suits, Spanish_deck.values)

    def __str__(self):
        return f"Baraja Española: {', '.join(map(str, self.deck))}"
    
class English_deck(Deck):
    suits = ["Clubs","Spades","Hearts","Diamonds"]
    values = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]

    def __init__(self):
        super().__init__(English_deck.suits, English_deck.values)
    
    def __str__(self):
        return f"English deck: {', '.join(map(str, self.deck))}"

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = Hand()
    @property
    def name(self):
        return self.__name.capitalize()
    @name.setter
    def name(self, player_name):
        if isinstance(str,player_name):
            self.__name = player_name
    