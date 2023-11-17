#Implement a class Dice. By default, the die will have 6 faces.
import random
class Dice:
    def __init__(self, faces = 6, number = 0):
        self.faces = faces
        self.number = number
    @property
    def faces(self):
        return self.__faces
    @faces.setter
    def faces(self,value):
        self.__faces = value
    @property
    def number(self):
        return self.__number
    @number.setter
    def number(self,other_number):
        if other_number == 0:
            self.__number = random.randint(1,self.__faces)
        else:
            self.__number = other_number
    def __repr__(self):
        return f"El número es {self.number} y el número de caras del dado es: {self.faces}"
    
    def roll (self):
        self.number = random.randint(1,self.faces)
        
d1 = Dice()
print(d1)
