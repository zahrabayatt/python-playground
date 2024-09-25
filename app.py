class Point:
    # __init__ is a magic method.
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # we can reimplement the str method:
    def __str__(self):
        return f"({self.x}, {self.y})"

    def draw(self):
        print(f"Point ({self.x}, {self.y})")


point = Point(1, 2)

# magic methods wrap two underline and they call automatically by python interpreter
# magic docs: https://realpython.com/python-magic-methods/#representing-objects-as-strings

print(point)
print(point.__str__())
print(str(point))
# by default it returns the name of module and the memory object followed by memory address.
# <__main__.Point object at 0x00000205ECFF7FD0>
