class Student:
    name = "Mohit Yadav "
    age = 23
    college = "IIT Patna"
    branch = "CSE"
    Marks = 95

    def __init__(self,name,age,college,branch,Marks):
        self.name = name
        self.age = age
        self.college = college          
        self.branch = branch
        self.Marks = Marks

student1 = Student("Ankit Kumar",22,"IIT Delhi","ECE",90)
student2 = Student("Riya Singh",21,"IIT Bombay","ME",92)            
print(student1.name)
print(student2.college)         
print(student2.branch)
print(student1.Marks)
if student1.Marks < student2.Marks:
    print(f"{student1.name} has scored more marks.")