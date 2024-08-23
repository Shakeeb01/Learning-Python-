# python do not have abstraction in python so we have to import abstraction from another library.

from abc import ABC,abstractmethod   # this is how we import abstraction from library.

from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def stop_engine(self):
        pass

class Car(Vehicle):
    def start_engine(self):
        print("Car engine started.")

    def stop_engine(self):
        print("Car engine stopped.")

class Bike(Vehicle):
    def start_engine(self):
        print("Bike engine started.")

    def stop_engine(self):
        print("Bike engine stopped.")

# Create instances of Car and Bike
car = Car()
bike = Bike()

# Use the methods defined in the subclasses
car.start_engine()  # Output: Car engine started.
car.stop_engine()   # Output: Car engine stopped.

bike.start_engine() # Output: Bike engine started.
bike.stop_engine()  # Output: Bike engine stopped.
