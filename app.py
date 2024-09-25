
class Point:
    # class attribute
    default_color = "red"

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print(f"Point ({self.x}, {self.y})")


point = Point(1, 2)
point.draw()

# we can also define attributes after defending object because objects in python like JS is dynamic
point.z = 10

# all the attributes that we are defining so far(x,y,z), are instance attributes, so every point object has attributes with different value

another = Point(3, 4)
another.draw()


# we can also define class attributes and these are attributes that we define in class level and they are shared with all instances.
Point.default_color = 'yellow'

print(point.default_color)
print(Point.default_color)
print(another.default_color)
