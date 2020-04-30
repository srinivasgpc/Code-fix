from pathlib import Path

# various way to denote path

Path(r"C:\Program Files")# absolute path with raw string
Path("/user/local") #related path
Path()#path object
Path()/"ecommerce" /"__init__.py" #combine path
Path.home()#home directory of the current user

#for comprehensive list goto pathlid in google
path = Path("ecommerce/__init__.py")

path.exists()
path.is_file()
path.is_dir()
print(path.name, path.stem, path.suffix, path.parent)# returns filename, without extention, return parent folder

path = path.with_name("file.txt")#use this to create new path with in the existing path

print(path.absolute())#gets absolute value of the path

path = path.with_suffix(".txt")#change the extention of the file

