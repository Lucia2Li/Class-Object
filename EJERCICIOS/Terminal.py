#Implemtación de la clase Terminal
class Terminal:
    def __init__(self,phone_number):
        self.phone_number = phone_number
        
    @property
    def phone_number(self):
        return self.__phone_number
    
    @phone_number.setter
    def phone_number(self, telefono):
        lista = ["9","6","7"]
        if telefono[0] in lista and len(telefono) == 9 and telefono.isdigit():
            self.__phone_number = telefono
        else:
            raise ValueError("El número es incorrecto")
        
    def __str__(self):
        return f"El número de teléfono es {self.phone_number}"
   
t1 = Terminal("966112233")
print(t1)




        

        






