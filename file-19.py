#inheritence

#lass Animal:
 #  alive=True
   #def eat(self):
  #     print("eating")
  # def sleep():
#       print("sleeping")
#class Rabbit(Animal):
#   print("rab")
#class Fox(Animal):
 #  print("horrible")
#rabbit=Rabbit()
#fox=Fox()
##print(rabbit.alive)
#fox.eat()


#multilevel inhertence

class organism:
    alive=True
class Animal(organism):
    def eat(self):
       print("eating")
class Dog(Animal):
     def bark(self):
       print("barking")
dog=Dog()
print(dog.alive)
dog.eat()
dog.bark()