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
            self.set_card = []
        @property
        def set_card(self):
            return self.__set_card
        @set_card.setter
        def set_card(self,cards):
            self.__set_cards = cards
#Recibir una carta
        def receive(self,card):
            self.__set_card.append(card)

#Robar una carta de una baraja
        def draw(self,deck):
            card = deck.draw()
            self.receive(card)
            


