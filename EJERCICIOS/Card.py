import random
#Creación de clases
#1.  Card to simulate a playing card. A playing card has a suit (from a set of suits) and a
#value (from a set of values).

class Card:
    def __init__(self, suit, value):
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
        return f"{self.suit}, {self.value}"

#CLASS Hand

class Hand:
    def __init__(self):
        self.cards = []
    @property
    def cards(self):
        return self.__cards
    @cards.setter
    def cards(self,card):
        self.__cards = card

    def discard(self,card):
        self.cards.remove(card)
    
    def draw(self,card):
        self.cards.append(card)

#CLASS DECK
class Deck:
    def __init__(self,suits,values):
        self.deck = []
        for s in suits:
            for v in values:
                self.añadir(s,v)

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
    def hand_out(self):
        return self.deck.pop(0)

#Deal a set of cards to a player, those cards are removed from the deck.
    def deal(self,other_player,num):
        if len(self.deck) < num:
            return None
        card_deal = self.deck[:num]
        other_player.draw(card_deal)
        self.remove_cards(card_deal)
#draw
    def draw(self,cards):
        self.cards.extend(cards)
#añadir
    def añadir(self,s,v):
        self.deck.append(Card(s,v))

#remove cards
    def remove_cards(self,cards):
        for card in cards:
            if card in self.deck:
                self.deck.remove(card)

#hand.draw(deck.pop)/hand_out
#CLASS
class Spanish_deck(Deck):
    suits = ["Oros","Copas","Bastos","Espadas"]
    values = ["A","2","3","4","5","6","7","8","9","10","11","12","13"]
    
    def __init__(self):
        super().__init__(self.suits,self.values)

    def __rpr__(self):
        return f"Spanish Deck: {', '.join(map(str, self.deck))}"


class English_deck(Deck):
    suits = ["Clubs","Spades","Hearts","Diamonds"]
    values = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
    def __init__(self):
        super().__init__(self.suits,self.values)

    def __rpr__(self):
        return f"English Deck: {', '.join(map(str, self.deck))}"



