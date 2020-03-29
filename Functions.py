def func1(name):
    return f"Hello {name}"


def func2(name):
    return f"{name} , how you doing?"


def func3(func4):
    return func4('Dear learner')


print(func3(func1))

print(func3(func2))


def func():
    print("first funtion")

    def func1():
        print("first chid function")

    def func2():
        print("Second chaild function")

    func2()
    func1()

""" Child function"""

def func(n):
    def func1():
        return "srinivas"
    def func2():
        return "GPC"
    if n == 1:
       return func1
    else:
        return func2

a = func(1)
b = func(2)

print(a())
print(b())

