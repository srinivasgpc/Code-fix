# Data Structures

#LISTS

letters = ["a", "b", "c", "d"]
matrix = [[0, 2], [3, 1]]
zeros = [0] * 5
combined = zeros + matrix
print(combined)
print(letters[0:-1])

#Dsplay every second or third element
print(letters[::2])

#list of numbers
numbers = list(range(20))
print(numbers)

#Display in reverse order

print(numbers[::-1])

#list on packing

number =[1,2,3,4,5,6,7]
first, second, *other, last = number

print(first)
print(other)
print(last)

#loop over the list

for letter in enumerate(letters):
    print(letter)

items = (0, "a")

index, letter = items

for index, letter in enumerate(letters):
    print(index, letter)

# adding and removiing list items

letters.append("f")
letters.insert(4,"e")

print(letters)
letters.pop()
letters.remove("a")
del letters[0:2]
print(letters)

