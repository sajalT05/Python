'''
Used to access methods of super class(just above parent class) in the desired child class.

super().method()
    call constructor of the base class
'''

# parent class
class Class:
    def method(self):
        print("method of class.")
# other parent class
class Class1:
    def method1(self):
        print("this is method of class1")
# child class to class1
class Class2(Class1):
    def method2(self):
        print("this is method of class2")
    # change method2 of parent class1
    def method1(self):
        print("this is method of class1. upodated in class2")
# child class to class2
class Class3(Class2):
    def method3(self):
        print("this is method of class3")
    # change method3 of parent class2
    def method2(self):
        print("this is method of class2. updated in class3")
    # change method1 of parent class1
    def method1(self):
        print("this is method of class1. updated in class3")
# child class to class and class1
class Class4(Class,Class1):
    def method4(self):
        print("this is method of class4")
    def method(self):
        print("this is method of class. updated in class4.")
    def method1(self):
        print("this is method of class1. updated in class4.")
    # trying to update method of non-parent class.
    def method2(self):
        print("this is method of class2. updated in class4.")
# child class to class
class Class5(Class):
# using super method
    def method(self):
        super().method() # returns method output of class
        print("another line with super.")

# instance to class1
a=Class1()
a.method1()
# instane to class2
b=Class2()
b.method2()
# using class1 method in instance of class2
b.method1()
# instance to class3
c=Class3()
c.method3()
# using class2 method in instance of class3
c.method2()
# using class1 method in instance of class1
c.method1()
# instance to class4
d=Class4()
d.method4()
# using class method in class4
d.method()
# using class1 method in class4
d.method1()
# using class2 method in class4 (defined in class)
d.method2() # this is working fine, returning true
# using class3 method in class4 (not defined in class)
# d.method3() # this returns an error
# instance to class5
e=Class5()
e.method()