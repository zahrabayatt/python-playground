# Scope: it refers to to the region of the code where a variable is defined.

# in this example the scope of the name and message variables are the great function and we refer to these variables as local variables in this function. they are local in this function which means they don't exist anywhere else. And that means we can have another function with the same variable names and they are completely separate.


def greet(name):
    message = "a"  # the scope of this variable is the great function.


def send_email(name):
    message = "b"

# print(message) // we got error


# these variables have a short lifetime, so in this example when we call the great function and pass the name, Python interpreter will allocate some memory and have the name and message variables reference those memory locations. when we finish executing the greet function because these variables are not referenced or used anywhere else eventually they get garbage collected, which means Python Interpreter will release the memory that allocated for these variables.
greet("Zahra")

# In contrast to local variables, we have global variables. If we define a variable outside of the function, now it's a global variable. which means it's accessible anywhere in this file, So the scope of this variable is this file.  We can use it anywhere in this file in any functions or outside of a function.

# for this reason, global variables stay in memory for a longer period of time until they are garbage collected. And you should not use them that often. In fact global variables are really evil. so as a best practice create functions with parameters and local variables.

message = "c"

greet("Zahra")
print(message)
# a - because by default Python interpreter treats this message variable as a local variable at the greet function, even though it has the same name as the global variable that we defined, So these two variables are separate.

# Modifying global variables within functions using the global keyword can lead to bugs because changes in one function may unexpectedly affect other functions that rely on the same variable. This practice makes the code harder to manage and debug. The advice is to avoid modifying global variables inside functions unless absolutely necessary.

# Example:
# message = "c"

# def greet(name):
#     global message
#     message = "b"

# greet("Zahra")
# print(message) #output: c
