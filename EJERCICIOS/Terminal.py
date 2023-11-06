#Implemtación de la clase Terminal
class Terminal:
    def __init__(self,phone_number,digit):
        self.__phone_number = phone_number
        
    @property
    def get_phone_number(self):
        return self.__phone_number
    
    @phone_number.setter
    def phone_number(self):
        lista = ["9","6","7"]
        if phone_number[0] in lista:






