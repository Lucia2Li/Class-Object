class Person:
    def __init__(self, name, id, age):
        self.name = name
        self.id = id
        self.age = age
    def copy(self):
        new = Person(self.name, self.id, self.age)
        return new
    
joe =Person("Joe","shsf",20)
copy = joe.copy()
copy.age = 18
print(joe.age)