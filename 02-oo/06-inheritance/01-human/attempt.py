class Human:
    def __init__(self, name):
        self.__name = name
    
    @property
    def name(self):
        return self.__name
    
class Archer(Human):
    def __init__(self, num_arrows):
        super().__init__('Jos')
        self.__num_arrows = num_arrows
    
    @property
    def num_arrows(self):
        return self.__num_arrows