from Vehicle_parent import *
class Car(Vehicle):
    def __init__(self, wheels, capacity, colour, year, brand, model, licenseplate, airbag):
        super(). __init__(wheels, capacity, colour, year)
        self.brand = brand
        self.model = model
        self.licenseplate = licenseplate
        self.airbag = airbag

    def music(self):
        return "Yo, Ill tell you what I want, what I really, really want, So tell me what you want, what you really, really want Ill tell you what I want, what I really, really want So tell me what you want, what you really, really want I wanna, (ha) I wanna, (ha) I wanna, (ha) I wanna, (ha) I wanna really, really, really wanna zigazig ah"
    def horn(self):
        return 'HONK HONK!!'
    def lock_it(self):
        return '*click*'
    def aircon(self):
        return 'mmmm cool air'
    def openwindow(self):
        return 'oh no its raining again that was a mistake'


