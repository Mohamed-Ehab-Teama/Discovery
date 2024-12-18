# from abc import ABC, abstractmethod

# class phone(ABC):
#     @abstractmethod
#     def turn_on(self):
#         pass

#     @abstractmethod
#     def turn_off(self):
#         pass
      
# class Huawei(phone):
#     def turn_on(self):
#         return ' The phone is opend now '
#     def turn_off(self):
#         return ' The Phone will close now'
    
# h1 = Huawei()
# print ( h1.turn_on() )
# print ( h1.turn_off() )


# class Animal:
#     def speak(self):
#         pass
    
    
# class Dog(Animal):
#     def speak(self):
#         return ' Wouf Wouf '


# class Cat(Animal):
#     def speak(self):
#         return ' Meow Meow '



# Method Overloading
class Calculator:
    def add(sefl, a = 0 , b = 0 , c = 0 ):
        return a + b + c

clac = Calculator()

print ( clac.add() )
print ( clac.add(10) )
print ( clac.add(10 , 50 ) )
print ( clac.add(10 , 40 , 60) )