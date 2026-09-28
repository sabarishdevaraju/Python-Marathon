from sabalib.Bike import Bike
from sabalib.Automobile import Automobile
#import sabalib
from sabalib.User import get_user
import sabalib.User as sabauser
from sabalib.Car import Car


print(get_user("Sabarish"))

print(sabauser.get_user("Sam"))

car1 = Car("BMW","340i","TN22AB1234",60)
car2 = Car("Audi","Z4","TN23AB4321",120)

car1.start()
car2.start()

car1.batt = 56
car2.batt = 70

#Call with Object instance
car1.get_battery()
car2.get_battery()

#Call with Class
Car.get_battery(car1)
Car.get_battery(car2)

Car.build_aston("TN23SG3435") #Classmethod
Car.build_db11("TN34RE3435") #staticmethod

#del car1.batt
#Call with Object instance
car1.get_battery()

#getter
print(car1.speed)
print(car2.speed)

#setter
car1.speed = 100
car2.speed = 80

print(car1.speed)
print(car2.speed)

#deleter
del car1.speed
del car2.speed


#change type of car
print(car1.type)
car1.type = "Hatchback"
print(car1.type)

Car.type = "SUV"
print(Car.type)

d = Automobile("KTM", "Duke", "TN23RHB3443", 350)
d.make = "KTM TM"
print(d.make)

c = Car.build_from_automobile(d)
c.start()