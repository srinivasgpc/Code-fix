# funtions
#Perform a task

def greet(first_name, last_name):
    print(f" Hello {first_name} {last_name} !") #Formmatted string
    print(f"How you doing {last_name}")

greet("Srinivas", "Gaddam")

#Return a Value

def get_greeting(name):
    return f"Hi {name}"

massage = get_greeting("Srinivas")

#collection of arguments

def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total

print('start')
print(multiply(2, 3, 4, 5))

# save information of a user

def save_user(**user): #double hash represents hold multiple values
    print(user)

save_user(id=1, name='srinivas', age = 22)

# Scope

message = 'a' # globle variable can access any time

def greet1(name):
    global message # modify in local
    message = 'b'

greet1("Srinivas")
print(message)


def fizz_buzz(input):
    if (input % 3 == 0) and (input % 5 == 0):
        return "FizzBuzz"
    elif input % 3 == 0:
        return "fizz"
    elif input % 5 == 0:
        return "buzz"

    return input

print(fizz_buzz(27))




