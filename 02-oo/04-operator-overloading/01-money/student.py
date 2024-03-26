class Money:
    def __init__(self, amount, currency):
        self.__amount = amount
        self.__currency = currency
        
    def __add__(self, other):
        if self.__currency == other.__currency:
            return Money(
                self.__amount + other.__amount, self.__currency
            )
        else:
            raise RuntimeError("Mismatched currencies!")
        
    def __sub__(self, other):
        if self.__currency == other.__currency:
            return Money(
                self.__amount - other.__amount, self.__currency
            )
        else:
            raise RuntimeError("Mismatched currencies!")
    
    def __mul__(self, value):
        if value > 0:
            return Money(self.__amount * value, self.__currency)
        else:
            raise ValueError("You can't multiply with a negative number")