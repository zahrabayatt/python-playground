# fizz buzz algorithm:
# 3 -> Fizz
# 5 -> Buzz
# 15 -> Fizz Buzz
# others -> input

def fizz_buzz(input):
    if input % 15 == 0:
        return "FizzBuzz"
    elif input % 3 == 0:
        return "Fizz"
    elif input % 5 == 0:
        return "Buzz"
    return input


print(fizz_buzz(7))
