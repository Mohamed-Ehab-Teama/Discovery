'''
{{Inheritance}} is when a class (child) derives from another class (parent), acquiring its attributes and methods
    Inheritance is best used when there is an "is-a" [relationship] between the classes. For example, a [Dog] "is-a" [Animal]
        class Animal        class dog(animal)

{{Composition}} means using instances of other classes as attributes, meaning the relationship is more "has-a" than "is-a."
    Composition is appropriate when one class logically "contains" another. For example, a Car has-a Engine.


{{Method overriding}} occurs when a subclass provides a specific implementation for a method that is already defined in its parent class
    The method in the subclass has the same "name", "signature", and "parameters" as the one in the parent class


Decide Between Composition and Inheritance:
    classes => Viechle, Engine, bike, car

'''


# class Engine:
#     def __init__(self, power):
#         self.power = power

#     def startEngine(self):
#         print('This Engine is so powerful')
# #########################################
# class Car:
#     def __init__(self,make ,model ,engine):
#         self.make = make
#         self.model = model
#         self.engine = engine

#     def speed(self):
#         print("Car is speeding")

# e1 = Engine("500")
# carr = Car("BMW","2020", e1)

# print(carr.engine.power)
# print(carr.engine.startEngine())


# class Veichle:
#     def go(self):
#         print("Veichle is going")

# class Car(Veichle):
#     def go(self):
#         print("Here the Car is going")


# class Bike(Veichle):
#     def go(self):
#         print("Byclce is going")

# v = Veichle()
# c = Car()
# b = Bike()

# v.go()
# b.go()
# c.go()


class Engine:
    def __init__(self, power):
        self.power = power

class Veichle:
    def __init__(self,make ,engine):
        self.make = make
        self.engine = engine

    def walk(self):
        return f"The Veichle: {self.make} and power: {self.engine.power}"

class Car(Veichle):
    def walk(self):
        return f"The Car : {self.make} and power: {self.engine.power}"

class Bike(Veichle):
    def walk(self):
        return f"The Bike : {self.make} and power: {self.engine.power}"


e1 = Engine("350")
e2 = Engine("200")
e3 = Engine("100")

vv = Veichle("This is Viechle", e1)
cc = Car("BMW x5", e2)
bb = Bike("Honda", e3)

# print(vv.walk())
# print(cc.walk())
print(bb.walk())











