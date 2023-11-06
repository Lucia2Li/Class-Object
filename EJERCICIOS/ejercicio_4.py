#Implement a class Dice. By default, the die will have 6 faces.
import random

class Dice:
    def __init__(self, faces = 6, number = 0):
        self.__faces = faces
        if number == 0:
            self.__number = random.randint(1,self.__faces)
        else:
            self.__number = number
    @property
    def number(self):
        return self.__number
    @number.setter
    def number(self,value):
        self.__number = value
    @property
    def face(self):
        return self.__faces
    @face.setter
    def face(self,value):
        self.__faces = value
        
    def __repr__(self):
        return f"El número es {self.__number} y el número de caras del dado es: {self.__faces}"
    def roll (self):
        self.__number = random.randint(1,self.__faces)
