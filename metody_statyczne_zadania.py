from datetime import datetime

# zadanie 1

from obiekty_i_klasy_zadania import Calculator

class AdvancedCalculator(Calculator):
    PI = 3.14159265

    @staticmethod
    def computer_circle_area(r):
        return PI * r ** 2

"""To nie działa bo takie parametr nie jest dostepny w funkcja classy, 
musialby by byc zadeklarowany w __init__ - generalnie to zadanie jest dla mnie niezrozumiale"""

# f = AdvancedCalculator()
# print(f.computer_circle_area(5))

# zadanie 2

class BankAccount:
    next_acc_number = 1
    def __init__(self, cash=0.0):

        if not type(cash) == float:
            raise ValueError(f"Attribute '{cash}' isn't float")

        self._cash = cash
        self.acc_number = self.next_acc_number
        BankAccount.next_acc_number += 1

    def deposit_cash(self, amount):
        if amount < 0.0:
            raise ValueError(f"Deposit amount: '{amount}' needs to be >0")

        self._cash += amount

        return self._cash

    def withdraw_cash(self, amount):
        if amount < 0.0:
            raise ValueError(f"Withdraw amount: '{amount}' needs to be >0")

        if not self._cash - amount >= 0:
            raise ValueError(f"Amount: '{amount}' is too high, top up your account")

        self._cash -= amount

        return self._cash

    def print_info(self):
        return f'Account number: {self.acc_number}\n' \
               f'Current balance: {self._cash}'


# f = BankAccount()
#
# f.deposit_cash(1000)
# f.withdraw_cash(10)
#
# print(f.print_info())
# print(f.acc_number)
# print(f.next_acc_number)

# zadanie 3

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return "{} is {} years old.".format(self.name, self.age)

    @classmethod
    def create_person(cls, name, year_of_birth):
        currentYear = datetime.now().year
        return cls(name, currentYear - year_of_birth)

# f = Person.create_person("Brian", 1984)
# print(f)
