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

if __name__ == "__main__":
    d = Dinosaur()
    print("Dinozaur chodzi:")
    print(d.walk(), "\n")  # "\n" to znak oznaczający nową linię.

    print("Dinozaur wydaje dźwięk:")
    print(d.make_sound())

f = Bird()
print(f.make_sound())