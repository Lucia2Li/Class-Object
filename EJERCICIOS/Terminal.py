class Terminal:
    def __init__(self,phone_number):
        self.phone_number = phone_number
        self.__time_call = 0
        self.__time_received = 0   

    @property
    def phone_number(self):
        return self.__phone_number
    @phone_number.setter
    def phone_number(self,phone_number):
        if phone_number[0] in ["9","7","6"] and len(phone_number) == 9 and phone_number.isdigit():
            self.__phone_number = phone_number
        else:
            raise ValueError("El télefono introducido es incorrecto")
        
    @property
    def time_call(self):
        return self.__time_call
    @time_call.setter
    def time_call(self,time):
        self.__time_call += time
    
    @property
    def time_received(self):
        return self.__time_received
    @time_received.setter
    def time_received(self,time):
        self.__time_received += time
    
    def total_time(self):
        return self.time_call+self.time_received   

    def call(self, other_phone, time):
        self.time_call = time
        other_phone.time_received += time
    def __str__(self):
        return f"{self.phone_number}-Conversation time: {self.total_time()}"



class Mobile(Terminal):
    def __init__(self, phone_number, rate):
        super().__init__(phone_number)
        self.rate = rate
        self.charge = 0

    @property
    def rate(self):
        return self.__rate
    @rate.setter
    def rate(self,value):
        if value == "rat":
            self.__rate = 0.05/60
        elif value == "monkey":
            self.__rate = 0.15/60
        elif value == "elephant":
            self.__rate = 0.03/60
        else:
            raise ValueError("Rate incorrecto")
        
    @property
    def charge(self):
        return self.__charge
    @charge.setter
    def charge(self, charge):
        self.__charge = charge
    
    def call(self, terminal, time):
        super().call(terminal, time)
        self.charge= super().time_call * self.rate

    


    def __str__(self):
        self.charge
        return f"{super().phone_number} - {super().total_time()}s of conversation - charged {self.charge}€"




