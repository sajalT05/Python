list=[1,5,10,15,20,25,30,35,40,45,50]
another_list=['a','b','c','d','e','f','g','h','i','j','k']
dict_list={}
dict_two_list={}
dict={'hi':'hello','bye':'goodbye'}
dict_dict={}
list1_dict=[]
list2_dict=[]

# list to dictionary
for value in list:
    dict_list[value]=value*2
print(dict_list)

# two list to dictionary
for (key,value) in zip(another_list,list):
    dict_two_list[key]=value
print(dict_two_list)

# dictionary to dictionary
for (key,value) in dict.items():
    dict_dict[key]=value.upper()
print(dict_dict)


