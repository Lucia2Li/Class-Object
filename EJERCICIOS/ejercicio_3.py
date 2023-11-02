from ejercicio_2 import Point

class Rectangle:
    def __init__(self, p1, p2):
        self.__p1 = p1
        self.__p2 = p2

    def __str__(self):
        return f"({self.__p1}, {self.__p2})"
    @property
    def area(self,p1,p2):
        return ((self.__p1.x-p2.x)*(self.__p1.y-p2.y))
    @property
    def perimeter(self,p1,p2):
        return 2 * ((self.__p1.x-p2.x) + (self.__p1.y-p2.y))
