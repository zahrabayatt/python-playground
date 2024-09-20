numbers = [3, 51, 2, 8, 6]

# sort acc
numbers.sort()

# sort dec
numbers.sort(reverse=True)

# to get the new list with specific sort:
print(sorted(numbers, reverse=True))
print(sorted(numbers))

print(numbers)

items = [
    ("product1", 10),
    ("product2", 9),
    ("product3", 12),
]

# for sorting lists with complex object like list of topples, the sort method didn't work
items.sort()
print(items)

# to sort list with complex object:


def sort_item(item):
    return item[1]  # sort items base on price


items.sort(key=sort_item)
print(items)
