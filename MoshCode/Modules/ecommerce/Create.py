
from MoshCode.Modules.ecommerce.shopping import Sales


#returns directory of the module
print(Sales.__name__)
print(Sales.__package__)

print(Sales.__name__)
from pathlib import Path

path = Path("MoshCode/Modules/ecommerce")


# path.exists()
# path.mkdir()
# path.rmdir()
#path.stat() #statistics
#  path.rename("ecommerce2")
#
# path.iterdir() #iterate it and generate new on

#all directories
path = [p for p in path.iterdir() if p.is_dir()]

print(path)

#all py files

py_files = [p for p in path.glob("*.py")]

print(py_files)