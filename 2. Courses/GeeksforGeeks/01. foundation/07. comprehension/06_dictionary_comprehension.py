dict={'hi':'hello','bye':'goodbye', 'a':1, 'b':2, 'c':3, 5:100, '9':'nine'}
list1=['a','b','c','d','e','f','g','h','i','j']
list2=[1,2,3,4,5,6,7,8,9,10]
print("input dictionary:", dict)

# list to dictionary
# simple
dict_list_simple={key:value for (key,value) in zip(list1,list2)}
print("lists to dictionary:", dict_list_simple)
# arithmetic
dict_list_arithmetic={key:value*2 for (key,value) in zip(list1,list2)}
print("lists to dictionary using arithmetics:", dict_list_arithmetic)
# condition
dict_list_condition={key:value for (key,value) in zip(list1,list2) if value%2==0}
print("lists to dictionary using conditions:", dict_list_condition)

# dictionary to dictionary
# simple
dict_dict_simple={key:value for (key,value) in dict.items()}
print("dictionary to dictionary:", dict_dict_simple)
# arithmetic
output_dict_arithmetic={key:value for (key,value) in dict.items()}
print("dictionary to dictionary using arithmetics:", output_dict_arithmetic)
# condition
# key
output_dict_condition_key={key:value for (key,value) in dict.items() if type(key)==int}
print("dictionary to dictionary using conditions, integer keys:", output_dict_condition_key)
# values
output_dict_condition_values={key:value for (key,value) in dict.items() if type(value)==int}
print("dictionary to dictionary using conditions, integer values:", output_dict_condition_values)
