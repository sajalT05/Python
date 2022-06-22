'''
for loop is used to iterate through a sequence like strings,lists,tuples
//lists,tuples,strings are iteerables

for(condition): --> use colon just like while/if-elif-else loops
    //statement
'''

# # print all elments in a list //tra
# list=[1,5,9,"word"]
# for items in list: #use 'items' to fetch elements in list,string,tuples during a for loop
#     print(items)

# range functions
'''
// used to generate sequence of numbers
// specify start,stop,step-size
'''

# print using for loop and range function
# for i in range(8): #from 0 to 7
#     print(i)
# for i in range(2,8): #from 2 to 8
#     print(i)
# for i in range(2,8,2): # from 2 to 8 with step size 2 //step size skips every second elments in sequence
#     print(i)

# # using else with for loop
# for i in range(5):
#     print(i)
# else:
#     print('end of for loop')

'''
break statement
// used to come out of the loop
// instructs to terminate the loop sequence and exit at that moment
'''
# # break a for loop
# for i in range(5):
#     print(i)
#     break #loop is terminated at first sequence,i.e. 0

'''
continue statement
// used alongwith for statement
// skips execution at a particular value or set of values defined
'''
# # continue a for loop
# for i in range(5):
#     if(i==3): #skips condition execution when value is 3
#         continue
#     print(i)


