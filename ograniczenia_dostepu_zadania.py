from obiekty_i_klasy_zadania import Shape, Employee
from math import pi


# Zadanie 1

class Dinosaur:

    def walk(self):
        return "Chodzę!"

    def make_sound(self):
        return "Roar!"


class Bird(Dinosaur):
    def fly(self):
        return "Latam!"

    def make_sound(self):
        return "Ćwir Ćwir"


# if __name__ == "__main__":
# d = Dinosaur()
# print("Dinozaur chodzi:")
# print(d.walk(), "\n")  # "\n" to znak oznaczający nową linię.
#
# print("Dinozaur wydaje dźwięk:")
# print(d.make_sound())

# f = Bird()
# print(f.make_sound())

# Zadanie 2

class Circle(Shape):
    def __init__(self, x, y, color, radius):
        super().__init__(x, y, color)
        self._radius = radius

    def describe(self):
        return f'x = {self.x}, y = {self.y}, color = {self.color}, radius = {self._radius}.'

    def area(self):
        return f'Area is equal to {pi * self._radius ** 2:.2f}.'

    def perimeter(self):
        return f'Perimeter is equal to {2 * pi * self._radius:.2f}.'


# f = Circle(2, 4, 'black', 3)
#
# print(f.describe())
# print(f.area())
# print(f.perimeter())

# Zaanie 3

class HourlyEmployee(Employee):
    def __init__(self, id, first_name, last_name):
        super().__init__(id, first_name, last_name)

    def compute_payment(self, hours):
        self._hours = hours

        return self._salary * self._hours


# f = HourlyEmployee(123, 'Luk', 'Puk')
#
# f.set_salary(100.00)
# print(f.compute_payment(10))

# Zadanie 4

class SalariedEmployee(Employee):
    def __init__(self, id, first_name, last_name):
        super().__init__(id, first_name, last_name)

    def compute_payment(self):
        return self._salary * 190

# f = SalariedEmployee(123, 'Luk', 'Puk')

# f.set_salary(100.00)
# print(f.compute_payment())
