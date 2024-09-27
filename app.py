class Animal:
    def __init__(self):
        print("Animal Constructor")
        self.age = 1

    def eat(self):
        print("eat")


class Mammal(Animal):
    # we overwriting the base constructor and we don't have age attribute
    # def __init__(self):
    #     self.weight = 2

    def __init__(self):
        super().__init__()  # we call base constructor then we have age attribute
        print("Mammal Constructor")
        self.weight = 2
        # we can change the order of calling constructor by moving super().__init__() to end of the mammal constructor

    def walk(self):
        print("walk")


class Fish(Animal):
    def swim(self):
        print("swim")


m = Mammal()
print(m.age)
print(m.weight)
