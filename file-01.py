#first_name="div"
#second_name="shr"
#full_name=first_name +""+second_name
#print("Hello" +full_name)
#age=20
#age+=1
#print("your age is:"+str(age))
#heigth=200.65
#print(heigth)
#print(type(heigth))
#human=False
#print(type(human))
#name,age,attend="div",20,100
#print(name,age,attend)
#name=age=attend=30
#print(name,age,attend)
#name="divya"
#print(len(name))
#print(name.find("d"))
#print(name.capitalize())
#print(name.upper())
#print(name.lower())
#p#rint(name.isdigit())
#print(name.isalpha())
#print(name.count("d"))
#print(name.count("c"))
#print(name.replace("v","d"))
#print(name*5)
#x=10
#y=19.20
#z="3"
##z=int(z)
##print(y*3)
#print(z*7)

#x = input('Enter your name:')
#age=int(input("how old r u:"))
#age=age+1
#print('Hello, ' + x)
#print("u r"+str(age)+"years old")
#import math
#pi=3.14
#x=10
#y=20

#print(round(pi))
#print(math.ceil(pi))
#print(math.floor(pi))
#print(math.sqrt(pi))
#3print(pow(pi,5))
#print(max(x,y))
#print(min(x,y))
#name="divya shree"
#first_name=name[:]
#last_name=name[2:11]
#frek_name=name[0:11:3]
#reversed_name=name[::-7]
#print(reversed_name)
#website="http://inner.com"
#slice=slice(4,-6)
#print(website[slice])
#age=int(input("how old r u:"))
#if(age<=50):
   #print(" match:")
#elif age==100:
   #print("century:")
#elif age<0:
    #print("not yet born")
#else:
  #print(" not correct")
#print(age)
#temp=int(input("how is temp outside:"))
#if not(temp>=0 and temp<=30):
   #print("so poor thing")
   #print("stay in home")
#elif not(temp<0 or temp>50):

  #print("the temp is good")
   #print("go out")
#name=None
#while not name:
    #name=input("Enter ur name:")
#print("hello"+name)
#for i in range(5+1,9+1,7):
   # print(i)
#for i in "divya":
  # print(i)
#import time
#for seconds in range(5):
    #print(seconds)
    #time.sleep(1)
#print("new year")

o=1
rows=int(input("enter no of rows:"))
m=rows
symbol=input("enter the symbol:")

for i in range(rows):
    for j in range(m):
        print(" ",end="")
    m=m-1
    for k in range(o):
        print(symbol,end="")
    o=o+1
    print()
