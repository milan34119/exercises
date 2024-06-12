class Human:
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name


class Archer(Human):
    def __init__(self, name, num_arrows):
        super().__init__(name)
        self.__num_arrows = num_arrows

    def get_num_arrows(self):
        return self.__num_arrows

    def use_arrows(self, num):
        if num > self.__num_arrows:
            raise Exception("Not enough arrows")
        else:
            self.__num_arrows -= num
            
class CrossbowMan(Archer):
    def __init__(self):
        super().__init__('Jos', 69420)
    
    def triple_shot(self, target):
        if self.__num_arrows >= 3:
            self.__num_arrows -= 3
            print(f'{target.name} has been shot by {self.name}')
        else:
            raise ValueError('not enough arrows couz')
        
        