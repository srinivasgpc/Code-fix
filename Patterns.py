# pyramid
print("pyramid")


def pattern(n):
    k = 2 * n - 2
    for i in range(0, n):
        for j in range(0, k):
            print(end=" ")
        k = k - 1
        for j in range(0, i + 1):
            print("* ", end="")
        print("\r")


pattern(5)


# inverse paramide
print("inverse paramid")


def pattern(n):
    k = n - 2
    for i in range(n, -1, -1):
        for j in range(k, 0, -1):
            print(end=" ")
        k = k + 1
        for j in range(0, i + 1):
            print("* ", end="")
        print("\r")


pattern(5)


# right start pattern
print("right start pattern")


def pattern(n):
    for i in range(0, n):
        for j in range(0, i + 1):
            print("* ", end="")
        print("\r")
    for i in range(n, -1, -1):
        for j in range(0, i + 1):
            print("* ", end="")
        print("\r")


pattern(5)


# left start pattern
print("left start pattern")


def pattern(n):
    k = 2 * n - 2
    for i in range(0, n - 1):
        for j in range(0, k):
            print(end=" ")
        k = k - 2
        for j in range(0, i + 1):
            print("* ", end="")
        print("\r")
    k = - 1
    for i in range(n - 1, -1, -1):
        for j in range(k, -1, -1):
            print(end=" ")
        k = k + 2
        for j in range(0, i + 1):
            print("* ", end="")
        print("\r")


pattern(5)


# hour class pattern
print("hour class pattern")


def pattern(n):
    k = n - 2
    for i in range(n, -1, -1):
        for j in range(k, 0, -1):
            print(end=" ")
        k = k + 1
        for j in range(0, i + 1):
            print("* ", end="")
        print("\r")


pattern(5)

print("Left half paramid")


def pattern(n):
    k = 2 * n - 2
    for i in range(0, n + 1):
        for j in range(0, k):
            print(end=" ")
        k = k - 1
        for j in range(0, i + 1):
            print("* ", end="")
        print("\r")


pattern(5)


# half right pyramid:
print("half right pyramid")


def pattern(n):
    for i in range(0, n):
        for j in range(0, i + 1):
            print("* ", end="")
        print("\r")


pattern(5)


# half right down pyramid:
print("half right down pyramid")


def pattern(n):
    k = 2 * n - 2
    for i in range(0, n):
        for j in range(0, k):
            print(" ", end="")
        k = k - 2
        for j in range(0, i + 1):
            print("* ", end="")
        print("\r")


pattern(5)


# half left down pattern:
print("Half left down pattern")


def pattern(n):
    for i in range(n, -1, -1):
        for j in range(0, i):
            print("* ", end="")
        print("\r")


pattern(5)


# diamond star  pattern:
print("Diamond star  pattern")


def pattern(n):
    for i in range(5):
        for j in range(5):
            if i + j == 2 or i - j == 2 or j - i == 2 or i + j == 6:
                print("*", end="")
            else:
                print(end=" ")
        print()


pattern(5)

"""
NUMBER PATTERNS
"""
print("NUMBER PATTERNS")


def pattern(n):
    x = 0
    for i in range(0, n):
        x += 1
        for j in range(0, i + 1):
            print(x, end=" ")
        print("\r")
    x = n + 1
    for i in range(n - 1, -1, -1):
        x -= 1
        for j in range(0, i + 1):
            print(x, end=" ")
        print("\r")


pattern(5)


# pascal traingle
print("Pascal traingle")


def pattern(n):
    for i in range(0, n):
        for j in range(0, i + 1):
            print(function(i, j), " ", end="")
        print()


def function(n, k):
    res = 1
    if k > n - k:
        k = n - k
    for i in range(0, k):
        res = res * (n - i)
        res = res // (i + 1)
    return res


pattern(7)


print("half right number pattern pyramid")


def pattern(n):
    x = 0
    for i in range(0, n):
        x = x + 1
        for j in range(0, i + 1):
            print(x, end=" ")
        print("\r")


pattern(10)


def pattern(n):

    for i in range(n, 0, -1):
        for j in range(1, i+1):
            print(j, end=" ")
        print("\r")


pattern(5)

"""
Charector value patterns
"""

def pattern(n):
    x=65
    for i in range (0, n):
        ch = chr(x)
        x = x + 1
        for j in range (0, i+1):
            print(ch, end=" ")
        print("\r")

pattern(26)


print("Pyramid pattern with alphabets")


def pattern(n):
    k = 2*n - 2
    x = 65
    for i in range(0, n):
        for j in range(0, k):
            print(end=" ")
        k = k -1
        for j in range(0, i+1):
            ch = chr(x)
            print(ch, end=" ")
            x += 1
        print("\r")
pattern(10)

print("K style Printing letter, k ")

for i in range(7):
    for j in range(7):
        if j == 0 or i - j == 3 or i + j == 3:
            print("k ", end="")
        else:
            print(end=" ")
    print()




