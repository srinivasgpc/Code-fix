"""

Find the Closest value to the given number

In a Array containing duplicate values and nagative numbers.

Examples:

    Input : arr[] = {1, 2, 3, 4, 5, 6, 6, 7, 9, 10 , 11}

    Target number = 11

    output = 9
     9 is the closest value to 11 in the given array


"""


A =[2,4,5,6,10, 11,]





def find_closest_num(A, target):
    min_diff = float("inf")
    low = 0
    high = len(A) - 1
    closest_num = None

    # Edge cases for empty list or
    #when the list is only one element.
    if len(A) == 0:
        return None
    if len(A) == 1:
        return A[0]


    while low <= high:
        mid = (low + high) // 2

        if mid + 1 < len(A):
            min_diff_right = abs(A[mid +1] - target)

        if mid > 0:
            min_diff_left = abs(A[mid - 1] - target)

        #check if the absolute value btw left and aright
        # elements are smaller than any seen prior


        if min_diff_left < min_diff:
            min_diff = min_diff_left
            closest_num = A[mid - 1]

        if min_diff_right < min_diff:
            min_diff = min_diff_right
            closest_num = A[mid +1]

        # MOve the mid-point accordingly as is done
        # via binary target

        if A[mid ] <  target:
            low  = mid +1
        elif A[mid] > target:
            high = mid -1
        else:
            return A[mid]

    return closest_num



y = find_closest_num(A, 8)
print(y)



