'''
Class Structure: A class in Python typically has attributes (data) and methods (functions) that act on the data.
Attributes: These are variables inside the class that hold data.
Methods: These are functions inside the class that define behaviors or actions.
Constructors: Special methods (e.g., __init__) used to initialize objects when they are created

'''


class human:    
    def __init__ (self, user_name, user_age, user_hairColor) :
        self.name = user_name
        self.age = user_age
        self.hair_color = user_hairColor

    def walk(self):
        return f'{self.name} is Walking'
    def run(self):
        return 'running'    
    def eat(self):
        return 'eating'
    
    def getProperities(self):
        # print ( f"your name is:{self.name}   /"   ,    
        # f'   your age is:{self.age}      /',
        # f'     your hair color is:{self.hair_color}' )
        print ( f"Name : {self.name} -- Age: {self.age} -- HairColor: {self.hair_color}" )
        # print ( f"Name : {self.age}" )
        # print ( f"Name : {self.hair_color}" )
    

person1 = human("Ali",25,"Black")
person2 = human("Ahmed",27,"Red")
print ( person1.getProperities() )
print ( person2.getProperities() )