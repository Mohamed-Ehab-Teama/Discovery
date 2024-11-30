'''
Class Structure: A class in Python typically has attributes (data) and methods (functions) that act on the data.
Attributes: These are variables inside the class that hold data.
Methods: These are functions inside the class that define behaviors or actions.
Constructors: Special methods (e.g., __init__) used to initialize objects when they are created

'''

class Laptop:
    def __init__ ( self , color, model, ram ):
        self.color = color
        self.model = model
        self.ram = ram
        
    def open(self):
        return ( f" {self.model} is opened" )
        
    def shutdown(self):
        return ( f" {self.model} is closing" )

hp = Laptop("Black" , "HP Z-book G2", "8 GB")
asus = Laptop("Gray", "ASUS VivoBOOK", "16 GB")

print ( hp.color )
print ( hp.model )
print ( hp.ram )
print ( hp.open() )
print ( hp.shutdown() )
print ("---------------------")
print ( asus.color )
print ( asus.model )
print ( asus.ram )
print ( asus.open() )
print ( asus.shutdown() )