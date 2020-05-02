
"""
ATM Transaction with $dollor
Categories:
1. Balance enquiry
2. Cash Withdrawl
3. Pay In Cash
4. Return your Card
"""
print("Well come to SBI")
chances=3
restart ="Y"
balance= 67.4
while chances>=0:
    pin = int(input("Please enter your 4 digit pin:"))
    if pin == (1234):
        print("You entered correct pin")
        restart = ("Y")
        while restart not in ("NO", "n", "no", "N"):
            print("Press 1 To check balance:\n")
            print("Press 2 To Withdrawl Cash:\n")
            print("Press 3 To Pay in:\n")
            print("Press 4 To Return Card:\n")
            option = int(input("WHAT DO YOU CHOOSE?"))
            if option == 1:
                print("Your balance is A$", balance, "\n")
                restart = input("Would you like to choose \n")
                if restart in ("NO", "n", "no", "N"):
                    print("Thankyou")
                    break
            elif option == 2:
                withdrawl = float(input("How much amount would you like to withdraw ? \n $20 $40 $60 $80 $100 ?"))
                if withdrawl in [10, 20, 60, 40, 100, 80 ]:
                    rembalance =balance - withdrawl
                    if rembalance <0:
                        print("insufficent balance")
                    else:
                        print("\nRemaining balance is: ", rembalance)
                    restart=input("would you like to go back?")
                    if restart in ("NO", "n", "no", "N"):
                        print("Thankyou")
                        break
                elif withdrawl not in [10, 20, 60, 40, 100, 80 ]:
                    print("please enter valid amount!\n")
                    restart=("Y")
                elif withdrawl ==1:
                    withdrawl = float(input("Enter a desire number:"))
            elif option ==3:
                Pay_in = float(input("How much amount would you Pay IN?"))
                balance = balance + Pay_in
                print("\nRemaining balance is: ", balance)
                restart = input("would you like to go back?")
                if restart in ("NO", "n", "no", "N"):
                    print("Thankyou")
                    break
            elif option ==4:
                print("\nPlease wait we will return your Card!")
                print("Thank you using Sbi, Have a Great day!")
                break
            else:
                print("Please enter a correct number. . .\n")
                restart=("Y")
    elif pin != ('1234'):
        print("incorrect Pin")
        chances =chances-1
        if chances==0:
            print("\n no tries left")
            break



