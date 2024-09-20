list1 = [1, 2, 3]
list2 = [10, 20, 30]

# To get a list from these two lists where each item is a tuple,the first element of the tuple comes from list1, and the second element comes from list2, like this:
# [(1, 10), (2, 20), (3, 30)]
# to achieve this we use zip function:

zip_object = zip(list1, list2)
print(zip_object)

# zip_object is a iterable object
for item in zip_object:
    print(item)

list3 = list(zip(list1, list2))
print(list3)

# we can also pass a string :
print(list(zip("hello", list1, list2)))
