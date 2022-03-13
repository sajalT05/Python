'''
self parameter can be replaced by any other word
e.g. slf, word
'''

# creating employee class
class Employee:
    # create methods
    # blank function
    # print employee joining year
    def printYear():
        print("Joined in year 2010")
    # using self parameter
    # print office
    def printOffice(self):
        print("Office is Mumbai.")
    # print salary
    # print object attributes
    def printSalary(self):
        # print salary of employee
        print(f"{self.fullName} salary is, {self.salary} thousand Rupees.")
    

# create an new employee object -- 'sajal'
sajal=Employee()
# create full-name and salary instance attributes
# define name of sajal
sajal.fullName="Sajal Tiwari"
# print instance argument
# print employee full name
print("Employee Name: ",sajal.fullName)
# use blank function on object
# sajal.printYear()
    # returns error ->TypeError: Employee.printYear() takes 0 positional arguments but 1 was given
# Employee.printYear(sajal)
    # returns error ->TypeError: Employee.printYear() takes 0 positional arguments but 1 was given
# use self parameter with class and objects
# undefined self parameter, instance argument
sajal.printOffice()
    # returns default statment defined in class method
# pre-defined self parameter, instance argument
# define salary of sajal
sajal.salary=10000
# call function to print salary
# retrns function statement using object attributes
sajal.printSalary()