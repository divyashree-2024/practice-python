#import os

#import os
#path="//home//alpha//Desktop//test.py"
#3if os.path.exists(path):
    # print("that location exists")
     #if os.path.isfile(path):
        #print("this is file")
     #elif os.path.isdir(path):
        #print("thats a directory")
#else:
     #print("not exists")


#read file content

try:
   with open('//home//alpha//Desktop//test2.tx') as file:
       print(file.read())
except FileNotFoundError:
    print("That was not found:")
