# break a list into a n lists

list=[4,44,5,55,6,66,7,77,8,88,9,99,10,100]
n=4

print(
    [list[i*n:(i+1)*n] for i in range(len(list)//n + len(list)%n -1)]   
)