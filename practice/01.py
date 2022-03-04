#take input from users
'''
input command reads input as a string
'''
number1=input("Enter first number, i.e. number1=")
number2=input("Enter second number, i.e. number2=")

#print datatype of inputs
print("Datatype of number1 and number2 are, ", type(number1), " and ", type(number2), "respectively")

#convert datatype of input to integers
number1=int(number1)
number2=int(number2)

#print datatype of inputs
print("Updated Datatype of number1 and number2 are, ", type(number1), " and ", type(number2), "respectively")


# addition of two numbers
print("Addition of input is,", number1 + number2)
# multiplication of two numbers
print("Multiplication of input is,", number1 * number2)

#comparison operator
print("Is number1 greater?", (number1>number2))

#arithmetic operation
#square
print("Square of number1 and nyumber2 is,", number1 * number1, "and", number2*number2, " respectively.")
#emainder
print("Remainder when number1 divided by number2,", number1/number2)
#average
print("Average of number1 and number2 is,", (number1+number2)/2)