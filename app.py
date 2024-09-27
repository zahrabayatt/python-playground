# too much of every thing is a bad thing! and that is very true about inheritance.
class Animal:
    def __init__(self):
        print("Animal Constructor")
        self.age = 1

    def eat(self):
        print("eat")


class Brid(Animal):
    def fly(self):
        print("fly")


# but chechen can not fly!
class Chicken(Brid):
    pass

# Another example of inheritance abuse is the concept of employees. People say, "an employee is a person, a person is a living creature," and so on. This is what we call multilevel inheritance, and it can really complicate your software.
# Just because an employee is a person and a person is a living creature doesn’t mean you should have these classes in your software. Your methods should solve a business problem. For example, just because an animal can eat in real life doesn’t mean your animal class needs an eat method.
# Avoid multilevel inheritance. If you use inheritance, keep it to one or two levels. Trust me, going beyond that? You're going to shoot yourself in the foot.
