import random
#Creación de clases
#1.  Card to simulate a playing card. A playing card has a suit (from a set of suits) and a
#value (from a set of values).
class Card:
    def __init_(self, suit, value):
        self.suit = suit
        self.value = value
#Suit
    @property
    def suit(self):
        return self.__suit
    @suit.setter 
    def suit(self,value):
        self.__suit = value
#Value
    @property
    def value(self):
        return self.__value
    @value.setter
    def value(self,value):
        self.__value = value
    
    def __str__(self):
        return f"{self.card}-{self.value}"
    
#Class Hand
    class Hand:
        def __init__(self):
            self.set_card = []  #vacio...
        @property
        def set_card(self):
            return self.__set_card
        @set_card.setter
        def set_card(self,cards):
            self.__set_cards = cards

#Decartar una carta
        def discard(self,card):
            self.remove(card)

    class Deck:
        def __init__(self):
            self.deck = []

        @property
        def deck(self):
            return self.__deck
        @deck.setter
        def deck(self,cards):
            self.__deck = cards
        

#Método shuffle: baraja una lista  
        def shuffle(self):
            random.shuffle(self.deck)
#Método draw: the first card can be taken from the deck
        def draw(self):
            self.deck.pop(0)

#Deal a set of cards to a player, those cards are removed from the deck.
        def deal(self,other_player):
            return "Hola"
#remove cards
        def remove(self,card):
            self.deck.remove(card)




#hand.draw(deck.pop)

