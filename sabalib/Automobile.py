class Automobile:
        
        
        def __init__(self, make, model, regno, speed):
          #Instance Attributes
          self.make = make
          self.model = model
          self.regno = regno
          self._speed = speed
         
          
        @property
        def speed(self):    #getter
            return self._speed

        @speed.setter
        def speed(self, value):   #setter
            if value < 0:
               raise ValueError("Speed cannot be negative")
            self._speed = value

        @speed.deleter
        def speed(self):     #deleter
           del self._speed 
           print(f"Deleting speed of {self.regno} {self.model} ")