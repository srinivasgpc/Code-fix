from pathlib import Path
from time import ctime
import shutil
from zipfile import ZipFile
path = Path("MoshCode/Modules/Library")


# path.exists()
# path.mkdir()
# path.rmdir()
#path.stat() #statistics
#  path.rename("Library2")
print(ctime(path.stat().st_ctime))
# path.iterdir() #iterate it and generate new on

#all directories
path = [p for p in path.iterdir() if p.is_dir()]

print(path)

#all py files

py_files = [p for p in path.glob("*.py")]

print(py_files)


#copy files from source to target

source = path("")
target = path()/"__init.py"

shutil.copy(source, target)
target.write_text(source.read_text())



#working with zipfiles

with ZipFile("files.zip", "w") as Zip:
    for path in Path("Library").rglog("*.*"):
        zip.write(path)

with ZipFile("files.zip", "w") as Zip:
    print(zip.namelist())
    info = zip.getinfo("Library/__init__.py")
    print(info.file_size)
    print(info.compress_size)
    zip.extractall