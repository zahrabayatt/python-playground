# rasing exceptions comes with the cost and we not use them often:

from timeit import timeit

code1 = """
def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("Age cannot be 0 or less.")
    return 10 / age


try:
    calculate_xfactor(-1)
except ValueError as error:
    # print(error)
    pass # this pass statement doesn't do anything, and we use it because except block can not be empty.
"""

code2 = """
def calculate_xfactor(age):
    if age <= 0:
        return None
    return 10 / age

xfactor = calculate_xfactor(-1)
if xfactor == None:
    pass
"""
# print time execution of code1 after 1000 times execution.
print("Code1=", timeit(code1, number=10000))
print("Code2=", timeit(code2, number=10000))

# In small applications with few users, raising exceptions won't significantly affect performance. However, in performance-critical applications, it's better to only raise exceptions when necessary. A general guideline is to first consider handling issues with simple if statements, as this can result in cleaner and more efficient code. Only raise exceptions when truly needed.
