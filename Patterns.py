# pyramid
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


# inverse paramid
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
def pattern(n):
    for i in range(0, n):
        for j in range(0, i + 1):
            print("* ", end="")
        print("\r")


pattern(5)


# half right pyramid:

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


# downard half right pattern:

def pattern(n):
    for i in range(n, -1, -1):
        for j in range(0, i):
            print("* ", end="")
        print("\r")


pattern(5)


# diamond star  pattern:

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
