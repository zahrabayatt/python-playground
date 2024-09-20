letters = ["a", "b", "c"]

print(letters.index("c"))

# if item doesn't exist in the list we got the error
# print(letters.index("d"))

# to prevent this error we should first check the item is exist and then find it in the list:
if "d" in letters:
    print(letters.index("d"))

# to get numbers of the item with specific value:
print(letters.count("d"))

# we must to pass a argument to count method unless we got the error
# print(letters.count())
