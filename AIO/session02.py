
class Phone:
    
    # Instance Attributes
    def __init__(self, ram, storage, color, camera):
        self.ram = ram
        self.storage = storage
        self.color = color
        self.camera = camera
    
    # def __init__(self):
    #     u_ram = input('Enter Ram \n')
    #     u_storage = input('Enter Storage \n')
    #     u_color = input('Enter Color \n')
    #     u_camera = input('Enter Camera \n')
        
    #     self.ram = u_ram
    #     self.storage = u_storage
    #     self.camera = u_camera
    #     self.color = u_color
    
    
    # Class Attributes
    # ram = '8 GB'
    # color = 'Black'
    # camera = '64 MB'
    
    # Instance Method
    def speak(self):
        print("Hello from function")
       
    # Calss Method 
    def sayHello():
        print ("Hello From Class Method")
    
ph1 = Phone("12 GB", "128 GB", "Red", "100 MP")
# ph1.speak()

Phone.sayHello()


# ph120 = Phone()
# print (ph120.camera)
# print (ph120.ram)
# print (ph120.storage)
# print (ph120.color)









# print(ph1.color)

# ph1.color = 'Red'

# print(ph1.color)