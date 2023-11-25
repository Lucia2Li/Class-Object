from Card import Card, Hand, Deck, English_deck, Spanish_deck
#Carta
c1 = Card("Palos",6)
print(c1)

s = Spanish_deck()
print(s)
print(s.hand_out())
print(s.hand_out())
print(s.shuffle())
print(s)


hand = Hand()
e = English_deck()
e.deal(hand, 5)
print(e.hand_out())
print(hand)