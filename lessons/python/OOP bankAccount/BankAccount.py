class BankAccount():
    def __init__(self, balance = 0):
        self.__balance = balance

    def get_balance(self):
        return self.__balance
    
    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount > self.__balance:
            raise ValueError("На счёте недостаточно средств")
        self.__balance -= amount
        

    def transfer(self, account, amount):
        self.withdraw(amount)
        account.deposit(amount) 