# command = ""
# while command.lower() != "quit":
#     command = input(">")
#     print("ECHO", command)

while True:
    command = input(">")
    print("ECHO", command)
    if command.lower() == "quit":
        break
