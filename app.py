def multiply(*numbers):
    print(numbers)
    total = 1
    for number in numbers:
        total *= number
    return total


print(multiply(2, 3, 4, 5))

# Tuple: (1,2,3,4,5)
# List: [1,2,3,4,5]

# Tuple is a collection of objects and like list is iterable but we can't modify that.
