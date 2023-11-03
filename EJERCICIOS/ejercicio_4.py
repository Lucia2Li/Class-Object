#Implement a class Dice. By default, the die will have 6 faces.
import random

class Dice:
    def __init__(self, faces = 6, number = 0):
        self.__faces = faces
        if number == 0:
            self.__number = random.randint(1,self.__number)
        else:
            self.__number = number
        
        @num.setter
        def num(self,value):
            return self.__number == value
        @property
        def get_number(self):
            return self.__number
        @face.setter
        def face(self, value):
            return f"El número de encima es {value} y el número de caras es {self.__faces} "






