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

#parent classes

class Vehicle:
    pass

class FlightVehicle(Vehicle):
    pass

class Starship(FlightVehicle):
    pass

#child classes

class GroundVehicle(Vehicle):
    pass

class Airplane(FlightVehicle):
    pass

#sub-child classes

class Car(GroundVehicle):
    pass

class Motorcycle(GroundVehicle):
    pass
