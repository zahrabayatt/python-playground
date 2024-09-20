items = [
    ("product1", 10),
    ("product2", 9),
    ("product3", 12),
]

prices = []
for item in items:
    prices.append(item[1])

print(items)
print(prices)

# better way is using map function:

map_object = map(lambda item: item[1], items)

prices = list(map(lambda item: item[1], items))

print(map_object)
print(prices)
