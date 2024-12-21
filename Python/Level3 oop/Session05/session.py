# class Engine:
#     def __init__(self):
#         self.engine_Power = "2000 Horse"
#     def engine_method(self):
#         return f" We are in engine {self.engine_Power} "
    

# class Car:
#     def __init__(self, model, color):
#         self.model = model
#         self.color = color
#         self.eng = Engine()  

#     def speed(self):
#         return f" The {self.model} is Speedig "
#     def stop(self):
#         return f" The {self.model} is Stopping Now "
    
# c1 = Car("Marcedes", "White")

# print( c1.eng.engine_Power )
# print( c1.eng.engine_method() )

# print( c1.color )
# print( c1.speed() )
# print( c1.stop() )



class Shape:
    def draw(self):
        return " Drawing a shape "

class Circle(Shape):
    def draw(self):
        return " Drawing a Circle "

class Square(Shape):
    def draw(self):
        return " Drawing a Square "
    

Classes_list = [ Circle(), Square() ]

for i in Classes_list:
    print( i.draw() )