#Implemtación de la clase Terminal
class Terminal:
    def __init__(self,phone_number):
        lista = ["9","6","7"]
        if self.__phone_number in lista and len(self.__phone_number) == 9:
            self.__phone_number = phone_number
        else:
            raise ValueError("It should start with 9,6 or 7")
        
    @property
    def get_phone_number(self):
        return self.__phone_number
    
    
