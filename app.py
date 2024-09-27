from collections import namedtuple


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # by default. Python compares objects based on where they are stored in memory. to change this behaver we can reimplement the __eq__ magic method:
    # def __eq__(self, other):
    #     return self.x == other.x and self.y == other.y


p1 = Point(1, 2)
p2 = Point(1, 2)
# these two object located in different place in memory and has different reference
print(p1 == p2)

# id is a built in function that return the address of memory location where object is stored:
print(id(p1))
print(id(p2))

# after reimplement __eq__:
print(p1 == p2)

# Writing all this code for data classes is a little bit tedious. If you're dealing with classes that have no behavior, no methods,they only have data, you can use a named tuple instead:

Point = namedtuple("Point", ["x", "y"])
# As the first argument, we specify the name for this new type you want to create.as the second argument, we pass an array of field names or attributes names:
p1 = Point(x=1, y=2)
# we got error because we can't named a attribute of named tuple after we initialize it.
# p1.x = 10
# if you really need to do this you jsut need to create another Point:
# p1 = Point(x=10, y=2)
p2 = Point(x=1, y=2)
print(p1 == p2)
