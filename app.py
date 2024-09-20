items = [
    ("product1", 10),
    ("product2", 9),
    ("product3", 12),
]

prices = list(map(lambda item: item[1], items))
# another way to map list, we can use List Comprehensions:
prices = [item[1] for item in items]

filtered_items = list(filter(lambda item: item[1] >= 10, items))
# another way to filter list, we can use List Comprehensions:
filtered_items = [item for item in items if item[1] >= 10]
