#writing files

#text="Have a nice day:\n"
#ith open('test.txt','a') as file:
  #   file.write(text)


#copying files

#import shutil

#shutil.copy('test.txt','copy.txt')


#move files

#import os
#source="pink.txt"
#destination="//home//alpha//Projects//pink.txt"
#try:
   # if os.path.exists(destination):
      # print("already its there")
    #else:
      # os.replace(source,destination)
#       print(source+" was moved")
#
#except FileNotFoundError:
#    print(source+" was not found")
