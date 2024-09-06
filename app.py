# whenever you work with texts you should surround your text with quotes.

# You can either use double quotes or single quotes. That's more of a personal preference, but quite often we use double quotes.

course_name = "Python Programming"

# We also have triple quotes and we use them to format a long string. for example if you have, let's say a variable message. That is the message we want to include in the body of an email. You can use triple quotes to format it like this.

message = """
Hi John, 

This is Zahra from companyName.com

Blah blah blah
"""

# a few useful things you can do with strings:

# - For getting the length of strings, we have built-in function:
print(len(course_name))

# - For getting access to a specific character in the string, we use square bracket notation:
print(course_name[0])  # it returns first character form the start of string
print(course_name[2])  # it returns third character form the start of string
print(course_name[-2])  # it returns second character form the end of string

# - For slicing a string, we can use:
print(course_name[0:3])
print(course_name[0:])
print(course_name[:3])
print(course_name[:])  # it returns a copy of original string
