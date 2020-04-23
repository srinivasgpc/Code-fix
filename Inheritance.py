





# Relation between animal and mammal
#Self represents the current object
class Animals:
    def __init__(self):
        print("Animal constructure")
        self.age = 1
    def eat(self):
        print("eat")


class Mammal(Animals):
    def __init__(self):

        print("mammal constructure")
        self.weight = 2
        super().__init__()
    def walk(self):
        print("walk")

class Fish(Animals):
    def swim(self):
        print("swim")

class Bird(Animals):
    def fly(self):
        print("fly")

class Chicken(Bird):
    pass

m = Mammal()
m.eat()
m.walk()
## returnss boolean if there is instance
print(isinstance(m, Animals))

print(m.weight)
print(m.age)


# Multiple inheritance

class Employee:
    def greet(self):
        print("Employee Greet")

class Person:
    def greet(self):
        print("Person Greet")

class Manager(Employee, Person):
    pass
#create object
manager =Manager()

manager.greet()

#Extending builtin types

class Text(str):
    def duplicate(self):
        return self + self

text = Text("Python")

print(text.duplicate())


class TrackableList(list):
    def append(self, object):
        print("Append called")
        super().append(object)

list = TrackableList()
list.append("1")

#
#Data Classes


class Point:
    def __init__(self, x ,y):
        self.x =x
        self.y =y
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
p1 = Point(1,2)
p2 = Point(1,2)

print(id(p1))
print(id(p2))