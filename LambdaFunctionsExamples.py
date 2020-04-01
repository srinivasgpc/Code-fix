# lambda arugments: expression
from functools import reduce
x = lambda a: a*a
print(x(3))

# anonymous fuctions within user defined functions


def A(x):

    return(lambda y:x+y)


t = A(4)
print(t(8))

# Lambda within a filter

mylist = [2, 3, 4, 5, 6]
newlist = list(filter(lambda a:(a/3==2), mylist))# SYNTAX: filter(funtion, interables
print(newlist)

#Map
mylist = [2, 3, 4, 5, 6]
newlist = list(map(lambda a:(a/3!=2), mylist))# SYNTAX: filter(funtion, interables
print(newlist)

#reduce

x= reduce(lambda a,b: a+b, [23, 56, 43, 98, 1])
print(x)

# solve algebra expressions
# inear expression 3x+4y

s =lambda x,y: 3*x+4*y
print(s(4,7))

# quadradic expression

b = lambda a,b: (a+b)**2
print(b(2,3))

# map-Reduce fucntions

output = list(map(lambda x: x+3, [1,2,3,4]))
print(output)


output = list(filter(lambda x: x>=3, [1,2,3,4]))
print(output)

output = reduce(lambda x,y: x*y, [1,2,3,4,5])
print(output)


#filter within the map function

c = tuple(map (lambda x:x+x, filter(lambda x: (x>=3), (1,2,3,4,5))))
print(c)

c = set(filter(lambda x:(x>=4), map(lambda x: x+x, (1,2,3,4,5,6))))
print(c)
#map and filter with in reduce

r =reduce(lambda x,y:x+y, map(lambda x:x+x, filter(lambda x:(x<=4),[1,2,3,4,5,6])))
print(r)