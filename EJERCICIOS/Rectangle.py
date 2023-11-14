from Point import Point

class Rectangle:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.area = 0
        self.perimeter = 0

    @property
    def area(self):
        self.area = ((self.p1.x - self.p2.x) * (self.p1.y - self.p2.y))
        return self.area

    @property
    def perimeter(self):
        self.perimeter = 2 * ((self.p1.x - self.p2.x) + (self.p1.y - self.p2.y))
        return self.perimeter

    def __str__(self):
        return f"({self.p1}, {self.p2})"


    
    

