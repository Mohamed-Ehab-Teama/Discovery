# Composition vs Inheritance
    # Inheritance:
        # Models an "is-a" relationship.
        # The child class derives from a parent class, inheriting its attributes and methods.
        # Best for hierarchical relationships.
    # Composition:
        # Models a "has-a" relationship.
        # A class contains objects of other classes as attributes.
        # Best for modular, loosely coupled designs.
        
# ----------------------------------------------

# Inheritance:
class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        print("Some generic sound")

class Dog(Animal):
    def make_sound(self):
        print("Woof Woof")

# Usage
dog = Dog("Buddy")
dog.make_sound()  # Output: Woof Woof

# ----------------------------------------------

# Composition:
class Engine:
    def start(self):
        print("Engine started")

class Car:
    def __init__(self, brand):
        self.brand = brand
        self.engine = Engine()  # Composition

    def start(self):
        self.engine.start()

# Usage
car = Car("Toyota")
car.start()  # Output: Engine started

# ----------------------------------------------

# Method Overriding:
    # Allows a subclass to redefine a method from its parent class.
    # Enables polymorphism, where the same method call behaves differently for different objects.
    
class Shape:
    def draw(self):
        print("Drawing a shape")

class Circle(Shape):
    def draw(self):
        print("Drawing a circle")

class Square(Shape):
    def draw(self):
        print("Drawing a square")

# Polymorphism in action
shapes = [Circle(), Square()]
for shape in shapes:
    shape.draw()


# ----------------------------------------------
# ----------------------------------------------
# ----------------------------------------------
# ----------------------------------------------


# Task

# Step 1: Define the Base Class
#     Create a class called Animal.
#     Add an attribute name to store the animal's name.
#     Add a method make_sound() to print a generic sound.

# Step 2: Create Subclasses
#     Create two subclasses: Dog and Cat.
#     Override the make_sound() method in both classes to print specific sounds.
    
# Step 3: Use the Classes
#     Create objects for Dog and Cat.
#     Call the make_sound() method for each object to see the overridden behavior.