
#QUEUES/DEQUEUES
from collections import deque

q = deque()

q.append('W')
q.append('E')
q.append('W')

print("INITIAL QUEUE:")
print(q)

print("\nDEQUEUED ELEMENTS FROM THE QUEUE:")
print(q.popleft())
print(q.popleft())
print(q.popleft())

print("\nQUEUE AFTER REMOVING ELEMENTS:")
print(q)