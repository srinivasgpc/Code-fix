# date 5th may 2020

# Today learning algorithm
#Binary Search with python

data = [2, 3, 4, 5, 8, 9, 12, 22, 25, 28, 33, 23, 37]
target = 28


# Linear Search

def linear_search( data, target ):
    for i in range(len(data)):
        if data[i] == target:
            return True
    return False

#iterative Binary search

def binary_search_iterative(data, target):
    low = 0
    high =len(data)

    while low <= high:
        mid = (low + high) //2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            high = mid+1
        else:
            low = mid -1
    return False

#Recursive BInary Search

def binary_Search_Recursive(data, target, low, high):
    if low >high:
        return False
    else:
        mid = (low - high) // 2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            return binary_search_iterative(data, target, low, mid-1)
        else:
            return binary_search_iterative(data, target, mid+1, high)

print(binary_search_iterative(data, target))
print(binary_Search_Recursive(data, target, 0, len(data)-1))





