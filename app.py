# we use all lowercase letters and separate multiple words by underscore for variable and function names.
# we use pascal naming convention for classes.

class Point:
    def draw(self):  # all functions in classes must have at least one parameter.
        print("draw")


point = Point()
print(type(point))
# output: <class '__main__.Point'> - main is the name of our module.
point.draw()

# to check if the object is instance of class:
print(isinstance(point, Point))
print(isinstance(point, int))
