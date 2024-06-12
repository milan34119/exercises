class PadZip:
    def __init__(self, left, right, padding):
        self.__left = iter(left)
        self.__right = iter(right)
        self.__padding = padding
    
    def __iter__(self):
        return self
    
    def __next__(self)