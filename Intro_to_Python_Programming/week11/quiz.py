class Account(object):

    def __init__(self, name, balance):
        self.__name = name
        self.__balance = balance



    def deposit(self, amount):
        self.__balance += amount



    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount


    def getBalance(self):
        return self.__balance


    def getName(self):
        return self.__name

class CheckingAccount(Account):
    minBalance = 500.00

    def __init__(self, name, balance):
        super().__init__(name, balance)

    def withdraw(self, amount):
        if self.getBalance() - amount < CheckingAccount.minBalance:
            return False
        else:
            super().withdraw(amount)

def main():
    account_list = []
    a1 = Account('Normal Account', 501)
    a2 = CheckingAccount('Checking Account', 501)
    account_list.append(a1)
    account_list.append(a2)

    for account in account_list:
        print(f"\naccount: {account.getName()}\nBalance: {account.getBalance()}")
        account.withdraw(1)
        print(f'new balance: {account.getBalance()}')

main()