#Implemtación de la clase Terminal
class Terminal:
    def __init__(self,phone_number):
        self.__phone_number = phone_number
    @property
    def get_phone_number(self):
        return self.__phone_number
    
    @numero.setter
    def numero(self):
       if self.__phone_number.startswith(9,6 or 7) and self.__phone_number <= 9:
           return self.__phone_number
       else:
           raise ValueError("Invalid phone number please enter another one")