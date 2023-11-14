from Point import Point

class Rectangle:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    @property
    def area(self):
        return abs((self.p1.x - self.p2.x) * (self.p1.y - self.p2.y))


    @property
    def perimeter(self):
        return 2 * (abs(self.p1.x - self.p2.x) + abs(self.p1.y - self.p2.y))

    def __str__(self):
        return f"({self.p1}, {self.p2})"


    
    

