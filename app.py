# String Methods:

course = "  Python programming  "
print(course.upper())  # return a new string, original string didn't effected
print(course.lower())
print(course.title())
print(course.strip())  # trim space
print(course.rstrip())
print(course.lstrip())
print(course.find("pro"))
print(course.find("Pro"))
print(course.find("p"))
print(course.replace("p", "j"))
print("pro" in course)  # check if the string is exist in course
print("swift" not in course)
print(course)
