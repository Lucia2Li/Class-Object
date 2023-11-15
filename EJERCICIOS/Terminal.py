#Implemtación de la clase Terminal
class Terminal:
    def __init__(self,phone_number,digit):
        self.phone_number = phone_number
        
    @property
    def get_phone_number(self):
        return self.__phone_number
    
    @phone_number.setter
    def phone_number(self, teléfono):
        lista = ["9","6","7"]
        if teléfono[0] in lista and len(teléfono) == 9 and teléfono.isdigit():
            self.__phone_number = teléfono

        

        






