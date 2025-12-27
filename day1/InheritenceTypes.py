# create a Employuee class as Super class has start_time and End_time attributes as class variables 
# crerate a adminStaff class as parent class inheriting from Employee class hasn role attribute
# create a Accountant class as child class inheriting from AdminStaff class has salary attribute
class Employee:
    start_time = "9 AM"  # class variable
    end_time = "5 PM"    # class variable

    def __init__(self, name):  # constructor
        self.name = name  # instance variable

    def getEmployeeDetails(self):  # instance method
        return f"Employee Name: {self.name}, Working Hours: {Employee.start_time} to {Employee.end_time}"   
# Parent class inheriting from Employee class
class AdminStaff(Employee): 
    def __init__(self, name, role):
        super().__init__(name)  # calling parent class constructor
        self.role = role  # additional instance variable for parent class

    def getAdminDetails(self):  # instance method
        parent_details = self.getEmployeeDetails()  # calling parent class method
        return f"{parent_details}, Role: {self.role}"   

# Child class inheriting from AdminStaff class
class Accountant(AdminStaff):
    def __init__(self, name, role, salary):
        super().__init__(name, role)  # calling parent class constructor
        self.salary = salary  # additional instance variable for child class

    def getAccountantDetails(self):  # instance method
        parent_details = self.getAdminDetails()  # calling parent class method
        return f"{parent_details}, Salary: {self.salary}"   

# create an instance of Accountant class
accountant1 = Accountant("John", "Accountant", 60000)   
print(accountant1.getAccountantDetails())
# create an instance of AdminStaff class
admin1 = AdminStaff("Jane", "HR Manager")  
print(admin1.getAdminDetails())
# create an instance of Employee class
employee1 = Employee("Mike")  
print(employee1.getEmployeeDetails())
# End of InheritenceTypes.py
# some object creation and demonstration of multi-level inheritence 
employee2 = Employee("Sara")  
print("Employee Details:", employee2.getEmployeeDetails())
admin2 = AdminStaff("Tom", "IT Support")  
print("Admin Staff Details:", admin2.getAdminDetails()) 
accountant2 = Accountant("Emma", "Finance Manager", 75000)  
print("Accountant Details:", accountant2.getAccountantDetails())    
# Note: In this example, we have demonstrated multi-level inheritance where the Accountant class inherits from the AdminStaff class, which in turn inherits from the Employee class.
# Each class has its own attributes and methods, and the child classes can access the methods of their parent classes using the super() function.
# This allows for code reusability and the creation of hierarchical relationships between classes.      
# Always remember to follow best practices for encapsulation and data hiding to ensure the integrity of your objects.
# This will help you create well-structured and reliable code that is easy to understand and maintain           
# In summary, multi-level inheritance allows a child class to inherit attributes and methods from a parent class, which in turn inherits from another parent class, promoting code reusability and hierarchical relationships.
# Protected members (indicated by a single underscore) are intended for use within the class and its subclasses, and accessing them directly from outside is discouraged.
# Using getter and setter methods is a recommended approach to manage access to protected members while maintaining encapsulation.
# By adhering to these principles, you can create robust and maintainable object-oriented code in Python.
# Always remember to follow best practices for encapsulation and data hiding to ensure the integrity of your objects.
# This will help you create well-structured and reliable code that is easy to understand and maintain.