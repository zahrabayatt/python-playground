successful = True
# successful = False
for number in range(3):
    print("Attempt", number, number * ".")
    if successful:
        print("Successful")
        break
else:  # Executed when the for never breaks and complete iteration
    print("Attempted 3 times and fail")
