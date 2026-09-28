from .Automobile import Automobile

class Car(Automobile):
     #Class Attribute
     type="Sedan"

     #constructor
     def __init__(self, make, model, regno, speed):
          #Instance Attributes
          super().__init__(make, model, regno, speed)
          self.batt = 0
          if self.type == "Sedan":
               self.breakpow = "100%"
          elif self.type == "Hatchback":
               self.breakpow = "75%"

     @classmethod
     def build_from_automobile(cls, d: Automobile):
          c = cls(d.make, d.model, d.regno, d.speed)
          return c

     def start(self):
          print(f"{self.make} {self.model} is ready for drive.")

     def get_battery(self):
          print(f"Battery: {self.batt}%")

     @classmethod
     def  build_aston(cls, regno):
          g = cls("Aston Marton", "ASTON12", "TN32DV1234", 120)
          g.start()

     @staticmethod
     def derive_max_speed():
          print("I am all independent car's @staticmethod")

     @staticmethod
     def build_db11(regno):
          cls = Car
          g = cls("Aston Marton", "DB11", "TN32DV5432", 80)
          g.start()



def get_anything1():
     print("I am all independent")