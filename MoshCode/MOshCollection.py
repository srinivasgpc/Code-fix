from array import array
from pprint import pprint
from collections import deque
from sys import getsizeof
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
print(point[0:2])
# x,y,z = point
if 10 in point:
    print("exists")

# we cant add any items in tuples

#Uses, not to modify any sequence of items in a set of things


#Swapping valriable

x= 10
y= 11

z= x
x= y
print(x,y,z)


#ARRAYS

number =array("f",[1, 2, 3])
number[0] = 1.0
print(number)


#delete duplicates in Array

num = [1, 2, 2, 2, 3, 4, 4]

first =set(num)
second = {1, 4}
#union and intersection
print(first | second , first & second , first ^ second , first - second    )

#set doesnt supports indexs

if 1 in first:
    print("yes")

#dictionary
"""
list()
tuple()
set()
dict()
"""

point = {"x": 1, "y": 2}
point = dict(x=1, y=2)
point["x"] =5
point["z"] =10
print(point.get("a",0))
del point["x"]
print(point)


values = [] #empty array
for x in range(5):
    values.append(x*2) # adding values to the array
# comprehensions can be use in dict, lists, set
values = [x*2 for x in range(100000)]
print("list:", getsizeof(values))
values = (x*2 for x in range(100000))
print("gen:", getsizeof(values))
print(values)

#printing of individual item (unpacking elements)

numb = [1,2,3]
values =[*range(5), *"Hello"]
print(*numb, values)

first = {"x": 1}
second = {"x": 10, "y": 1}
combined = {**first, **second, "z": 1}
print(combined)

#program to count the charectorsin the sentance

sentance = "This is a common interview question"

char_frequency ={}
for char in sentance:
    if char in char_frequency:
        char_frequency[char] += 1
    else:
        char_frequency[char] = 1
print(sorted(char_frequency.items(), key=lambda kv:kv[1], reverse= True))
