# # 01
# # hindi and english dictionary
# hindi_english={
#     'kitaab':'book',
#     'dwaar':'door',
#     'paani':'water'
# }
# input_word=input('enter hindi word (kitaab, dwaar, paani): ')
# print('transalation of your choice word is,', hindi_english.get(input_word))

# # 02
# # display unique numbers after an input number
# number1=input("Enter number: ")
# number2=input("Enter number: ")
# number3=input("Enter number: ")
# number4=input("Enter number: ")
# number5=input("Enter number: ")
# numberSet={number1,number2,number3,number4,number5}
# print('set of numbers is', numberSet)

# # 03
# # 18 as an integer and string in a set
# int=18
# change_int=18
# print(type(change_int)) #change_int is an integer
# str=str(change_int) #convert change_int into string datatype
# print(type(str)) #change_int i.e. str is a string
# set={int,str} #create a set
# print(set) # print a set with an integer and a string

# 04
# find length of a string
s = set()
s.add(20)
s.add(20.0)
s.add('20')
# maybe 3, because integers, floats and strings are there ---> wrong assumption
#floats and integers are same in a set, i.e. 20.0 and 20 same elments in a set
print(s)
print(len(s))