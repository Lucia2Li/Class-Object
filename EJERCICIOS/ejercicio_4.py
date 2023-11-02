#Implement a class Dice. By default, the die will have 6 faces.
import random

class Dice:
    def __init__(self, faces = 6, number = 0):
        self.__faces = faces
        self.__number = number
        self.__num = random.randint(1, 6)
    
    @property
    def get_number(self):
        return self.__number
    @property
    def get_faces(self):
        return self.__faces
    @face.setter
    def face(self, value):
        return self.__faces == value
    @number.setter
    def number(self, num):
        return self.__number ==  num
    



d1 = Dice()
print(d1)



