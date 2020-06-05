# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class

# The vehicle class is the parent class
class Vehicle:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"The vehicle is {self.name}"


class GroundVehicle(Vehicle):
    def __init__(self, name, brand):
        super().__init__(name)
        self.brand = brand

    def __str__(self):
        return super().__str__() + f" and it's brand is {self.brand}."
    
class Car(GroundVehicle):
    def __init__(self, name, brand, model ):
        super().__init__(name,brand)
        self.model=model
        
    def __str__(self):
        return super().__str__() + f" The model of this car is {self.model}"
        


vehicle = Vehicle("speed car")
groundVehicle = GroundVehicle("speed car", "Toyota")
car= Car("speed car", "Toyota", "Sequoia")
print(vehicle)
print(groundVehicle)
print(car)
