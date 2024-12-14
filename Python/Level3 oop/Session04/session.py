# class Person:
#     def __init__(self, name ,age ,role):
#         self.name = name
#         self.age = age
#         self.role = role
    
#     def introduce(self):
#         return ( f' Welcome {self.name} ' )
    
# class Teacher(Person):
#     def introduce(self):
#         return ( f' Hello Teacher: {self.name} ' )

# class Student(Person):
#     def introduce(self):
#         return ( f' Hello Student: {self.name} ' )
    
# st = Student("Omar", 16, "Student")
# te = Teacher("Ali",25,"Teacher")

# print( st.introduce() )
# print( te.introduce() )
# -------------------------------------------------------

# from abc import ABC, abstractmethod

# class Vichle(ABC):
#     @abstractmethod
#     def stop(self):
#         pass
#     @abstractmethod
#     def go(self):
#         pass
    
# class Car(Vichle):
#     def stop(self):
#         return ' The car Will Stop '
#     def go(self):
#         return ' The car Will go '
    
# class Bike(Vichle):
#     def stop(self):
#         return ' The Bike Will Stop '
#     def go(self):
#         return ' The Bike Will go '
    
# b1 = Bike()
# print (b1.stop())
# print (b1.go())

# c1 = Car()
# print (c1.stop())
# print (c1.go())

# -------------------------------------------------------

# class Animal:
#     def speak(self):
#         pass

# class Dog(Animal):
#     def speak(self):
#         return "Woof Woof !!"

# class Cat(Animal):
#     def speak(self):
#         return "Meow Meow !!"
    
# c = Cat()
# print ( c.speak() )
# d = Dog()
# print ( d.speak() )
    
# -------------------------------------------------------
# from abc import ABC, abstractmethod

# class phone(ABC):   # Abstract Class
#     def __init__(self, model):
#         self.model = model
    
#     @abstractmethod
#     def turn_on(self):
#         pass
    
#     @abstractmethod
#     def turn_off(self):
#         pass
    
# class Apple(phone):
#     def turn_on(self):
#         return f" {self.model} is Open "
#     def turn_off(self):
#         return f" {self.model} is Closed "
    
# class Huawei(phone):
#     def turn_on(self):
#         return f" {self.model} is Open "
#     def turn_off(self):
#         return f" {self.model} is Closed "
    
# iphone12 = Apple(" Iphone 12 Pro ")
# y9Prime = Huawei(" Huawei Y9 Prime 2019 ")

# print( iphone12.turn_off() )
# print( iphone12.turn_on() )

# print( y9Prime.turn_off() )
# print( y9Prime.turn_on() )

# -------------------------------------------------------

class Calculator:
    def add(self, a, b=0, c=0):
        return a + b + c
    
calc = Calculator()

print ( calc.add(10, 50, 100) )