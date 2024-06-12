class Cycle:
    def __init__(self, lst):
        self.__lst = list(lst)
        self.__index = -1
    
    def __iter__(self):
        return self
    
    def __next__(self):
        self.__index = (self.__index + 1) % len(self.__lst)
        return self.__lst[self.__index]