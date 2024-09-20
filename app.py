letters = ["a", "b", "c"]

# Adding Items in Lists:

# Add item to end of the list
letters.append("d")

# Add item in specific position in the List
letters.insert(2, "-")

# Add item in the begining of the list
letters.insert(0, "h")


# Remove items in lists:

# Remove item at the end of the list
letters.pop()
# you can pass the index to remove a item in given index
letters.pop(0)

# remove a first item with specific value
letters.remove("-")
# for remove all items with specific value you should iterate the letter and use remove method

# another way to delete item in specific position
del letters[0]

# delete a range of items in the list
del letters[0:2]

# to remove all items in the list
letters.clear()

print(letters)
