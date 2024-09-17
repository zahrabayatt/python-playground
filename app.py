letters = ["a", "b", "c", "d"]
print(letters[-1])  # return fist item from the end of the list
letters[0] = "A"  # modify items in list
print(letters)

# slice list
# # return a new list with first three items
print(letters[0:3])
# if we dont' specify the end index, by default the length of list will be used:
print(letters[0:])

# if we do't specify the first item, 0 be assumed by default:
print(letters[:3])

# get a copy of list
print(letters[:])

# step:
# we can specify the step so in this example it will return every second element in list form the beginning:
print(letters[::2])
# it will return every third element in the list from the end:
print(letters[::-3])

# we can get all original items of list in revers order with step:
numbers = list(range(21))
print(numbers[::-1])
