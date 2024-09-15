'''
                Encapsulation and Inheritance

{Class Attributes} are shared across all instances of a class, whereas {Instance Attributes} are unique to each instance

{Instance Methods} operate on an instance of the class, while {Class Methods} work with class attributes

{Encapsulation} hides the internal workings of an object, protecting its data and functionality using methods like getters and setters

{Inheritance} : A class can inherit attributes and methods from another class, promoting code reuse and flexibility

{static method} is a method that belongs to a class rather than an instance of the class

{Static methods} don't modify class or instance state, but can be used for utility functions related to the class

'''


# class Student:
#     grade = "A+"         # class attribute

#     def __init__(self, name, age):
#         self.name = name        # instance attribute
#         self.age = age


#     def hello(self):                # instance method
#         return f"Hello, my name is {self.name}"
    

#     @classmethod
#     def hi(clc):
#         return f"Hello from the class my grade is {Student.grade}"




# amr = Student("Amr", 30)
# omar = Student("Omar", 20)



# print(amr.name)
# print(omar.age)
# print(Student.grade)

# print(amr.hello())
# print(omar.hello())
# print(Student.hi())

# print(omar.grade)



# InstanceName.instanceAttributeOrMethod
# ClassName.ClassAttributeOrMethod


        #Encapsulation
# class human:
#     def __init__(self, name, salary):
#         self.name = name
#         self._salary = salary

#     def setSSN(self, ssn):
#         self.__ssn = ssn

#     def getSSN(self):
#         return self.__ssn


# h1 = human("Ahmed", "5000")
# h1.setSSN("302010")
# print(h1.getSSN())


#inheritance
# class car:

#     def go(self):
#         return "GOOOO"
    
    
#     def horn(self):
#         return "beeeeeeeb"
    

#     def stop(self):
#         return "Stop Now"
    

# class BMW(car):
#     pass

# b1 = BMW()
# print(b1.go())
# print(b1.horn())
# print(b1.stop())




# # Static Method
# class Device:
#     def __init__(self, name, color):
#         self.name = name
#         self.color = color

#     def here(self):
#         return "We are here"


#     @staticmethod
#     def ThisisStatic():
#         return "I'm a Static Method"
    

#     @staticmethod
#     def Stativ2():
#         return "I'm another Static method"


# # d = Device("Oppo", "Red")
# # print(d.name)
# # print(d.color)
# # print(d.here())
# print(Device.ThisisStatic())
# print(Device.Stativ2())







##########################################################################

        # Class and Instance Attributes

# class Vehicle:
#     vehicle_type = 'Automobile'  # Class attribute

#     def __init__(self, make, model):
#         self.make = make  # Instance attribute
#         self.model = model  # Instance attribute

# car1 = Vehicle('Toyota', 'Camry')
# car2 = Vehicle('Honda', 'Civic')

# print(Vehicle.vehicle_type)  # Output: Automobile
# print(car1.make, car1.model)  # Output: Toyota Camry
# print(car2.make, car2.model)  # Output: Honda Civic





        # Class and Instance Methods

# class Dog:
#     species = 'Canis lupus'  # Class attribute

#     def __init__(self, name):
#         self.name = name  # Instance attribute

#     # Instance method
#     def speak(self):
#         return f"{self.name} says Woof!"

#     # Class method
#     @classmethod
#     def change_species(cls, new_species):
#         cls.species = new_species

# dog1 = Dog("Max")
# print(dog1.speak())  # Output: Max says Woof!

# Dog.change_species("Canis familiaris")
# print(Dog.species)  # Output: Canis familiaris





        # Encapsulation

# class Person:
#     def __init__(self, name, age):
#         self.__name = name  # Private attribute
#         self.__age = age  # Private attribute

#     # Getter method
#     def get_age(self):
#         return self.__age

#     # Setter method
#     def set_age(self, age):
#         if age > 0:
#             self.__age = age

# person = Person("John", 30)
# print(person.get_age())  # Output: 30

# person.set_age(35)
# print(person.get_age())  # Output: 35


        # Inheritance and multpile inhertance

# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def speak(self):
#         return f"{self.name} makes a sound."

# class Dog(Animal):
#     def speak(self):
#         return f"{self.name} barks."

# dog = Dog("Buddy")
# print(dog.speak())  # Output: Buddy barks



        # Encapsulation with Static Methods, Getters, and Setters

# class Temperature:
#     def __init__(self, celsius):
#         self.__celsius = celsius

#     # Getter method
#     def get_fahrenheit(self):
#         return (self.__celsius * 9/5) + 32

#     # Setter method
#     def set_celsius(self, celsius):
#         if celsius >= -273.15:
#             self.__celsius = celsius

#     # Static method for conversion
#     @staticmethod
#     def to_kelvin(celsius):
#         return celsius + 273.15

# temp = Temperature(25)
# print(temp.get_fahrenheit())  # Output: 77.0
# print(Temperature.to_kelvin(25))  # Output: 298.15

