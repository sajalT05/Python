list=[1,5,9,11,15,19, 22, 24, 26, 30]
print("input list:", list)
dict={'hi':'hello','bye':'goodbye', 'a':1, 'b':2, 'c':3, 5:100, '9':'nine'}

# list to list

# simple
output_list=[value for value in list]
print("output list:", output_list)

# arithmetic operation
output_list_arithmetic=[value*2 for value in list] 
print("output list using arithmetics:", output_list_arithmetic)

# conditions
output_list_condition=[value for value in list if value%2==0]
print("output list using conditions:", output_list_condition)

# dictionary to list

# simple
# key
list_dict_key=[key for key in dict.keys()]
print("dictionary keys:", list_dict_key)
# values
list_dict_values=[value for value in dict.values()]
print("dictionary values:", list_dict_values)
# key and values
list_dict_key_values=[(key,value) for (key,value) in dict.items()]
print("dictionary key and values:", list_dict_key_values)

# arithmetic
# key
list_dict_key_arithmetic=[key*2 for key in dict.keys()]
print("dictionary keys using arithmetics:", list_dict_key_arithmetic)
# values
list_dict_values_arithmetic=[value*2 for value in dict.values()]
print("dictionary values using arithmetics:", list_dict_values_arithmetic)
# key and values
list_dict_key_values_arithmetic=[(key*2,value*2) for (key,value) in dict.items()]
print("dictionary key and values using arithmetics:", list_dict_key_values_arithmetic)


# conditions
# key
list_dict_key_condition=[key for key in dict.keys() if type(key)==int]
print("dictionary keys using conditions, integer keys:", list_dict_key_condition)
# values
list_dict_values_condition=[value for value in dict.values() if type(value)==str]
print("dictionary values using conditions, string values:", list_dict_values_condition)
# key and values
list_dict_key_values_condition=[(key,value) for (key,value) in dict.items() if type(key)==str and type(value)==str]
print("dictionary key and values using conditions, string keys and values:", list_dict_key_values_condition)
