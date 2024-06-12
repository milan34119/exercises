class calendar:
    def __init__(self, today):
        self.__today = today
        
    @property
    def today(self):
        return self.__today
        
    @today.setter
    def today(self, value):
        if value is None:
            raise ValueError("can't be none")
        self.__today = value
        
class CalendarStub:
    def __init__(self, today):
        self.__today = today
        
    @property
    def today(self):
        return self.__today
    
    @today.setter
    def today(self, value):
        if value is None: 
            raise ValueError("cant be none")
        self.__today = value
        