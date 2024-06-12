class BankAccount:
    def __init__(self, account_number, initial_balance):
        self.__account_number = account_number
        self.__balance = initial_balance
        
    def get_account_number(self):
        return self.__account_number
    
    def get_balance(self):
        return self.__balance
    
    def deposit(self, value):
        if value <= 0:
            raise ValueError("Must be positive")
        self.__balance += value
    
    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
        else:
            raise ValueError('You have insufficient funds bitch')
        
        