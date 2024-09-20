# set is another data structure in python which is basically a collection without duplication items.

numbers = [1, 2, 3, 1, 4, 4]
uniques = set(numbers)
print(uniques)

# we use curly braces {} to define a set
second = {1, 4}
second.add(5)
second.remove(5)
len(second)
print(second)

# one the useful usage of sets is when we want to union two lists and we what the result list didn't have duplicate items:
first = set([1, 2, 3, 4])
second = set([1, 4, 5, 6])

print(first | second)

# we can also get intersections of two sets:
print(first & second)

# we can also get the different of two sets:
print(first - second)
print(second - first)

# we can also get the items either in first or second set but not in both:
print(first ^ second)

# to convert a set to list, use list function:
print(list(uniques))

# set unlike list are unordered collection, we can not access item by index, so if you need to access by index, use list
# print(first[0])

# to check if item exists in a set:
if 1 in first:
    print("yes")
