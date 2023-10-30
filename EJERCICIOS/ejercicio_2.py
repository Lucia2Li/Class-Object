#ejercicio 2
import math
class Point:
    def __init__(self, x: int, y: int):
        self.__x =x
        self.__y = y
    @property
    def x(self):
        return self.__x
    @x.setter
    def x(self,value):
        return self.__x = value
    
    @property
    def y(self):
        return self.__y
    @property
    def y(self):
        return self.__y = value

    def invert_coordinates(self):
        if isinstance(self.__x,int) and isinstance(self.__y, int):
            self.__x,self.__y = self.__y,self.__x
        else:
            raise TypeError(f"{self.__x} and {self.__y} are not instances of int")
    def __str__(self):
        return f"({self.x}, {self.y})"
    
    def distance_to(self, value):
        return math.sqrt((self.__x-value.x)**2 + (self.__y-value.y**2))
        