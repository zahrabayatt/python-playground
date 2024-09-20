try:
    # whenever we open a file using a with statement, python will automatically call file.close. in other words the with statement is used to automatically release external resources
    # we can open multiple file using the with statement:
    # with open("app.py") as file, open("another.txt") as target:

    with open("app.py") as file:
        print("File opened.")
        # if a object has these two magic methods, it supports the context management protocol. the magic method start with __
        file.__enter__
        file.__exit__
        # if a object supports the context management protocol, we can use as object with the with statement and we don't need finally block.

    age = int(input("Age: "))
    xfactor = 10/age
except (ValueError, ZeroDivisionError):
    print("You didn't enter a valid age.")
else:
    print("No exceptions were thrown.")
