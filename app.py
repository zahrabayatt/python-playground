for x in range(5):
    print(x)

print(type(range(5)))  # <class 'range'>

# In python we have primitive types and complex types, range is one of the complex types.

# range object is iterable which means you can iterate over it or use it in a for loop.

# range function return a range object that is iterable and because of that we can iterate it using for loop.

# There is other object that is iterable in Python like strings:

for x in "Python":
    print(x)

# we have another complex type called list which we use it to store a list of objects, this is also iterable:

for x in [1, 2, 3, 4]:
    print(x)

# custom objects are iterable.
