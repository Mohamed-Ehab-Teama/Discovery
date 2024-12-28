class Phone:
    def __init__(self, model, year, color, ram, storage):
        self.model = model
        self.year = year
        self.color = color
        self.ram = ram
        self.storage = storage
        
    def turn_on(self):
        pass
    def turn_off(self):
        pass
    def raise_sound(self):
        pass
    def lower_sound(self):
        pass
    
    def get_info(self):
        return f" Model : {self.model} \n Year : {self.year} \n Model : {self.model} \n "
        
    

class Huawei(Phone):
    def turn_on(self):
        return " Huawei Phone is Opening "
    def turn_off(self):
        return " Huawei Phone is Closing "
    def raise_sound(self):
        return " Huawei Phone is Sound Raised "
    def lower_sound(self):
        return " Huawei Phone is Sound Reduced "
    
class Oppo(Phone):
    def turn_on(self):
        return " Oppo Phone is Opening "
    def turn_off(self):
        return " Oppo Phone is Closing "
    def raise_sound(self):
        return " Oppo Phone is Sound Raised "
    def lower_sound(self):
        return " Oppo Phone is Sound Reduced "
    
class Nokia(Phone):
    def turn_on(self):
        return " Nokia Phone is Opening "
    def turn_off(self):
        return " Nokia Phone is Closing "
    def raise_sound(self):
        return " Nokia Phone is Sound Raised "
    def lower_sound(self):
        return " Nokia Phone is Sound Reduced "
    
class Vivo(Phone):
    def turn_on(self):
        return " Vivo Phone is Opening "
    def turn_off(self):
        return " Vivo Phone is Closing "
    def raise_sound(self):
        return " Vivo Phone is Sound Raised "
    def lower_sound(self):
        return " Vivo Phone is Sound Reduced "
    
    
y9 = Huawei(" Huawei Y9 Prime ", " 2019 ", " Black " , " 4GB ", " 128GB " )
