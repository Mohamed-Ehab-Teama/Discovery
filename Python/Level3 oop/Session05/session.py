class Engine:
    def __init__(self):
        self.horse = "2000"
    def start_Engine(self):
        return " The Engine is Started "


class Car:
    def __init__(self, model, color):
        self.model = model
        self.color = color
        self.engine = Engine()
    def speed(self):
        return " The Car Is speeding "
    
bmw = Car("BMW", "Black")
print ( bmw.engine.start_Engine() )
print ( bmw.speed() )