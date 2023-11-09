#ejercicio 2
import math

class Point:
    def __init__(self, x: int, y: int):
        self.x =x
        self.y = y
    @property
    def x(self):
        return self.__x
    @x.setter
    def x(self,value):
        self.__x = value
    
    @property
    def y(self):
        return self.__y
    @y.setter
    def y(self,value):
        self.__y = value

    def invert_coordinates(self):
        self.__x,self.__y = self.__y,self.__x
       
    def __str__(self):
        return f"({self.x}, {self.y})"
    
    def distance_to(self, value):
        return math.sqrt((self.__x - value.x)**2 + (self.__y - value.y)**2)