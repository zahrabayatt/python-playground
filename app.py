class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    # class method:
    @classmethod  # decorator
    def zero(cls):  # cls is a reference to class
        return cls(0, 0)

    # instance method
    def draw(self):
        print(f"Point ({self.x}, {self.y})")


point = Point(1, 2)
point.draw()

another = Point.zero()
another.draw()
