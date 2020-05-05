# sorting numbers in ascending order

def sort(n):

    for i in range(5):

        minpos = i

        for j in range (i, 6):

            if n[j] < n[minpos]:

                minpos = j

        temp = n[i]
        n[i] = n[minpos]

        n[minpos] = temp





n = [9, 7, 5, 2, 4, 8]
sort(n)
print(n)
