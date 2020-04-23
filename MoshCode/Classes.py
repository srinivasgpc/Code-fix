"""
Class:  is a blueprint for creating new objects
Object: instance of a class

Class: Human
Objects: John, Mary, Jack
"""
class Point:

    def __init__(self, x, y):
        self.x =x
        self.y=y

    @classmethod
    def zero(cls):
        return cls(0,0)

    def __str__(self):
        return f"({self.x}, {self.y})"

    def draw(self):
        print(f"Point ({self.x}, {self.y})")

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __gt__(self, other):
        return self.x > other.x and self.y > other.y



point =Point(2,20000)
other = Point(1,1000)
print(str(point > other))

class TagCloud:
    def __init__(self):
        self.__tags = {}
    def add(self, tag):
        self.__tags[tag.lower()] = self.__tags.get(tag, 0) + 1
    def __get__(self, tag):
         return self.__tags.get(tag.lower(), 0)
    def __set__(self, tag, count):
        self.tages[tag.lower() ] = count

    def __len__(self):
        return len(self.__tags)
    def __iter__(self):
        return iter(self.__tags)

cloud =  TagCloud()
#cloud["python"] = 10
cloud.add("Python")
cloud.add("python")
cloud.add("Python")

print(cloud.__tags)