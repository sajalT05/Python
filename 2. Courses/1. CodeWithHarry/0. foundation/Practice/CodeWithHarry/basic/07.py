# # 01
# # create a functionto find greatest of three numbers
# def great(list):
#     list.sort()
#     highest_number=list[-1]
#     return print("gretaest of the number is", highest_number)
# num1=int(input("first numbers: "))
# num2=int(input("second numbers: "))
# num3=int(input("third numbers: "))
# numlist=[num1,num2,num3]
# great(numlist)

# # 02
# # temperature convertor // celsius to fahrenheit
# def temprature(celsius):
#     fahrenheit=32+(9*celsius/5) 
#     return print(fahrenheit,"F")
# value=int(input("enter temprerature: "))
# temprature(value)

# # 03
# # prevent print() function to print a new line at the end
# print("text ", end="")
# print("is ", end="")
# print("good.")

# # 04
# # recursive function to calculate sum of first n natural numbers
# '''
# n=1+2+3+....+(n-1)+n
# n=n+(n-1)
# '''
# def natural_sum(num):
#     if num<1:
#         return 0
#     else:
#         return num + natural_sum(num-1)
# print(natural_sum(10))

# 05
# print falling tree stars using recursive
# # using for loop
# n=5
# for i in range(n): #range is also a nuilt in function
#     print("*"*(n-i))
# # using recursive function
# def falling_stars(n):
#     return print("*"*n)

# # 06
# # create a function to remove a word from a string and sprit the string
# '''
# string_name.strip()
# // by default it strips all apces from the string. all spaces before and after the string
# // when argument is defined, i.e. string_name.strip("name") //it strips "name" string fro the given string
# '''
# # creating a function for modficaiton of any string
# # string is the argument for the string and word is for word to be stripped
# def string_modification(string,word):
#     string1=string.replace(word," ") #replace the word in the string with a space
#     string2=string1.strip()
#     return print(string2)
# mystring="       my name is sajal tiwari. what is your name      "
# remove="name"
# string_modification(mystring,remove)

