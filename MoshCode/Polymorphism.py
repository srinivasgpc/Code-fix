from abc import ABC, abstractmethod
from collections import namedtuple
# poly means many and morph means forms is known as polymorphism

# defining a base class and then we define the common methons in it
class UIControl(ABC):
    @abstractmethod
    def draw(self):
        pass

class TextBox(UIControl):
    def draw(self):
        print("TextBox")

class DropDownList(UIControl):
    def draw(self):
        print("DropDownList")
# controls has to be iterable to access the for loop

#duckTyping

def draw(controls):
    for control in controls:
        control.draw()


ddl = DropDownList()
textbox = TextBox()
draw([ddl, textbox])


class Text(str):
    def duplicate(self):
        return self + self

text = Text("Python ")

print(text.duplicate())


class TrackableList(list):
    def append(self, object):
        print("Append called")
        super().append(object)


list =TrackableList()
list.append("1")


#Data Classes


class Point:
    def __init__(self, x, y):
        self.x =x
        self.y =y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
p1 = Point(1,2)
p2 = Point(1,2)

print(id(p1))
print(id(p2))



Point = namedtuple("Point", ["x", "y"])
p1 = Point(x =1, y =2 )
p1.x = 10

p1 = Point(x =1, y =2 )