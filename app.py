# we use [] to define list or sequence objects. in between of [] we can have object of any type like string, numbers,...

letters = ["a", "b", "c"]
matrix = [[0, 1], [2, 3]]
zeros = [0] * 100
zeros = [0] * 5  # using a star or an asterisk (*) to repeat items in a list
combined = zeros + letters  # using plus(+) to concatenate multiple lists.

# in python, every object in the list can be of a different type, so they don't have to be exactly the same type.

# we can use list function to create a list, the list function get a iterable input like string, range object,..
# with list function we can create a list like numbers from 1 until 20:
numbers = list(range(1, 21))
# or we can create a list of character of string:
chars = list("Hello World")

print(zeros)
print(combined)
print(numbers)
print(chars)

print(len(chars))  # with len function we can get the length of a list
