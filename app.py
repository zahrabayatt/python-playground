# Debug this code using vs code

def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
        return total


print("Start")
print(multiply(1, 2, 3))
