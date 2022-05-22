# create a employee class
class Employee:
    # create a variable for this class
    company="Google"
    language="Python"
    # create a function in pernt class
    def getcompany(self):
        print(f"Company name is {self.company}.")
    def getlanguage(self):
        print(f"Language is {self.language}.")

# create programmer class as a child class and use programmer class as a parent class
class Programmer(Employee):
    # create a variable in programmer class
    department="Development"
    # change varibale of parent class
    company="Microsoft"
    # create a function in child class
    def getdepartment(self):
        print(f"Department is {self.department}.")
    #  change parent class function in child class.
    def getlanguage(self):
        print(f"Updated Language is {self.language}.")

# create an instance for employee class
# sajal as an object
sajal=Employee()
# run company function on sajal object
sajal.getcompany()
# run language function on sajal object
sajal.getlanguage()
# create an instance for programmer class
# mohan as an object
mohan=Programmer()
# run department method on object
mohan.getdepartment()
# run company method of parent employee class on programmer child class on instance of child class
# variable of parent class is changed in child class
mohan.getcompany()
# run method updated in child class derived from parent class on instance of child class
# method of parent class is changed in parent class
mohan.getlanguage()

 