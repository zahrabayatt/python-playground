class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x+other.x, self.y + other.y)


point = Point(1, 2)
other = Point(1, 2)

combined = point + other
print(combined)
print(combined.x, combined.y)


# other Arithmetic Operations docs: https://docs.python.org/3/reference/datamodel.html#emulating-numeric-types
