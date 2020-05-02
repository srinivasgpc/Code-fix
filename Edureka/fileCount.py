import os

# Open a file
path = "/Users\DELL\PycharmProjects\Code-fix"
dirs = os.listdir( path )

a =len(dirs)
print("number of files = ",a)

# This would print all the files and directories
for file in dirs:
    print(file)

