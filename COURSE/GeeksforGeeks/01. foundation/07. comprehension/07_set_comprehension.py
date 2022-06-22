list=[1,5,9,11,15,19, 22, 22, 24, 26, 30, 30]
print("input list:", list)
dict={'hi':'hello','bye':'goodbye'}
print("input dictionary:", dict)

# list

# simple
set_list=set(list)
print("list set:", set_list)

# arithmetic
set_list_arithmetic=set(value*2 for value in list)
print("list set using arithmetics:", set_list_arithmetic)

# condition
set_list_condition=set(value for value in list if value%2==0)
print("list set using conditions:", set_list_condition)


# dictionary
# simple
set_dict=set(dict.items())
print("dictionary set:", set_dict)
# arithmetic
set_dict_arithmetic=set(value*2 for (key,value) in dict.items())
print("dictionary set using arithmetics:", set_dict_arithmetic)