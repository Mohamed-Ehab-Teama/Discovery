'''
Project on level 3
'''

# Create Phone Class
    # properities : model, year, color, RAM, Storage
    # methods : turn_on, turn_off, raise_sound, lower_sound
    
# Create Subclasses inherits form Phone ( oppo, Vivo, huawei, Nokia )
    # perform Method OverLoading
    # Create method Get_Info : get the info of all properities


class Cpu:
    def __init__(self, core, hz):
        self.core = core
        self.hz = hz

    def cpuPower(self):
        return "The SnapDragon CPU is so Powerful"


class Phone:
    def __init__(self, ram, screenSize, space, cpu):
        self.ram = ram
        self.screenSize = screenSize
        self.space = space
        self.__ID = 0
        self.cpu = cpu

    def setID(self, id):
        self.__ID = id

    def getID(self):
        return self.__ID

    def turnOn(self):
        return "The Phone is Starting"

    def turnOff(self):
        return "The Phone is Closing"


class Sony(Phone):
    def turnOn(self):
        return "The Sony Phone is Starting tttttttttttt"

    def turnOff(self):
        return "The Sony Phone is Closing ttttttttttttttt"


cpu1 = Cpu("8 Core", "3.7 GHz")
phone1 = Phone("8 GB", "8 inch", "128 GB", cpu1)
# s1 = Sony("4 GB", "5 inch", "64 GB")

print(phone1.cpu.core)
print(phone1.cpu.hz)
print(phone1.cpu.cpuPower())


# print(phone1.turnOn())
# print(s1.turnOn())

# print(s1.turnOn())
# print(s1.turnOff())
# # s1.setID(66654)
# print(s1.getID())


# phone1.setID(20356)
# print(phone1.getID())

# print(phone1.ram)
# print(phone1.screenSize)
# print(phone1.space)
# print(phone1.turnOn())
# print(phone1.turnOff())



