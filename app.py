numbers = [1, 2, 3, 4]
print(numbers)

# unpacking operator
print(*numbers)

# we can unpack iterable object like range:
values = list(range(5))
print(values)
values = [*range(5), *"Hello"]
print(values)

# using unpack operator we can concatenate two lists:
first = [1, 2]
second = [3]
values = [*first, "a", *second]
print(values)

# we can unpack dictionary using ** operator:
first = {"x": 1}
second = {"x": 10, "y": 2}
combined = {**first, **second, "z": 1}
# the value of x is 10, so if we have sames keys, the last value will be used.
print(combined)
