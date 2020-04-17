from collections import deque
queue = deque([])
queue.append(1)
queue.append(2)
queue.append(3)
queue.popleft()
print(queue)
if not queue:
    print("empty")


#Tuples

point = (1, 2) * 3
# print(type(point))
print(point)

# we cant add any items in tuples