class Person:
    def __init__(self, name, id, age):
        self.name = name
        self.id = id
        self.age = age
    def copy(self):
        new = Person(self.name, self.id, self.age)
        return new
    
