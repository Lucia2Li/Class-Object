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
        self.y = value

    def invert_coordinates(self):
        self.x,self.y = self.y,self.x
       #SETTER = GETTER
    def __str__(self):
        return f"({self.x}, {self.y})"
    
    def distance_to(self, other_point):
        return math.sqrt((self.x - other_point.x)**2 + (self.y - other_point.y)**2)
    #self.x getter