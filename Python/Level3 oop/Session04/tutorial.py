# Abstraction
    # Abstraction is the process of hiding implementation details and only exposing the essential features of an object or system.
    # Helps in designing systems with clear boundaries and interfaces.
    # To use Abstraction:
        # Use abstract base classes (ABC) and the abc module.
        # Define abstract methods that must be implemented in child classes.
        
from abc import ABC, abstractmethod

# Abstract class
class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def stop_engine(self):
        pass

# Concrete class
class Car(Vehicle):
    def start_engine(self):
        print("Car engine started")
    def stop_engine(self):
        print("Car engine stopped")

class Motorcycle(Vehicle):
    def start_engine(self):
        print("Motorcycle engine started")
    def stop_engine(self):
        print("Motorcycle engine stopped")

# --------------------------------------------------------------------------

# Polymorphism:
    # Polymorphism means many forms. It allows a single interface to be used for different types of objects.
        # Examples include method overriding and treating objects interchangeably.

class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

# --------------------------------------------------------------------------

# Hands-On Activity: implementing inheritance and polymorphism
from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, name):
        self.name = name
    @abstractmethod
    def start(self):
        pass
    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):
    def start(self):
        print(f"{self.name} car started")
    def stop(self):
        print(f"{self.name} car stopped")

class Bike(Vehicle):
    def start(self):
        print(f"{self.name} bike started")
    def stop(self):
        print(f"{self.name} bike stopped")

# --------------------------------------------------------------------------

# Method Overloading?
    # method overloading is achieved using default arguments.
    
class Calculator:
    def add(self, a, b=0, c=0):
        return a + b + c

calc = Calculator()
print(calc.add(5))         # Output: 5
print(calc.add(5, 10))     # Output: 15
print(calc.add(5, 10, 15)) # Output: 30


# --------------------------------------------------------------------------
# --------------------------------------------------------------------------
# Task

    # Create a system for managing animals in a zoo. Follow the steps below:

    # Step 1: Create an Abstract Base Class
        # Define a class Animal using ABC (Abstract Base Class).
        # Add an abstract method make_sound().
    
    # Step 2: Create Subclasses
        # Create subclasses Lion and Parrot that inherit from Animal.
        # Implement the make_sound() method in each subclass:
        # Lion should return "Roar!"
        # Parrot should return "Squawk!"
    
    # Step 3: Implement Polymorphism
        # Create a list of animals (both Lion and Parrot objects).
        # Use a loop to call the make_sound() method for each animal in the list.
    
    # Step 4: Add an Attribute
        # Add an attribute name to the Animal class and initialize it via the constructor.
        # Modify the make_sound() method to include the animal's name in the output.
        # Expected Output:
        # If you create a Lion named "Simba" and a Parrot named "Polly," the output should look like this:

    # Output
        # Simba says: Roar!
        # Polly says: Squawk!