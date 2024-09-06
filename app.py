# we use input function to get input from the user.

# as an argument that pass a string which will be a label that will be displayed in the terminal.

# Don't run this program using the code runner extension because code runner by default runs your program in the output window which is read only so you won't be able to enter a value!

# when we receive a input from the user, this input always comes as a string. so we need to convert this string to a number then we be able to add it to 1.

# In python we have a few built in functions for type conversion:
# int(x)
# float(x)
# bool(x)
# str(x)

# with type function which is a python built in function, we can find out the type of variable:
# type(x)

x = input("x: ")
print(type(x))

y = int(x) + 1
print(f"x: {x}, y: {y}")

# There are values that are not exactly a boolean True or False, but they can be interpreted as a boolean True or False. So, here are the falsy values in Python:
# "" - empty strings
# 0
# None - it is a object that presents the absence of a value.
# Anything else will be True

print(bool(0))
print(bool(1))
print(bool(-1))
print(bool(""))
print(bool("Hello"))
