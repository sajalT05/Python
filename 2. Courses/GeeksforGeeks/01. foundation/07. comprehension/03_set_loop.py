input_list=[1,5,9,11,15,19, 22, 24, 26, 30]
dict={'hi':'hello','bye':'goodbye'}
set_list=set()
set_list_arithmetic=set()
set_list_condition=set()
set_dict=set()

# list

# simple
for value in input_list:
    set_list.add(value)
print(set_list)

# arithmetic
for value in input_list:
    set_list_arithmetic.add(value*2)
print(set_list_arithmetic)

# condition
for value in input_list:
    if value%2==0:
        set_list_condition.add(value)
print(set_list_condition)
