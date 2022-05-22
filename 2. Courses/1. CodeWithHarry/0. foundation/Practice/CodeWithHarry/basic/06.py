# # 01
# # multiplication table using for loop
# # conventional method
# a=int(input("enter a number: "))
# for i in range (1,11):
#     # print(str(a) + "*" + str(i) + "=", a*i)
# # best method
# # '''
# # f strings
# # // use variables in curly brackets
# # // fuse f before string
# # // evaluation of expressions is allowed
# # '''
#     print(f"{a}*{i}={a*i}")

# # 02
# # greet people with names starting from s
# list=["harry",'sohan','sachin']
# for name in list:
#     if(name.startswith("s")):
#         print("Good Morning, ", name)

# # 03
# # multiplication table using while loop
# num=int(input("enter a number: "))
# i=0
# while(i<=10):
#     print(f"{num}*{i}={num*i}")
#     i+=1

# # 04
# # check prime number
# num=int(input("enter a number: "))
# condition=False
# if(num==0 or num==1):
#     print("neither prime not composite")
# elif(num==2):
#     print(num, "is prime number")
# else:
#     pass

# if num>2:
#     for i in range(2,num):
#         if(num%i!=0):
#             condition=True
#         else:
#             condition=False
#     if condition is True:
#         print(num, "is prime")
#     else:
#         print(num, "is not prime")

# # 05
# # factorial of a number
# num=int(input("enter a number: "))
# print("factorial of",num,"is\n")
# factorial=1
# while(num>0):
#     # factorial = factorial*num
#     factorial*=num
#     # reducing num by 1 in each loop
#     num-=1
# print(factorial)

# # 06
# # sum of n natural numbers using while loop
# num=int(input("enter a number: "))
# print("sum of all natural numbers till",num,"is")
# sum=0
# while(num>0):
#     # a new variable sum is created to calculate sum
#     # += operator means,both variables integers are added and then new value is assigned to left variable
#     # sum+=num, means sum=sum+num  
#     sum+=num
#     num-=1
# print(sum)


# 07
# print star
# # ladder method
# num=int(input("enter star height: "))
# i=1
# # height of star
# for i  in range (num):
#     print("*"*(i+1))
# # tree method
# num=int(input("enter star height: "))
# i=1
# for i in range(1,num+1):
#     # a new concept
#     # '''
#     # use end="" in print function
#     # this helps printing consecutive statements in a single line
#     # '''
#     print(" "*(num-i), end=" ")
#     print("*"*(2*i-1), end=" ")
#     print(" ")

# # 08
# # print special pattern
# i=0
# for i in range(1,4):
#     if(i==2):
#         print("*" + " " + "*" )
#     else:
#         print("*"*3)

# # 09
# # multiplication table in reverse order
# num=int(input("enter number for multiplication: "))
# limit=int(input("enter limit for multiplication: "))
# i=0
# for i in range(10):
#     print(f"{str(num)}*{str(limit-i)}={num*(limit-i)}")


