# # 01
# # find greatest of four numbers in input
# num1=int(input('enter first number: '))
# num2=int(input('enter second number: '))
# num3=int(input('enter third number: '))
# num4=int(input('enter fourth number: '))
# # way1
# # create a list and sort
# num_list=[num1,num2,num3,num4]
# num_list.sort()
# print('list of numbers', num_list)
# print('list method, highest of number added is', num_list[-1])
# # use if conditions
# # compare numbers individually
# if (num1>num2):f1=num1
# else: f1=num2
# if(num3>num4):f2=num3
# else:f2=num4
# if(f1>f2): print('individual if conditions', f1, 'is highest number')
# else: print('individual if conditions', f2, 'is highest number')
# # # compare numbers at the same time
# # if(num1>num2 & num1>num3 & num1>num4): print(num1, 'is highest')

# # 02
# # check student pass
# mark1=int(input('enter first subject marks: '))
# mark2=int(input('enter second subject marks: '))
# mark3=int(input('enter third subject marks: '))
# average=(mark1+mark2+mark3)/3
# # individual check
# # if(average<40):print('you are failed')
# # elif(mark1<33):print('you are failed')
# # elif(mark2<33):print('you are failed')
# # elif(mark3<33):print('you are failed')
# # else:print("Congratulations! You are passed")
# # combined check
# if(mark1,mark2,mark3<33):print("you failed")
# elif(average<40):print("you failed")
# else:print('you passed')
    
# # 03
# # detect in an input letter
# letter=input('enter your name: ')
# spam=False

# if(letter=='sajal'):spam=True
# elif(letter=='mohan'):spam=True
# elif(letter=='radhe'):spam=True
# elif(letter=='ram'):spam=True

# if(spam==True):print('detected')
# else:print('not detected')

# # 04
# # check character count in an username
# name=input('enter username: ')
# if(len(name)<10):print('less then 10 characetrs in a string')
# else:print('more than 10 characters')

# # 05
# # find names in a list
# list=['sajal','rohan', 'mohan','radhe']
# name=input('enter your name: ')
# if(name in list):print('name found')
# else:print('name not found')

# # 06
# # grade a student
# from numpy import average
# mark1=int(input('enter marks in first subject: '))
# mark2=int(input('enter marks in first subject: '))
# mark3=int(input('enter marks in first subject: '))
# average=(mark1+mark2+mark3)/3
# if(average>90):print('Ex')
# elif(average>80):print('A')
# elif(average>70):print('B')
# elif(average>60):print('C')
# else:print('Fail')

# # 07
# # detect a string in a a string
# letter=input("enter your text: ")
# letter_small=letter.lower()
# check="HarRy"
# check_lower=check.lower()
# if(letter_small.find(check_lower)!=-1):print("Harry Found in text")
# else:print("Harry not found")