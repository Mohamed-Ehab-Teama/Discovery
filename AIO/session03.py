class computer :
    def __init__(self, screen, ram, cpu, gpu, power):
        self.screen = screen
        self.ram = ram
        self.cpu = cpu
        self.gpu = gpu
        self.power = power
        
    def sayPower(self):
        return 'My power is : ' + self.power


class HP(computer):
    def sayPower(self):
        return "The Hp Power is " + self.power


hp01 = HP('32 Inch', '32 GB', 'Rayzen 5', 'Rx 6600', '650 W')
print (hp01.sayPower())


# hp_Zbook = computer('24 Inch', '64 GB', 'Rayzen 7', 'RTX 3090 ti', '1000 W')

# print ( hp_Zbook.sayPower() )
