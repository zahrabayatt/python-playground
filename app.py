letters = ["a", "b", "c"]
for letter in letters:
    print(letter)

# to get index and value of each element in list:

for letter in enumerate(letters):
    print(letter, letter[0], letter[1])

# The enumerate object yields pairs containing a index (from start, which defaults to zero) and a value yielded by the iterable argument.

# unpack the topple:
for index, letter in enumerate(letters):
    print(index, letter)
