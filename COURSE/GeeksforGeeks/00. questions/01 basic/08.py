# print prime number in interval as list

list=[]
def prime(x):
    for i in range(x+1):
        # if x is 0 or 1, return empty list
        if i==0 or i==1:
            continue
        else:
            # iterate through all numbers from 2 to x iterable
            for j in range(2,i):
                # if i is divisible by j, break
                if i % j == 0:
                    break
            # if not divisible by any number from 2 to x, append to list
            else:
                # if not divisible, add i to list
                list.append(i)
    # print list
    print(list)

# call
prime(101)


