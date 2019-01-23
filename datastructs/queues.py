# queue function. First in first out
# using deque since queues are inefficient in python

from collections import deque

queue = deque()

queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)

x = queue.popleft()

print(queue)
