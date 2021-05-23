import math


class nix:
    pass

a = nix()

print(type(a))


class Cat():
    def __init__(self, name):
        self.name = name

missy =  Cat("Missy")
lucy = Cat("Lucky")

print(missy.name)
print(lucy.name)


class Person():
    pass


class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

P1 = Person("Hans", 52)
print(P1.name)




class Vector():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __len__(self):
        return math.sqrt(self.x * self.x + self.y + self.y)

    def __str__(self):
        return "(" + str(self.x) + "/" + str(self.y) + ")"



v1 = Vector(100,200)
v2 = Vector(500,730)
v3 = v1 + v2

print(v3)