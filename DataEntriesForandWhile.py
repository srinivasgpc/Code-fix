
travelling = input("Are you yes or no")
while travelling =="yes":
    n = int (input("Enter number of persons:"))
    for n in range(1,n+1):
        name =input("name")
        age=input("age")
        sex=input("sex")
        print(name)
        print(age)
        print(sex)
        travelling =(input("OOps forgot someone:"))
