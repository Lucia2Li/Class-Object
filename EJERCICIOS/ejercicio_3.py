from ejercicio_2 import Point

class Rectangle:
    def __init__(self, p1, p2):
        self.__p1 = p1
        self.__p2 = p2
        self.__area = 0
        self.__perimeter = 0

    @property
    def area(self):
        self.__area = abs((self.__p1.x - self.__p2.x) * (self.__p1.y - self.__p2.y))
        return self.__area

    @property
    def perimeter(self):
        self.__perimeter = 2 * ((self.__p1.x - self.__p2.x) + (self.__p1.y - self.__p2.y))
        return self.__perimeter

    def __str__(self):
        return f"({self.__p1}, {self.__p2})"


    
    

