#Implemtación de la clase Terminal
class Terminal:
    def __init__(self,phone_number):
        self.phone_number = phone_number
        self.tiempo = 0
        self.tiempo_total = 0
        self.tiempo_recivido = 0
        
        
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
    @property
    def tiempo(self):
        return self.__tiempo
    @tiempo.setter
    def tiempo(self,tiempo_llamada):
        self.tiempo += tiempo_llamada
        self.tiempo_total += tiempo_llamada
    
    @property
    def tiempo_recibido(self):
        return self.tiempo_recibido
    
    @tiempo_recibido.setter
    def tiempo_recibido(self, tiempo_llamada):
        self.tiempo_recibido = tiempo_llamada
        self.tiempo_total = tiempo_llamada 

    def __str__(self):
        return f"El número de teléfono es {self.phone_number}"
   
t1 = Terminal("966112233")
t2 = Terminal("666744459")

print(t1)


        

        






