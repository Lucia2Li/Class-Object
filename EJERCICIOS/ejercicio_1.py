#ejercicio 1
import random
class Dice:
    def __init__(self):
        self.__sides = 6
    def roll(self):
        return random.randint(1,self.__sides) 