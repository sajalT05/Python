# create a class
class ApplicationForm:
    # define few variables
    # this is a variable
    formName="Registration Form"
    # class attributes
    department="Marketing"
    # create a function to print information
    # this is a method
    def printFormData(self):
        # take name and age as input
        # print the information of the object
        print(f"{self.name} age is {self.age}")



# call class
# create an object
userApplication=ApplicationForm()
# instance attributes
# name and age are instane attributes
# adding instance attributes
userApplication.name="Sajal Tiwari"
userApplication.age=25
# change object's class attributes
# department is class attributes
userApplication.department
print("Default Department:", userApplication.department) #print default department for object
# changing class attributes for userApplication from marketing to sales
userApplication.department="Sales"
print("New Department:", userApplication.department) #print new department for object
# run the method
# call the function
userApplication.printFormData()

