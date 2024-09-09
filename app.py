# So you have learned that we use for loops to iterate over iterable objects.

# In python We have another kind of loop that is a while loop:

number = 100
while number > 0:
    print(number)
    number //= 2  # or number = number // 2

# Example : simulate interactive python shell
command = ""
while command.lower() != "quit":
    command = input(">")
    print("ECHO", command)
