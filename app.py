try:
    age = int(input("Age: "))
    xfactor = 10/age
except ValueError as ex:
    print("You didn't enter a valid age.")
except ZeroDivisionError:
    print("Age can not be zero.")
else:
    print("No exceptions were thrown.")
print("Execution continues.")


try:
    age = int(input("Age: "))
    xfactor = 10/age
except (ValueError, ZeroDivisionError) as ex:
    print("You didn't enter a valid age.")
    print(ex)
except ZeroDivisionError:
    print("Age can not be zero.")  # it is not going to be executed!
else:
    print("No exceptions were thrown.")
print("Execution continues.")

# if we have multiple except, and one of them executed, other ones are going to be ignored.
