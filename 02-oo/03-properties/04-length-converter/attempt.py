class LengthConverter:
    FEET_PER_METER = 3.28084
    INCH_PER_METER = 39.3701
    
    def __init__(self):
        self.__distance_in_meter = 0
    
    @property
    def meter(self):
        return self.__distance_in_meter
    
    @meter.setter
    def meter(self, value):
        self.__distance_in_meter = value
        
    @property
    def inch(self):
        return (self.__distance_in_meter * LengthConverter.INCH_PER_METER)
    
    @property
    def feet(self):
        return (self.__distance_in_meter * LengthConverter.FEET_PER_METER)
    