from vehicle2filipe import *

class Car2(Vehicle2):
    def __init__ (self, wheels, capacity, colour, make, model, plate):
        super().__init__(wheels, capacity, colour)
        self.make = make
        self.model = model
        self.plate = plate
        self.__miles = 0 #visibility and access is restricted
        self._accidents = 0  #visibility is limited

    def make_sound(self):
        return 'reving my car'

    def accelerate(self):
        self.__increase_miles()    # using encapsulated method
        return 'vroooom'

    def show_miles(self):   #Getter
        return self.__miles

    def set_miles(self, miles):   #setter
        #checking security stuff before setting in real life (verified user for example)
        self.__miles = miles
        return 'miles set to ' + miles

    def __increase_miles(self):   # encapsulated private method
        self.__miles += 100


