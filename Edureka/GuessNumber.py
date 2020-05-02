import random

n = 20
guess_random = int(n * random.random())+1

guess =0

while guess != guess_random:
    guess =int(input("new number:"))
    if guess>0:
        if guess>guess_random:
            print('is too large')
        elif guess<guess_random:
            print('number to short')
    else:
        print("sorry that you give up")
        break
else:
    print("congradulation correct number")






