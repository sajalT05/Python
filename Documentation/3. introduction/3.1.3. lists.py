list=[1,2.0,56,"hi"]

# indexing
print(list[0]) # first position element
print(list[-1]) # last position element

# slicing
print(list[0:2]) # forward --> lower index position included, higher exluded
print(list[-3:-1]) # backward --> lower index position included, higher exluded
print(list[2:-1]) # forward+backward --> lower index position included, higher exluded

# concatenation
new_list = list + ["new",51]
print(new_list)

# mutation
print(list)
list[1]=565.232
print(list)

# appending
list.append(56.36)
print(list)
list.append(5*6/2)
print(list)

# replacement
list[1:4]=["koi",5665,23.121]
print(list)

# length of list
print(len(list))

# nesting
a=[0,1]
b=[2.3]
c=[a,b]
print(c)
print(c[0][0])