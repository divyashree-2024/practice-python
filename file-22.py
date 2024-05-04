#abstract class

from abc import ABC,abstractmethod
class vehicle(ABC):
   # @abstractmethod
  #  def go(self):
       pass
class cycle(vehicle):
    def go(self):
       print("moving cycle")
class motorcycle(vehicle):
    def go(self):
       print("its moving")
       #pass
cycle=cycle()
motorcycle=motorcycle()
vehicle=vehicle()


cycle.go()
motorcycle.go()
#vehicle.go()