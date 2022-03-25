'''
// group of statements performing a single task
// function can be used in a complex programme any number of times
// def is used to define a function name
// in small brackets, 

// when we wan to call a function, we name the function followed by parenthesis()

Function definition: statements written inside a function
/// A set of instructions already defined, executed when the function is called in a programmes

Types of functions:
1. Built in functions: already defined functions. e.g. print(),len()
2. Use defined functions: created by the programmer e.g. myCustomFunction()
//argumens: function accept these values when called

-> return is necessary to use at then en dof the function for instruct for returning a value on function call

'''

#percentage
# standard
list_marks=[50,85,98,23] #list of marks
set_marks={64,78,95,64} #set of marks
tuple_marks=(46,48,92,94) #tuple of marks
subjects=4
# Total marks
list_marks_sum=sum(list_marks) #sum of list of marks
list_marks_sum_manual=(list_marks[0]+list_marks[1]+list_marks[2]+list_marks[3])
set_marks_sum=sum(set_marks) #sum of set of marks
tuple_marks_sum=sum(tuple_marks) #sum of tuple of marks
# percentage
list_marks_percentage=(list_marks_sum/(subjects*100))*100
# --> define a perentage function with mark argument
def percentage(marks):
    return ((marks[0]+marks[1]+marks[2]+marks[3])/400)*100
# OUTPUT
print("Marks List sum",list_marks_sum,"or", list_marks_sum_manual)
print("Marks list percentage", list_marks_percentage)
print("Function percetage list marks", percentage(list_marks))

# default argument --> uses a default value when no other value is assigned to the argument when fuction call
# // argument=default_argument
def greet(name="user"):
    print("Hello, " + name)
# when argument is placed
print("when argument is placed")
greet("sajal")
# when no argument is used
print("when no argument is used")
greet()
