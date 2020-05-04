pos = -1

def binary(list, n):
    list = sorted(list)
    low = 0
    high = len(list) - 1
    while low <= high:
        mid = (low + high) // 2

        if list[mid] == n:
            globals()['pos'] = mid
            return True
        else:
            if list[mid] < n:
                low = mid + 1
            else:
                high = mid -1
    return False




list = [72, 98 ,7890, 54, 76 ,32, 1, 99, 85679]
n= 54

if binary(list,n):
    print('Number found at position', pos +1 )
else:
    print('NO number in the list')
