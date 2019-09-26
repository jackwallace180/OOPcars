from Vehicle_parent import *
from car_class import *
from Bike_class import *
from Boat import *
print('////////////////////////////////////////////////////////////////')
vehicle_1=Vehicle(4, 6, 'blue', 1996)
print(vehicle_1.wheels)
print(vehicle_1.capacity)
print(vehicle_1.colour)
print(vehicle_1.accelerate())
print(vehicle_1.make_sound())
print('////////////////////////////////////////////////////////////////')

car_1=Car(4, 5,'pink',2005, 'peagueot', '305tdi', 'ee45thg', 'yes')
print(car_1.wheels)
print(car_1.capacity)

print(car_1.accelerate())
print('////////////////////////////////////////////////////////////////')
bike_1=Bike(2, 1, 'green', 2012, 21, 'professional', 'small')

print(bike_1.make_sound())
print('////////////////////////////////////////////////////////////////')
boat_1=Boat(0, 1000, 'red', 1830, 100000000, 'jet')

print(boat_1.make_sound())
print(boat_1.wave())
print('////////////////////////////////////////////////////////////////')

print(car_1.turn('left'))