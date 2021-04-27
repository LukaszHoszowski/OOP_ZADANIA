# Zadanie 1

class Calculator:
    def __init__(self):
        self.result = []

    def add(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        result = self.num1 + self.num2
        self.result.append(f'added {self.num1} to {self.num2} got {result}')
        return result

    def multiply(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        result = self.num1 * self.num2
        self.result.append(f'multiplied {self.num1} with {self.num2} got {result}')
        return result

    def print_operations(self):
        for res in self.result:
            print(res)


# f = Calc()
# f.add(2, 3)
# f.multiply(9, 9)
# f.add(10, 9)
#
# g = Calc()
# g.add(2, 3)
# g.multiply(9, 9)
# g.add(10, 9)
#
# f.print_operations()
# g.print_operations()

# Zadanie 2

class Shape:
    def __init__(self, x, y, color):
        self.color = color
        self.x = x
        self.y = y

    def __str__(self):
        return f'Figura koloru {self.color} o środku w punkcie ({self.x}, {self.y})'

    def describe(self):
        return f'x = {self.x}, y = {self.y}, color = {self.color}.'

    def distance(self, shape):
        _result = ((self.x - shape.x) ** 2 + (self.y - shape.y) ** 2) ** 0.5
        return f'{_result:.1f}'


# f = Shape(3, 5, 'czarny')
# g = Shape(1, 2, 'white')
# print(f.describe())
# print(g.describe())
# print(f.distance(g))
# print(g.distance(f))
# print(f)
# print(g)

# Zadanie 3

class BankAccount:
    def __init__(self, number, cash=0.0):

        if not int(number):
            raise ValueError(f"Attribute '{number}' isn't an integer")

        if not type(cash) == float:
            raise ValueError(f"Attribute '{cash}' isn't float")

        self._number = number
        self._cash = cash

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
        return f'Account number: {self._number}\n' \
               f'Current balance: {self._cash}'


# f = BankAccount(793)
#
# f.deposit_cash(1000)
# f.withdraw_cash(10)
#
# print(f.print_info())

# Zadanie 4

class Employee:
    def __init__(self, id, first_name, last_name):
        self.last_name = last_name
        self.first_name = first_name
        self.id = id

    def set_salary(self, salary):
        if not type(salary) == float:
            raise ValueError(f"Salary amount: '{salary}' isn't float")

        if salary < 0.0:
            raise ValueError(f"Salary amount: '{salary}' needs to be > 0")

        self._salary = salary

    def employee_info(self):
        return f'Employee: {self.first_name}, {self.last_name}\n' \
               f'ID: {self.id}\n' \
               f'Rate per hour: {self._salary}'

# f = Employee(123, "Luk", "Puk")
#
# f.set_salary(100.0)
#
# print(f.employee_info())
