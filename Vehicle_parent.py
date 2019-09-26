class Vehicle():

    def __init__(self, wheels, capacity, colour, year):
        self.wheels = wheels
        self.capacity = capacity
        self.colour = colour
        self.year = year

    def accelerate(self):
        return 'vrooooommmmm'
    def brake(self):
        return 'sccccrrrrhhchhhscrrrhhhhhhh'
    def turn(self, turnn):
        return 'you are turning ' + turnn
    def make_sound(self):
        return 'vroomvroomvroom'



