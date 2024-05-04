#sort


#students=["squidword","sandy","sponge"]
#students.sort(reverse=True)
#sorted_students=sorted(students,reverse=True)
#for i in sorted_students:
 #  print(i)

students=(("squidword","A",24),
           ("sandy","D",30,),
           ("sponge","C",26))
age=lambda age:age[1]
#students.sort(key=grades)
sorted_students=sorted(students,key=age)
for i in sorted_students:
   print(i)
