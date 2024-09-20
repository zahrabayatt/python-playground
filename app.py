# Stack: last in, first out

browsing_session = []
# Add item to top of Stack
browsing_session.append(1)
browsing_session.append(2)
browsing_session.append(3)
print(browsing_session)

# remove item from top of the Stack
last = browsing_session.pop()
print(last)
print(browsing_session)

# check stack is empty or not
if not browsing_session:
    print("list is not empty")

# get item from top of the Stack
if not browsing_session:
    print(browsing_session[-1])
