#ejercicio 2
import math
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def invert_coordinates(self):
        if isinstance(self.x,int) and isinstance(self.y, int):
            self.x, self.y = self.y, self.x
    def __str__(self):
        return f"{self.x} - {self.y}"
    
    def distance_to(self):
        return math.sqrt((coord[0]-self.x)**2-(coord[1]-self.y))**2