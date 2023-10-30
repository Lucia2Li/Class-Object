#Implement a class Dice. By default, the die will have 6 faces.
import random

class Dice:
    def __init__(self):
        self.__num = random.randint(1, 6)
        
    def __str__(self):
        return f"El número del dado es: {self.__num}"

    def top_face(self, value):
         return f"El número del dado es: {self.__num} y el top face es: {value}"


d1 = Dice()
print(d1)



