# Class and Instance Attributes
    # Class Attributes: Shared across all instances of the class.
    # Instance Attributes: Unique to each object (instance).
    
class Vehicle:
    wheels = 4  # Class attribute

    def __init__(self, brand, model):
        self.brand = brand  # Instance attribute
        self.model = model  # Instance attribute

# Create instances
car1 = Vehicle("Toyota", "Camry")
car2 = Vehicle("Honda", "Civic")

# Access attributes
print(Vehicle.wheels)   # Output: 4 (class attribute)
print(car1.brand)       # Output: Toyota (instance attribute)
print(car2.model)       # Output: Civic (instance attribute)

# ------------------------------------------------------------------------------------
# Class Methods and Instance Methods
    # Instance Methods: Operate on individual objects and use self.
    # Class Methods: Operate on the class itself and use cls.
    
class Circle:
    pi = 3.14159  # Class attribute

    def __init__(self, radius):
        self.radius = radius  # Instance attribute

    # Instance method
    def area(self):
        return Circle.pi * self.radius**2

    # Class method
    @classmethod
    def update_pi(cls, new_pi):
        cls.pi = new_pi

# Create instance
circle = Circle(5)
print(circle.area())  # Output: 78.53975

# Update class attribute using class method
Circle.update_pi(3.14)
print(circle.area())  # Output: 78.5

# ------------------------------------------------------------------------------------

# Encapsulation
    # Encapsulation hides the internal state of an object and only exposes necessary methods.
        # Private Attributes: Denoted with _ or __.
        # Use getters and setters to control access.
class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.__balance = balance  # Private attribute

    # Getter
    def get_balance(self):
        return self.__balance

    # Setter
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Invalid withdrawal amount.")

# Create instance
account = BankAccount("Alice", 1000)
print(account.get_balance())  # Output: 1000
account.deposit(500)
print(account.get_balance())  # Output: 1500
account.withdraw(2000)        # Output: Invalid withdrawal amount.

# ------------------------------------------------------------------------------------

# Inheritance:
    # Inheritance allows one class (child) to inherit attributes and methods from another class (parent)
class Animal:
    def __init__(self, species):
        self.species = species

    def make_sound(self):
        print("Some generic sound")

# Dog inherits from Animal
class Dog(Animal):
    def __init__(self, breed):
        super().__init__("Dog")     # used to call the constructor of the parent class
        self.breed = breed

    def make_sound(self):
        print("Woof Woof")

# Create objects
generic_animal = Animal("Unknown")
generic_animal.make_sound()  # Output: Some generic sound

dog = Dog("Golden Retriever")
dog.make_sound()             # Output: Woof Woof
print(dog.species)           # Output: Dog

# ------------------------------------------------------------------------------------

# Multiple Inheritance
    # A class can inherit from multiple parent classes.
class Walker:
    def walk(self):
        print("Walking...")

class Swimmer:
    def swim(self):
        print("Swimming...")

class Amphibian(Walker, Swimmer):
    pass

# Create object
frog = Amphibian()
frog.walk()  # Output: Walking...
frog.swim()  # Output: Swimming...

# ------------------------------------------------------------------------------------

# Encapsulation with Static Methods
    # Static Methods: Methods that don’t modify class or instance attributes
class MathUtils:
    @staticmethod
    def add_numbers(a, b):
        return a + b

# Use static method
result = MathUtils.add_numbers(5, 10)
print(result)  # Output: 15

# ------------------------------------------------------------------------------------

# Class Attributes	    Shared by all instances of the class.
# Instance Attributes	Unique to each object.
# Instance Methods	    Operate on individual objects.
# Class Methods	        Operate on the class itself.
# Static Methods	    Independent methods, used without modifying class state.
# Encapsulation	        Hides implementation details, uses getters and setters.
# Inheritance	        Reuses attributes and methods from a parent class.
# Multiple Inheritance  Inherits from more than one parent class.

# ------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------

# Assignment:
    # - Create a parent class Person and child classes Student and Teacher:
    #     * Include attributes like name, age, and role.
    #     * Add a method introduce that is overridden in Student and Teacher.
    # - Demonstrate Encapsulation:
    #     * Use private attributes for grades (in Student) and salary (in Teacher).
    #     * Add getters and setters to control access.
