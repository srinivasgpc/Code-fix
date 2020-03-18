
# factorial defining a for loop
n = int(input("Enter a number :"))
factorial =1
if n <= 0:
    print("please enter a positive number n.")
else:
    for i in range(1, n + 1):
        factorial = factorial * i
print("Factorial of", n, 'is', factorial)

#nested loop