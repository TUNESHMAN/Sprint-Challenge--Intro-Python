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
        return super().__str__() + f" and it is a {self.brand}."


class Car(GroundVehicle):
    def __init__(self, name, brand, model):
        super().__init__(name, brand)
        self.model = model

    def __str__(self):
        return super().__str__() + f" The model of this car is {self.model}"


class Motorcycle(GroundVehicle):
    def __init__(self, name, brand, model):
        super().__init__(name, brand)
        self.model = model

    def __str__(self):
        return super().__str__() + f" The model of this motorcycle is {self.model}"


class FlightVehicle(Vehicle):
    def __init__(self, name, type):
        super().__init__(name)
        self.type = type

    def __str__(self):
        return super().__str__() + f" and it is an {self.type}"
    
class Airplane(FlightVehicle):
    def __init__(self, name, type, model):
        super().__init__(name, type)
        self.model = model

    def __str__(self):
        return super().__str__() + f" The model of this plane is {self.model}"
    
class Starship(FlightVehicle):
    def __init__(self, name, type, model):
        super().__init__(name, type)
        self.model = model

    def __str__(self):
        return super().__str__() + f" The model of this plane is {self.model}"


vehicle = Vehicle("ground vehicle")
groundVehicle = GroundVehicle("ground vehicle", "speed car")
car = Car("ground vehicle", "speed car", "Toyota")
motorcycle = Motorcycle("ground vehicle", "motorcycle", "power bike")
flightVehicle = FlightVehicle("flight vehicle", "helicopter")
airplane=Airplane("flight vehicle", "airplane", "bellview")
starship=Airplane("flight vehicle", "airplane", "starship")

print(vehicle)
print(groundVehicle)
print(car)
print(motorcycle)
print(flightVehicle)
print(airplane)
print(starship)