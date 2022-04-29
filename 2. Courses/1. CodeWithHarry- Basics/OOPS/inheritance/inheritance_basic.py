'''
// all methods and attributes of parent class are used in child class.

1. we can use methods/functions and attributes/variables of parent class in child cass.
2. we can modify methods of parent clas in child class.
'''
class Employee:
    # statements, methods and attributes
    variableEmployeeName="String"

class Programmers(Employee): #use employee as parent class in programmer class
    # statements, methods and attributes
    VariableProgramerName="String Other"
