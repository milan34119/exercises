class Repeat:
    def __init__(self, value_to_repeat):
        self.__value_to_repeat = value_to_repeat
        
    def __iter__(self):
        return self
    
    def __next__(self):
        return self.__value_to_repeat