#integer Exception

try:
    with open("ATM.py") as file:
        print("File Opened")
    age = int(input("Age: "))
    xFactor = 10/ age
except (ValueError,ZeroDivisionError ):
    print("You didn't enter the valid age.")
else:
    print("No exceptions were thrown.")
finally:
    file.close()
