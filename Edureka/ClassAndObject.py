
class Choco():
    def __init__(self,DateOfManftu,BestBefore,  Price):
        self.DateOfManftu =DateOfManftu
        self.BestBefore = BestBefore
        self.Price = Price
# deefining class

    def Price_inc(self):
        self.Price = int(self.Price*1.15)


Dairy = Choco(2015, 2017, 50)
Kitkat = Choco(2013, 2014, 60)
#  print all the elements in the instance variable
print(Dairy.__dict__)


print(Dairy.Price)
Dairy.Price_inc()
print('New Price = ', Dairy.Price)


# INheritense with parent class
class SuperChoco(Choco):
   pass

Dairy = SuperChoco(2015, 2017, 50)
Kitkat = SuperChoco(2013, 2014, 60)

print( Dairy.BestBefore)
print(Dairy.Price)
Dairy.Price_inc()
print('New Price = ', Dairy.Price)


# overwrite the init metho=od with child and parent class


class Parent:
    def __init__(self, fname, fage):
        self.name = fname
        self.age = fage
    def view(self):
        print(self.name, self.age)

class Child(Parent):
    def __init__(self, fname, fage):
        Parent.__init__(self, fname, fage)
        self.lastname= "Kumar"
    def view(self):
        print( self.age, self.name, self.lastname)

ob =Child( "Srinivas", 23)
ob.view()
# single inheritance
class Parent:
    def func1(self):
        print('this is function 1')
class Child(Parent):
    def func2(self):
        print('this is function 2')

ob = Child()
ob.func1()
ob.func2()

#Multiple inheritence

class Parent:
    def func1(self):
        print('this is function 1')
class Parent2:
    def func3(self):
        print('this is function 3')
class Child(Parent, Parent2):
    def func2(self):
        print('this is function 2')

ob = Child()
ob.func1()
ob.func3()

#Multi Level interitence

class Parent:
    def func1(self):
        print('this is function 1')
class Parent2(Parent):
    def func3(self):
        print('this is function 3')

class Parent3():
    def func4(self):
        print('this is funtion 4')
class Child( Parent, Parent3):
    def func2(self):
        print('this is function 2')


ob.func1()
ob.func3()

#Hierarchi inheritance

ob1 = Parent2()


#hibrid inheritance


ob2 = Child()
ob2.func4()