'''
Recursion
// function which calls itself
// use mathematical formula as a function
// most direct way to code and algorithm
--> keep extreme safety as function will keep calling itself

//way of moving backword
'''
# factorial
# # basic
# n=4
# i=0
# product=1
# for i in range(n):
#     product*=(i+1)
# print(product)
# --> factorial function
# systemetic method
# def factorial(n):
#     product=1
#     if n==0 or n==1:
#         return 1
#     else:
#         for i in range(n):
#             product*=(i+1)
#         return print(product)
# factorial(5)
# direct
# def factorial(n):
#     product=1
#     for i in range(n):
#         product*=(i+1)
#     return print(product)
# factorial(5)

'''
n!=1*2*3*.....*(n-1)*n
n!=n*(n-1)!
'''

# use recursion -->example
def factorial_recursive(n):
    if n==1 or n==0:
        return 1 #if n is 1 or 0, return 1 as output.
    return n*factorial_recursive(n-1) #problem at 1 and 0. 
# print a function --> a function can be used in an other function --> function can also be used as an argument
print(factorial_recursive(5))