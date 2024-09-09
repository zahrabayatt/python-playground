# by is optional parameter. all optional parameters should comes after required parameters.
def increment(number, by=1):
    return number + by


print(increment(2))
print(increment(2, 5))
