#reduce

#import functools
#etters=["A","B","C","D"]
#word=functools.reduce(lambda x,y:x+y,letters)
#print(word)

#factorial=[5,4,3,2,1]
#result=functools.reduce(lambda x,y:x*y,factorial)
#print(result)

#list comprehension

#squares=[]
#for i in range(1,10):
  # squares.append(i*i)
#rint(squares)
#squares=[i*i for i in range(1,10)]
#print(squares)
students=[100,90,80,70,60,50,10]
#passed_students=list(filter(lambda x:x>=60,students))
passed_students=[i if i>=60 else "failed" for i in students]
print(passed_students)