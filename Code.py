from collections import defaultdict
print("damn it works")
print("damn it works tooooooooooo")
name = 'srinivas'
print(name)
print(name.upper())
print (name[2:5])
L1 =['ray', 'taz', 'ytr', 'yug', 'taz'] #list
print(L1)
L1.append(6)
print(L1)
L1.insert(2, 'tad')
print(L1)
L1.reverse()
print(L1)
Courses = {1: 'Science', 2: 'Social', 2: 'Soal', 3: 'Math', 'fourth': 'Chemistry'} #dictiionary
print(Courses)
print(Courses[3])
print(Courses.get('fourth'))
Courses['fourth'] = 'language C'

print(Courses)
bag = (10, 30, 10, 10, 'pen', 'pencile', 'chocolate', 'pen') #tuple
print(bag)
print(bag.count('pen'))
set ={'ram', 'raju', 'shtam', 'ram'} #Set
print(set)
print(list(range(100, 300)))
print(list(range(100)))
# type coversion

x=10
name= 'ram'
b= {4, 4, 6}
print(str(x) +name, tuple(b), list(b))
""" 
lists-
declared in square [] brackets,
allows duplicates, 
elements can be access with indexes 
 it is mutable change the data
sets -
-unordered 
-declare in curly () brackets
- can not access with index
- no duplicate allowed
tuples -
ordered and can not chance once we declare
duplicate allows
Dictionary- with key value pairs
change the values 
() declaration
"""
"""
Specialise collection data types
namedtuple() - returns with a named valued for each element in the tuple
deque() - optimize to list for deletion and insertion
chaninmap() - dictionary type like class for creating a single view of multiple mappings
Counter() - Counter is a dictionary subclass for counting hashable objects.
OrderedDict() - OrderedDict is dictionary subclass which remembers the order in which the entries were done
Defaultdict() - subclass which callsa factory fuction to supplymissing values
UserDict()- class acts a wrapper arount dictionaryobject for easier dict sub-classing
UserList()- wrapper around list objects for easier List sub-classing
UserString()- wrapper around Sring objects for easier String sub-classing
"""
#namedtuple()
# a = namedtuple("courses", "name , tecchnology" )
# print(s)
#deque
# a2 = [10, 20, 30]
# d =deque(a2)
# d.appendleft('pyhton')
# print(d)
# d.popleft() #delete element python
# print(d)

#Chanimap
# a ={1: 'emra', 2: 'lafoot'}#dictionaries
# b ={3: 'mo', 4: 'dda'}
# a1 =ChainMap(a,b)
# print(a1)

#Counter
# a =[1,2,2,2,2,2,3,4,5,6,6,6,6,]
# c = Counter(a)
# print(c)
# print(list(c.elements()))
#
# sub ={2:1 , 5:1}
# print(c.subtract(sub))
# print(list(c.most_common()))

#OrderedDict
#
# d =OrderedDict()
# d[1] ='f'
# d[2] = 'r'
# d[3] = 'a'
# d[4] = 'd'
# d[5] = 'v'
# d[6] = 'b'
# d[7] = 'u'
# print(d)
# print(d.keys())
# print(d.get())

#defaultdict


d = defaultdict(int)
d[1] = "ram"
d[2]="laxman"
print(d[3])
