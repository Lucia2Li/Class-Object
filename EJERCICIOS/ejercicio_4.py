#Implement a class Dice. By default, the die will have 6 faces.
import random



class Dice:
    def __init__(self, faces = 6, number_on_top = 0):
        self.__faces = faces
        if number_on_top == 0:
            self.__number_on_top = random.randint(1,self.__number_on_top)
        else:
            self.__number_on_top = number_on_top
        
        @num.setter
        def num(self,value):
            return self.__number_on_top = value
        @property
        def get_number_on_top(self):
            return self.__number_on_top
        @face.setter
        def face(self, value):
            return f"El número de encima es {value} y el número de caras es {self.__faces} "






