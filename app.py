from sys import getsizeof

values = [x * 2 for x in range(10)]

print("list: ", getsizeof(values))

# print(values)
for x in values:
    print(x)

values = (x * 2 for x in range(10))

# comprehensions tuple is a Generator Expressions that returns a generator object which is efficient for large collectors because unlike list it doesn't store all items in memory and because of that we can use len function for that to get count of collection and we have to iterate over generator object which is iterable object and get the count.

print("list: ", getsizeof(values))

print(values)
# print(len(values)) # error

for x in values:
    print(x)
