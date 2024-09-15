# Session 01

# Create a Person class with the following attributes: name (string), age (integer), The class should have a method greet that prints a greeting message with the person's name

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
    
#     def greet(self):
#         print(f"Hello, my name is {self.name}.")


# st = Person("Mohamed", 25)
# print(st.name)
# print(st.age)
# print(st.greet())

######################################################################
# Session 02

# Create the Vehicle class with a constructor and a method  // properities: make, model, year // method---prints that "{make} + {model} + {year} the engine has started" 
# Create a dictionary that hold the same properties of the viechle (make, model, year)
# Creat 2 ojects from the Vehichle class

# class Vehicle:
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
    
#     def start_engine(self):
#         print(f"{self.year} {self.make} {self.model}'s engine is starting...")

# vehicle_dict = {
#     "make": "Toyota",
#     "model": "Corolla",
#     "year": 2021
# }

# toyota = Vehicle("Toyota", "Corolla", 2021)
# toyota.start_engine()  # Using the class method

# bmw = Vehicle("BMW", "X6", 2024)
# bmw.start_engine()  # Using the class method


######################################################################
# Session 03

# Create a Super class with encapsulation then: create 2 other classes that inherits the super class //
# Creating instance from the two childs and use them.

# class car:
#     def __init__(self, make, model, year,snum):
#         self.make = make
#         self.model = model
#         self.year = year
#         self._serialNumber_ = snum

#     def startOn(self):
#         print(f"The {self.make} {self.model} {self.year} is Strating Engine")

#     def getSN(self):
#         return self._serialNumber_


# class BMW(car):
#     pass

# class Marc(car):
#     pass

# x6 = BMW("BMW", "X6", 2020,"19548")
# x6.startOn()
# print("the Private Number is : ",x6.getSN())



######################################################################
# Session 04

# Create a Vehicle class with the following:

# Private Attribute: _speed (integer) to represent the vehicle's speed.
# Method: move() to print a message that the vehicle is moving at a certain speed.
# Getter and Setter: get_speed() to retrieve the speed and set_speed(speed) to set the speed.
# Create a Car class that inherits from Vehicle:

# Method: move() to print a specific message like "The car is driving at speed km/h."
# Create a Bicycle class that also inherits from Vehicle:

# Method: move() to print a specific message like "The bicycle is pedaling at speed km/h."
# Polymorphism in Action:

# Create instances of Car and Bicycle, set their speeds, and call the move() method on both. Show how the same move() method behaves differently depending on the vehicle.
# Abstraction:

# Discuss how the Vehicle class hides the complexity of setting and getting speed, and how each vehicle can focus on its specific way of moving.


# Step 1: Create the Vehicle class with abstraction
# class Vehicle:
#     def __init__(self, speed=0):
#         self._speed = speed  # Private attribute
    
#     def move(self):
#         print(f"The vehicle is moving at {self._speed} km/h.")
    
#     def get_speed(self):
#         return self._speed
    
#     def set_speed(self, speed):
#         self._speed = speed

# # Step 2: Create the Car class inheriting from Vehicle
# class Car(Vehicle):
#     def move(self):
#         print(f"The car is driving at {self._speed} km/h.")

# # Step 3: Create the Bicycle class inheriting from Vehicle
# class Bicycle(Vehicle):
#     def move(self):
#         print(f"The bicycle is pedaling at {self._speed} km/h.")

# # Step 4: Polymorphism - Using the same method for different objects
# car = Car()
# bicycle = Bicycle()

# car.set_speed(60)
# bicycle.set_speed(15)

# car.move()        # The car is driving at 60 km/h.
# bicycle.move()    # The bicycle is pedaling at 15 km/h.


######################################################################
# Session 05

# Step 1: Create the Animal class
# class Animal:
#     def __init__(self, name, sound):
#         self.name = name
#         self.sound = sound
    
#     def make_sound(self):
#         print(f"{self.name} says {self.sound}")

# # Step 2: Create the Lion class inheriting from Animal
# class Lion(Animal):
#     def __init__(self, name, sound, roar_volume):
#         super().__init__(name, sound)
#         self.roar_volume = roar_volume
    
#     def roar(self):
#         print(f"{self.name} roars at volume {self.roar_volume}")

# # Step 3: Create the Zoo class using composition
# class Zoo:
#     def __init__(self):
#         self.animals = []  # List to hold Animal instances
    
#     def add_animal(self, animal):
#         self.animals.append(animal)
    
#     def show_animals(self):
#         for animal in self.animals:
#             animal.make_sound()

# # Step 4: Hands-on Activity
# # Create instances of Animal and Lion
# elephant = Animal("Elephant", "Trumpet")
# lion = Lion("Lion", "Roar", 10)

# # Create a Zoo and add animals
# zoo = Zoo()
# zoo.add_animal(elephant)
# zoo.add_animal(lion)

# # Show all animals in the zoo
# zoo.show_animals()

# # Demonstrate Lion's roar method
# lion.roar()


##############################################################################

# project

# Create a Animal class:

# Attributes: name (string), sound (string), _age (integer, private)
# Methods:
# make_sound() prints the sound the animal makes.
# get_age() returns the age of the animal.
# set_age(age) sets the age of the animal.
# Create a Lion class that inherits from Animal:

# Additional Attribute: roar_volume (integer)
# Methods:
# roar() prints the roar volume.
# Create a Elephant class that inherits from Animal:

# Additional Attribute: trunk_length (integer)
# Methods:
# trumpet() prints a message about the trumpet sound.
# Create a Zoo class using composition:

# Attribute: animals (a list to hold instances of Animal)
# Methods:
# add_animal(animal) adds an animal to the zoo.
# show_animals() prints the names and sounds of all animals in the zoo.
# Hands-on Activity:

# Create instances of Lion, Elephant, and add them to the Zoo.
# Demonstrate how to use methods from different classes.
# Show how Lion and Elephant share common functionalities from Animal, but have their unique features.

#   Code

# Step 1: Create the Animal class
# class Animal:
#     def __init__(self, name, sound, age):
#         self.name = name
#         self.sound = sound
#         self._age = age  # Private attribute
    
#     def make_sound(self):
#         print(f"{self.name} says {self.sound}")
    
#     def get_age(self):
#         return self._age
    
#     def set_age(self, age):
#         self._age = age

# # Step 2: Create the Lion class inheriting from Animal
# class Lion(Animal):
#     def __init__(self, name, sound, age, roar_volume):
#         super().__init__(name, sound, age)
#         self.roar_volume = roar_volume
    
#     def roar(self):
#         print(f"{self.name} roars at volume {self.roar_volume}")

# # Step 3: Create the Elephant class inheriting from Animal
# class Elephant(Animal):
#     def __init__(self, name, sound, age, trunk_length):
#         super().__init__(name, sound, age)
#         self.trunk_length = trunk_length
    
#     def trumpet(self):
#         print(f"{self.name} trumpets with trunk length {self.trunk_length}")

# # Step 4: Create the Zoo class using composition
# class Zoo:
#     def __init__(self):
#         self.animals = []  # List to hold Animal instances
    
#     def add_animal(self, animal):
#         self.animals.append(animal)
    
#     def show_animals(self):
#         for animal in self.animals:
#             animal.make_sound()
#             print(f"Age: {animal.get_age()}")

# # Step 5: Hands-on Activity
# # Create instances of Lion and Elephant
# lion = Lion("Leo", "Roar", 5, 10)
# elephant = Elephant("Ellie", "Trumpet", 8, 12)

# # Create a Zoo and add animals
# zoo = Zoo()
# zoo.add_animal(lion)
# zoo.add_animal(elephant)

# # Show all animals in the zoo
# zoo.show_animals()

# # Demonstrate Lion's roar method
# lion.roar()

# # Demonstrate Elephant's trumpet method
# elephant.trumpet()
