items =[
    ("product1",10),
    ("product2",9),
    ("product3",12),
]
# SOrting
def sort_item(item):
    return item[1]

items.sort(key=sort_item)
print(items)

# sorting with lambda functions

items.sort(key=lambda item:item[1])
print(items)


# Transform this list to list of numbers

prices =[]

for item in items:
    prices.append(item[1])

print(prices)

#using map funtion
# x = list(map(lambda  item: item[1], items))
#print(x)

#Filtered

y = list(filter(lambda item:item[1] >= 10, items))
print(y)

#Comprehension

z = [item[1] for item in items]
print(z)

zFilter = [item for item in items if item[1]>=10]
print(zFilter)


#Zip Function combines lists

list1 = [1, 2, 3]
list2 = [10, 20, 30]

print(list(zip("abc",list1, list2)))


# STACK DIFFERS LIST OF ITEMS

stack =[]
stack.append(2)
stack.append(3)
stack.append(5)

print(stack)

#pop to remove item  top of the stack

last = stack.pop()
print(last)
print(stack)

#redirect

if not stack:
    stack[-1]

#Queues







