import random

class Dado:
    def __init__(self, caras = 6):
        self.__caras = caras
        self.__numero = random.randint(1, self.__caras)
    @property
    def numero(self):
        return self.__numero
    @property
    def caras(self):
        return self.__caras
    