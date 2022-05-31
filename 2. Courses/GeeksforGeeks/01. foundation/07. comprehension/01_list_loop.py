input_list=[1,5,9,11,15,19, 22, 24, 26, 30]
output_list_simple=[]
output_list_condition=[]
output_list_while_loop=[]
dict={'hi':'hello','bye':'goodbye'}
list1_dict=[]
list2_dict=[]

# arithmetic operations
for value in input_list:
    output_list_simple.append(value*2)
print(output_list_simple)

# conditions
for value in input_list:
    if value%2==0:
        output_list_condition.append(value)
print(output_list_condition)

# dictionary to list
for (key,value) in dict.items():
    list1_dict.append(key)
    list2_dict.append(value)
print(list1_dict)
print(list2_dict)