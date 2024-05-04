#pass objects as args

#class Car:
 #  color=None
#def change_color(car,color):
  # car.color=color
#ar_1=Car()
#car_2=Car()
#car_3=Car()
##print(car_1.color)
#print(car_2.color)
#print(car_3.color)


#duck typing

class Duck:
    def walk(self):
       print("walking")
    def talk(self):
       print("talking")
class chicken:
    def walk(self):
       print("chiken walking")
    def talk(self):
       print("chicken talking")
class person():
    def catch(self,Duck):
       duck.walk()
       duck.talk()
       print("u cougth")
duck=Duck()
chicken=chicken()
person=person()
person.catch(duck)