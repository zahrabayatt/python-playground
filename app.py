items = [
    ("product1", 10),
    ("product2", 9),
    ("product3", 12),
]

# Filter list and get items with price greater than or equal 10

x = filter(lambda item: item[1] >= 10, items)

print(x)

# x is a iterable object:
for item in x:
    print(item)

filtered_items = list(filter(lambda item: item[1] >= 10, items))

print(filtered_items)
