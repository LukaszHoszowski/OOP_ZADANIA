from random import randint
from functools import lru_cache


# Zadanie 1

class Dice:
    def __init__(self, dice_type):
        DICE_SIDES = [3, 4, 6, 8, 10, 12, 20, 100]

        if not dice_type in DICE_SIDES:
            raise ValueError(f'Wrong sides parameter - {dice_type}, available options - {DICE_SIDES}')

        self.dice_type = dice_type

    def roll(self):
        return randint(1, self.dice_type)


# f = Dice(100)
# print(f.roll())

# Zadanie 2

class Dice2:
    def __init__(self, dice_type, number_of_rolls):
        DICE_SIDES = [3, 4, 6, 8, 10, 12, 20, 100]

        if not dice_type in DICE_SIDES:
            raise ValueError(f'Wrong Dice Type parameter - {dice_type}, available options - {DICE_SIDES}')

        if not int(number_of_rolls):
            raise ValueError(f'Only integers allowed in {number_of_rolls}')

        self.dice_type = dice_type
        self.number_of_rolls = number_of_rolls

    def __iter__(self):
        return self

    def __next__(self):
        while self.number_of_rolls:
            self.number_of_rolls -= 1
            return randint(1, self.dice_type)
        else:
            raise StopIteration('end of collection')


# f = Dice2(10, 2)
# i = iter(f)

# print('1st', next(i))
# print('2nd', next(i))
# print('3rd', next(i))

# for throw in Dice2(6,10):
#     print(throw)

# Zadanie 3

def roll_the_dice(n=3):
    for x in range(3):
        yield randint(1, 6)


# a = roll_the_dice(3)
#
# print(a.__next__())
# print(a.__next__())
# print(a.__next__())
# print(a.__next__())

# Zadanie 4

song = ['Wlazł kotek na płotek i mruga,',
        'ładna to piosenka, nie długa. Nie długa, nie krótka, lecz w sam raz,',
        'zaśpiewaj koteczku, jeszcze raz.']


def sing(song):
    for x in song:
        yield x


# a = sing(song)
#
# print(a.__next__())
# print(a.__next__())
# print(a.__next__())
# print(a.__next__())

# Zadanie 5

@lru_cache(2)
def fib(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# for element in fib(37):
#     print(element)
