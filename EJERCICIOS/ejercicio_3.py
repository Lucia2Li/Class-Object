from ejercicio_2 import Point

class Rectangle:
    def __init__(self, p1, p2,area, perimeter):
        self.__p1 = p1
        self.__p2 = p2
        self.__area = 0
        self.__perimeter = 0

    def __str__(self):
        return f"({self.__p1}, {self.__p2})"
    @property
    def area(self,other_point):
        return ((self.__p1.x-other_point.x)*(self.__p1.y-other_point.y))
    @property
    def perimeter(self,other_point):
        return 2 * ((self.__p1.x-other_point.x) + (self.__p1.y-other_point.y))
    
    

