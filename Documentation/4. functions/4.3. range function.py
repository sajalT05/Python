# // for loop
# // print numbers from 0((included) to 4(excluded)
for i in range(5):
    print(i,end=',')

print('\n')

# create a list in range
# print a list in range from 0((included) to 10(excluded)
print(list(range(5,10)))

#  stepping in range
# create a list in range with stepping
# print a list in range from 0((included) to 10(excluded), with stepping of 2
print(list(range(5,10,2)))

# iterate in a range over indices in a sequece
# indices : elements in a sequences
a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i,'.', a[i])  