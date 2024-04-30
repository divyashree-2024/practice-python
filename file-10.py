#**kwargs

#def  hello(**kwargs):
     #print("hi who r u " +kwargs['fir']+" "+kwargs['las'])
     #print("hello",end=" ")
     #for key,value in kwargs.items():
        # print(value,end=" ")

#hello(fir="div",mid="sh",las="di")


#str format


#animal='cow'
#item='moon'
#print("the "+animal+" jumped over the "+item)
#print("The {} jumped over the {}".format(animal,item))
#print("The {0} jumped over the {1}".format(animal,item))#positional args
#print("The {animal} jumped over the {item}".format(animal="cow",item="moon"))#keywordargs
#text="The {} jumped over the {}"
#print(text.format(animal,item))
#name="divya"
#print("hello,my name is {}".format(name))
#print("hello,my name is {:>10}".format(name))
#print("hello,my name is {:^10}".format(name))
#print("hello,my name is {:<10}".format(name))
number=150000
print("The number  is {:E}".format(number))