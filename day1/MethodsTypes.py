class Methods:
    help = "May i help you i am available with everyOne"

    def __init__(self,RAM,Storage):  # constructor
        self.RAM = RAM
        self.Storage = Storage

    def phoneInfo(self):  #instance method
       # return f"This phone has {self.RAM} GB RAM and {self.Storage} GB Storage and {Methods.help}"   
        return f"This phone has {self.RAM} GB RAM and {self.Storage} GB Storage and {self.help}"  # accesing class variable using instance

    @classmethod  # decorator declaring it a class method
    def getHelp(cls):  # static method
        return f"This is a static method and {cls.help}"  # accessing class variable using class name
     
     # static method
    @staticmethod  # decorator declaring it a static method
    def calc_Discount(price,discount):
        return price - (price * discount)/100 
    
phone1 = Methods(8,128)
print(phone1.phoneInfo())   
#class Method Verification
print(Methods.getHelp())
print(phone1.getHelp()) 

#static Method Verification
# using class name
print(Methods.calc_Discount(1000,10))

# using instance
# print(phone1.calc_Discount(2000,15))  
# This is not a good practice to call static method using instance but it is possible
# So, it is recommended to call static method using class name only
# But still if you want to call using instance then you can do it as below
print(Methods.calc_Discount(2000,15))    

