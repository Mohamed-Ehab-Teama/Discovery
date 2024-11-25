class Car:
    def __init__ (self, color, model , year):
        self.color = color
        self.model = model
        self.year = year
        
    
    def go(self):
        print ( ' Car Is Going Now ')
        
    def bark(self):
        print ( ' Car Is making sound ')
        
    def stop(self):
        print ( ' Car Is Stopping Now ')
        


class BMW(Car):
    def speed(self):
        print ( ' Car Is speeding Now ')
        


b = BMW("Red", "BMW", 2021)

print( b.color)
b.go()
b.stop()
b.speed()