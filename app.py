numbers = [1, 2, 3]
first = numbers[0]
second = numbers[1]
third = numbers[2]

# another way is to unpack list like that:
first, second, third = numbers

# the number of variables that we have on the left side of the assignment operator should be equal  to the number of items we have in the list.
# first, second = numbers # we got the error

# we unpack only the first two element of list and pack other element in another variable:
first, second, *other = numbers
print(first)
print(second)
print(other)

# when we prefix a parameter with an asterisk, Python would get all these arbitrary argument and packed them into a list:


def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total


multiply(1, 2, 3, 4, 5, 6)

# if we want only first and last item in the list:
first, *other, last = numbers
print(first)
print(last)
print(other)
