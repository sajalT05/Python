# create a class
# employee details
class EmployeeDetails:
    # create a class attribute
    office="Mumbai"
    joining=2020

# create object instance
# create Shyam and Radha as object instances
# Shyam and Radha are employees
shyam=EmployeeDetails()
radha=EmployeeDetails()
# print class attributes of objects
# print office
print("Shyam Office:",shyam.office)
print("Radha Office:",radha.office)
# create instance attributes
# salary attributes
shyam.salary=100
radha.salary=50
# print instance attributes
# print salary
print("Shyam salary:",shyam.salary)
print("Radha salary:",radha.salary)
# change default class attributes
# change office of radha
radha.office="Delhi"
# print updated class attribute of the object
# print office of radha
print("Radha Office(new):",radha.office)
# show attribute --> when attribute is not defined in object/instance but in class
# joining year for shyama and radha (when not changed)
print("Shyam Joining year:", shyam.joining)
print("Radha Joining year:", radha.joining)
# show attribute --> when attribute is not defined in object/instance & class
# return error
# department for shyam
print("Shyam Department:", shyam.department)


