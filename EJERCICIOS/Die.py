"""Design in Python a class called Dice to simulate the behaviour of a standard six-sided
die, ensuring that each face has an equal probability of being rolled."""

import random

class Dice:
    def __init__(self):
        self.__faces = 6

    @property
    def faces(self):
        return self.__faces
    
    def roll(self):
        return random.randint(1,self.faces)
    