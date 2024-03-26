class BankAccount:
    def __init__(self, account_number, initial_balance):
        self.__account_number = account_number
        self.__balance = initial_balance

    def get_account_number(self):
        return self.__account_number

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount > 0 and self.__balance > 0:
            self.__balance += amount
        else:
            raise ValueError("You can't deposit a negative amount.")

    def withdraw(self, amount):
        if amount > 0 and self.__balance > amount:
            self.__balance -= amount
        else:
            raise ValueError("You can't withdraw a negative amount")
