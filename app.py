# a Tuple is basically a readonly list, we can't modify, add, remove items to Tuples

point = (1, 2)
print(type(point))  # tuple

point = 1, 2
print(type(point))  # tuple

point = 1
print(type(point))  # int

point = 1,
print(type(point))  # tuple

# empty tuple
point = ()
print(type(point))  # tuple

# concatenate tuples:
point = (1, 2) + (3, 4)
print(type(point))  # tuple
print(point)

point = (1, 2) * 3
print(type(point))  # tuple
print(point)

# convert the list to tuple:
point = tuple([1, 2, 3, 4])
print(point)

# we can use tuple function to convert any iterable object like string to tuple:
letters = tuple("Hello World")
print(letters)

# accessing items in tuple:
print(point[0])
print(point[0:1])
print(point[1:])
print(point[:2])

# unpack topples
x, y, z = point

# check item is exist in tuple
if 10 in point:
    print("existsj")

# point[0] = 10 # we can not modify the tuple


# where in the real world we use topples?
# Let's say you're dealing with a sequence of object and you want to make sure that you don't accidentally modify this sequence. You don't accidentally add a new object to it or remove an existing object so instead of a list you can use a topple to prevent these accidental errors.
