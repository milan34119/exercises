class Time:
    def __init__(self, hours, minutes, seconds):
        self.__hours = hours
        self.__minutes = minutes
        self.__seconds = seconds
        
    @property
    def hours(self):
        return self.__hours
    
    @property
    def minutes(self):
        return self.__minutes
    
    @property
    def seconds(self):
        return self.__seconds
    
    @hours.setter
    def hours(self, value):
        if 0 < value < 23:
            self.__hours = value
        else:
            raise ValueError("kan toch ni joh")
        
    @minutes.setter
    def minutes(self, value):
        if 0 < value < 59:
            self.__minutes = value
        else: 
            raise ValueError("nee jonge")
        
    @seconds.setter
    def seconds(self, value):
        if 0 < value < 59:
            self.__seconds = value
        else:
            raise ValueError('man man man')