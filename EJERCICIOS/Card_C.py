import random

#Creating classes

#Card to simulate a playing card. A playing card has a suit (from a set of suits) and a 
# value (from a set of values).



class Card:
    def __init__(self, suit, value):#Initialize the attributes for the suit and value of the card.
        self.suit = suit
        self.value = value
#Suit
    @property
    def suit(self):
        return self.__suit
    @suit.setter
    def suit(self, s):
        self.__suit = s
#Value    
    @property
    def value(self):
        return self.__value
    @value.setter
    def value(self,v):
        self.__value = v

    def get_numeric_value(self):
        if self.value in ["J", "Q", "K"]:
            return 10
        elif self.value == "A":
            return 11
        else:
            return int(self.value)
            

    
#Hand to simulate card-player hand, i.e., a set of playing cards that a player has. Players
# can draw a card from a deck. Once drawn, the player has one more card, and the deck
# has one less. They can discard a card. They can receive cards

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

    def add_card(self,s,v): 
        self.cards.append(Card(s,v))
    
    def total_value(self):
        total_value = 0
        num_aces = 0
        for card in self.cards:
            total_value += card.get_numeric_value()
            
            if card.value == "A":
                num_aces += 1

        while total_value > 21 and num_aces:
            total_value -= 10  # Tratar un As como 1 en lugar de 11
            num_aces -= 1

        return total_value, num_aces


#Deck to simulate a deck of playing cards. Initially, it contains the cards that are provided
# with the constructor. It can deal a set of cards to a player. Those cards are removed from
# the deck. The first card can be taken from it (draw). It can be shuffled.

class Deck:
    def __init__(self, suits, values):  
        self.deck = []#Initialize an empty deck of cards
        for suit in suits:
            for value in values:
                self.deck.append(Card(suit,value))

    @property
    def deck(self):
        return self.__deck
    @deck.setter
    def deck(self, card):
        self.__deck = card
    
    def draw_card(self):
        self.deck.pop(0)

    def shuffle(self):  #Implement the method to shuffle the deck.
        random.shuffle(self.deck)
    

       