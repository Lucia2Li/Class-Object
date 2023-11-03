#Implement a class Dice. By default, the die will have 6 faces.
import random



class Dice:
    def __init__(self, faces = 6, number = 0):
        self.__faces = faces
        self.__number = number

    
    @property
    def get_number(self):
        return self.__number
    @property
    def get_faces(self):
        return self.__faces
    @face.setter
    def face(self, value):
        return self.__faces == value
    @num.setter
    def num(self, numero):
         if self.__number == 0:
            return random.randint(1,self.number)
         else: 
             return self.__number == numero

    



d1 = Dice()
print(d1)



