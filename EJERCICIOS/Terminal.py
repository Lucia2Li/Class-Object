#Implementación de la clase terminal

class Terminal:
    def __init__(self,phone_number):
        self.phone_number = phone_number
        self.time_call = 0
        self.tiempo_recieved = 0
        self.total_time = 0
    @property
    def phone_number(self):
        return self.__phone_number
    @phone_number.setter
    def phone_number(self,phone_number):
        if phone_number[0] in ["9","7","6"] and len(phone_number) == 9 and phone_number.isdigit():
            self.__phone_number = phone_number
        else:
            raise ValueError
        
    @property
    def time_call(self):
        return self.__time_call
    @time_call.setter
    def time_call(self,tiempo):
        self.__time_call += tiempo
        self.__total_time += tiempo
    
    @property
    def time_recieved(self):
        return self.__time_recieved
    @time_recieved(self)




