#multiple inheritence

#class Prey:
#    def flee(self):
 #     print("flees")
#class predator:
 #   def hunt(self):
  #    print("hunting")
#class Rabbit(Prey):
#      pass
#class hawk(predator):
#      pass
#rabbit=Rabbit()
#hawk=hawk()
#rabbit.flee()
#hawk.hunt()


#method overriding

class Animal:
   def eat(self):
     print("eating")
class rabbit(Animal):
   def eat(self):
     print("rabbit is funny")
rabbit=rabbit()
rabbit.eat()