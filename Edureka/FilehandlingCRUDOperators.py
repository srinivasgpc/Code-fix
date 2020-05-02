
import os
file = open("text.txt", "r")
# print(file.read())
for line in file:
    print(file.readline())
file.close()

""" File Handleing - writing"""

file = open("text.txt", "w")
file.write("Hello world")
file.write("hello world again")

file.close()


""" File Handleing - writing"""
#
# file = open("text.txt", "w")
# file.write("oops")
#
#
# file.close()


""" File Handleing - Create and write file"""

# file = open("new file1.txt", "x")
# file.write("Newtext createed by srk")

file.close()


""" File Handleing - Create and write file"""

# os.remove("new file.txt")
""" File Hantedleer for read"""


file = open("text.txt", "r")
print(file.readline())#read line only
print(file.readlines())# read all the lines
file.close()

if os.path.exists("new file1.txt"):
    os.remove("new file1.txt")
else:
    print("File doesnot exit")



