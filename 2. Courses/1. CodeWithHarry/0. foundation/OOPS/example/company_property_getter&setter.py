# create a class
class Company:
    # create class attributes
    # string attributes
    # name of the company
    companyName="Google"
    # integer variables
    # salary in the company
    '''
    totalSalary     >   total salary of an employee
    baseSalary      >   base salary of an employee
    bonus           >   bonus given to an employee

    totalSalary =  baseSalary+baseSalary
    '''
    # commenting few varibales
    # totalSalary=100
    baseSalary=80
    bonus=20

    # creating methods
    # constructor
    # show base salary when class is assigned to an object in an instance.
    def __init__(self):
        print(f"Base Salary: {self.baseSalary}")
    # getter method
    # total salary method 
    #   --> property method 
    #   --> can be used as a variable
    @property
    def totalSalary(self):
        # sum of base salary and bonus
        # return sum of class attributes
        #   --> base salary + bonus
        return self.baseSalary + self.bonus
    # setter method
    #  use total salary value passed in the instance to calculate bonus
        #  base salary is same
        # bonus will change according to total salary
    @totalSalary.setter
    # totalSalaryArgument is the value defined to total salary in the instance
    def totalSalary(self,totalSalaryArgument):
        # bonus = total salary argument - base salary
        # bonus value is changed for the instance.
        self.bonus=totalSalaryArgument-self.baseSalary

# create instance to company class
# sajal is the object
sajal=Company()
# check class attributes
# check salary defined in the class
# bonus
print(f"Predifned Bonus: {sajal.bonus}")
# total salary
print(f"Total Salary: {sajal.totalSalary}")
# change total salary
# happening due to setter method
sajal.totalSalary=200
print("total salary is changed...")
# show updated total salary
print(f"New Total Salary: {sajal.totalSalary}")
print(f"New Bonus: {sajal.bonus}")
print(f"Base Salry(same): {sajal.baseSalary}")





