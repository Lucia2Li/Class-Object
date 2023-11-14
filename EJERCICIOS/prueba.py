import random

class Dice:
    def __init__(self):
        self.__faces = 6

    @property
    def faces(self):
        return self.__faces
    
    def roll(self):
        return random.randint(1,self.faces)
    
die1 = Dice()
die2 = Dice()

for idx in range(5):
    roll1 = die1.roll()
    roll2 = die2.roll()
    print(f'Die1 = {roll1} and Die2 = {roll2}' )