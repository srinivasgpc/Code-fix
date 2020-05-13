

def FBH(age):
    max_heart_rate = 206.9-(0.67*age)
    target = 0.65* max_heart_rate


    print('your target fat-burning heart rate  is: ', round(target, 2))

FBH(age = int(input('Enter your age:')))

