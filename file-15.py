import os
import shutil
path='fold'
try:
    #os.remove(path)
    #os.rmdir(path)
    shutil.rmtree(path)
except FileNotFoundError:
    print("not found")
except IsADirectoryError:
    print("yes it is")
except OSEError:
    print("is empty")
else:
    print("deleted")
