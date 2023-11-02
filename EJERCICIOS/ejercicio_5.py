#Implemtación de la clase Terminal
class Terminal:
    def __init__(self,phone_number):
        self.__phone_number = phone_number
        
    @property
    def get_phone_number(self):
        return self.__phone_number
