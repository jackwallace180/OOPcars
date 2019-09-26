from car2_filipe import *

car_example = Car2(2, 4, 'blue', 'volvo', 'estate', 'woijrij45')
# print(car_example)
# print(car_example.accelerate())

print('playing with encapsulation')
print(car_example.wheels)
print(car_example._accidents)
# print(car_example.__miles)  # this will break the print as it is encapsulated

print(car_example.show_miles())

# print(car_example.__increase_miles())
print(car_example.accelerate())
print(car_example.show_miles())