from  Vehicle_parent import *
class Bike(Vehicle):
    def __init__(self, wheels, capacity, colour, year, gears, handlebar, basket_size):
        super(). __init__(wheels, capacity, colour, year)
        self.gears = gears
        self.handlebar = handlebar
        self.basket_size = basket_size

    def peddle(self):
        return 'left right left right left right left right ......'
    def wheely(self):
        return 'whooooaaaaaaa look how cool i look'
    def chain_it(self):
        return 'now no one can steal my bike'

    def make_sound(self):
        return 'ring ring'



