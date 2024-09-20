values = []

for x in range(5):
    values.append(x * 2)

# better solution:

values = [x * 2 for x in range(5)]
print(values)

# we can also use comprehensions for set and dictionary:

# we use curly braces to define dictionary and set:

values = {x * 2 for x in range(5)}
print(values)

values = {x: x * 2 for x in range(5)}
print(values)
