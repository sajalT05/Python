# Company class
class Company:
    company="Google"
    className="Company"

    def __init__(self):
        print("Company class...")

    def getCompany(self):
        print(f"this is '{self.company}' company,")

    def code(self):
        print("this is company code.")

    def className(self):
        print(f"class name is: {self.className}")

'''
Error done:
1. when creating child class, 
    a. remember to place parent class in parenthesis of child class.
    b. use parent class as argument for child class.
2. 
'''
# Department class --> child class to company.
class Department(Company):
    department="marketing"
    className="Department"

    def __init__(self):
        super().__init__()
        print("Department class...")

    def getDepartment(self):
        print(f"and '{self.department}' department,")
    
    def code(self):
        super().code()
        print("this is department code.")
    
    def className(self):
        print(f"class name is: {self.className}")


#  Employee class --> child class to department
class Employee(Department):
    employee="Programmer"
    className="Employee"

    def __init__(self):
        super().__init__()
        print("Employee Class...")
    
    def getEmployee(self):
        print(f"and employee type is '{self.employee}'.")

    def code(self):
        super().code()
        print("this is emplpoyee code.")

    def className(self):
        print(f"class name is: {self.className}")


# instance to employee class
# testing def __init__ with super()
print("testing def __init__ with super()")
name=Employee()
print("\n")
# using methods of parent class with child class instance.
print("using methods of parent class with child class instance.")
name.getCompany()
name.getDepartment()
name.getEmployee()
print("\n")
# adding additional print commands in each child class to method of grand parent class with super().
print("adding additional print commands in each child class to method of grand parent class.")
name.code()
print("\n")
# modifying methods of grand parent class in child class
print("modifying methods of grand parent class in child class")
# name.className() # --returning error --> self.classname is not working.
print("\n")