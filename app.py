# if you dealing with large of items in the list, we have a more efficient type in python called Array

from array import array

# array function get a typecode as argument which is string of one character that determines the type of object in the array:
# typecode in python3 docs: https://docs.python.org/3/library/array.html

numbers = array('i', [1, 2, 3])

# array like list has these methods and we can access the item by its index:
numbers.append(4)
numbers.insert(2, 9)
numbers.pop()
numbers.remove(9)
print(numbers[0])

# we can not add item with different type in array unlike lists
numbers[0] = 1.0  # we got type error
