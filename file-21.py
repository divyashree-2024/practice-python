#method chaining

#class Car:
#  def turn_on(self):
 #   print("start")
#    return self

#  def drive(self):
#    print("drrive")
#    return self
#  def turn_off(self):
#    print("turn off")
#    return self
#car=Car()
#car.turn_on().drive().turn_off()


#super function

class rectangle:
   def __init__(self,length,width):
      self.length=length
      self.width=width
class Square(rectangle):
   def __init__(self,length,width):
      super().__init__(length,width)
   def area(self):
      return self.length*self.width
class Cube(rectangle):
   def __init__(self,length,width,height):
      super().__init__(length,width)
      self.height=height
   def volume(self):
      return self.length*self.width*self.height
square=Square(3,3)
cube=Cube(3,3,3)

print(square.area())
print(cube.volume())