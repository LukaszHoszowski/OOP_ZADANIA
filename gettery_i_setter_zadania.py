# Zadanie 1

class Lightsaber:
    def __init__(self, color):
        self._color = color

    @property
    def __str__(self):
        bright = ('Blue', 'Green', 'Purple')
        return f'Lighstaber: {self._color}, force: {"Bright" if self._color in bright else "Dark"}'

# f = Lightsaber('Blue')
# print(f.__str__)

# Zadanie 2

class Lightsaber2:
    def __init__(self, color):
        self.color = color

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        colors = ('blue', 'green', 'purple', 'red')
        if color in colors:
            self._color = color
        else:
            raise ValueError("Incorrect color.")

    @property
    def __str__(self):
        light = ('Blue', 'Green', 'Purple')
        return f'Lighstaber: {self._color}, force: {"Light" if self._color.casefold() in light else "Dark"}'



# f = Lightsaber2('blue')
# print(f.color)
# print(f.__str__)

# Zadanie 3

class Lightsaber3:
    def __init__(self, color):
        self.color = color

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        colors = ('blue', 'green', 'purple', 'red')
        if color in colors:
            self._color = color
        else:
            raise ValueError("Incorrect color.")

    @property
    def force_side(self):
        light = ('Blue', 'Green', 'Purple')
        if self._color in light:
            force_side = 'Light'
        else:
            force_side = "Dark"
        return force_side

    @property
    def __str__(self):
        return f'Lighstaber: {self._color}, force: {self.force_side}'

# f = Lightsaber3('blue')
# print(f.color)
# print(f.__str__)