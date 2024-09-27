# In Python a class can have multiple base classes.
# similar to multilevel inheritance it's a source of issues If you don't use it properly, you're going to introduce all sorts of bugs in your programs.
class Employee:
    def great(self):
        print("Employee Greet")


class Person:
    def great(self):
        print("Person Great")


class Manager(Employee, Person):
    pass


manager = Manager()
manager.great()  # Employee greet
# We get employee greet because we added the employee class first. So when the Python interpreter tries to execute this line, first it looks at the manager class to see if it has a method called greet. If it doesn't, it will look at its first base class. Does the employee have a greet method? Yes. So, the lookup terminates here. If the employee class doesn't have the greet method, then it will look at the person class.

# So why is this an issue? Because if tomorrow another programmer joins our team and, for whatever reason, they decide to change the order of these base classes, our program will have a different behavior. So if they move this person class over here and run the program, now we get a different output.

# Multiple inheritance is not always a bad thing. It's bad if you don't use it properly.
# Good Example of Using Multiple Inheritance:


class Flyer:
    def fly(self):
        pass


class Swimmer:
    def swim(self):
        pass


class FlyingFish(Flyer, Swimmer):
    pass
