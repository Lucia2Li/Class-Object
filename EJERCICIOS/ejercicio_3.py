from ejercicio_2 import Point

class Rectangle:
    def __init__(self, p1, p2):
        self.__p1 = p1
        self.__p2 = p2
        self.area = 0
        self.perimeter = 0
    @property
    def get_area(self):
        return self.__area
    
    @area.setter
    def area(self):
        ((self.__p1.x-self.__p2.x)*(self.__p1.y-self.__p2.y))

    @property
    def get_perimeter(self):
        return self.__perimeter

    @perimeter.setter
    def perimeter(self):
        2 * ((self.__p1.x-self.__2.x) + (self.__p1.y-self.__p2.y))

    def __str__(self):
        return f"({self.__p1}, {self.__p2})"

    

    
    
    
    

