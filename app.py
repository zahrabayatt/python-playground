
class Point:
    # every functions that we define in class must has at least one parameter which we called by convention self.
    # self is a reference to current object.
    def __init__(self, x, y):
        # x, y is attributes of Point
        self.x = x
        self.y = y

    def draw(self):
        print(f"Point ({self.x}, {self.y})")


point = Point(1, 2)
print(point.x)
print(point.y)

# we dont need to supply the value for self argument, python interpreter does that for us.
point.draw()
