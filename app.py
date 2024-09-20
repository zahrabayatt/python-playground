items = [
    ("product1", 10),
    ("product2", 9),
    ("product3", 12),
]


def sort_item(item):
    return item[1]

# items.sort(key=sort_item)


# another way is use lambda functions:
items.sort(key=lambda item: item[1])

print(items)
