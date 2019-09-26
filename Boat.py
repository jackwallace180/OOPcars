from Vehicle_parent import *

class Boat(Vehicle):
    def  __init__(self, wheels, capacity, colour, year, hullsize, prop):
        super(). __init__(wheels, capacity, colour, year)
        self.hullsize = hullsize
        self.propellant = prop

    def wave(self):
        return 'oh no a wave hold onto your hats'

    def make_sound(self):
        return 'BERRRRRR BERRRRRRR'

