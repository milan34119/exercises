class LengthConverter:
    FEET_PER_METER = 3.28084
    INCH_PER_METER = 39.3701
    
    def __init__(self):
        self.__length_in_meter = 0
        
    @property
    def meter(self):
        return self.__length_in_meter
    
    @meter.setter
    def meter(self, meter):
        self.__length_in_meter = meter
        
    