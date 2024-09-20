from collections import deque
# Queue: First in- First out (FIFO)

# we can use a list to implement a Queue in Python, if the list is large, the efficient way is to use the deque object:

queue = deque([])
queue.append(1)
queue.append(2)
queue.append(3)
queue.popleft()

print(queue)
if not queue:
    print("empty")
