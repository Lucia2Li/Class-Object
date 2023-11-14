class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
    @property
    def x(self):
        return self.__x
    @x.setter
    def x(self,value):
        if isinstance(value,int):
            self.x = value
    @property
    def y(self):
        return self.__y
    @y.setter
    def y(self,value):
        if isinstance(value,int):
            self.y = value
    
