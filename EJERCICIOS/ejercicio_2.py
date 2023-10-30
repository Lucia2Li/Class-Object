#ejercicio 2
import math
class Point:
    def __init__(self, x: int, y: int):
        self.__x =x
        self.__y = y
    @property
    def x(self):
        if isinstance(self.__x, int):
            return self.__x
        else:
            raise TypeError(f"{self.__x} is not an instance of int")
    
    @property
    def y(self):
        if isinstance(self.__y, int):
            return self.__y
        else:
            raise TypeError(f"{self.__y} is not an instance of int")
       