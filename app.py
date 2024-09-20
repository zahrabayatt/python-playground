# in dictionary in python,we use immutable types for keys, so quiet often we use string or number for keys, but for values we can use any type.

point = {"x": 1, "y": 2}

# we can use dict function for defining dictionary:
point = dict(x=1, y=2)

# we can access items by key not the index:
point["x"] = 10
print(point["x"])

# add new item to dictionary:
point["z"] = 20

print(point)

# if we use the key that didn't exist we got error:
# print(point["a"])

# to check if key exist:
if "a" in point:
    print(point["a"])

# Or we can use get method to get value by key, if key didn't exist it returns None but we can also set the default value if key didn't exist:
print(point.get("a"))
print(point.get("a", 0))

# to delete item in dictionary:
del point["x"]

print(point)

# to loop over a dictionary:

for key in point:
    print(key, point[key])

# or

for x in point.items():
    print(x)

for key, value in point.items():
    print(key, value)
