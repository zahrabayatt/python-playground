def save_user(**user):
    print(user)
    print(user["id"])
    print(user["name"])


save_user(id=1, name="Zahra", age=22)  # pass multi keyword arguments

# Dictionary: it's a complex type. e.g. {'id': 1, 'name': 'Zahra', 'age': 22}
