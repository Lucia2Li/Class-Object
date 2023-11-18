class Terminal:
    def __init__(self,phone_number):
        self.phone_number = phone_number
        self.__time_call = 0
        self.__time_received = 0
        self.__total_time = 0
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
    def time_call(self,time):
        self.__time_call += time
        self.__total_time += time
    
    @property
    def time_received(self):
        return self.__time_received
    @time_received.setter
    def time_received(self,time):
        self.__time_received = time
        self.__total_time = time
    
    def call(self, other_phone, time):
        self.time_call = time
        other_phone.time_received = time
    def __str__(self):
        return f"{self.__phone_number}-Conversation time: {self.__total_time}"
    
t1 = Terminal("666112233")
t2 = Terminal("666744459")
t3 = Terminal("632128919")
t4 = Terminal("664135818")
print(t1)
print(t2)
t1.call(t2, 420)
t1.call(t3, 210)
print(t1)
print(t2)
print(t3)
print(t4)