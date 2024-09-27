class Animal:
    def __init__(self):
        self.age = 1

    def eat(self):
        print("eat")


class Mammal(Animal):
    def walk(self):
        print("walk")


class Fish(Animal):
    def swim(self):
        print("swim")


# Animal: Parent, Base
# Mammal: Child, Sub
# Fish: Child, Sub

m = Mammal()
m.eat()
print(m.age)
print(isinstance(m, Mammal))
print(isinstance(m, Animal))
# every class we define, it inherits from object class
o = object()
print(isinstance(m, object))
print(issubclass(Mammal, Animal))
print(issubclass(Mammal, object))
print(issubclass(Animal, object))
