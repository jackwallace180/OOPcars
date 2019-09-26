from vehicle2filipe import *

class Car2(Vehicle2):
    def __init__ (self, wheels, capacity, colour, make, model, plate):
     super().__init__(wheels, capacity, colour)
     self.make = make
     self.model = model
     self.plate = plate

    def make_sound(self):
        return 'reving my car'

print(Car2(2, 4, 'green'))
print(Car2(2, 4, 'green').accelerate())

print(Vehicle2(2, 4, 'blue').make_sound())