class Students:
    college_name = "IIT Patna" # class variable
    def __init__(self,name,age,branch): # constructor, where name, age, branch are parameters
        self.name = name  # these are instance variables
        self.age = age
        self.branch = branch    
student1 = Students("Ankit Kumar",22,"ECE")
print(student1.name)
print(student1.college_name)  # accessing class variable using instance 
student2 = Students("Riya Singh",21,"ME")
print(student2.branch)
print(student2.college_name)  # accessing class variable using instance
print(Students.college_name)  # accessing class variable using class name
