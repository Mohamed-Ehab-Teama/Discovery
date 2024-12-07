# class Human:
#     # Class Attribute
#     type = 'Male'
    
#     # Instance Attributes
#     def __init__ (self, u_name, u_age, u_height):
#         self.name = u_name
#         self.age = u_age
#         self.height = u_height
        
# ali = Human("Ali Ahmed", 29, 179)
# ahmed = Human("Ahmed Emad", 30, 175)

# print( ali.name )
# print ( Human.type )


# class Human:
    
#     # Instance Method
#     def walk(self):
#         return "Walking now"

#     # Class Method
#     @classmethod
#     def greet(cls):
#         return " This is Class Method "

# h1 = Human()
# print ( h1.walk() )
# print ( Human.greet() )



# class BankAccount:
#     def __init__(self, name):
#         self.AccountName = name
#         self.__balance = 0
       
#     # Setter 
#     def set_balance(self, amount):
#         self.__balance += amount
        
#     # Getter
#     def get_balance (self):
#         return self.__balance

# ali = BankAccount("Ali Mohamed")
# print ( ali.get_balance() )
# ali.set_balance(2500)
# ali.set_balance(2000)
# print ( ali.get_balance() )



# class Animal:
#     def __init__(self, animal_name, animal_sound):
#         self.name = animal_name
#         self.sound = animal_sound
        
#     def make_sound(self):
#         return f" say {self.sound} "
    
# class Cat(Animal):
#     pass

# c1 = Cat("Cat 01", "Meow Meow")
# print ( c1.name )
# print ( c1.sound )
# print ( c1.make_sound() )