# inheritence in python : is defined as the process where a class (child class) can inherit attributes and methods from another class (parent class). This allows for code reusability and the creation of hierarchical relationships between classes.
# single underscore is used to indicate that a variable is protected    
class Employee:
    company = "Google" 
    role = "SoftWare Developer" # class variable

    def __init__(self, name, salary):  # constructor
        self.name = name  # instance variable
        self._salary = salary  # protected variable
    def getSalary(self):
        return self._salary

    def getDetails(self):  # instance method
        return f"Employee Name: {self.name}, Salary: {self.getSalary()}, Company: {Employee.company}, Role: {Employee.role} "
    
# child class inheriting from Employee class
class Programmer(Employee):
    def __init__(self, name, salary, language):
        super().__init__(name, salary)  # calling parent class constructor      
        self.language = language  # additional instance variable for child class
    def getProgrammerDetails(self):  # instance method
        parent_details = self.getDetails()  # calling parent class method
        return f"{parent_details}, Programming Language: {self.language}" 
      
# create an instance of Programmer class
prog1 = Programmer("Alice", 90000, "Python")   
print(prog1.getProgrammerDetails())
# accessing protected variable from parent class (not recommended but possible) 
# print("Accessing protected salary from parent class:", prog1._salary)
# Note: Accessing protected members outside the class hierarchy is discouraged and should be avoided in practice.
# The protected member is intended to be used within the class and its subclasses only.
# In Python, this is just a convention and does not enforce access restrictions.
# However, it is still possible to access it directly as shown above.
# In real-world scenarios, it's best to respect the intended access levels of class members.
# If you need to access or modify protected members, consider using getter and setter methods within the class hierarchy.
# This helps maintain encapsulation and ensures that the internal state of the object is managed properly.
# For example, you could add a method in the Employee class to get the salary:
# Then you can call this method from the child class or outside the class hierarchy if needed.
# This way, you maintain control over how the protected member is accessed and modified.
# Always follow best practices for encapsulation and data hiding to ensure the integrity of your objects.
# Remember, the single underscore is just a convention and does not enforce access restrictions in Python.
# It's up to the developer to respect these conventions and use them appropriately in their code.
# By following these guidelines, you can effectively use inheritance and encapsulation in your Python classes while maintaining good coding practices.
# In summary, inheritance allows a child class to inherit attributes and methods from a parent class, promoting code reusability.
# Protected members (indicated by a single underscore) are intended for use within the class and its subclasses, and accessing them directly from outside is discouraged.
# Using getter and setter methods is a recommended approach to manage access to protected members while maintaining encapsulation.
# By adhering to these principles, you can create robust and maintainable object-oriented code in Python.
# Always remember to follow best practices for encapsulation and data hiding to ensure the integrity of your objects.
# This will help you create well-structured and reliable code that is easy to understand and maintain.

# End of Inheritence.py
# some object creation and demonstration of inheritence and protected variable access 
prog2 = Employee("Bob", 80000)  
print("Employee Details:", prog2.getDetails())
# print("Programmer Details:", prog2.getProgrammerDetails())   raise error as prog2 is not an instance of Programmer class
print("Accessing protected salary from parent class using getter method:", prog2.getSalary())
