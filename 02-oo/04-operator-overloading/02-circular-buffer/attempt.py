class CircularBuffer:
    def __init__(self, n):
        self.__n = n
        self.__lst = []
        
    @property
    def lst(self):
        return self.__lst
    
    @property
    def n(self):
        return self.__n
    
    def add(self, item):
        if len(self.__lst) < self.__n: 
            self.__lst.append(item)
        else:
            self.__lst.pop(0)
            self.__lst.append(item)