from collections import deque
from queue import LifoQueue

#basic stack

# stack = []

# stack.append("first")
# stack.append("second")
# print(stack)

# stack.pop()
# print(stack)

#stack through deque

# stack = deque()
# stack.append("nazmul")
# stack.append("hasan")
# print(stack)

#stack in queue

stack = LifoQueue(maxsize=3)
stack.put("naz")
stack.put("mul")
stack.put("hasan")
print(stack.full())

