# BackSlash \ is the escape Charactor

course = "   PYTHON \"course"
print(course)

#formatted Strings

first ="Srinivas"
Last = "Gaddam"
full = f"{first} {Last}"
print(full)

#Function Available on string

print(course.upper())
print(course.strip())
#find the index
print(course.find("cou"))
#replace the string

print(course.replace("P", "z"))

# Complex Numbers

x = 1 + 2j


y = 6 + 7j

z = x / y

print(z)

# rounding a number

print(round(2.9))

# abs of number

print(abs(-2.9))

# input value manually

x = input("x: ")



y = int(x) +1


print(f"x: {x}, y: {y}")

# IF Else using turnory operators
high_income =True
Good_Credit = True
student = False

if high_income and Good_Credit and not student:
    massage = "Eligible"
else:
    massage = " Not Eligible"

print(massage)

#Chaining Coparison Operators

age = 25

if 22 >= age < 65:
    print(age)

# For loop

for number in range(1, 10, 2):
    print("Attempt", number, number * '.')


# For loop 2

sucessfull = True

for number in range(3):
    print("Attempt")
    if sucessfull:
        print("sucessfull")
        break

else:
    print("Attempted 3 times and filed")

#Nested loops

for x in range(5): #Iterables with the value of range
    for y in range(3): # Child loop with respective parent
        print(f"({x}, {y})")

# Display hte list of items

for x in [1, 2, 3, 4, 5]:
    print(x)

# While loop

#repeat something as long as the condition is true


number = 100

while number>0:
    print(number)
    number //=2
    break

while True:
    command = input(">")
    print("ECHO", command)

#Infinate loop
    if command.lower() == "quit":
        break
count =0
for x in range(1, 10):
    if x%2 == 0:
        count += 1
        print(x)
print(f" we have count even numbers of {count}")







